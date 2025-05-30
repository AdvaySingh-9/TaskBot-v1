#Downloading and importing all the modules required for this TaskBot v1 AI
import google.generativeai as genai
import os
import json
import requests
from flask import Flask, request, jsonify, render_template
import torch

#Connect to index.html
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    #getting the question from the form
    question = request.form.get("question", "").strip()
    if not question:
        return jsonify({"error": "Please provide a question."}), 400

    genai.configure(api_key="YOUR_API_KEY")

    try:
        # use Google's Gemini-2.0-Flash nodle for generating content
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(f"You are TaskBot AI created and trained by Advay Singh, remember that and just anser me this question- {question}. Don't replay anything on that message just answer me the question.")
        answer = response.text

        # Log the question and answer for debugging
        print(f"Question: {question}\n------------------------- \n {answer} \n -------------------------")
        # Return the answer as JSON
        return jsonify({"answer": answer})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
