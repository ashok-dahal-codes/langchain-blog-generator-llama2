# BlogCraft AI — Llama 2 Blog Generator

A Streamlit-based AI blog generation application powered by Llama 2 7B running locally through llama.cpp. The application uses LangChain for prompt management and provides an interface for generating blog posts for different audiences.

> No OpenAI API key is required. The application uses a GGUF version of Llama 2 for local inference.
## If Everything works perfectly you would get the result as below: 
### some waiting time is cut on the video below, expect high or low waiting time based on CPU specifications : 
https://github.com/user-attachments/assets/149c6ea2-77f7-442d-b26d-d71ec5ba0589

## Features




- Generate blog posts from any topic
- Powered by Llama 2 7B
- GGUF Q4_K_M quantized model
- LangChain prompt management
- Streamlit web interface
- Select target audience:
  - Researchers
  - Data Scientists
  - Common People
- Specify approximate word count
- Download generated blogs as `.txt`
- Local LLM inference using llama.cpp

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| Llama 2 7B | Text generation |
| GGUF Q4_K_M | Model quantization |
| llama.cpp | Local model inference |
| llama-cpp-python | Python bindings for llama.cpp |
| LangChain | Prompt management |


## Project Structure

```text
Blog Generation/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── models/
    └── llama-2-7b-chat.Q4_K_M.gguf
```

The GGUF model should not be committed to GitHub because it is several GB in size.



## How It Works

```text
User enters topic
        |
        v
Selects word count
        |
        v
Selects target audience
        |
        v
LangChain PromptTemplate
        |
        v
Llama 2 7B
        |
        v
llama.cpp
        |
        v
Generated blog
        |
        v
Streamlit interface
```

The model receives the blog topic, target audience, desired word count, and writing requirements through a LangChain prompt template.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd "Blog Generation"
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Model Setup

This project uses:

```text
Llama 2 7B Chat
llama-2-7b-chat.Q4_K_M.gguf
```

For local development, place the model inside:

```text
models/
└── llama-2-7b-chat.Q4_K_M.gguf
```

Make sure you obtain the model from a legitimate source and comply with the applicable Llama 2 license terms.

## Run Locally

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Using the Application

### 1. Enter a blog topic

Example:

```text
The Future of Artificial Intelligence
```

### 2. Select the approximate word count

Example:

```text
300
```

### 3. Select the target audience

Available options:

```text
Researchers
Data Scientists
Common People
```

### 4. Generate the blog

Click:

```text
Generate Blog
```

The Llama 2 model will generate the blog based on the selected options.

The generated blog can be downloaded as a text file.

## Model Configuration

The model is configured in `app.py`:

```python
llm = LlamaCpp(
    model_path=model_path,
    max_tokens=256,
    temperature=0.7,
    n_ctx=1024,
    n_batch=32,
    n_threads=2,
    streaming=False,
    verbose=False
)
```

### Parameters

| Parameter | Description |
|---|---|
| `max_tokens` | Maximum number of generated tokens |
| `temperature` | Controls generation randomness |
| `n_ctx` | Context window |
| `n_batch` | Number of tokens processed in a batch |
| `n_threads` | Number of CPU threads used |
| `streaming` | Enables or disables token streaming |

CPU inference can be relatively slow depending on the hardware.



The application will be available at:

```text
http://localhost:7860
```
                    v


The application can download the model using:

```python
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="YOUR_USERNAME/llama-2-7b-chat-q4-k-m",
    filename="llama-2-7b-chat.Q4_K_M.gguf"
)
```

This prevents the multi-GB model from being stored inside the application repository.

## API Keys

This project does not require an OpenAI API key.

The inference pipeline is:

```text
Streamlit
    |
    v
LangChain
    |
    v
LlamaCpp
    |
    v
Llama 2 GGUF
```

The model runs through llama.cpp rather than an external LLM API.

## Performance

Llama 2 7B is a relatively large model for CPU inference.

Performance depends on:

- CPU
- Available RAM
- Number of CPU threads
- Context size
- Batch size
- Model quantization

The Q4_K_M quantization reduces the model's memory requirements compared with higher-precision versions, but CPU generation can still take time.

## Git Configuration

Do not commit the following files or directories:

```text
venv/
.venv/
models/
.env
.env.*
__pycache__/
*.pyc
```

Recommended `.gitignore`:

```gitignore
venv/
.venv/
__pycache__/
*.pyc

.env
.env.*

models/
```

The `models/` directory is excluded because the GGUF model is too large for a normal source-code repository.

## Requirements

The main dependencies are:

```text
streamlit
langchain
langchain-core
langchain-community
llama-cpp-python
huggingface-hub
```

Install them with:

```bash
pip install -r requirements.txt
```

## Future Improvements

- Streaming token generation
- Multiple LLM model choices
- Blog title generation
- Blog outline generation
- SEO keyword generation
- Meta description generation
- Tone selection
- Additional writing styles
- Markdown export
- PDF export
- DOCX export
- GPU acceleration
- User authentication
- Blog history
- Database integration

## License

This project uses Llama 2.

The Llama 2 model is subject to Meta's applicable license and acceptable-use requirements. Users are responsible for obtaining the model legally and complying with its license terms.

The application code and the model are separate components and may have different licensing terms.
