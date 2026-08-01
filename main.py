from data.items import items
from src.recommender import generate_recommendations


user_preferences = {
    "Python": 2,
    "AI": 3,
    "Machine Learning": 5
}


recommendations = generate_recommendations(
    items=items,
    user_preferences=user_preferences,
    top_n=3
)


print("\nRecommended Items:\n")


for recommendation in recommendations:

    print(
        f"{recommendation['name']} "
        f"→ {recommendation['score']}%"
    )