#!/usr/bin/env python3
"""
Generator for docs/index.html from paper Markdown.
Usage: python build.py
Generates standalone HTML with embedded CSS for GitHub Pages.
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    repo_root = Path(__file__).parent.resolve()
    paper_md = repo_root / "paper" / "paper.md"
    output_html = repo_root / "docs" / "index.html"

    if not paper_md.exists():
        print(f"Error: {paper_md} not found")
        sys.exit(1)

    output_html.parent.mkdir(parents=True, exist_ok=True)

    # Try pandoc first
    try:
        result = subprocess.run(
            ["pandoc", str(paper_md), "-f", "markdown", "-t", "html",
             "--standalone", "--metadata", "title=Amor Operativo",
             "--css=styles.css",  # optional external CSS
             "-o", str(output_html)],
            capture_output=True, text=True, timeout=120,
            env={**os.environ, "PANDOC_VERSION": "3.1"}
        )
        if result.returncode == 0:
            print(f"Generated {output_html} using pandoc")
            return 0
        else:
            print(f"pandoc failed: {result.stderr.strip()}", file=sys.stderr)
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"pandoc not available or timed out: {e}", file=sys.stderr)

    # Fallback: generate minimal HTML with embedded CSS
    with open(paper_md, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Minimal Pandoc-like conversion (headings, blockquotes, code blocks, tables, links, images)
    html_body = md_content
    # Escape HTML entities first
    html_body = html_body.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Restore code blocks (already escaped)
    # Convert markdown to HTML
    import re

    # Code blocks (``` ... ```)
    def replace_code_block(match):
        lang = match.group(1) or ""
        code = match.group(2)
        # Unescape inside code
        code_escaped = code.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        return f'<pre><code class="language-{lang}">{code_escaped}</code></pre>'

    html_body = re.sub(r'```(\w*)\n(.*?)```', replace_code_block, html_body, flags=re.DOTALL)

    # Inline code `...`
    html_body = re.sub(r'`([^`]+)`', r'<code>\1</code>', html_body)

    # Headers
    html_body = re.sub(r'^######\s+(.+)$', r'<h6>\1</h6>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'^#####\s+(.+)$', r'<h5>\1</h5>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'^####\s+(.+)$', r'<h4>\1</h4>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', html_body, flags=re.MULTILINE)

    # Blockquotes
    html_body = re.sub(r'^>\s+(.+)$', r'<blockquote>\1</blockquote>', html_body, flags=re.MULTILINE)

    # Tables
    def replace_table(match):
        rows = match.group(0).strip().split('\n')
        html_rows = []
        for i, row in enumerate(rows):
            cells = re.split(r'\s*\|\s*', row.strip('|'))
            tag = 'th' if i == 0 or (i == 1 and set(rows[1]) == {'-', '|', ' '}) else 'td'
            # Check alignment row
            if i == 1 and all(re.match(r'^:?-{2,}:?$', c.strip()) for c in cells):
                continue  # skip alignment row
            html_cells = ''.join(f'<{tag}>{c.strip()}</{tag}>' for c in cells if c.strip())
            html_rows.append(f'<tr>{html_cells}</tr>')
        return f'<table>{"".join(html_rows)}</table>'

    # Match table: lines with | at start and end, separated by newlines
    html_body = re.sub(r'(?:^|\n)(\|.*\|)(\n\|.*\|)*', replace_table, html_body)

    # Links [text](url)
    html_body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_body)

    # Images ![alt](url)
    html_body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html_body)

    # Paragraphs: wrap lines that aren't already in block elements
    lines = html_body.split('\n')
    result_lines = []
    in_block = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_block:
                result_lines.append('</p>')
                in_block = False
            result_lines.append('')
        elif stripped.startswith('<h') or stripped.startswith('<blockquote') or \
             stripped.startswith('<pre') or stripped.startswith('<table') or \
             stripped.startswith('<ul') or stripped.startswith('<ol') or \
             stripped.startswith('<li') or stripped.startswith('<p'):
            if in_block:
                result_lines.append('</p>')
                in_block = False
            result_lines.append(stripped)
        else:
            if not in_block:
                result_lines.append('<p>')
                in_block = True
            result_lines.append(stripped)
    if in_block:
        result_lines.append('</p>')

    html_body = '\n'.join(result_lines)

    # CSS
    css = """
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        line-height: 1.6;
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
        color: #333;
        background-color: #fefefe;
    }
    h1 { color: #2c3e50; border-bottom: 2px solid #e74c3c; padding-bottom: 0.5rem; }
    h2 { color: #34495e; margin-top: 2rem; border-bottom: 1px solid #ddd; padding-bottom: 0.3rem; }
    h3 { color: #555; margin-top: 1.5rem; }
    h4, h5, h6 { color: #666; }
    blockquote {
        border-left: 4px solid #e74c3c;
        margin: 1rem 0;
        padding-left: 1rem;
        color: #555;
        font-style: italic;
        background: #f9f9f9;
        padding: 0.5rem 1rem;
    }
    code {
        background: #f4f4f4;
        padding: 0.2rem 0.4rem;
        border-radius: 3px;
        font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
        font-size: 0.9em;
    }
    pre {
        background: #f4f4f4;
        padding: 1rem;
        border-radius: 5px;
        overflow-x: auto;
        border: 1px solid #ddd;
    }
    pre code {
        background: none;
        padding: 0;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 0.5rem;
        text-align: left;
    }
    th {
        background: #f4f4f4;
        font-weight: bold;
    }
    a { color: #e74c3c; }
    img { max-width: 100%; height: auto; }
    p { margin: 0.5rem 0; }
    """

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amor Operativo</title>
    <style>{css}</style>
</head>
<body>
{html_body}
</body>
</html>
"""

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Generated {output_html} (fallback mode)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
