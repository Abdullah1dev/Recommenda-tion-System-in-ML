from data.items import items


user_preferences = {
    "Python": 2,
    "AI": 3,
    "Machine Learning": 5
}


def calculate_match_score(user_preferences, item_tags):

    if not user_preferences:
        return 0

    score = 0

    for preference, weight in user_preferences.items():

        if preference in item_tags:
            score += weight

    total_weight = sum(user_preferences.values())

    match_percentage = (
        score / total_weight
    ) * 100

    return round(match_percentage, 2)


def filter_recommendations(recommendations):

    return [
        item
        for item in recommendations
        if item["score"] > 0
    ]


def get_top_recommendations(recommendations, n=3):

    return recommendations[:n]


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


# Sort
recommendations.sort(
    key=lambda item: item["score"],
    reverse=True
)


# Remove irrelevant recommendations
filtered_recommendations = filter_recommendations(
    recommendations
)


# Get Top-N
top_recommendations = get_top_recommendations(
    filtered_recommendations,
    n=3
)


# Display
for recommendation in top_recommendations:

    print(
        recommendation["name"],
        "→",
        recommendation["score"],
        "%"
    )