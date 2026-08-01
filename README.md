# 🎯 Smart Recommendation System

A content-based recommendation system built with **Python and Streamlit** that recommends relevant learning resources based on a user's interests and the importance they assign to each preference.

The project demonstrates the fundamental concepts behind recommendation systems, including preference matching, weighted scoring, ranking, filtering, testing, and interactive visualization.

---

## 📌 Project Overview

Recommendation systems are used to help users discover relevant content based on their interests and behavior.

In this project, I built a simple **content-based recommendation engine**.

The system takes:

- User interests
- Importance/weight of each interest
- Number of recommendations required

It then compares the user's preferences with the tags associated with each item and calculates a **weighted match percentage**.

The highest-scoring items are returned as recommendations.

---

## ✨ Features

- 🎯 Content-based recommendation
- 👤 User preference selection
- 🎚️ Preference importance/weighting
- 📊 Weighted match percentage
- 🏆 Ranked recommendations
- 🔢 Top-N recommendation selection
- 🏷️ Matched-interest explanations
- 🎨 Professional Streamlit interface
- 🧪 Automated backend tests using pytest
- 📱 Interactive web application

---

## 🧠 How It Works

The recommendation pipeline follows this process:

```text
User
  │
  ▼
Select Interests
  │
  ▼
Assign Importance
  │
  ▼
Compare Preferences
  │
  ▼
Calculate Match Score
  │
  ▼
Calculate Match Percentage
  │
  ▼
Rank Recommendations
  │
  ▼
Return Top-N Results