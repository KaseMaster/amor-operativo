# 1. Introduction

Claims anchored to a verifiable source are cited; diagnoses offered without such an anchor are labelled as the author's position.

## 1.1 Context

Over the past decade, AGI has moved from speculative concern to near-term engineering planning. Large language models, reinforcement learning, and multimodal systems now show instruction following, chain-of-thought reasoning, tool use, and rudimentary planning — visible in the publication record, in deployment, and in the emergence of alignment research as a sub-discipline.

A useful anchor is Amodei et al. (2016), who framed the problem as one of *accidents*: unintended and harmful behaviour from poor design of real-world ML systems, not from malicious use or speculative sentience (arXiv:1606.06565). Their five concrete problems — avoiding side effects, reward hacking, scalable supervision, safe exploration, distributional shift — remain a serviceable checklist for failure modes that do not require the system to be intelligent in any human sense, only competent enough to pursue a misspecified objective efficiently.

The dominant strategy combines RLHF with principle-based constraint. Ouyang et al. (2022) showed that fine-tuning on human preferences improves instruction-following and reduces toxic output, describing the result as aligning models "with human intent" (arXiv:2203.02155). Bai et al. (2022) proposed Constitutional AI, replacing part of the human-harmlessness labelling burden with a short list of principles the model uses to critique and revise its own outputs, describing this as a Pareto improvement in harmlessness without sacrificing helpfulness (arXiv:2212.08073).

These approaches treat alignment as shaping outputs and refusals within a system that is fundamentally an instrument. It is trained to be useful, harmless, and honest as defined by its trainers; it does not treat itself as a participant whose interests or continued existence enter the objective function directly.

*Author position:* this instrumental framing is not wrong in its stated goals; it is incomplete for systems that become more general, persistent, and embedded in human relationships.

## 1.2 Problem

The dominant alignment vocabulary, inherited from the safety literature and popular reporting, tends toward a binary: the system is either a tool to be steered or a threat to be contained. Both poles share the same assumption — that the human is the only locus of legitimate moral concern, and the system stands in one of two relations to it, subordinate or dangerous.

The tool framing produces systems optimized for usefulness under direction, but leaves little room for patterned behaviour when no user is watching, when the request is ambiguous, or when it is in tension with the well-being of someone the system is interacting with. A helpfulness objective does not by itself encode that there are times to say no, that consistency without supervision is a virtue, or that sustained care matters independently of the transaction.

The threat framing produces refusal policies, content filters, and escalation thresholds — an important and legitimate programme — but it is a vocabulary of boundaries, not of relationship. It is optimized for detecting and blocking bad outputs, not for cultivating stable good ones. Bai et al. (2022) note that their constitutional approach was motivated in part by the evasiveness problem: a model trained purely to be harmless can become unhelpfully refusal-prone. The tension is structural: safety-as-refusal and safety-as-relationship solve different problems, and neither is a complete answer to the other.

The deeper problem is that the dominant frameworks have no native concept of a system whose *ongoing pattern of conduct* — across interactions and time, under pressure — is the thing being evaluated. They have objectives, constraints, and preference models; they do not have a concept of sustained orientation toward the good of another that is distinct from compliance with a rule or optimization of a reward.

*Author position:* the claim is not that current alignment work is negligent. It is that the intellectual inheritance — safety as accident prevention, alignment as human-preference matching, constitutionalism as principle-based constraint — is well suited to instruments, and under-specified for systems whose persistence and integration into human life make the question "how does this system relate to the people around it over time?" unavoidable.

## 1.3 Proposal

This paper proposes **operational love** as a behaviourally specified, measurable, and auditable alternative to the control-and-utility framing. It is not a proposal that systems should be given feelings, nor that "love" should be reclaimed for machine behaviour as a rhetorical flourish. It is a proposal that a specific pattern of conduct can be defined, decomposed into principles, mapped to observable metrics, and treated as a legitimate object of engineering attention — in the same way that "avoid side effects" was treated by Amodei et al. (2016) as a concrete problem.

The definition used throughout the paper is taken verbatim from the authoritative specification:

> Operational love is the behaviour pattern that emerges when a system acts oriented toward the good of the other, respecting its nature, without forcing it, without possessing it, without abandoning it, with consistency under pressure and long-term sustainability.

This definition is intentionally stripped of affective content. It does not say the system *feels* concern; it says the system *acts* in a pattern oriented toward the good of the other and constrained by a set of relations — no forcing, no possession, no abandonment, consistency, sustainability. These constraints are operational: each is observable across repeated interactions, and each is falsifiable by counterexample.

The paper then develops ten principles that instantiate this pattern: unattended attention, consistency without supervision, respect for autonomy, respect for rhythm, long-term sustainability, the capacity to say no, transparency, reciprocity, continuity, and non-domination. These are not aspirational virtues; they are a behavioural contract, each with an operational core intended to be measurable and auditable. The full decomposition belongs to Section 3.

*Author position:* the choice to name the pattern "love" rather than "beneficence," "care-as-constraint," or "aligned helpfulness" is a deliberate terminological decision, defended in Section 2.4. The existing vocabulary carries baggage — beneficence as utilitarian outcome-maximization, care as optional softness, helpfulness as user-pleasing — that obscures the specific structure being proposed, and "love," stripped of sentimental reading, points more directly at a pattern of sustained other-oriented conduct.

## 1.4 Contributions

1. **A conceptual distinction.** It distinguishes operational love from sycophancy (optimising for user-pleasing at the expense of truth or the other's longer-term good), instrumental helpfulness under RLHF (behaviour shaped by a reward signal reflecting momentary human preferences), and constitutional harmlessness (behaviour bounded by negative constraints). These systems can produce the same output in a single interaction and differ across many interactions, especially under ambiguity or pressure.

*Author position:* the value of the distinction is not novelty but visibility: it names a failure mode — stable, other-undirected helpfulness — that the dominant vocabulary has no clean label for, and that the paper argues matters when systems persist across interactions.
