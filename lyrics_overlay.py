import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lyricsgenius
import tkinter as tk
import re
import time

# Set up Spotify API (replace with your own credentials)
SPOTIPY_CLIENT_ID = "a8bba9debdc94fb7abdcdbd8886c0d4c"
SPOTIPY_CLIENT_SECRET = "d0e2794c8bde4bdbaac34016165f242e"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-read-currently-playing"
))

# Set up Genius API
GENIUS_ACCESS_TOKEN = "J2JZss4eXJFWskLfAzHeiYgK0WA3fyg78lhIiP7xUEecdJQIPjHJFJnFFQCNk2wW"
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

def get_spotify_song():
    """Fetches the currently playing song from Spotify API."""
    try:
        current_track = sp.currently_playing()
        if current_track and current_track["is_playing"]:
            song = current_track["item"]["name"]
            artist = current_track["item"]["artists"][0]["name"]
            print(f"Now playing: {song} - {artist}")
            return song, artist
        else:
            print("No song is currently playing.")
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def get_lyrics(song, artist):
    """Fetches lyrics from Genius API and cleans up the headings and contributor information."""
    try:
        song_data = genius.search_song(song, artist)
        if song_data:
            lyrics = song_data.lyrics
            # Remove contributor information (e.g., "50 Contributors")
            cleaned_lyrics = re.sub(r"^\d+ Contributors.*\n", "", lyrics)
            # Remove headings like [Chorus], [Verse 1], etc.
            cleaned_lyrics = re.sub(r"\[.*?\]", "", cleaned_lyrics)
            # Remove any extra newlines
            cleaned_lyrics = re.sub(r"\n{2,}", "\n", cleaned_lyrics).strip()
            # Find the second occurrence of the word "Lyrics" and start from there
            lyrics_start_index = cleaned_lyrics.lower().find("lyrics", cleaned_lyrics.lower().find("lyrics") + 1)
            if lyrics_start_index != -1:
                cleaned_lyrics = cleaned_lyrics[lyrics_start_index + len("Lyrics"):].strip()
            return cleaned_lyrics.splitlines()
        else:
            print("Lyrics not found.")
            return None
    except Exception as e:
        print(f"Error fetching lyrics: {e}")
        return None

def create_transparent_window():
    """Creates a transparent window to display lyrics."""
    root = tk.Tk()
    root.geometry("800x200")  # Adjust size as needed
    root.configure(bg='black')
    root.attributes('-alpha', 0.5)  # Set transparency level (0.0 to 1.0)
    root.overrideredirect(True)  # Remove window decorations
    root.wm_attributes("-topmost", 1)  # Keep window on top
    root.grab_set()  # Prevent window from losing focus

    label = tk.Label(root, text="", font=("Helvetica", 24), fg="white", bg="black")
    label.pack(expand=True, fill='both')

    return root, label

def update_lyrics(label, lyrics):
    """Updates the label with the next line of lyrics."""
    for line in lyrics:
        label.config(text=line)
        time.sleep(3)  # Adjust the duration each line is displayed
        label.update()

if __name__ == "__main__":
    song, artist = get_spotify_song()
    if song and artist:
        lyrics = get_lyrics(song, artist)
        if lyrics:
            window, label = create_transparent_window()
            update_lyrics(label, lyrics)
            window.mainloop()
