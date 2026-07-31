from data.items import items


user_preferences = [
    "Python",
    "AI",
    "Machine Learning"
]


def calculate_match_score(user_preferences, item_tags):

    match_count = 0

    for preference in user_preferences:

        if preference in item_tags:
            match_count += 1

    return match_count


def get_top_recommendations(recommendations, n=3):

    return recommendations[:n]


recommendations = []


# Calculate score for every item
for item in items:

    score = calculate_match_score(
        user_preferences,
        item["tags"]
    )

    recommendations.append({
        "name": item["name"],
        "score": score
    })


# Sort all recommendations
recommendations.sort(
    key=lambda item: item["score"],
    reverse=True
)


# Get Top 3
top_recommendations = get_top_recommendations(
    recommendations,
    n=3
)


# Print ONLY Top 3
for recommendation in top_recommendations:

    print(
        recommendation["name"],
        "→",
        recommendation["score"]
    )