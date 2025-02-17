from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# OpenAI API Key
openai.api_key = "your-openai-api-key"  # Replace with your OpenAI API key

# Chatbot endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # Get JSON data from the client
    user_input = data.get("message", "")  # Get the user input message

    if not user_input:
        return jsonify({"error": "Message is required!"}), 400

    try:
        # OpenAI GPT API call
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use "gpt-4" if available
            prompt=f"Du bist ein hilfreicher Assistent, der auf Deutsch antwortet. Frage: {user_input}",
            max_tokens=150,
            temperature=0.7
        )
        bot_response = response.choices[0].text.strip()
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
