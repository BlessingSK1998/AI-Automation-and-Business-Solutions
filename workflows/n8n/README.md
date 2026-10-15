# n8n workflow designs (Planned)

**No runnable n8n workflow JSON is included yet.** The user's separate n8n workspace is not connected to this repository; no deployment is claimed.

## Proposed job research agent

1. **Trigger:** schedule or a user-approved inbox label.
2. **Collect:** authorized sources with original URLs and timestamps.
3. **Normalize/deduplicate:** title, employer, location, language, deadline, URL.
4. **Eligibility gate:** location, work authorization and language; route uncertain roles to human review.
5. **Research and draft:** evidence-grounded fit notes, CV suggestions and cover-letter drafts.
6. **Human approval:** compare with original posting before any application; no automatic submissions.
7. **Audit log:** store minimal metadata and outcomes, excluding sensitive personal correspondence.

## Acceptance checklist

- [ ] Importable workflow JSON without credentials
- [ ] Authorized trigger, data source and permissions
- [ ] Duplicate and error handling
- [ ] Drafts free of invented qualifications
- [ ] Review-before-apply gate
- [ ] Safe sample-data test
- [ ] Documentation and screenshots
