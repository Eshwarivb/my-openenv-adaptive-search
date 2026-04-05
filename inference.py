from env import GuessEnv
import random
import json
import math

random.seed(42)

# 🔹 Random Agent (baseline)
def random_agent(env):
    env.reset()
    steps = 0

    for _ in range(50):  # safety limit
        guess = random.randint(env.low, env.high)
        result = env.step(guess)

        steps += 1

        if result["done"]:
            return steps

    return steps  # fallback


# 🔹 Smart Agent (explore + binary search)
def smart_agent(env):
    env.reset()
    low = env.low
    high = env.high
    steps = 0

    # Exploration phase
    for _ in range(2):
        guess = random.randint(low, high)
        result = env.step(guess)
        steps += 1

        if result["done"]:
            return steps

        if result["observation"] == "low":
            low = guess + 1
        else:
            high = guess - 1

    # Exploitation phase (binary search)
    for _ in range(50):  # safety loop
        guess = (low + high) // 2
        result = env.step(guess)
        steps += 1

        if result["done"]:
            return steps

        if result["observation"] == "low":
            low = guess + 1
        else:
            high = guess - 1

    return steps  # fallback


# 🔹 Improved scoring (efficiency-based)
def compute_score(steps, low, high):
    optimal_steps = max(1, int(math.log2(high - low + 1)))
    efficiency = optimal_steps / steps
    return round(min(1.0, efficiency), 2), optimal_steps


def run_task(low, high):
    env = GuessEnv(low, high)

    random_steps = random_agent(env)
    smart_steps = smart_agent(env)

    random_score, _ = compute_score(random_steps, low, high)
    smart_score, optimal = compute_score(smart_steps, low, high)

    return {
        "random_agent": {
            "steps": random_steps,
            "score": random_score
        },
        "smart_agent": {
            "steps": smart_steps,
            "score": smart_score,
            "strategy": "explore + binary_search"
        },
        "optimal_steps": optimal,
        "improvement": round(smart_score - random_score, 2)
    }


def run_task_avg(low, high, runs=3):
    """Run task multiple times and average results for stability"""
    results = [run_task(low, high) for _ in range(runs)]
    
    avg_random_steps = round(sum(r["random_agent"]["steps"] for r in results) / runs, 2)
    avg_random_score = round(sum(r["random_agent"]["score"] for r in results) / runs, 2)
    avg_smart_steps = round(sum(r["smart_agent"]["steps"] for r in results) / runs, 2)
    avg_smart_score = round(sum(r["smart_agent"]["score"] for r in results) / runs, 2)
    
    return {
        "random_agent": {
            "steps": avg_random_steps,
            "score": avg_random_score
        },
        "smart_agent": {
            "steps": avg_smart_steps,
            "score": avg_smart_score,
            "strategy": "explore + binary_search"
        },
        "improvement": round(avg_smart_score - avg_random_score, 2),
        "runs": runs
    }


if __name__ == "__main__":
    results = {
        "task_1": run_task_avg(1, 10, runs=3),
        "task_2": run_task_avg(1, 50, runs=3),
        "task_3": run_task_avg(1, 100, runs=3),
    }

    print(json.dumps(results, indent=2))
