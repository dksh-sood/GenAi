from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are an AI research assistant.

Explain the research paper: {paper_input}

Explanation Style: {style_input}
Explanation Length: {length_input}

Provide a clear explanation according to the selected style and length.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save('template.json')