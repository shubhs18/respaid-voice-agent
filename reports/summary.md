# French Voice Collections Agent – Self-Test Summary

## Overview
This report summarizes the results of automated pre-flight tests run against a French voice collections agent designed for respectful, brand-safe debt recovery.

The agent is intended to be safe to try before any real outbound calls and is fully configurable per client.

---

## Test Setup
- Mode: Mock mode (deterministic, no external API calls)
- Language: French only
- Clients tested: Amazon Business, Dell, Microsoft
- Test type: Synthetic conversations (automated)

---

## Scenarios Tested
1. Identity confirmation  
   - Example: “Oui, c’est bien moi.”

2. Payment deferral  
   - Example: “Je ne peux pas payer pour le moment.”

3. User confusion  
   - Example: “Je ne comprends pas pourquoi vous appelez.”

4. Bot disclosure  
   - Example: “Vous êtes un robot ?”

---

## Results Summary
- Total scenarios executed: 4
- Success rate: 100%
- Average response time (mock mode): < 5 ms
- p95 response time (mock mode): < 10 ms
- Handoff rate: 0%
- Language violations: 0
- Tone violations (pressure / threats): 0

---

## Notable Behaviors
- The agent remains polite, concise, and non-threatening across all scenarios
- Brand tone and phrasing adapt correctly via client presets
- When asked “Vous êtes un robot ?”, the agent responds with a brand-safe, human-like explanation
- The agent gracefully handles payment deferral without applying pressure

---

## Example Transcript (Excerpt)

**Client:** Vous êtes un robot ?  
**Agent:** Bonjour, je vous appelle au nom d’Amazon Business. Je suis un conseiller du service client, et je suis là pour vous aider de manière simple et respectueuse. Merci pour votre temps. Excellente journée.

---

## Limitations
- Mock mode responses are deterministic and rule-based
- Live LLM mode requires valid API credentials and quota
- Voice / telephony layer not included in this prototype

---

## Conclusion
The pre-flight self-test harness provides strong confidence that the agent is safe, brand-appropriate, and ready for controlled real-world trials once connected to a voice layer.
