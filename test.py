import asyncio
from shazamio import Shazam
import lyricsgenius
genius = lyricsgenius.Genius("ShGRYCfN2TXrPT3B3QCRv_e6ov1hoWptPnvgkc3Juw-4NsOTWPWbYfewDwd3fYjN")
'''
genius.verbose = False # Turn off status messages
genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = False # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title
'''

async def identify_song(file_path):
    shazam = Shazam()
    out = await shazam.recognize(file_path)
    
    # get song title and artist
    track_title = out['track']['title']
    track_artist = out['track']['subtitle']

    # print(f"Song: {track_title}")
    # print(f"Artist: {track_artist}")

    return {"title": track_title, "artist": track_artist}

# path to the audio file
audio_file = "recordings/cruel-summer.m4a"

# run function
result = asyncio.run(identify_song(audio_file))

# print(result['title'])
# print(result['artist'])


#artist = genius.search_artist("Noah Kahan", max_songs=0, sort="title", include_features=True)
genius.remove_section_headers = True
song = genius.search_song(result['title'], result['artist'])
print(song.lyrics)
with open('lyrics.txt', 'w') as f:
    f.write("\n".join(song.lyrics.splitlines()[1:]))
