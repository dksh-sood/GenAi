# LangChain Practice Repository

This repository contains small LangChain examples organized by topic.

It is meant for learning and testing:

- LLM basics
- Chat models
- Chains
- Embeddings
- Output parsers
- Prompts
- Runnables

## Project Structure

- `1.LLMs/` - basic LLM example
- `2.ChatModels/` - chat model examples for OpenAI-compatible models, Gemini, and Hugging Face
- `3.chain/` - simple, sequential, parallel, and conditional chains
- `3.EmbeddedModels/` - embedding and similarity examples
- `4.output/` - structured and unstructured output parsing
- `5.Prompts/` - prompt templates, messages, placeholders, and a small UI example
- `6.Runnables/` - runnable primitives and notebook-based runnable examples

## Requirements

Install Python 3.10+ and then install dependencies:

```bash
pip install -r requirements.txt
```

If you want to run the UI example in `5.Prompts/prompts_ui.py`, install Streamlit too:

```bash
pip install streamlit
```

## Environment Setup

Create a `.env` file in the project root and add the API keys needed for the examples you want to run.

Common variables:

```env
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
HUGGINGFACEHUB_API_TOKEN=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

Note:

- Many scripts use `ChatOpenAI` with the OpenRouter base URL.
- For those scripts, use an OpenAI-compatible key in `OPENAI_API_KEY` if you are routing through OpenRouter.

## How To Run

Run any script directly from the project root:

```bash
python "1.LLMs/1_llm_demo.py"
python "3.chain/simple_chain.py"
python "4.output/unstructured_output/json_output_parser.py"
```

Run the prompt UI example with:

```bash
streamlit run "5.Prompts/prompts_ui.py"
```

Open the runnable notebooks in Jupyter if you want to explore the notebook-based examples.

## What This Repo Covers

This repo is useful if you want simple examples of:

- calling models with LangChain
- building prompt pipelines
- creating basic chains
- working with embeddings
- parsing model output into JSON or Pydantic schemas
- using LangChain runnable primitives

## Notes

- Most files are standalone practice scripts.
- Some examples are rough learning experiments, so model names and code style may vary across files.
