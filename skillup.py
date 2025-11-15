# SkillUp Project: Python Script for Education & Skill Development

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: prettier plots
sns.set(style="whitegrid")

# ----------------------------
# Step 1: Create Datasets
# ----------------------------

# Learners dataset with Community info
learners = pd.DataFrame({
    "LearnerID": range(1, 11),
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"],
    "Age": [20, 22, 21, 23, 22, 21, 24, 22, 23, 20],
    "Gender": ["F","M","M","F","M","F","M","F","M","F"],
    "Location": ["Urban","Rural","Urban","Rural","Urban","Urban","Rural","Urban","Rural","Urban"],
    "Community": ["Underserved","Underserved","Urban","Underserved","Urban","Urban","Underserved","Urban","Underserved","Urban"]
})

# Skills dataset
skills = pd.DataFrame({
    "SkillID": [101,102,103,104],
    "SkillName": ["Python","Web Development","Data Analysis","Graphic Design"],
    "Level": ["Beginner","Intermediate","Intermediate","Beginner"]
})

# Enrollments dataset
enrollments = pd.DataFrame({
    "LearnerID": np.random.randint(1,11,20),
    "SkillID": np.random.randint(101,105,20),
    "Progress": np.random.randint(0,101,20),  # percentage
    "LastActivityDays": np.random.randint(1,31,20)  # days since last activity
})

# Display datasets
print("=== Learners ===")
print(learners.head())
print("\n=== Skills ===")
print(skills.head())
print("\n=== Enrollments ===")
print(enrollments.head())

# ----------------------------
# Step 2: Data Exploration
# ----------------------------
print("\nMissing values in learners dataset:\n", learners.isnull().sum())
print("\nMissing values in enrollments dataset:\n", enrollments.isnull().sum())

print("\nLearners Age Summary:\n", learners['Age'].describe())
print("\nEnrollments Progress Summary:\n", enrollments['Progress'].describe())

# ----------------------------
# Step 3: Basic Analysis
# ----------------------------

# Average progress per skill
avg_progress = enrollments.groupby('SkillID')['Progress'].mean().reset_index()
avg_progress = avg_progress.merge(skills, on="SkillID")
print("\nAverage Progress per Skill:\n", avg_progress)

# Average progress per community (focus on underserved communities)
community_progress = enrollments.merge(learners, on='LearnerID')
avg_progress_community = community_progress.groupby('Community')['Progress'].mean()
print("\nAverage Progress per Community:\n", avg_progress_community)

# Learner activity patterns
active_learners = enrollments[enrollments['LastActivityDays'] <= 7]['LearnerID'].nunique()
print("\nNumber of highly active learners (last 7 days):", active_learners)

# ----------------------------
# Step 4: Visualizations
# ----------------------------

# 1️⃣ Line Chart — Average Progress per Learner
progress_trend = enrollments.groupby('LearnerID')['Progress'].mean()
plt.figure(figsize=(8,5))
progress_trend.plot(kind='line', marker='o')
plt.title("Average Progress per Learner")
plt.xlabel("LearnerID")
plt.ylabel("Average Progress (%)")
plt.show()

# 2️⃣ Bar Chart — Skill Popularity
skill_popularity = enrollments['SkillID'].value_counts().reset_index()
skill_popularity.columns = ['SkillID','Enrollments']
skill_popularity = skill_popularity.merge(skills, on='SkillID')

plt.figure(figsize=(8,5))
sns.barplot(x='SkillName', y='Enrollments', data=skill_popularity)
plt.title("Skill Popularity")
plt.ylabel("Number of Enrollments")
plt.show()

# 3️⃣ Histogram — Progress Distribution
plt.figure(figsize=(8,5))
plt.hist(enrollments['Progress'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Learner Progress")
plt.xlabel("Progress (%)")
plt.ylabel("Number of Enrollments")
plt.show()

# 4️⃣ Scatter Plot — Progress vs Days Since Last Activity
plt.figure(figsize=(8,5))
sns.scatterplot(x='LastActivityDays', y='Progress', data=enrollments, hue='SkillID', palette='Set2', s=100)
plt.title("Progress vs Days Since Last Activity")
plt.xlabel("Days Since Last Activity")
plt.ylabel("Progress (%)")
plt.legend(title='SkillID')
plt.show()

# 5️⃣ Optional: Bar Chart — Average Progress by Community
plt.figure(figsize=(6,4))
sns.barplot(x=avg_progress_community.index, y=avg_progress_community.values)
plt.title("Average Progress by Community")
plt.ylabel("Average Progress (%)")
plt.show()

# ----------------------------
# Step 5: Insights & Recommendations
# ----------------------------

# Learners needing support
low_progress = enrollments[enrollments['Progress'] < 50]
print("\nLearners needing support:\n", low_progress)

# Inactive learners (>14 days since last activity)
inactive_learners = enrollments[enrollments['LastActivityDays'] > 14]
print("\nInactive learners (last activity >14 days):\n", inactive_learners)

# Export report
import os
os.makedirs("Reports", exist_ok=True)
inactive_learners.to_csv("Reports/inactive_learners_report.csv", index=False)
print("\nReport exported to Reports/inactive_learners_report.csv")