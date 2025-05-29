import streamlit as st
import lyricsgenius

# Genius API token
GENIUS_ACCESS_TOKEN = "your_genius_access_token_here"
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN, timeout=15, retries=3)

# App UI
st.title("🎤 Lyrics Extractor")
st.write("Enter the artist and song title to fetch lyrics using the Genius API.")

artist = st.text_input("Artist")
song = st.text_input("Song Title")

if st.button("Get Lyrics"):
    if not artist or not song:
        st.warning("Please enter both artist and song title.")
    else:
        try:
            with st.spinner("Fetching lyrics..."):
                result = genius.search_song(song, artist)
                if result and result.lyrics:
                    st.text_area("Lyrics", value=result.lyrics, height=400)
                else:
                    st.error("Lyrics not found.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
