from src.recommender import items


user_preferences = [
    "Python",
    "AI",
    "Machine Learning"
]

def get_top_recommendations(recommendations , n=3):
    return recommendations[:n]


def calculate_match_score(user_preferences, item_tags):

    match_count = 0

    for preference in user_preferences:

        if preference in item_tags:
            match_count += 1

    return match_count


recommendations = []

for item in items:

    score = calculate_match_score(
        user_preferences,
        item["tags"]
    )

    recommendations.append({
        "name": item["name"],
        "score": score
    })
    
    recommendations.sort(
    key=lambda item: item["score"],
    reverse=True
)
    
    top_recommendations = get_top_recommendations(
    recommendations,
    n=3
)




for recommendation in recommendations:

    print(
        recommendation["name"],
        "→",
        recommendation["score"]
    )
    
    



