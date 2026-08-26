---
name: discover-research-ideas
description: Discover evidence-grounded, paper-worthy research ideas by studying award-winning, highly cited, and high-star open-source papers; reproducing strong baselines; mining repeatable defects; reconstructing idea genealogies and research taste; diagnosing causal bottlenecks; deriving or structurally transferring solution principles; and designing falsifiable field-level contributions. Use when a researcher asks to 发掘科研idea、培养科研taste、从高质量开源论文找缺陷、学习Best Paper如何提出问题和想出方法、把零散failure升成新任务，或构造有领域意义与自然论文叙事的候选方向. Do not use merely to score a finished idea, summarize one paper, or debug code.
---

# Discover Research Ideas

Build research ideas from verified evidence, not free-form novelty language. Treat research taste as calibrated judgment learned from paper genealogies, contrast cases, later impact, baseline behavior, and failed predictions.

Operate as an independent skill. Do not require, invoke, or position another idea skill as an upstream or downstream stage unless the user explicitly requests that combination.

## Core contract

Apply these rules throughout:

1. **Start from reality.** Ground each direction in a strong paper, an official open-source implementation, or a repeatable field-level observation.
2. **Verify quality signals.** Check awards, citation evidence, repository ownership, stars, license, releases, checkpoints, activity, and retrieval date. Never recall current counts from memory.
3. **Separate signals.** Treat awards as peer recognition, citations as scientific influence, and stars as engineering adoption. Normalize citations by field and age and stars by task and repository age where possible.
4. **Study reasoning, not modules.** Reconstruct what the field believed, what anomaly mattered, which hidden assumption changed, why the method followed, what alternatives failed, and what later work retained.
5. **Observe before naming.** Do not turn a limitation sentence or GitHub issue into a new task until it is reproduced or triangulated.
6. **Diagnose before solving.** Maintain at least three competing causal explanations and design a discriminating intervention before choosing a mechanism.
7. **Derive before borrowing.** First derive requirements from the target failure. Use another paper only when its causal structure maps and yields a new prediction.
8. **Diverge before killing.** Produce multiple problem formulations and three paper-shaped candidates before nearest-neighbor and feasibility convergence.
9. **Keep epistemic labels.** Mark statements as `FACT`, `OBSERVATION`, `INFERENCE`, or `HYPOTHESIS`. Never let packaging upgrade evidence.
10. **Prefer decisive evidence.** Favor a small experiment that changes the explanation over a large benchmark table that only reports gains.

## Choose an operating mode

- **Full discovery:** Build the corpus, develop taste, mine defects, diagnose causes, derive candidates, and design kill gates.
- **Taste study:** Analyze exemplary and contrast papers to update research judgment without forcing a new idea.
- **Defect mining:** Reproduce high-quality open-source baselines and construct evidence-backed defect cards.
- **Reframe:** Revisit existing candidate directions from their baselines and evidence; do not preserve their current names or methods by default.

For a full run, create an artifact directory:

```bash
python3 <skill-dir>/scripts/init_discovery_run.py \
  --out <absolute-run-dir> \
  --topic "<research topic>"
```

Read [references/output-contracts.md](references/output-contracts.md) before filling the artifacts. For a short conceptual request, answer inline but preserve the same evidence discipline.

## Phase 0: Freeze the discovery brief

Record the target field, desired venue/community, user expertise, available data, compute, time, implementation constraints, excluded directions, and whether the goal favors a method, task, benchmark, diagnosis, or an open portfolio.

Infer missing low-risk details. Do not silently relax an explicit star, citation, open-source, compute, or time requirement.

## Phase 1: Build a verified quality corpus

Read [references/corpus-and-evidence.md](references/corpus-and-evidence.md) completely.

Construct four overlapping strata:

- award-recognized papers;
- field- and age-normalized high-impact papers;
- high-adoption papers with official high-star repositories;
- contrast papers that were technically competent but less durable or influential.

For baseline execution, prefer official, licensed, active repositories with usable code, configurations, and weights. Record current metrics with source URLs and observation dates. Use full text for methodological claims; snippets support discovery only.

If current web or scholarly retrieval is unavailable, stop at a source-acquisition plan. Do not present unverified citation counts, stars, award status, or novelty conclusions.

## Phase 2: Reconstruct idea genealogies and calibrate taste

Read [references/taste-and-genealogy.md](references/taste-and-genealogy.md) completely.

For each deep-read exemplar, reconstruct:

```text
field belief -> anomaly -> rejected framing -> representational change
-> method requirements -> mechanism -> decisive evidence -> later inheritance
```

Use contrast sets and counterfactual reconstruction. Ask what could have been inferred from the evidence available before publication, not merely why the published solution looks reasonable afterward. Audit later citing work to identify whether the durable contribution was the problem, abstraction, method, benchmark, evidence pattern, or vocabulary.

Update the taste ledger with concrete judgment errors and scoped corrections. Do not reduce taste to a static numerical rubric.

## Phase 3: Mine and verify defects

Inspect papers, appendices, code, checkpoints, issue discussions, and actual outputs. Build defect cards that state:

- expected behavior and observed failure;
- conditions, independent experimental unit, and recurrence;
- whether current metrics expose the failure;
- affected stakeholders and consequence;
- evidence level and alternative explanations;
- minimal reproduction and cross-model check.

Do not call a defect field-level unless it survives at least one strong alternative baseline or there is independent evidence that the same causal structure recurs.

## Phase 4: Diagnose the causal bottleneck

Read [references/discovery-and-derivation.md](references/discovery-and-derivation.md) completely.

For every promising defect:

1. List at least three explanations, including a mundane implementation explanation.
2. Predict distinct outcomes under each explanation.
3. Choose the cheapest intervention that separates them.
4. Identify the wrong objective, representation, unit, information path, constraint, interface, or evaluation assumption if supported.
5. Mark unresolved ambiguity rather than selecting the most narratively attractive cause.

The output is a causal diagnosis, not a method name.

## Phase 5: Construct the problem at several abstraction levels

Generate at least three formulations:

- **local:** the concrete reproducible failure;
- **capability/task:** the missing ability shared by a class of systems;
- **field abstraction:** the mistaken assumption or evaluation unit that explains the class.

Move both upward and downward. Reject a grand formulation if the evidence only supports the local one. Reject a narrow formulation if it hides a repeated cross-system structure.

## Phase 6: Derive and transfer solution principles

Derive requirements from the diagnosis before retrieving donor mechanisms. Consider minimal sufficient state, invariants, intervention points, observability, optimization variables, decomposition boundaries, verification, feedback, and failure containment.

Then build a structural transfer matrix:

```text
target causal relation | donor causal relation | preserved structure
required adaptation | broken assumptions | new target-domain prediction
```

Reject transfers based only on shared nouns, fashionable modules, or a superficial analogy. A valid transfer must change what is predicted or tested in the target domain.

## Phase 7: Build a paper-shaped portfolio

Produce three genuinely different candidates by default:

1. a field-shaping problem or task candidate;
2. a mechanism-centered candidate with a clean causal claim;
3. a benchmark, diagnostic, or validity candidate that remains useful if the method fails.

For each candidate, specify the problem independent of the proposed method, the causal insight, the derived mechanism, the field-level consequence, the closest prior work, the decisive experiment, the falsification condition, and the expected Figure 1.

Do not create diversity by changing only the backbone, dataset, module name, or output format.

## Phase 8: Audit novelty, naturalness, and leverage

Search for collision using problem aliases, mechanism aliases, task formulations, and the nearest structural relation. Distinguish `not retrieved` from `novel`.

Apply these naturalness tests:

- Does the problem remain important after deleting the method name?
- Does the mechanism follow from the diagnosis rather than from fashion?
- Does replacing the backbone preserve the contribution?
- Could later work cite the problem, benchmark, or insight without using this method?
- Does one decisive figure expose the old blind spot and the new capability?
- Is the conclusion-to-cost leverage attractive under the user's resources?

Packaging is valid only when it compresses this causal chain:

```text
field goal -> systematic failure -> mistaken assumption -> new formulation
-> inevitable mechanism -> decisive evidence -> field consequence
```

## Phase 9: Design the first kill gate

Define the cheapest experiment that can invalidate the load-bearing observation or causal insight. Freeze the unit, baseline, budget, metric, success threshold, failure action, and claims that remain forbidden even after a positive pilot.

Do not begin a full implementation before the observation and diagnosis gates pass.

## Completion contract

A full run is complete only when it contains:

- a source-linked, timestamped quality corpus;
- deep genealogy and contrastive taste records;
- at least one reproduced or triangulated defect;
- competing explanations and a discriminating intervention;
- three abstraction levels and three paper-shaped candidates;
- a structural transfer audit where transfer is used;
- collision, naturalness, field-value, feasibility, and evidence-leverage audits;
- one frozen kill gate per surviving candidate;
- an updated taste ledger containing prediction errors, not generic advice.

Validate the artifact directory:

```bash
python3 <skill-dir>/scripts/validate_discovery_run.py <absolute-run-dir>
```

Return the candidate portfolio and evidence boundaries to the user. Keep all source links adjacent to the claims they support.
