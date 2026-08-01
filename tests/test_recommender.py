from src.recommender import (
    calculate_match_score,
    filter_recommendations,
    get_top_recommendations,
    generate_recommendations
)


def test_calculate_match_score():

    preferences = {
        "Python": 2,
        "AI": 3,
        "Machine Learning": 5
    }

    tags = [
        "Python",
        "Machine Learning"
    ]

    score = calculate_match_score(
        preferences,
        tags
    )

    assert score == 70.0


def test_case_insensitive_matching():

    preferences = {
        "Python": 2
    }

    tags = [
        "python"
    ]

    score = calculate_match_score(
        preferences,
        tags
    )

    assert score == 100.0


def test_empty_preferences():

    score = calculate_match_score(
        {},
        ["Python"]
    )

    assert score == 0


def test_empty_tags():

    score = calculate_match_score(
        {"Python": 2},
        []
    )

    assert score == 0


def test_filter_recommendations():

    recommendations = [
        {"name": "Python", "score": 100},
        {"name": "AI", "score": 50},
        {"name": "Cyber Security", "score": 0}
    ]

    filtered = filter_recommendations(
        recommendations
    )

    assert len(filtered) == 2


def test_top_recommendations():

    recommendations = [
        {"name": "A", "score": 100},
        {"name": "B", "score": 80},
        {"name": "C", "score": 60},
        {"name": "D", "score": 40}
    ]

    top = get_top_recommendations(
        recommendations,
        n=2
    )

    assert len(top) == 2
    assert top[0]["name"] == "A"
    assert top[1]["name"] == "B"


def test_generate_recommendations():

    items = [
        {
            "name": "Python Course",
            "tags": ["Python"]
        },
        {
            "name": "Cyber Security",
            "tags": ["Cyber Security"]
        }
    ]

    preferences = {
        "Python": 5
    }

    results = generate_recommendations(
        items,
        preferences,
        top_n=1
    )

    assert len(results) == 1
    assert results[0]["name"] == "Python Course"
    assert results[0]["score"] == 100.0