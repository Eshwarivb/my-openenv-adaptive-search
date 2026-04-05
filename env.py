import random

class GuessEnv:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.target = None
        self.steps = 0
        self.done = False

    def reset(self):
        self.target = random.randint(self.low, self.high)
        self.steps = 0
        self.done = False
        return {
            "observation": "Start guessing",
            "reward": 0,
            "done": False,
            "info": {}
        }

    def step(self, action):
        if self.done:
            return {
                "observation": "Game already finished",
                "reward": 0,
                "done": True,
                "info": {}
            }

        self.steps += 1

        if action == self.target:
            self.done = True
            return {
                "observation": "correct",
                "reward": 1.0,
                "done": True,
                "info": {"steps": self.steps}
            }

        else:
            distance = abs(action - self.target)
            reward = -distance / self.high  # partial progress reward
            
            if action < self.target:
                observation = "low"
            else:
                observation = "high"
            
            return {
                "observation": observation,
                "reward": reward,
                "done": False,
                "info": {}
            }
