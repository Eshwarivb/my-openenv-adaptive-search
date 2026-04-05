from fastapi import FastAPI
from env import GuessEnv

app = FastAPI()

env = None

@app.get("/")
def home():
    return {"message": "OpenEnv API running"}


@app.post("/reset")
def reset():
    global env
    env = GuessEnv(1, 100)
    obs = env.reset()
    return {"observation": obs}


@app.post("/step")
def step(action: int):
    global env
    result = env.step(action)
    return result
