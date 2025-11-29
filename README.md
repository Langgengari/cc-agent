# CCAgent | Code Chronicler Agent

**CCAgent** is an AI-powered agent that analyzes source code
repositories to automatically generate **technical documentation** and
**architecture diagrams**. It was designed to help developers, teams,
and reviewers quickly understand complex projects with minimal manual
effort.

> "From source code to knowledge."

------------------------------------------------------------------------

## ✨ Features

-   🔍 Automatic source code analysis
-   📝 Technical documentation generation
-   🗺️ Architecture and flow diagrams generation
-   🤖 Integration with Google ADK agents
-   🔐 Support for private repositories (via GitLab tokens)

------------------------------------------------------------------------

## 🏗️ Project Architecture

    ccagent/
    ├── agent/
    ├── services/
    ├── tools/
    ├── config/
    └── assets/

------------------------------------------------------------------------

## 🚀 Getting Started

### Prerequisites

-   Python \>= 3.10 \< 4.0
-   Git
-   Poetry

### Clone the repository

``` bash
git clone https://github.com/SEU-USUARIO/ccagent.git
cd ccagent
```

### Install dependencies

``` bash
poetry install
```

### Activate the virtual environment

``` bash
poetry shell
```

### Configure environment variables

Create a `.env` file:

``` env
GITLAB_TOKEN=your_token_here
GOOGLE_GENAI_USE_VERTEXAI=your_vertexai_here
GOOGLE_API_KEY=your_google_api_key_here
```

### Run the project

``` bash
adk web --port 8000
```

------------------------------------------------------------------------

## 📄 License

MIT License

------------------------------------------------------------------------


