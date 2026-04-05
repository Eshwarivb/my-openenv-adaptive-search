from fastapi import FastAPI
from env import GuessEnv

app = FastAPI()
env = None

@app.get("/")
def home():
    return {"message": "running"}

@app.post("/reset")
def reset():
    global env
    env = GuessEnv(1, 100)
    env.reset()
    return {"observation": "start"}

@app.post("/step")
def step(action: int):
    global env
    result = env.step(action)
    return {
        "observation": result["observation"],
        "reward": float(result.get("reward", 0.0)),
        "done": result["done"]
    }
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
