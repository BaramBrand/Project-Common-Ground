# PCG automation boundary

PCG's initial automated workflow is deliberately small, public and read-only.

## What the first workflow does
- Runs Python standard-library tests on pull requests and pushes to main.
- Checks that the canonical charter, governance, research, security, roadmap and contribution documents remain present.
- Checks that independence, human stewardship, evidence classifications and security-reporting language are not accidentally removed.
- Uses a GitHub-hosted Ubuntu runner with contents:read permission and no API keys or repository write credentials.

## What it does not do
- It does not call external AI model providers or transmit repository content to an inference API.
- It does not run private SSC source, SSC proprietary business logic or AURORA private data.
- It does not create issues, edit files, merge pull requests, publish releases or deploy the website.
- It does not establish a nonprofit, board, membership organization, research partnership, grant award or scientific result.

## Future work
Future PCG research automation may ingest public sources such as arXiv, Crossref and public patent records, provided source terms and API policies are respected. Each item must retain source identity, publication date, retrieval date, evidence class, method, uncertainty, alternative explanations and rights metadata.

Publication, external representation, funding applications, partnerships, sensitive data handling and material governance changes remain subject to human stewardship. PCG remains institutionally distinct from SSC. Shared infrastructure must be approved, purpose-limited and documented.

## Usage
Run locally:
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_project_integrity.py
