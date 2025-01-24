import openai

openai.api_key = "sk-1234567890abcdef1234567890abcdef"

messages = []

# Get the system message
system_message = input("What subject would you like to talk about? ")
messages.append({"role": "system", "content": system_message})

print("You are now talking about", system_message)

# Start the conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":  # Exit condition
        print("Goodbye!")
        break

    # Add user message to the conversation
    messages.append({"role": "user", "content": user_input})

    # Generate a response using OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure this matches the model you want to use
            messages=messages
        )
        ai_reply = response["choices"][0]["message"]["content"]
        print("Assistant:", ai_reply)
        messages.append({"role": "assistant", "content": ai_reply})

    except Exception as e:  # General exception handling
        print(f"An error occurred: {e}")
