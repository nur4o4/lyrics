import lyricsgenius
genius = lyricsgenius.Genius("ShGRYCfN2TXrPT3B3QCRv_e6ov1hoWptPnvgkc3Juw-4NsOTWPWbYfewDwd3fYjN")
'''
genius.verbose = False # Turn off status messages
genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = False # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title
'''

#artist = genius.search_artist("Noah Kahan", max_songs=0, sort="title", include_features=True)
genius.remove_section_headers = True
song = genius.search_song("Stick Season", "Noah Kahan")
print(song.lyrics)
with open('lyrics.txt', 'w') as f:
    f.write("\n".join(song.lyrics.splitlines()[1:]))
