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
            
            
    if not user_preferences:
        return 0
            
        
    match_percentage = (
        
        match_count / len(user_preferences)
        
        ) * 100
                
                
            
        

    return match_percentage


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


# 1. Sort
recommendations.sort(
    key=lambda item: item["score"],
    reverse=True
)


# 2. Remove irrelevant items
filtered_recommendations = filter_recommendations(
    recommendations
)


# 3. Select Top-N
top_recommendations = get_top_recommendations(
    filtered_recommendations,
    n=3
)


# 4. Display
if not top_recommendations:
    print("No top recommendations found.")
else:
    for recommendation in top_recommendations:
        print(
                recommendation["name"],
                "→",
                recommendation["score"]
            )
            

    
