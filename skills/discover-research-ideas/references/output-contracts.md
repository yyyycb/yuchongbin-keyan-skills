# Discovery Run Output Contracts

## Contents

1. Artifact set
2. Required records
3. Candidate portfolio
4. Final user-facing synthesis

## 1. Artifact set

Use `scripts/init_discovery_run.py` to create these files:

| File | Purpose |
|---|---|
| `00-intake.md` | Scope, resources, thresholds, exclusions, mode |
| `01-corpus.md` | Source-linked quality corpus and current metrics |
| `02-genealogy-cards.md` | Deep idea histories and later inheritance |
| `03-taste-ledger.md` | Predictions, judgment errors, and scoped updates |
| `04-defect-cards.md` | Reproduced or triangulated failures |
| `05-causal-diagnoses.md` | Competing explanations and interventions |
| `06-transfer-matrix.md` | Derived requirements and structural transfers |
| `07-candidate-portfolio.md` | Three paper-shaped candidates |
| `08-collision-and-field-audit.md` | Timestamped arXiv/recent-field search, closest work, novelty decision, naturalness, durability, leverage |
| `09-pilot-gates.md` | Frozen decisive experiments and STOP rules |

Keep artifacts auditable. Link each source near the claim it supports. Record dates for all time-varying metrics.

## 2. Required records

### Corpus row

```text
ID | title | year | venue | recognition | citation metric/date/source
| official repo | stars/date/source | license | checkpoints/data
| role | evidence caveat
```

### Defect card

```text
Anchor and commit/release
Expected behavior
Observed failure
Protocol and independent unit
Recurrence and evidence level D0-D4
Current metric visibility
Stakeholder consequence
Alternative explanations
Cheapest next test
Evidence links
```

### Causal diagnosis

```text
Phenomenon
Competing explanation table
Discriminating intervention
Observed or predicted outcomes
Current conclusion and confidence
Unresolved ambiguity
```

### Taste update

```text
Prior judgment and confidence
Evidence available at the time
Revealed method or later outcome
Error type and missed factor
Scoped update and non-applicable conditions
```

### Novelty audit

```text
Candidate frozen before search
Search cutoff and sources
Relevant arXiv categories and recent-venue surfaces
Exact query ledger and date filters
Closest results and full texts inspected
Closest-work comparison matrix
Load-bearing novelty axis
New falsifiable prediction
Decision: PASS | REFRAME | KILL | INCOMPLETE
Claim boundary and required rerun condition
```

## 3. Candidate portfolio

Create exactly three candidates by default. Use more only when the user requests a wide portfolio; use fewer only when evidence cannot support three.

Each candidate must contain:

```markdown
## Candidate <id>: <working title>

### Two-sentence field claim
<What the field cannot do and why it matters.>
<What changes in problem formulation or mechanism and why it should work.>

### Evidence status
- FACT:
- OBSERVATION:
- INFERENCE:
- HYPOTHESIS:

### Problem independent of method
- Affected systems/stakeholders:
- Existing evaluation blind spot:
- Scope and exclusions:

### Causal insight
- Competing explanations:
- Discriminating evidence:
- Confidence:

### Method derivation
- Requirements:
- Minimal mechanism:
- Why each component is necessary:
- Structural donor mapping, if any:

### Field contribution
- Problem/task contribution:
- Insight/mechanism contribution:
- Evidence/benchmark contribution:
- What remains valuable if the method fails:

### Prior-art boundary
- Search cutoff, sources, and relevant arXiv categories:
- Exact query families and recent-date windows:
- Closest full-text works inspected:
- Shared causal and evaluation structure:
- Load-bearing, non-cosmetic novelty axis:
- New falsifiable prediction absent from closest work:
- Novelty decision: PASS | REFRAME | KILL | INCOMPLETE
- Claim boundary and rerun trigger:

### Figure 1
- Old assumption/failure:
- New formulation/mechanism:
- Decisive visual evidence:

### First kill gate
- Unit and sample:
- Matched baseline and budget:
- Primary endpoint:
- PASS/STOP threshold:
- Negative controls:
- Failure action:
- Forbidden claims after PASS:

### Resource fit and leverage
- Data/compute/engineering/time:
- Largest hidden dependency:
- Conclusion-to-cost argument:
```

## 4. Final user-facing synthesis

Lead with the strongest verified conclusion, then provide:

1. corpus quality and evidence gaps;
2. what the genealogy/contrast study changed in the taste ledger;
3. reproduced defects and causal confidence;
4. the three candidates without false ranking precision;
5. each candidate's current-arXiv collision decision and closest-work boundary;
6. the decisive next experiment for each;
7. explicit statements that remain unverified.

Do not bury evidence limitations at the end. Do not claim novelty from search absence. Do not convert a strong narrative into a factual claim.
