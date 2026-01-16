from agent.agent import respond

def test_basic_response():
    reply = respond("Bonjour")
    assert "Bonjour" in reply

if __name__ == "__main__":
    test_basic_response()
    print("✅ All tests passed")
