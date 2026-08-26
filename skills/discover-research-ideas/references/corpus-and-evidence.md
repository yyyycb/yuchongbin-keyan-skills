# Corpus and Evidence Protocol

## Contents

1. Evidence hierarchy
2. Corpus strata
3. Open-source baseline gate
4. Citation and repository metrics
5. Minimum corpus for a full run
6. Search and verification procedure
7. Failure rules

## 1. Evidence hierarchy

Use the strongest available source for each claim:

| Claim | Preferred evidence |
|---|---|
| Paper identity, venue, award | Official venue or award page; publisher metadata |
| Method or limitation | Full paper, appendix, supplement, author documentation |
| Citation count or percentile | Named scholarly index with retrieval date |
| Repository ownership | Paper/project page linking the repository, or author organization |
| Stars, forks, releases, activity | Current official repository page or API with retrieval date |
| License | Repository license file or repository metadata |
| Reproducibility | Successful run, released weights/configs, independent reproduction |
| User pain | Repeated issues, downstream reports, or direct observation |

Treat search snippets as routing evidence only. Do not use snippets to assert method details, experimental results, limitations, or novelty.

Label evidence:

- `FACT`: directly supported by a cited source.
- `OBSERVATION`: produced by an inspected output or experiment with provenance.
- `INFERENCE`: reasoned from facts or observations; state the bridge.
- `HYPOTHESIS`: unverified prediction with a planned test.

## 2. Corpus strata

Build a stratified corpus because no single popularity signal teaches research taste.

### A. Recognition stratum

Include Best Paper, Honorable Mention, Test-of-Time, Oral, or equivalent papers from relevant venues. Verify the status on an official page. Record the exact distinction; do not collapse all recognition into "Best Paper."

### B. Scientific-impact stratum

Include papers with high field- and age-normalized influence. Prefer percentile or citation velocity. When only raw counts are available, report the count, index, date, publication age, and the limitation of the comparison.

### C. Adoption stratum

Include papers with official open-source repositories that are high-star relative to their task. Record stars, forks, contributors or releases when available, last meaningful activity, repository age, and whether weights/data/configurations are actually usable.

### D. Contrast stratum

Include competent contemporaneous papers that achieved good reported metrics but had weaker later adoption, weaker conceptual inheritance, or a less durable problem formulation. Match venue, year, task, and resource scale when possible. Do not call a paper "failed" merely because it has fewer citations.

### E. Lineage stratum

Include the immediate predecessors and successors needed to reconstruct what was knowable before the exemplar and what later work retained.

The same paper may belong to several strata. Preserve the labels rather than double-counting it.

## 3. Open-source baseline gate

Require every executable anchor baseline to satisfy:

- paper-to-repository provenance is verified;
- source code is accessible;
- license status is recorded;
- installation and evaluation paths are inspectable;
- required checkpoints/data are available or their absence is explicit;
- repository state is pinned by commit or release;
- compute and storage fit the user's declared resources, or a justified reduced protocol exists.

Default popularity policy when the user provides none:

- prefer an official repository with at least 500 stars; or
- for a niche task, accept a repository in the estimated top decile of directly comparable repositories with at least 100 stars;
- require at least one stronger community anchor when using a lower-star niche baseline;
- never silently lower an explicit threshold.

Popularity is a quality filter, not proof that a result is correct. A high-star repository can still be unreproducible, legally unusable, or scientifically unsuitable.

## 4. Citation and repository metrics

Record every time-varying metric with:

```text
value | source/index | observed_at | comparison cohort | normalization | caveat
```

For citations:

- compare within field and publication year;
- prefer citation percentile or velocity for recent papers;
- distinguish paper citations from repository citations or mentions;
- do not require new Best Papers to have mature citation counts.

For repositories:

- verify that the repository is official;
- compare stars within a matched task, not across all machine learning;
- consider repository age, forks, releases, contributors, downstream integrations, and issue health;
- exclude tutorial, list, wrapper, and model-aggregation repositories from paper adoption counts unless explicitly analyzed as downstream evidence.

## 5. Minimum corpus for a full run

Use these defaults unless the field is too small or the user changes them:

- 3-5 executable anchor baselines;
- at least 12 distinct exemplar/contrast papers;
- at least 3 recognition examples;
- at least 3 high-impact examples;
- at least 3 high-adoption examples;
- at least 3 matched contrast examples;
- at least 6 full-text deep reads;
- enough predecessors and successors to reconstruct at least 3 complete idea genealogies.

Overlap across positive strata is desirable, but do not allow one famous paper to satisfy the entire corpus. If the minimum is impossible, report the missing stratum and lower confidence rather than manufacturing entries.

## 6. Search and verification procedure

1. Define the target task and two adjacent task vocabularies.
2. Search official venue award pages for recognition examples.
3. Search scholarly indexes for high-impact papers and forward citations.
4. Resolve official project pages and repositories.
5. Verify repository metrics, license, checkpoints, and releases.
6. Retrieve full texts for deep-read papers.
7. Build predecessor/successor chains from references and citing work.
8. Select matched contrast papers from the same era and task.
9. Deduplicate by DOI, arXiv identifier, title, and repository provenance.
10. Recheck all current metrics immediately before final reporting.

Use primary sources for technical claims. Use multiple independent indexes when exact citation metrics materially affect inclusion or ranking.

## 7. Failure rules

- No current retrieval: emit a retrieval plan, not a quality-certified corpus.
- No official open-source baseline: do not claim executable baseline grounding.
- Repository lacks a usable license: flag legal/reuse risk; do not assume permission.
- Citation/star threshold unmet: keep the paper only in a clearly labeled exploratory or lineage role.
- Full text unavailable: do not infer the reasoning chain from the abstract.
- Evidence conflicts across sources: preserve both values, dates, and the discrepancy.
