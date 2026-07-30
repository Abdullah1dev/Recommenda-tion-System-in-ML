# items = [
#     {
#         "id": 1,
#         "name": "Python for Beginners",
#         "tags": ["Python", "Programming"]
#     },

#     {
#         "id": 2,
#         "name": "Machine Learning Fundamentals",
#         "tags": ["Python", "Machine Learning", "AI"]
#     },

#     {
#         "id": 3,
#         "name": "Deep Learning with Python",
#         "tags": ["Python", "Deep Learning", "AI"]
#     },

#     {
#         "id": 4,
#         "name": "Web Development Basics",
#         "tags": ["HTML", "CSS", "JavaScript", "Web Development"]
#     },

#     {
#         "id": 5,
#         "name": "Natural Language Processing",
#         "tags": ["Python", "NLP", "AI"]
#     },

#     {
#         "id": 6,
#         "name": "Computer Vision Fundamentals",
#         "tags": ["Python", "Computer Vision", "AI"]
#     },

#     {
#         "id": 7,
#         "name": "Data Science with Python",
#         "tags": ["Python", "Data Science", "Pandas"]
#     },

#     {
#         "id": 8,
#         "name": "Cyber Security Basics",
#         "tags": ["Networking", "Security", "Cyber Security"]
#     }
# ]


# user_preferences = [
#     "Python",
#     "AI",
#     "Machine Learning"
# ]




# for item in items:
#     print(item["tags"])



# item = {
#     "name": "Python for Beginners",
#     "tags": ["Python", "Programming"]
# }


# user_preferences = [
#     "Python",
#     "AI",
#     "Machine Learning"
# ]


def calculate_match_score(user_preferences, item_tags):

    match_count = 0

    for preference in user_preferences:

        if preference in item_tags:
            match_count += 1

    return match_count




user_preferences = [
    "Python",
    "AI",
    "Machine Learning"
]

item_tags = [
    "Python",
    "Machine Learning",
    "AI"
]

score = calculate_match_score(
    user_preferences,
    item_tags
)

print(score)



    

    