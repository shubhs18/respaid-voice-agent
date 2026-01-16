Respaid – French Voice Collections Agent

This repository contains a French voice collections agent designed for respectful, brand-safe debt recovery, along with a pre-flight self-test harness and a one-command demo.

The system is designed to be safe to try, configurable per client, and runnable locally in minutes.

✨ Features

🇫🇷 French-only agent (call path)

🤝 Polite, concise, non-threatening tone

🧠 Handles:

Identification

Payment deferral

Confusion recovery

“Vous êtes un robot ?” (brand-safe response)

🧩 Client presets via JSON (tone & phrasing)

🧪 Automatic self-test harness

🎬 One-command demo

🔒 Mock mode for safe demos without API credits

📁 Project Structure
respaid-voice-agent/
│
├── agent/
│   └── agent.py              # Core agent logic
│
├── presets/
│   └── clients.json          # Client-specific tone & phrasing
│
├── prompts/
│   └── system_prompt.txt     # Global agent instructions
│
├── tests/
│   └── test_agent.py         # Pre-flight test harness
│
├── reports/
│   └── summary.md            # Example test summary report
│
├── demo.py                   # One-command demo (end-to-end call)
├── requirements.txt          # Dependencies
└── README.md

⚙️ Setup (2 minutes)
1. Create & activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

2. Install dependencies
pip install openai

🚀 Running the Demo (Recommended: Mock Mode)

Mock mode runs the full agent flow without calling OpenAI (no billing required).

export MOCK_MODE=true
export PYTHONPATH=.
python demo.py


You’ll see a turn-by-turn French call simulation with response times.

🤖 Live Mode (Optional)

If you want to run with a real LLM:

export MOCK_MODE=false
export OPENAI_API_KEY=your_api_key_here
export PYTHONPATH=.
python demo.py


⚠️ Requires an OpenAI key with available quota.

🧪 Pre-flight Self-Test Harness

Runs multiple synthetic conversations before any real call.

export MOCK_MODE=true
export PYTHONPATH=.
python tests/test_agent.py

Example scenarios tested:

Identity verification

Payment deferral

User confusion

“Vous êtes un robot ?”

🧩 Client Presets

Client-specific tone and phrasing are defined in:

presets/clients.json


Example:

{
  "amazon_business": {
    "greeting": "Bonjour, je vous appelle au nom d’Amazon Business.",
    "tone": "very_polite",
    "closing": "Merci pour votre temps. Excellente journée."
  }
}


Changing one field automatically updates agent behavior.

📊 Summary Report

A sample one-page summary is included in:

reports/summary.md


It documents:

Scenarios tested

Success rate

Notable behaviors

Example transcripts

🔐 Privacy & Safety

No real debtor data

No personal data stored

Mock mode prevents accidental live calls

Brand-safe, non-threatening language only

📝 Notes for Reviewers

Mock mode is enabled by default for safe local testing

Live mode uses the same code path, only swapping the response generator

Designed to be production-ready with minimal changes (voice / telephony layer)