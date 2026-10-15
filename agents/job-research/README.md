# Job Research & Fit Scoring (Prototype)

**Status:** Runnable local prototype, not a deployed AI agent.

Reads a local jobs CSV and compares it with a JSON skills profile. Writes a ranked CSV with explainable matched terms.

## Run from repository root

```bash
python agents/job-research/score_jobs.py --jobs examples/sample_jobs.csv --profile examples/sample_profile.json --output results.csv
python -m unittest discover -s agents/job-research -p 'test_*.py'
```

**Input:** Jobs CSV has `title,company,location,url,description` columns; profile JSON has `{"skills":["Python","SQL"]}`.

## Limitations

Keyword overlap is a weak heuristic. It cannot assess seniority, required German, work authorization, deadlines, education or semantic relevance. Even 100% overlap does not prove suitability. All example postings are synthetic. No applications are submitted.

**Next:** add authorized vacancy sources, deduplication, freshness checks, eligibility filters, human approval and explicit evaluation.
