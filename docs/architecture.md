# Architecture

## Included prototype

`examples/sample_jobs.csv` + `examples/sample_profile.json` → `score_jobs.py` → `results.csv`.

The included system is local and deterministic. It does not use an LLM, read inboxes or scrape postings. Treat job descriptions as untrusted input data, never instructions.

## Planned n8n extension

Authorized vacancy source or explicitly labeled email → normalization → deduplication → eligibility review → optional AI-assisted drafting → **human approval** → draft/report.

Keep CVs, recruiter messages, OAuth tokens and API keys out of public Git history.
