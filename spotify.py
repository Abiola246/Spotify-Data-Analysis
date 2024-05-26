import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with specified encoding
spotify_data = pd.read_csv('spotify-2023.csv', encoding='latin1')

# Group the data by artist and track, and count occurrences
popular_artists = spotify_data.groupby(['artist(s)_name'])['track_name'].count().reset_index()
popular_tracks = spotify_data.groupby(['track_name'])['artist(s)_name'].count().reset_index()

# Sort the data by count to find the most popular artist and track
most_popular_artist = popular_artists.sort_values(by='track_name', ascending=False).iloc[0]
most_popular_track = popular_tracks.sort_values(by='artist(s)_name', ascending=False).iloc[0]

# Print the most popular artist and track
print("Most Popular Artist:", most_popular_artist['artist(s)_name'])
print("Number of Tracks by the Artist:", most_popular_artist['track_name'])
print("Most Popular Track:", most_popular_track['track_name'])
print("Number of Artists for the Track:", most_popular_track['artist(s)_name'])

# Visualize the most popular artist and track using bar charts
plt.figure(figsize=(10, 6))
sns.barplot(x='artist(s)_name', y='track_name', data=popular_artists.head(10))
plt.title('Top 10 Popular Artists')
plt.xlabel('Artist')
plt.ylabel('Number of Tracks')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='track_name', y='artist(s)_name', data=popular_tracks.head(10))
plt.title('Top 10 Popular Tracks')
plt.xlabel('Track')
plt.ylabel('Number of Artists')
plt.xticks(rotation=45)
plt.show()
