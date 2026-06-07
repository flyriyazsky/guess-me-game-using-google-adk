import ollama

message = []

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
    try:
        # guess = int(user_input)
        message.append({"role": "user", "content": user_input})
        response = ollama.chat(model="qwen2.5-coder:1.5b", messages=message)
        print(f"Agent: {response['message']['content']}")
        message.append({"role": "assistant", "content": response['message']['content']})
    except ValueError:
        print("Please enter a valid integer guess or 'exit' to quit.")
