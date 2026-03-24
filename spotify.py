import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set(style="darkgrid")

# Load dataset
df = pd.read_csv("data.csv")

print("\n✅ Dataset Loaded Successfully\n")
print(df.head())

# -------------------------------
# 🎤 Top 10 Artists
# -------------------------------
plt.figure()
top_artists = df['artist_name'].value_counts().head(10)
sns.barplot(x=top_artists.values, y=top_artists.index)
plt.title("Top 10 Artists")
plt.xlabel("Number of Songs")
plt.ylabel("Artist")
plt.tight_layout()
plt.show()

# -------------------------------
# ⭐ Popularity Distribution
# -------------------------------
plt.figure()
sns.histplot(df['popularity'], bins=20, kde=True)
plt.title("Song Popularity Distribution")
plt.xlabel("Popularity")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# 🔥 Correlation Heatmap
# -------------------------------
plt.figure()
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

# -------------------------------
# 🎶 Danceability vs Energy
# -------------------------------
plt.figure()
sns.scatterplot(x='danceability', y='energy', data=df)
plt.title("Danceability vs Energy")
plt.tight_layout()
plt.show()

# -------------------------------
# 🏆 Top 10 Most Popular Songs
# -------------------------------
top_songs = df.sort_values(by='popularity', ascending=False).head(10)

plt.figure()
sns.barplot(x='popularity', y='track_name', data=top_songs)
plt.title("Top 10 Most Popular Songs")
plt.tight_layout()
plt.show()

# -------------------------------
# 🎧 Explicit vs Non-Explicit
# -------------------------------
if 'explicit' in df.columns:
    plt.figure()
    sns.countplot(x='explicit', data=df)
    plt.title("Explicit vs Non-Explicit Songs")
    plt.tight_layout()
    plt.show()

print("\n🔥 Analysis Completed!")