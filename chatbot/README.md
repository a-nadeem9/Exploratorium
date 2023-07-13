# Chatbot

This is a simple chatbot project implemented using Python and the tflearn library. The chatbot is designed to handle various intents related to a shop, such as greetings, goodbyes, inquiries about business hours, accepted payments, etc., and respond accordingly.

## Description

The chatbot utilizes natural language processing (NLP) techniques to understand user inputs and generate appropriate responses. It uses the tflearn library to build a neural network model that can classify user queries into different intents. The chatbot learns from a set of predefined intents, patterns, and responses provided in the `intents.json` file.

The project involves the following steps:

1. **Data Preprocessing**: The chatbot preprocesses the data by tokenizing the patterns, applying stemming to reduce words to their base form, and converting them into numerical representations.

2. **Model Training**: The preprocessed data is used to train a neural network model. The model architecture consists of input and output layers with multiple hidden layers in between. The model is trained using the tflearn library, optimizing it to minimize the classification error.

3. **Chatbot Interaction**: Once the model is trained, the chatbot can interact with users. It takes user inputs, preprocesses them using the same techniques applied during training, and passes them through the trained model to predict the most appropriate intent. Based on the predicted intent, the chatbot generates relevant responses.


## Usage

1. Make sure you have the required dependencies installed.

2. Prepare the intents JSON file: `intents.json`. Customize the intents, patterns, and responses to suit your shop's needs. Here are some examples from the `intents.json` file:

- **Greeting**
  - Patterns: "Hi", "How are you", "Is anyone there?", "Hello", "Good day"
  - Responses: "Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"

- **Goodbye**
  - Patterns: "Bye", "See you later", "Goodbye"
  - Responses: "See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."

- **Thanks**
  - Patterns: "Thanks", "Thank you", "That's helpful"
  - Responses: "Happy to help!", "Any time!", "My pleasure"

- **Hours**
  - Patterns: "What hours are you open?", "What are your hours?", "When are you open?"
  - Responses: "We're open every day 9am-9pm", "Our hours are 9am-9pm every day"

- **Payments**
  - Patterns: "Do you take credit cards?", "Do you accept Mastercard?", "Are you cash only?"
  - Responses: "We accept VISA, Mastercard and AMEX", "We accept most major credit cards"

- **Opentoday**
  - Patterns: "Are you open today?", "When do you open today?", "What are your hours today?"
  - Responses: "We're open every day from 9am-9pm", "Our hours are 9am-9pm every day"

3. Run the chatbot by executing the following command:
   `python main.py`
   
4. Start a conversation with the chatbot by entering text inputs. Type "quit" to exit the chat.



