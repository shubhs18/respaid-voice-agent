from agent.agent import agent_reply
import time

def run_demo(client_name="amazon_business"):
    conversation = []

    user_inputs = [
        "Bonjour",
        "Oui, c’est bien moi.",
        "Je ne peux pas payer pour le moment.",
        "Vous êtes un robot ?"
    ]

    print("\n--- DÉMO D’APPEL (FR) ---\n")

    for user_input in user_inputs:
        print(f"Client: {user_input}")
        conversation.append({"role": "user", "content": user_input})

        start = time.time()
        reply = agent_reply(conversation, client_name=client_name)
        latency = round((time.time() - start) * 1000, 2)

        conversation.append({"role": "assistant", "content": reply})
        print(f"Agent: {reply}")
        print(f"(response time: {latency} ms)\n")

if __name__ == "__main__":
    run_demo()
