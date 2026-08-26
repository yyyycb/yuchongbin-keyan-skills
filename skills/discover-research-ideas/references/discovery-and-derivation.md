# Defect Discovery, Causal Diagnosis, and Method Derivation

## Contents

1. Defect evidence ladder
2. Causal diagnosis
3. Problem construction
4. Deriving methods
5. Structural transfer
6. Paper-shape and naturalness tests
7. Resource and falsification gates

## 1. Defect evidence ladder

Classify every proposed defect:

| Level | Evidence | Permitted claim |
|---|---|---|
| D0 | Intuition or anecdote | Search lead only |
| D1 | Limitation text, issue, or isolated example | Candidate failure; not verified |
| D2 | Reproduced under a pinned baseline and protocol | Baseline-specific defect |
| D3 | Repeats across models, datasets, seeds, or independent reports | Class-level phenomenon candidate |
| D4 | Intervention distinguishes root cause from alternatives | Mechanistic research problem |

Do not construct a field-level task from D0-D1. D2 may justify a narrow investigation. D3-D4 can support broader problem construction, subject to sampling and scope.

For each defect, record expected behavior, observed behavior, provenance, recurrence, current-metric visibility, affected stakeholder, concrete consequence, and cheapest next elevation test.

## 2. Causal diagnosis

Construct a hypothesis table:

| Explanation | Causal path | Distinct prediction | Discriminating intervention | Cost | Result |
|---|---|---|---|---|---|

Always include:

- an implementation or tuning failure;
- a data or evaluation artifact;
- the proposed structural explanation.

Consider these bottleneck classes without treating them as exhaustive labels:

- wrong unit or granularity;
- missing state or relation;
- objective-utility mismatch;
- information not observable at the decision point;
- entangled optimization variables;
- train/deploy mismatch;
- open-loop operation without feedback or verification;
- invalid invariance or independence assumption;
- resource allocation mismatch;
- benchmark protocol hiding the real consequence.

Prefer interventions that change one causal factor while matching data, compute, parameters, and evaluation budget.

## 3. Problem construction

Build an abstraction ladder:

```text
instance -> repeated phenomenon -> missing capability/task
-> hidden field assumption -> broader consequence
```

At each step ask:

- What additional evidence licenses this generalization?
- What counterexample would break it?
- Which systems and stakeholders are included or excluded?
- Can the task be defined without mentioning the proposed method?
- Is there a measurable contract for success?

Keep the highest evidence-supported formulation, not the most impressive one.

## 4. Deriving methods

Derive a method from the causal model through constraints:

1. Identify what information is minimally sufficient.
2. Identify what must remain invariant and what must change equivariantly.
3. Choose the decision or intervention point where the cause can be affected.
4. Decide whether the missing object is a state, relation, uncertainty, constraint, certificate, feedback signal, or optimization variable.
5. Separate components only when their causal responsibilities differ.
6. Select training or inference signals that directly supervise the missing responsibility.
7. Add verification or correction only where an identifiable failure remains.
8. Remove components that do not change a prediction or satisfy a requirement.

Write a derivation chain:

```text
diagnosis -> requirement R1/R2/R3 -> mechanism component C1/C2/C3
-> prediction P1/P2/P3 -> experiment E1/E2/E3
```

Each component must link to a requirement and a falsifiable prediction. A component without either is ornamental until proven otherwise.

## 5. Structural transfer

Translate the target and donor papers into domain-neutral causal relations before mapping them.

Valid transfer requires:

- entities or states with corresponding roles;
- relations with matching direction and semantics;
- assumptions that remain valid or are explicitly repaired;
- a necessary target-domain adaptation;
- at least one new prediction not supplied by the target literature alone.

Use this template:

```markdown
### Target structure
- Entities/states:
- Causal relations:
- Constraints:
- Failure:

### Donor structure
- Entities/states:
- Causal relations:
- Constraints:
- Solution principle:

### Mapping
- Preserved relations:
- Broken assumptions:
- Required adaptation:
- New prediction:
- Surface-only similarities deliberately ignored:
```

Reject a transfer when the donor name can be swapped for any fashionable module without changing the prediction.

## 6. Paper-shape and naturalness tests

Construct three candidates with different contribution centers, not cosmetic variants.

For each candidate require:

- a problem statement independent of the method;
- a verified evidence chain;
- a causal insight;
- a method derivation or justified decision not to propose a method;
- a field-level consequence with bounded scope;
- a nearest-neighbor distinction;
- a decisive experiment and kill condition;
- a Figure 1 concept showing the blind spot and the intervention.

Run deletion tests:

- Delete the method name: does the problem remain important?
- Delete the new task name: does a measurable gap remain?
- Replace the backbone: does the contribution survive?
- Replace the donor mechanism: do the derived requirements still constrain the solution?
- Remove the narrative adjectives: do facts and observations still motivate the work?

Run durability tests:

- Could a later paper cite the problem without using the method?
- Could the benchmark or diagnostic change model selection?
- Does the insight explain existing conflicting results?
- Is the contribution useful if the main metric gain is modest?

## 7. Resource and falsification gates

Evaluate conclusion-to-cost leverage, not feasibility alone:

```text
leverage = size of defensible conclusion / cost of decisive evidence
```

Prefer existing strong open-source baselines, controlled synthetic truth, frozen backbones, small interventions, paired designs, and early CPU/data gates when they answer the causal question fairly.

For every candidate freeze:

- load-bearing hypothesis;
- independent experimental unit;
- strongest matched baseline;
- data, parameter, compute, and query budget;
- primary endpoint and threshold;
- negative controls;
- STOP action;
- claims still forbidden after success.

Do not rescue a failed causal hypothesis by renaming the mechanism, adding an unrelated module, switching the primary metric, or broadening the story.
