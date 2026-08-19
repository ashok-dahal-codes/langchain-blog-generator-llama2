from pathlib import Path 

import streamlit as st 
from langchain_core.prompts import PromptTemplate 
from langchain_community.llms import LlamaCpp 


# --------------------------------------------------------- 
# PAGE CONFIG 
# --------------------------------------------------------- 

st.set_page_config( 
    page_title="BlogCraft AI", 
    page_icon="✍️", 
    layout="wide", 
    initial_sidebar_state="expanded" 
) 


# --------------------------------------------------------- 
# CUSTOM CSS 
# --------------------------------------------------------- 

st.markdown(""" 
<style> 

    /* Main background */ 
    .stApp { 
        background: #f7f8fc; 
    } 

    .block-container { 
        padding-top: 2rem; 
        padding-bottom: 3rem; 
        max-width: 1200px; 
    } 

    /* Hero */ 
    .hero { 
        background: linear-gradient( 
            135deg, 
            #111827 0%, 
            #312e81 50%, 
            #4f46e5 100% 
        ); 
        padding: 45px 50px; 
        border-radius: 24px; 
        margin-bottom: 30px; 
        color: white; 
    } 

    .hero h1 { 
        font-size: 3rem; 
        font-weight: 800; 
        margin-bottom: 10px; 
    } 

    .hero p { 
        font-size: 1.15rem; 
        opacity: 0.85; 
        max-width: 700px; 
    } 

    /* Section title */ 
    .section-title { 
        font-size: 1.4rem; 
        font-weight: 700; 
        color: #111827; 
        margin-top: 15px; 
        margin-bottom: 12px; 
    } 

    /* Input labels */ 
    label { 
        font-weight: 600 !important; 
        color: #374151 !important; 
    } 

    /* Inputs */ 
    .stTextInput input, 
    .stNumberInput input { 
        border-radius: 12px; 
        border: 1px solid #d1d5db; 
        padding: 12px; 
    } 

    /* Select box */ 
    .stSelectbox div[data-baseweb="select"] > div { 
        border-radius: 12px; 
    } 

    /* Generate button */ 
    .stButton > button { 
        width: 100%; 
        border-radius: 12px; 
        padding: 12px 20px; 
        font-size: 1rem; 
        font-weight: 700; 
        border: none; 
        background: #4f46e5; 
        color: white; 
        transition: all 0.2s ease; 
    } 

    .stButton > button:hover { 
        background: #4338ca; 
        transform: translateY(-1px); 
    } 

    /* Output card — target the real container wrapper */ 
    .st-key-blog_output { 
        background: white; 
        padding: 30px; 
        border-radius: 18px; 
        border: 1px solid #e5e7eb; 
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05); 
        margin-top: 25px; 
    } 

    /* Generated blog text */ 
    .st-key-blog_output p, 
    .st-key-blog_output h1, 
    .st-key-blog_output h2, 
    .st-key-blog_output h3, 
    .st-key-blog_output h4, 
    .st-key-blog_output li, 
    .st-key-blog_output strong, 
    .st-key-blog_output em, 
    .st-key-blog_output span { 
        color: #111827 !important; 
    } 

    /* Output header */ 
    .output-header { 
        font-size: 1.5rem; 
        font-weight: 750; 
        color: #111827 !important; 
        margin-bottom: 15px; 
    } 

    /* Spinner text */ 
    [data-testid="stSpinner"], 
    [data-testid="stSpinner"] p { 
        color: #111827 !important; 
    } 

    /* Sidebar */ 
    section[data-testid="stSidebar"] { 
        background: #111827; 
    } 

    section[data-testid="stSidebar"] * { 
        color: white; 
    } 

    /* Divider */ 
    hr { 
        border: none; 
        border-top: 1px solid #e5e7eb; 
        margin: 25px 0; 
    } 

</style> 
""", unsafe_allow_html=True) 

# --------------------------------------------------------- 
# LOAD MODEL 
# --------------------------------------------------------- 

@st.cache_resource 
def load_model(): 

    llm = LlamaCpp( 
        model_path=str( 
            Path(__file__).resolve().parent 
            / "models" 
            / "llama-2-7b-chat.Q4_K_M.gguf" 
        ), 

        max_tokens=256, 
        temperature=0.7, 

        n_ctx=1024, 
        n_batch=32, 
        n_threads=2, 

        streaming=False, 

        verbose=False 
    ) 

    return llm 


# --------------------------------------------------------- 
# GENERATE BLOG 
# --------------------------------------------------------- 

def get_llama_response(input_text, no_words, blog_style): 

    llm = load_model() 

    template = """ 
You are an expert blog writer. 

Write a high-quality blog about: 

Topic: {input_text} 

Target audience: {blog_style} 

Approximate length: {no_words} words. 

Requirements: 
- Give the blog a suitable title. 
- Use clear paragraphs. 
- Make the content informative and engaging. 
- Match the writing style to the target audience. 
- Avoid unnecessary repetition. 
- Do not explain the instructions. 
- Output only the blog. 

Blog: 
""" 

    prompt = PromptTemplate( 
        input_variables=[ 
            "input_text", 
            "blog_style", 
            "no_words" 
        ], 
        template=template 
    ) 

    final_prompt = prompt.format( 
        input_text=input_text, 
        blog_style=blog_style, 
        no_words=no_words 
    ) 

    response = llm.invoke(final_prompt) 

    return response 


# --------------------------------------------------------- 
# SIDEBAR 
# --------------------------------------------------------- 

with st.sidebar: 

    st.markdown("## ✍️ BlogCraft AI") 

    st.markdown( 
        "Generate blog content locally using " 
        "Llama 2." 
    ) 

    st.divider() 

    st.markdown("### ⚙️ Model") 

    st.markdown( 
        """ 
        **Model:** Llama 2 7B   
        **Quantization:** Q4_K_M   
        **Runtime:** llama.cpp   
        **Mode:** Local 
        """ 
    ) 

    st.divider() 

    st.markdown("### 💡 Tips") 

    st.markdown( 
        """ 
        - Use a specific topic 
        - Choose the appropriate audience 
        - 300–700 words works well 
        - Generation may take time on CPU 
        """ 
    ) 


# --------------------------------------------------------- 
# HERO 
# --------------------------------------------------------- 

st.markdown(""" 
<div class="hero"> 

    <h1>✍️ BlogCraft AI</h1> 

    <p> 
        Create informative and engaging blog posts using 
        a locally running Llama 2 language model. 
        No API key required. 
    </p> 

</div> 
""", unsafe_allow_html=True) 


# --------------------------------------------------------- 
# INPUT SECTION 
# --------------------------------------------------------- 

st.markdown( 
    '<div class="section-title">Create your blog</div>', 
    unsafe_allow_html=True 
) 

input_text = st.text_input( 
    "Blog Topic", 
    placeholder="e.g. The future of Artificial Intelligence in healthcare" 
) 


col1, col2 = st.columns(2) 

with col1: 

    no_words = st.number_input( 
        "Approximate Word Count", 
        min_value=50, 
        max_value=2000, 
        value=300, 
        step=50 
    ) 


with col2: 

    blog_style = st.selectbox( 
        "Target Audience", 
        [ 
            "Researchers", 
            "Data Scientists", 
            "Common People" 
        ] 
    ) 


st.write("") 


# --------------------------------------------------------- 
# GENERATE BUTTON 
# --------------------------------------------------------- 

generate = st.button( 
    "✨ Generate Blog" 
) 


# --------------------------------------------------------- 
# GENERATION 
# --------------------------------------------------------- 

if generate: 

    if not input_text.strip(): 

        st.warning( 
            "Please enter a topic before generating your blog." 
        ) 

    else: 

        with st.spinner( 
            "🤖 Llama 2 is writing your blog..." 
        ): 
            try: 
                response = get_llama_response( 
                    input_text, 
                    no_words, 
                    blog_style 
                ) 
            except Exception as error: 
                st.error( 
                    "The model could not generate a response. " 
                    f"Check the terminal for details: {error}" 
                ) 
                st.stop() 

        with st.container(key="blog_output"): 

            st.markdown( 
                '<div class="output-header">' 
                '📝 Generated Blog' 
                '</div>', 
                unsafe_allow_html=True 
            ) 

            st.markdown(response) 

        st.download_button( 
            label="📥 Download Blog", 
            data=response, 
            file_name="generated_blog.txt", 
            mime="text/plain" 
        )