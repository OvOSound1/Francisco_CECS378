import random

# === Perception ===
# Simulate user engagement scores (0 to 100)
user_scores = [random.randint(0, 100) for _ in range(10)]

engagement_threshold = 60
promo_sent_count = 0

# === Reason + Act + Learn ===
for i, score in enumerate(user_scores):
    print(f"User {i+1} Engagement Score: {score}")

    # Reason
    if score >= engagement_threshold:
        decision = "Send Promo Email"
        promo_sent_count += 1  # Learn
    else:
        decision = "Do Not Send"

    # Act
    print(f"Decision: {decision}\n")

# Learn result
print(f"Total Promo Emails Sent: {promo_sent_count}")
