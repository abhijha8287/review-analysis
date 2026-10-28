# Review Analysis

A Streamlit app that turns a free-text review into sentiment, themes, pros, cons and a summary.

## Why this exists
First of three versions exploring LangChain structured output. This one uses `with_structured_output` with a TypedDict schema. See also [reviewanalysis2](https://github.com/abhijha8287/reviewanalysis2) (Pydantic) and [reviewanalysisjson](https://github.com/abhijha8287/reviewanalysisjson) (JSON Schema).

## What it does
- Takes a product or service review
- Returns sentiment, key themes, pros, cons and a short summary as structured fields
- Displays each field separately in the app

## Project structure
```
review-analysis/
├── withstrucuteoutput.py  Streamlit app and LangChain chain
└── requirements.txt       Python dependencies
```

## Getting started
Requirements: Python 3.10+, an OpenAI API key.
```bash
git clone https://github.com/abhijha8287/review-analysis.git
cd review-analysis
pip install -r requirements.txt streamlit
mkdir -p .streamlit && echo 'api_key = "sk-..."' > .streamlit/secrets.toml
streamlit run withstrucuteoutput.py
```

## Configuration
| Variable | Purpose |
|:--|:--|
| `api_key` in `.streamlit/secrets.toml` | OpenAI API key |

## Tech stack
Python, LangChain, OpenAI GPT-4, Streamlit

## Notes
Live demo: https://reviewanalysisbyabhishek.streamlit.app (on the free Streamlit tier it may take a few seconds to wake up). `requirements.txt` lists more LangChain integrations than the app uses; only OpenAI is needed.
