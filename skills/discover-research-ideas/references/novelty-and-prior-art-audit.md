# Novelty and Current Prior-Art Audit

## Contents

1. Purpose and limits
2. Freeze the candidate
3. Build a query lattice
4. Search current arXiv and the field
5. Construct the closest-work matrix
6. Decide whether novelty is sufficient
7. Collision actions and failure rules

## 1. Purpose and limits

Treat novelty as a time-indexed, falsifiable boundary claim, not a feeling or a synonym for an unfamiliar paper. Search actively for work that would invalidate the candidate's contribution.

A current public search cannot prove that no unpublished concurrent work exists. It can support only this bounded statement:

```text
No collision was found within the recorded sources, queries, categories,
dates, and full-text comparisons as of <cutoff timestamp>.
```

Never translate that statement into "nobody has done this." Distinguish:

- `not retrieved`: the search did not surface a collision;
- `not inspected`: a result was found but full text was not checked;
- `distinct within scope`: the closest inspected work differs on a load-bearing axis;
- `novel`: a bounded conclusion justified by the complete audit below.

## 2. Freeze the candidate

Before retrieval, record the candidate without novelty adjectives:

```text
problem and affected systems
reproduced phenomenon
causal claim
minimal mechanism principle
evaluation unit and success contract
intended problem/task, insight/mechanism, and evidence/benchmark contributions
new prediction that existing work is not expected to make
```

Do not change these fields silently after finding nearby work. Preserve the pre-search version and log every subsequent reframe.

## 3. Build a query lattice

Use multiple query families because neighboring papers rarely use identical names:

1. **Problem aliases:** failure, limitation, affected object, user consequence, and negated desired behavior.
2. **Task/capability aliases:** formal task name, informal capability description, input-output contract, and evaluation formulation.
3. **Mechanism aliases:** module names, domain-neutral operating principle, optimization intervention, and alternative technical vocabulary.
4. **Structural queries:** the causal relation between entities, states, constraints, or information paths without project-specific nouns.
5. **Combination queries:** problem + mechanism, task + failure, evaluation + blind spot, and key pairs of contribution claims.
6. **Adjacent-field queries:** the same causal structure in neighboring communities, datasets, modalities, or application domains.
7. **Known-neighbor expansion:** title phrases, references, citing papers, authors, project pages, and "similar/related" results from the closest hits.

Record every query verbatim. Include negative and broader queries; do not search only the candidate's preferred terminology.

## 4. Search current arXiv and the field

Run the audit after candidates are concrete and rerun it immediately before committing to a full project or making a novelty claim.

At minimum:

- search arXiv across every relevant primary and cross-listed category;
- sort and inspect by initial submission date as well as relevance;
- conduct an intensive sweep of the latest 90 days and 24 months;
- search the full historical range for foundational and exact structural neighbors;
- search recent proceedings and preprint surfaces used by the target community, such as official conference proceedings or OpenReview where relevant;
- inspect references and forward citations of the closest work;
- check author/project pages and official repositories for newer titles or renamed versions;
- deduplicate conference, workshop, and arXiv versions while preserving arXiv `v1`, latest-version, and venue dates.

For each source record:

```text
source | categories/venue | exact query | filters | searched_at
result count inspected | candidate hits | full texts inspected | caveat
```

Use the current date and source links. If live retrieval is unavailable, return `INCOMPLETE`; do not use memory to certify novelty.

## 5. Construct the closest-work matrix

Retain the strongest collision candidates, not only papers that are easy to distinguish. Read the full text of at least the three closest hits and more whenever the boundary remains ambiguous.

Compare:

| Work | Problem/setting | Causal insight | Mechanism principle | Evaluation unit | Claimed contribution | Shared structure | Load-bearing difference | New prediction unique to candidate | Verdict |
|---|---|---|---|---|---|---|---|---|---|

A difference is cosmetic when it changes only a backbone, dataset, modality label, module name, prompt wording, loss wrapper, output format, or benchmark scale without changing the causal claim or prediction.

Treat a cross-domain transfer as novel only when the target domain breaks an assumption, requires a nontrivial adaptation, and produces a target-specific prediction that the donor work does not imply directly.

## 6. Decide whether novelty is sufficient

Require at least one load-bearing novelty axis:

- **problem/task:** a previously unformalized, evidence-backed capability gap or wrong unit;
- **causal insight:** a distinct explanation supported by a discriminating intervention;
- **mechanism principle:** a non-obvious intervention derived from the diagnosis, not a module swap;
- **evidence/benchmark:** a validity correction or measurement contract that changes scientific conclusions or model selection.

The novelty axis is sufficient only when all are true:

1. it differs non-cosmetically from the strongest closest work;
2. it matters to the field goal after deleting the method and project names;
3. it generates a falsifiable prediction or decisive comparison absent from the closest work;
4. the supporting defect and abstraction level are evidence-backed;
5. the contribution is not merely an untested combination of known components;
6. the claim is scoped to what the recorded search can defend.

Use one decision:

- `PASS`: sufficient novelty survives;
- `REFRAME`: the evidence is useful but the current task, mechanism, or contribution collides;
- `KILL`: the central contribution is already covered or only cosmetically distinct;
- `INCOMPLETE`: retrieval, coverage, or full-text inspection is insufficient.

Do not average several weak differences into a high novelty score.

## 7. Collision actions and failure rules

- Direct problem + mechanism + evaluation collision: `KILL` unless a different causal claim with new evidence can be reconstructed.
- Problem collision but distinct causal diagnosis: narrow the claim, design a discriminating test, then rerun as `REFRAME`.
- Mechanism collision but newly verified field-level problem: separate task/evidence contribution from method contribution and rerun.
- Only cross-domain application novelty: require broken assumptions, necessary adaptation, and a new prediction; otherwise `KILL`.
- Search coverage misses relevant categories, synonyms, recent dates, or closest full texts: `INCOMPLETE`.
- Candidate changes after search: preserve the old decision and run a new audit from the frozen fields.
- A paper appears after the audit: update the cutoff, closest-work matrix, decision, and claim boundary.

Never rescue novelty through renaming, selective citation, an artificially weak baseline, or a narrower search vocabulary.
