import numpy as np
import matplotlib.pyplot as plt


# Triangular membership function
def triangular(x, a, b, c):
    if a == b:  # Left-shoulder
        return np.where(x <= b, 1, np.maximum((c - x) / (c - b), 0))
    elif b == c:  # Right-shoulder
        return np.where(x >= a, 1, np.maximum((x - a) / (b - a), 0))
    else:  # Normal triangular
        return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)


# Fuzzification for temperature
def fuzzify_temperature(temp):
    low = triangular(temp, 0, 0, 25)
    medium = triangular(temp, 15, 30, 45)
    high = triangular(temp, 35, 50, 50)
    return {"low": low, "medium": medium, "high": high}


# Fuzzification for fan speed
def fuzzify_fan_speed(speed):
    slow = triangular(speed, 0, 0, 50)
    medium = triangular(speed, 25, 50, 75)
    fast = triangular(speed, 50, 100, 100)
    return {"slow": slow, "medium": medium, "fast": fast}


# Rule base
def apply_rules(temp_fuzzy):
    rules = {
        "slow": temp_fuzzy["low"],
        "medium": temp_fuzzy["medium"],
        "fast": temp_fuzzy["high"]
    }
    return rules


# Defuzzification (Centroid method)
def defuzzify(rules, resolution=100):
    x = np.linspace(0, 100, resolution)
    agg_membership = np.zeros_like(x)

    for label, strength in rules.items():
        mf = fuzzify_fan_speed(x)[label]
        agg_membership = np.fmax(agg_membership, np.fmin(strength, mf))

    if np.sum(agg_membership) == 0:
        return 0, x, agg_membership
    else:
        crisp_value = np.sum(x * agg_membership) / np.sum(agg_membership)
        return crisp_value, x, agg_membership


# Example usage
temperature = 37
temp_fuzzy = fuzzify_temperature(temperature)
rules = apply_rules(temp_fuzzy)
fan_speed, x, agg = defuzzify(rules)

# Results
print(f"Input Temperature: {temperature}°C")
print(f"Calculated Fan Speed: {fan_speed:.2f}%")


# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x, agg, label="Aggregated Output")
plt.axvline(fan_speed, color="r", linestyle="--", label=f"Crisp Output = {fan_speed:.2f}")
plt.title("Fuzzy Inference System: Fan Speed Control")
plt.xlabel("Fan Speed (%)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(True)
plt.show()
