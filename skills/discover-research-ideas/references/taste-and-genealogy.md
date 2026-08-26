# Research Taste and Idea Genealogy

## Contents

1. What taste means
2. Genealogy card
3. Counterfactual reconstruction
4. Contrastive study
5. Later-impact audit
6. Taste ledger
7. Common false learning

## 1. What taste means

Treat research taste as an evolving ability to rank uncertain opportunities before the results are known. It includes judgment about:

- **importance:** whether solving the problem changes practice or understanding;
- **truth:** whether the motivating phenomenon is real and recurring;
- **abstraction:** whether the problem is named at the right level;
- **timing:** whether a recent change makes the work newly possible or necessary;
- **inevitability:** whether the method follows from the diagnosis;
- **simplicity:** whether the core insight survives removal of ornamental complexity;
- **evidence:** whether decisive experiments can distinguish the explanation;
- **leverage:** whether modest resources can support a large conclusion;
- **durability:** whether later work could retain the problem or insight after replacing the method;
- **community fit:** whether the relevant community recognizes the consequence without artificial framing.

Do not collapse these dimensions into one permanent score. Use pairwise judgments, written predictions, evidence, and later calibration.

## 2. Genealogy card

Create one card per deep-read exemplar:

```markdown
## <paper>

### Verified position
- Venue/year/distinction:
- Citation evidence and date:
- Official repository/adoption evidence and date:
- Why selected:

### Before the paper
- Dominant field belief:
- Standard problem formulation:
- Strongest available baselines:
- Technical or social enablers:

### Generative evidence
- Anomaly, contradiction, or unmet need:
- Why it was easy to dismiss:
- Evidence available before the proposed method:

### Intellectual move
- Hidden assumption exposed:
- Representation/objective/unit/agent/timescale changed:
- New abstraction introduced:
- Why this abstraction was neither too local nor too broad:

### Method derivation
- Requirements implied by the diagnosis:
- Alternatives considered or reconstructable:
- Why the selected mechanism satisfies the requirements:
- Which components are load-bearing versus implementation detail:

### Evidence design
- Decisive experiment:
- Alternative explanation excluded:
- Negative control or falsifier:
- Claim boundary:

### Later inheritance
- What later work actually retained:
- What did not endure:
- Problem/method/benchmark/vocabulary inheritance:

### Transferable taste lesson
- Scoped principle:
- Conditions where it applies:
- Conditions where it should not be reused:
```

## 3. Counterfactual reconstruction

Avoid hindsight by separating three passes:

### Pass A: Before-method reconstruction

Read only the chronological field context, baseline behavior, problem evidence, and any pre-method material that does not disclose the central mechanism. Propose:

- three competing problem formulations;
- three causal explanations;
- solution requirements, not named modules;
- the experiment with highest expected information gain.

Record memory contamination when the paper is already familiar. Do not pretend a famous result is blind.

### Pass B: Reveal and compare

Read the full method, appendix, and experiments. Compare the paper with the reconstruction:

- Which observation did the paper weight differently?
- Which abstraction did it choose that the reconstruction missed?
- Which constraint made its method natural?
- Did the paper actually validate its motivating explanation?
- Was a simpler alternative insufficient?

### Pass C: Outcome audit

Inspect later citations, successors, repositories, and adopted benchmarks. Determine whether the original paper's durable contribution matches its own headline claim.

## 4. Contrastive study

Create matched sets rather than reading only winners:

- one recognized or durable paper;
- one high-metric contemporary paper with less conceptual inheritance;
- one later successor;
- their shared predecessor.

Compare them on the same questions:

1. Which paper selected the more consequential failure?
2. Which changed the problem representation rather than only the solver?
3. Which method was easiest to derive from the stated diagnosis?
4. Which experiment most strongly excluded an alternative explanation?
5. Which contribution survived replacement of the original implementation?
6. Which paper benefited from timing, platform, scale, or community factors?

Do not moralize citation or star differences. Record plausible confounders such as paper age, lab visibility, benchmark popularity, code quality, compute access, and title clarity.

## 5. Later-impact audit

Classify citing work by what it inherits:

- `PROBLEM`: adopts the problem definition or failure phenomenon;
- `ABSTRACTION`: adopts the conceptual representation;
- `METHOD`: reuses or extends the mechanism;
- `BENCHMARK`: uses the dataset, protocol, or metric;
- `EVIDENCE`: reuses the intervention or evaluation logic;
- `VOCABULARY`: cites the framing without substantive dependence;
- `NEGATION`: challenges or overturns the claim.

High raw citations dominated by `VOCABULARY` teach a different lesson from fewer citations dominated by `PROBLEM` or `ABSTRACTION` inheritance.

## 6. Taste ledger

Record concrete prediction errors:

```markdown
## <date> — <case>
- Decision made before outcome:
- Confidence:
- Evidence used:
- Outcome or revealed paper:
- Error type: importance | truth | abstraction | timing | mechanism | evidence | feasibility | narrative
- Missed factor:
- Updated scoped judgment:
- Where the update does not apply:
- Next discriminating test:
```

Prefer updates such as:

> When adding capacity does not change the failure but a state intervention does, test whether the represented object is wrong before framing the problem as insufficient memory.

Reject updates such as:

> Think more causally next time.

## 7. Common false learning

- **Winner imitation:** copying visible traits of Best Papers instead of reconstructing their evidence and constraints.
- **Outcome worship:** treating citations, awards, or stars as proof of correctness.
- **Module taxonomy:** turning deep papers into a list of routers, compilers, critics, or losses.
- **Hindsight compression:** making the final method seem obvious after reading it.
- **Survivorship-only corpus:** omitting matched papers that looked promising but did not endure.
- **Narrative leakage:** allowing a compelling title to substitute for a reproduced phenomenon.
- **Universal rule creation:** extracting a general slogan from one success without recording boundary conditions.
