# AI Automation & Business Solutions

**Practical automation, AI-assisted research, and data-driven business workflows.**

An evolving portfolio by [Blessing Sekeramavi](https://github.com/BlessingSK1998), bringing together data science, project coordination and business problem-solving.

## Project status

| Initiative | Status | What exists |
| --- | --- | --- |
| [Job Research & Fit Scoring](agents/job-research/) | **Runnable prototype** | Python CLI that scores transparent keyword overlap between a local jobs CSV and an example candidate profile; no job scraping, LLM or application submission |
| [n8n Job Research Assistant](workflows/n8n/) | **Planned** | Workflow design and implementation checklist |
| Inbox-to-Task Workflow | **Planned** | Design concept in [roadmap](docs/roadmap.md) |
| Business KPI Reporting Automation | **Planned** | Design concept in [roadmap](docs/roadmap.md) |

The included Python script is runnable, but its heuristic matching has **not** been validated as a reliable measure of hiring fit. No production automations are claimed here.

## Quick start

Requires Python 3.10+; standard library only.

```bash
python agents/job-research/score_jobs.py --jobs examples/sample_jobs.csv --profile examples/sample_profile.json --output results.csv
python -m unittest discover -s agents/job-research -p 'test_*.py'
```

The jobs are **synthetic examples**, not real vacancies. Manually verify eligibility, language, location and employment terms before applying.

## Structure

```text
agents/job-research/       Local matching prototype and unit tests
examples/                  Synthetic job listings and example skills
workflows/n8n/             Planned agent design
docs/                      Architecture, privacy and development roadmap
.github/workflows/         Automated Python unit-test configuration
```

## Design principles

- Human review before consequential decisions or job applications
- Privacy by default: no CVs, personal inbox contents, or credentials committed
- Traceable inputs, outputs, assumptions and limitations
- Honest maturity labels: planned, prototype, tested, deployed
- Business impact demonstrated with evidence, rather than unverified claims

## Skills demonstrated

Python · CSV/JSON processing · rule-based ranking · unit testing · workflow architecture · GitHub Actions · business process analysis

**Future focus:** n8n, AI-assisted research, email triage, reporting automation, APIs and business dashboards.

## Contact

[GitHub profile](https://github.com/BlessingSK1998) · Bremen, Germany
