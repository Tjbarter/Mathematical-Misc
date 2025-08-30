import numpy as np
import matplotlib.pyplot as plt

def simulate_light_game_vectorized(S_values, mu=5, sigma=1, num_runs=100000):
    """
    Simulates the light game for multiple stopping times to estimate success rates.

    Parameters:
        S_values (array): Array of stopping times in seconds.
        mu (float): Mean illumination time (default 5 seconds).
        sigma (float): Standard deviation of illumination time (default 1 second).
        num_runs (int): Number of simulated runs.

    Returns:
        success_rates (array): Success rates for each stopping time in S_values.
    """
    # Generate random illumination times for all runs
    illumination_times = np.random.normal(loc=mu, scale=sigma, size=num_runs)

    # Calculate success rates for each stopping time in S_values
    success_rates = [np.mean(illumination_times <= S) for S in S_values]

    return np.array(success_rates)

def estimate_successes_per_hour_vectorized(S_values, mu=5, sigma=1, num_runs=100000):
    """
    Estimates the total number of successes per hour for multiple stopping times.

    Parameters:
        S_values (array): Array of stopping times in seconds.
        mu (float): Mean illumination time.
        sigma (float): Standard deviation of illumination time.
        num_runs (int): Number of simulated runs.

    Returns:
        successes_per_hour (array): Estimated number of successes per hour for each stopping time.
    """
    # Simulate success rates for all stopping times
    success_rates = simulate_light_game_vectorized(S_values, mu, sigma, num_runs)

    # Calculate the number of runs per hour for each stopping time
    runs_per_hour = 3600 / S_values

    # Calculate the estimated successes per hour for each stopping time
    successes_per_hour = success_rates * runs_per_hour

    return successes_per_hour

# Simulate across a range of stopping times between S = 6 and S = 7
if __name__ == "__main__":
    mu = 5  # Mean illumination time
    sigma = 1  # Standard deviation of illumination time
    num_runs = 100000  # Reduced number of simulations for faster performance

    # Generate a fine-grained range of stopping times between 6 and 7
    S_values = np.linspace(6, 7, 100)  # Focused range for higher precision
    scores = estimate_successes_per_hour_vectorized(S_values, mu, sigma, num_runs)

    # Find the optimal S within this range
    optimal_index = np.argmax(scores)
    optimal_S = S_values[optimal_index]

    # Plot the results
    plt.figure(figsize=(8, 5))
    plt.plot(S_values, scores, label="Successes per hour")
    plt.title("Successes per Hour vs. Stopping Time S (6 to 7)")
    plt.xlabel("Stopping Time S (seconds)")
    plt.ylabel("Estimated Successes per Hour")
    plt.axvline(optimal_S, color='r', linestyle='--', label=f"Optimal S ≈ {optimal_S:.4f}")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Optimal stopping time S = {optimal_S:.4f} seconds")