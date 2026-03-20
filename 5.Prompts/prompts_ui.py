from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1"
)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

# Prompt Template
# template = PromptTemplate(
#     template="""
# You are an AI research assistant.

# Explain the research paper: {paper_input}

# Explanation Style: {style_input}
# Explanation Length: {length_input}

# Provide a clear explanation according to the selected style and length.
# """,
#     input_variables=["paper_input", "style_input", "length_input"],
# )

template = load_prompt('template.json')

## now there is nthg problm but we r using the two invoke function we can replace it with single invoke function
# if st.button("Summarize"):

#     prompt = template.invoke(
#         {
#             "paper_input": paper_input,
#             "style_input": style_input,
#             "length_input": length_input,
#         }
#     )

#     result = model.invoke(prompt)

# single time invoking 
if st.button("Summarize"):
    chain = template | model 
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,     
    })
    st.write(result.content)