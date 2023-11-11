import random
chatgpt_faqs = {
    "what is chatgpt?": "ChatGPT is a language model developed by OpenAI that is designed for natural language conversation. It can answer questions, generate text, and have interactive discussions with users.",
    "how does chatgpt work?": "ChatGPT is powered by a deep learning model called GPT (Generative Pre-trained Transformer). It's trained on a large corpus of text from the internet and uses that knowledge to generate human-like text based on input.",
    "what can i do with chatgpt?": "You can use ChatGPT for a variety of tasks, such as answering questions, generating text, creating content, providing recommendations, and much more.",
    "is chatgpt free to use?": "OpenAI offers both free and paid access to ChatGPT. There may be usage limitations on the free tier, and you can check OpenAI's pricing for more details.",
    "what is prompt engineering?": "Prompt engineering is the process of designing specific instructions or questions to obtain desired responses from a language model like ChatGPT. It involves crafting prompts to be clear and effective in conveying your intent.",
}
rules = {
    "hello": ["Hi there!", "Hello!", "How can I help you today?"],
    "how are you": ["I'm just a computer program, so I don't have feelings, but thanks for asking! How can I assist you?", "I'm here to help. What can I do for you?"],
    "bye": ["Goodbye!", "Have a great day!", "See you later!"],
    "help": ["You can ask me questions or say hello. If you want to exit, just type 'bye'."],
}
def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()
    if user_input_lower in chatgpt_faqs:
        return chatgpt_faqs[user_input_lower]
    elif user_input_lower in rules:
        return random.choice(rules[user_input_lower])
    else:
        return "I'm not sure I understand. Can you please rephrase your question or greeting?"
print("Chatbot: Hi! I'm your friendly chatbot. You can start a conversation with me or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)