import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hey there! How can I help you today?"
    
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "Goodbye! Have a great day!"

    
    elif re.search(r"\b(time|current time|what time is it)\b", user_input):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    
    elif re.search(r"\b(weather|forecast)\b", user_input):
        return "I can't check the weather right now, but you can try looking it up online!"
    
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

def main():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
