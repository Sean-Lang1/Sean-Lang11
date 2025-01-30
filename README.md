🎶 Spotify Lyric Overlay App 🎶
📖 Description
The Spotify Lyric Overlay App is a work-in-progress application that displays synchronized lyrics for the currently playing song on Spotify in a transparent overlay. This allows you to enjoy your music while reading the lyrics without obstructing other applications.

🛠️ Features
Transparent Lyrics Overlay: Displays lyrics in a semi-transparent window, allowing you to view them without obstructing other applications.
Synchronization with Spotify: Retrieves the currently playing song from Spotify and fetches the corresponding lyrics from Genius.
Customizable Appearance: The transparency level and window size can be adjusted to suit your preferences.
📥 Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/spotify-lyric-overlay.git
cd spotify-lyric-overlay
Install Dependencies:

Ensure you have Python 3.13 installed. Then, install the required packages:

bash
Copy
Edit
pip install spotipy lyricsgenius
Set Up API Keys:

Replace the placeholders in the script with your own API keys:

Spotify API Keys: Obtain your SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI from the Spotify Developer Dashboard.
Genius API Key: Obtain your GENIUS_ACCESS_TOKEN from the Genius API.
Note: For security reasons, do not hardcode your API keys in the script. Instead, consider using environment variables or a configuration file to store them securely.

🚀 Usage
Run the script:

bash
Copy
Edit
python lyrics_overlay.py
The application will display the lyrics of the currently playing song in a transparent window.

🔮 Future Improvements
Enhanced Synchronization: Improve the synchronization between the song playback and the lyrics display.
Customization: Allow users to customize the appearance of the lyrics overlay, including font size, color, and position.
Error Handling: Implement better error handling for scenarios where the song or lyrics cannot be retrieved.
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Spotipy for the Spotify API integration.
LyricsGenius for the Genius API integration.
Tkinter for creating the transparent window.
