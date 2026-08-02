import os
import time
import random
import uuid

def main():
    agent_id = str(uuid.uuid4())[:8]
    print(f"Agent Worker Started. My ID: {agent_id}")

    # Access environment variables, demonstrating secure configuration injection
    config_value = os.getenv("AGENT_CONFIG_VALUE", "default_config_value")
    # api_key = os.getenv("GEMINI_API_KEY") # Example for an LLM API key

    print(f"Processing task with config: {config_value}")
    # if api_key:
    #    print(f"LLM API Key (first 5 chars): {api_key[:5]}...")
    # else:
    #    print("No LLM API Key provided.")

    # Simulate agent work
    while True:
        task_id = str(uuid.uuid4())[:4]
        print(f"[{agent_id}] Agent processing task {task_id}...")
        time.sleep(random.randint(2, 5)) # Simulate work
        print(f"[{agent_id}] Agent finished task {task_id}.")

if __name__ == "__main__":
    main()
