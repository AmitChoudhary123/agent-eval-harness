# Contributing

Agent Eval Harness welcomes contributions that make AI evaluation more practical, transparent, and useful for enterprise teams.

## Good contributions

- New benchmark packs under `data/`
- New metric profiles under `configs/profiles/`
- New scoring dimensions with tests
- Report exporters for Markdown, HTML, or JSON
- Docs that help teams design better AI release gates

## Contribution standard

Every meaningful change should include:

- A clear evaluation problem being solved
- Tests for scoring or report behavior
- A sample benchmark row when adding a metric
- No dependency on paid APIs for default tests

## Local validation

```bash
pip install -r requirements.txt
pytest -q
python demo/run_demo.py
```