import requests

# Replace with your own API key and search engine ID
API_KEY = "YOUR_GOOGLE_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! It's nice to chat with you. How can I assist you today?"

    # Asking about well-being
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm here to help! How are you doing?"

    # Asking about the chatbot's name
    elif "your name" in user_input:
        return "I'm a friendly chatbot created by coder subham. You can ask me anything about Python or how I was built!"

    # Asking about Python
    elif "what is python" in user_input:
        return ("Python is a versatile, high-level programming language that emphasizes code readability. "
                "It's widely used for web development, data analysis, artificial intelligence, and more. "
                "What would you like to learn about Python?")

    # Asking for help with Python topics
    elif "help with python" in user_input:
        return ("Sure! I can help with basic Python concepts like loops, functions, or data structures. "
                "What specific topic would you like to learn more about?")

    # Asking about how the chatbot was built
    elif "how were you built" in user_input:
        return ("I was built using Python, with a simple rule-based logic to handle different user inputs. "
                "My responses are based on predefined patterns. You can also create a more advanced chatbot "
                "using machine learning or natural language processing libraries!")

    # Saying goodbye
    elif "bye" in user_input:
        return "Goodbye! It was great talking to you. Feel free to chat with me anytime!"
    

    # Default response with a Google search
    else:
        return google_search(user_input)

def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        # Return the title and link of the first search result
        result = data['items'][0]
        title = result['title']
        link = result['link']
        return f"I found something that might help: {title}\n{link}"
    else:
        return "I'm sorry, I couldn't find any relevant information on the web."

if __name__ == "__main__":
    print("Chatbot: Hello! I am your Python chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
