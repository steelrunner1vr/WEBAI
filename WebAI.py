import re
import speech_recognition as sr
import datetime
import webbrowser
import time
import wikipedia
from gtts import gTTS
import pygame
import os
import urllib.parse
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the AI server!"

@app.route("/process", methods=["POST"])
def process():
    statement = request.form.get("statement")
    if statement:
        if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
            return "See you later!"

        if 'open youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            return "YouTube is now open"

        elif "open peter's channel" in statement:
            webbrowser.open_new_tab("https://www.youtube.com/@hunterfour4971")
            return "Opening Hunter 4 on YouTube"

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            return "Google Chrome is open now"

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            return "Google Mail is open now"

        elif 'tell me about' in statement:
            query = statement.replace("tell me about", "").strip()
            try:
                summary = wikipedia.summary(query, sentences=2)
                return summary
            except wikipedia.exceptions.DisambiguationError:
                return "There are multiple options for this query. Please provide more specific information."
            except wikipedia.exceptions.PageError:
                search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
                webbrowser.open_new_tab(search_url)
                return f"I couldn't find any information about {query}. Here are the search results."

        elif 'search' in statement:
            query = statement.replace("search", "").strip()
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            webbrowser.open_new_tab(search_url)
            return f"Here are the search results for {query}."

        elif 'what time is it' in statement:
            current_time = datetime.datetime.now()
            time_string = current_time.strftime("%I:%M %p")
            return f"The current time is {time_string}"

    return ""

if __name__ == '__main__':
    app.run()
