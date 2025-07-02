import random

# === Perception ===
# Simulated health values over time
health_levels = [random.randint(20, 100) for _ in range(10)]

attack_threshold = 60
attack_counter = 0

# === Reason + Act + Learn ===
for health in health_levels:
    print(f"Bot Health: {health}")

    # Reason
    if health > attack_threshold:
        decision = "Attack"
        attack_counter += 1  # Learn
    else:
        decision = "Defend"

    # Act
    print(f"Bot decides to: {decision}\n")

# Learn result
print(f"Total Attacks: {attack_counter}")
