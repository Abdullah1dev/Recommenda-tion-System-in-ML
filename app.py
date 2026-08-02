import streamlit as st

from data.items import items
from src.recommender import generate_recommendations


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Recommendation System",
    page_icon="🎯",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🎯 Smart Recommendation System")

st.markdown(
    """
    ### Find the right content based on your interests.

    Select your interests, assign how important each one is to you,
    and our recommendation engine will rank the most relevant items.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Recommendation Settings")

st.sidebar.markdown(
    """
    ### How it works

    1. Select your interests
    2. Set their importance
    3. Choose how many recommendations you want
    4. Click **Get Recommendations**
    """
)

st.sidebar.divider()


# ============================================================
# AVAILABLE PREFERENCES
# ============================================================

available_preferences = [
    "Python",
    "AI",
    "Machine Learning",
    "Data Science",
    "Deep Learning",
    "NLP",
    "Computer Vision",
    "Web Development",
    "Cyber Security"
]


# ============================================================
# USER PREFERENCES
# ============================================================

st.subheader("👤 Your Interests")

selected_preferences = st.multiselect(
    "Select the topics you're interested in:",
    options=available_preferences,
    placeholder="Choose your interests..."
)


# ============================================================
# WEIGHTS
# ============================================================

user_preferences = {}

if selected_preferences:

    st.subheader("🎚️ Set Preference Importance")

    st.caption(
        "1 = Low importance | 5 = Very important"
    )

    for preference in selected_preferences:

        weight = st.slider(
            f"How important is {preference}?",
            min_value=1,
            max_value=5,
            value=3,
            key=f"weight_{preference}"
        )

        user_preferences[preference] = weight


# ============================================================
# TOP N SETTING
# ============================================================

st.subheader("🔢 Number of Recommendations")

top_n = st.slider(
    "How many recommendations do you want?",
    min_value=1,
    max_value=8,
    value=3
)


st.divider()


# ============================================================
# RECOMMENDATION BUTTON
# ============================================================

if st.button(
    "🚀 Get Recommendations",
    use_container_width=True
):

    # --------------------------------------------------------
    # Validate preferences
    # --------------------------------------------------------

    if not user_preferences:

        st.warning(
            "⚠️ Please select at least one interest first."
        )

    else:

        # ----------------------------------------------------
        # Generate recommendations
        # ----------------------------------------------------

        recommendations = generate_recommendations(
            items=items,
            user_preferences=user_preferences,
            top_n=top_n
        )


        # ----------------------------------------------------
        # Display results
        # ----------------------------------------------------

        st.subheader("🏆 Your Recommendations")


        if not recommendations:

            st.info(
                "No matching recommendations were found. "
                "Try selecting different interests."
            )

        else:

            st.success(
                f"Found {len(recommendations)} "
                f"recommendation(s) for you."
            )


            # ------------------------------------------------
            # Recommendation Cards
            # ------------------------------------------------

            for index, recommendation in enumerate(
                recommendations,
                start=1
            ):

                name = recommendation["name"]
                score = recommendation["score"]
                tags = recommendation["tags"]


                with st.container(border=True):

                    col1, col2 = st.columns(
                        [4, 1]
                    )


                    with col1:

                        st.markdown(
                            f"### #{index} {name}"
                        )

                        st.write(
                            "🏷️ "
                            + " • ".join(tags)
                        )


                    with col2:

                        st.metric(
                            "Match",
                            f"{score}%"
                        )


                    st.progress(
                        min(score / 100, 1.0)
                    )




st.divider()

