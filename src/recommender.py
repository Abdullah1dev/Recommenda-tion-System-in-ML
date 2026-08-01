def calculate_match_score(user_preferences, item_tags):
    """
    Calculate the weighted match percentage
    between user preferences and item tags.
    """

    if not user_preferences or not item_tags:
        return 0

    score = 0

    # Normalize item tags
    normalized_tags = {
        tag.strip().lower()
        for tag in item_tags
    }

    # Compare preferences with item tags
    for preference, weight in user_preferences.items():

        normalized_preference = preference.strip().lower()

        if normalized_preference in normalized_tags:
            score += weight

    # Maximum possible score
    total_weight = sum(user_preferences.values())

    if total_weight == 0:
        return 0

    # Convert score to percentage
    match_percentage = (
        score / total_weight
    ) * 100

    return round(match_percentage, 2)


def filter_recommendations(recommendations):
    """
    Remove recommendations with zero match.
    """

    return [
        item
        for item in recommendations
        if item["score"] > 0
    ]


def get_top_recommendations(recommendations, n=3):
    """
    Return the top N recommendations.
    """

    return recommendations[:n]


def generate_recommendations(
    items,
    user_preferences,
    top_n=3
):
    """
    Generate, score, rank, filter,
    and return top recommendations.
    """

    recommendations = []

    # Calculate score for every item
    for item in items:

        score = calculate_match_score(
            user_preferences,
            item["tags"]
        )

        recommendations.append({
            "name": item["name"],
            "score": score,
            "tags": item["tags"]
        })

    # Sort highest score first
    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # Remove irrelevant items
    filtered_recommendations = filter_recommendations(
        recommendations
    )

    # Return Top-N
    return get_top_recommendations(
        filtered_recommendations,
        top_n
    )