import random
from fastapi import FastAPI

app = FastAPI()

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "I would tell you a UDP joke, but you might not get it.",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'"
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Random Joke API! Visit /joke to get a joke."}

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(jokes)}
