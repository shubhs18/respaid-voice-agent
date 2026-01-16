import json
import os
from openai import OpenAI

# --- Flags ---
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"

# --- OpenAI client (only used if MOCK_MODE = false) ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_system_prompt():
    with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def load_client_preset(client_name):
    with open("presets/clients.json", "r", encoding="utf-8") as f:
        clients = json.load(f)
    return clients[client_name]


def agent_reply(conversation_history, client_name="amazon_business"):
    preset = load_client_preset(client_name)

    # --- MOCK MODE (no API calls, safe demo & tests) ---
    if MOCK_MODE:
        last_user_message = conversation_history[-1]["content"].lower()

        if "robot" in last_user_message:
            body = (
                "Je suis un conseiller du service client, "
                "et je suis là pour vous aider de manière simple et respectueuse."
            )
        elif "payer" in last_user_message:
            body = (
                "Je comprends tout à fait. "
                "Nous pouvons envisager une solution ou un rappel ultérieur."
            )
        else:
            body = (
                "Je vous appelle concernant une situation administrative en cours. "
                "Nous pouvons en discuter tranquillement."
            )

        return f"{preset['greeting']} {body} {preset['closing']}"

    # --- LIVE MODE (requires OpenAI quota) ---
    system_prompt = load_system_prompt()

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "system",
            "content": (
                f"Greeting: {preset['greeting']}\n"
                f"Tone: {preset['tone']}\n"
                f"Closing: {preset['closing']}"
            )
        }
    ]

    for turn in conversation_history:
        messages.append(turn)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content
