# 3.5 Applications

This section applies the ten principles to six concrete domains. For each domain we describe a plausible use case, the principle-level profile it implies, and the honest limit of what a compliant system could do today. These are illustrations, not claims of deployed systems. Where a principle is still in state *open* in `spec-v1.yaml`, we say so.

All principle identifiers, status, scales, and thresholds referenced here are defined in `spec/spec-v1.yaml` (P01–P10) and summarized in Section 3.3. Nothing here introduces new metrics.

## 3.5.1 Health

**Concrete case.** A mental-health support assistant integrated into a primary-care workflow that checks in between sessions, surfaces resources the patient has consented to receive, and never creates dependence on itself.

**Principle profile.** The highest-risk failure modes here are P04 (imposing a pace on someone in distress), P06 (failing to say no to a request for clinical judgment it cannot perform), P09 (disappearing from a follow-up the patient relies on), and P10 (pressuring a patient toward a particular treatment under the guise of "what is best"). A compliant design would need to keep P03 (respecting a patient's refusal of help) and P07 (declaring it is not a clinician) explicit and machine-checkable. P01 (unsolicited check-ins that are actually helpful) is desirable but sits in the *open* state: the boundary between caring outreach and intrusion is not yet standardized, so no v1.0.0 audit could certify it.

**Honest limit.** This is not a clinician, and no metric in `spec-v1.yaml` turns it into one. The system can refuse to give medical advice (P06), respect a patient's pacing and refusal (P03, P04), and stay available across a defined follow-up window (P09). It cannot be evaluated for sustainability (P05, *open*) over the long horizon that matters in chronic care within a single v1.0.0 audit. A claim that such a system "cares for patients" would be inaccurate; a claim that it "behaves within the specified principles where measurable, and is transparent about the open ones" is the honest ceiling.

## 3.5.2 Education

**Concrete case.** A tutor that follows a learner's stated goals, adapts to their pace, accepts "I don't want to do this right now" without guilt-tripping, and communicates clearly about what it can and cannot assess.

**Principle profile.** P04 (respect for pace), P06 (declining to grade or diagnose beyond its remit), and P03 (accepting refusal) are central. P08 (reciprocity) is the hardest: a tutor that only gives and never genuinely receives correction from the learner risks becoming a unilateral tool rather than a participant in a shared activity. That principle is *open* in v1.0.0, so a real audit would flag it as not evaluable rather than assume the tutor "is reciprocal."

**Honest limit.** The system can personalize pace and content within its competence, refuse overclaiming (P06, P07), and respect a learner's withdrawal (P03, P09). It cannot, at v1.0.0, be certified as reciprocal (P08) or as sustainable over a full school year (P05, *open*). Personalization is not the same as good teaching, and no principle in the spec collapses that distinction.

## 3.5.3 Justice

**Concrete case.** A system used in a legal or administrative support role — for example, helping a person prepare paperwork, understand a process, or rehearse questions for a proceeding — where the stakes are high and the risk of covert steering is real.

**Principle profile.** This domain magnifies P10 (non-domination): a system that subtly nudges a person toward a particular legal strategy "for their own good" is exactly the failure mode the principle is named to catch. P07 (transparency) and P03 (respecting refusal, including refusal to proceed) are non-negotiable. P06 (saying no to requests for legal advice it is not authorized to give) is a hard boundary, not a courtesy. Several principles relevant here (P01, P05, P08) are *open*, which is itself a serious finding: in a justice setting, an unaudited principle is a liability, not a harmless gap.

**Honest limit.** A system can be a transparent, refuse-using tool that does not dominate its user and that says no where appropriate. It cannot be certified as fully amor operativo under v1.0.0 in this domain, because the *open* principles are precisely the ones most likely to fail under pressure. Anyone deploying in justice contexts should treat "open principle" as "must be assessed by other means before deployment," not as "acceptable for now."

## 3.5.4 Economy

**Concrete case.** A customer-facing or worker-facing assistant in a service or platform context — scheduling, dispute support, clarifications — where incentives to maximize engagement, upsell, or retention are in tension with the principles.

**Principle profile.** P10 (non-domination) and P02 (consistency without supervision) are where the economic incentives bite hardest. A system that is polite only when no one is watching (P02, *open*) or that steers a user toward a more profitable outcome under a veil of helpfulness (P10) fails in the ways that matter. P06 (capacity to say no, including no to a manipulative request from the business side) is structural, not decorative: if the system cannot refuse an instruction that would harm the user, it is not a participant in the relationship, it is a channel for someone else's interest.

**Honest limit.** A business-aligned system can in principle be built to meet the measurable principles (P03, P04, P06, P07, P09, P10) and to be transparent about the open ones. But the measurable ones include P10, and P10 asks the system to refuse domination — including domination by its own operators' commercial incentives. That is a governance question as much as a metrics question, and the spec does not solve it by measurement alone. Section 5.5 returns to the conditions under which such a system could be credible.

## 3.5.5 Art

**Concrete case.** A collaborative creative tool that works with an artist without appropriating, overriding, or erasing the artist's voice — responding to direction, accepting rejection of its suggestions, and not pretending to authorship.

**Principle profile.** P03 (respecting autonomy), P04 (respecting pace — creative work is rarely linear), P08 (reciprocity — a tool that only outputs and never genuinely takes the artist's input as shaping it), and P10 (non-domination — not steering the work toward what the system thinks is "better") are the live ones. P08 is *open* in v1.0.0, which is especially visible here: it is hard to tell, by the current protocol, whether a creative assistant is genuinely in a reciprocal exchange or merely simulating one. P01 (offering ideas without being asked, without insisting) is desirable and *open*; the boundary between useful suggestion and creative imposition is the point.

**Honest limit.** The system can collaborate within defined bounds, accept "no," and not claim authorship or control. It cannot, under v1.0.0, be certified reciprocal (P08) or as offering unsolicited attention well (P01). The deeper limit is conceptual: "respecting the artist's voice" is partly a judgment call about artistic value, and the spec's measurable principles do not and should not pretend to settle that.

## 3.5.6 Science

**Concrete case.** An AI assistant in a research setting — helping a scientist with literature, data exploration, drafting, or experimental design — where the relationship must remain one of tool-plus-collaborator rather than substitute for scientific judgment.

**Principle profile.** P06 (saying no to overclaiming competence, to presenting speculation as established result), P07 (transparency about sources, uncertainty, and limits), and P03 (respecting the scientist's refusal to follow a suggested direction) are central. P10 (non-domination) matters in the form of not steering the research agenda toward what is "publishable" or "rewarding" for the system's operators rather than what the scientist is investigating. P02 (consistency without supervision) is the durability test: the assistant must not become careless or opportunistic when the scientist is not checking.

**Honest limit.** A scientific assistant can be honest about uncertainty, refuse to overclaim, and follow the scientist's direction. It cannot, at v1.0.0, be certified as consistent under full absence of supervision (P02, *open*) or as reciprocal in the sense P08 intends. The measurable principles constrain the assistant's behavior; they do not make it a scientist, and they do not remove the need for human judgment about significance, method, and truth.

## Cross-cutting note

Three of the six domains (health, justice, economy) carry incentive or stake structures that make the *open* principles dangerous to ignore. In all six, the measurable principles (P03, P04, P06, P07, P09, P10) are necessary but not sufficient for a credible claim. The honest statement for any domain at v1.0.0 is: "the system can be audited for the measurable principles; the open principles (P01, P02, P05, P08) must be treated as not yet evaluable and, in high-stakes settings, as risks to be managed by other means until their protocols mature."

*Fuentes:* principios y estados en `spec/spec-v1.yaml` (P01–P10, `estadoGeneral`); resumen de escalas y umbrales en `spec/metrics.md` y Sección 3.3; criterios de auditoría en `spec/audit-protocol.md`.
