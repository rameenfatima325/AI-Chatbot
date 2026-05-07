# ✦ ChatBot AI

A sleek, dark-themed AI chatbot built with Flask and Google Gemini 2.5 Flash. Switch between multiple personalities, define your own custom persona, and keep a full persistent chat history, all in a clean, modern UI.


## Features
- 4 Built-in Personalities:Friendly, Professional, Funny, Sarcastic
- Custom Personality: Define any persona you want
- Chat History: Persisted in the browser, grouped by Today / Yesterday / Older
- Multi-turn Conversations: Full context sent with every message
- Responsive Design: Works on desktop and mobile
- Gemini 2.5 Flash: Fast, capable AI responses


## Getting Started

### Prerequisites

- Python 3.8 or higher
- A free Google Gemini API key → [Get one here](https://aistudio.google.com/app/apikey)


### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root of the project:

```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the app

```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**


## Usage

1. Choose a personality from the sidebar: Friendly, Professional, Funny, or Sarcastic
2. Custom mode: click Custom, describe any persona, hit Apply ✓, then start chatting
3. Chat history is saved automatically in your browser and grouped by date
4. Click any past chat in the sidebar to reload it, or hit New Chat to start fresh


## Environment Variables

| Variable | Description |
--------------------------
| `GEMINI_API_KEY` | Your Google Gemini API key (required) |


## Dependencies

| Package | Purpose |
---------------------
| `flask` | Web framework |
| `google-generativeai` | Gemini API client |
| `python-dotenv` | Load `.env` variables |


## Troubleshooting

**`API key not found` error**
Make sure your `.env` file is in the same folder as `app.py` and contains `GEMINI_API_KEY=your_key`.

**`ModuleNotFoundError`**
Run `pip install -r requirements.txt` and make sure your virtual environment is activated.

**Port already in use**
Change the port in `app.py`: `app.run(debug=True, port=5001)`
