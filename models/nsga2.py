import numpy as np

def evaluate_solutions(input_data):
    distance = input_data["distance_km"]
    has_car = input_data["has_car"]
    has_bike = input_data["has_bike"]

    comfort_pref = input_data["comfort_pref"]
    cost_pref = input_data["cost_pref"]
    env_pref = input_data["env_pref"]
    punctuality_pref = input_data["punctuality_pref"]

    # Modes possibles
    modes = ["Walk", "Bike", "Bus", "Train", "Car", "Scooter"]

    results = []
    for mode in modes:
        comfort = np.random.uniform(0,1)
        cost = np.random.uniform(0,1)
        env = np.random.uniform(0,1)
        punctuality = np.random.uniform(0,1)

        score = (
            comfort_pref * comfort +
            cost_pref * cost +
            env_pref * env +
            punctuality_pref * punctuality
        )

        results.append((mode, round(score, 3)))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[0], results


def run_nsga2(input_data):
    best_mode, all_scores = evaluate_solutions(input_data)

    return {
        "recommended_mode": best_mode[0],
        "score": best_mode[1],
        "all_modes_ranked": all_scores
    }
