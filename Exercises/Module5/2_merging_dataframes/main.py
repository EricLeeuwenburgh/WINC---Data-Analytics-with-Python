# Default starting template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%load_ext google.colab.data_table

artists = pd.read_csv("./artists.csv", sep=";")
albums = pd.read_csv("./albums.csv", sep=";")
tracks = pd.read_csv("./tracks.csv", sep=";")

#print(artists)
#print(albums)
#print(tracks)

# What is the birth year of the artist that produced "Dirty Mind"?
artists_and_albums = pd.merge(artists, albums, on="Artist")
print(artists_and_albums)
print(artists_and_albums.loc[artists_and_albums.Album.str.fullmatch("Dirty Mind"), "Year of Birth"])

# When was the album with the song "Fruits of the Night" released?
albums_and_tracks = pd.merge(albums, tracks, on="Album")
print(albums_and_tracks)
print(albums_and_tracks.loc[albums_and_tracks.Track.str.fullmatch("Fruits of the Night"), "Year of release"])

# What's the real/full name of the artist of the track "One Last Time"?
artists_and_albums = pd.merge(artists, albums, on="Artist")
all = pd.merge(artists_and_albums, tracks, on="Album")
print(all)
print(all.loc[all.Track.str.fullmatch("One Last Time"), "Real name"])