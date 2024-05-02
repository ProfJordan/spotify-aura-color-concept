# Spotify Audio Aura Color Concept

This is a concept for inspired by Spotify's "[audio aura](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/)". It creates a color using [Spotify Web API](https://developer.spotify.com/documentation/web-api/) data. Similar to how Spotify might use the same data in their annual [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped).

This was originally course work from an Intro to Computer Science course. Uploaded here for future reference & archival.

## Usage
    python rgb.py

You can change the `songs.db` file to your own sqlite3 data inside `rgb.py`.

## Notes, Reflection & Considerations
### If songs.db contains the top 100 songs of one listener from 2018, how would you characterize their audio aura?
- I would take the average calues of danceability, energy & valence and associate them with the colors of red, green & blue.
- I would use the following query to get the values: `SELECT AVG(danceability) AS r, AVG(energy) AS g, AVG(valence) AS b FROM songs;`
- I would then convert each decimal value to an equivalent rgb value by multiplying it by 255 and rounding it to the nearest integer.
- I would then have a color I could associate with the audio aura. I could then save that output to a file or template and display it to the user.
- For example using the songs.db user data I would get back the following values:
    - Danceability Avg: 0.71646
    - Energy Avg: 0.6590600000000001
    - Valence Avg: 0.4844429999999997
-Converting them as mentioned above and associating them with a color would give me the RGB values:
    - Red: 183
    - Green: 168
    - Blue: 124
- This would give an RGB color for the Aura of `RGB(183, 168, 124)`.

### Hypothesize about why the way you’ve calculated this aura might not be very representative of the listener.
- If a user only listened to 1 song that had the same values as the average of a user that listened to multiple songs; they would get the same aura color.
- This is also true if a user only listened to 3 songs.
- Let's take for example an unrealistic scenario where a user listened to a song where all the values were 0.75.
- Then another user listened to that same song but also 2 other songs with values that were +/- 0.25 respectively.
- So you'd have 1.00, 0.50 & 0.75 as your values. If you then averaged those out you'd still end up with 0.75.
- That would give you the same audio aura color as the first user or as if you had only just listened to the 0.75 value song.
- This isn't a very accurate representation of the differences in values.

### What better ways of calculating this aura would you propose?
- It could be more accurate to use a slightly modified approach. Such as summing the total from each column.
- Then rounding to the nearest whole integer and using that as the RGB values.
- Using the following query or similar instead of the above averages: `SELECT SUM(danceability) AS r, SUM(energy) AS g, SUM(valence) AS b FROM songs;`
- Should a value exceed 255. Then we could divide the whole rounded sum by 255 to get our new RGB values.
- This would allow a users auras to change based on how many songs they listened to & songs with higher values would add up quicker.
- If we kept it to only consider the top 255 songs; no user should go over the 255 mark.
- For example using the songs.db user data I would get back the following values:
    - Danceability Avg: 0.71646
    - Energy Avg: 0.6590600000000001
    - Valence Avg: 0.4844429999999997
-Converting them as mentioned above and associating them with a color would give me the RGB values:
    - Red: 72
    - Green: 66
    - Blue: 48
- This would give an RGB color for the Aura of `RGB(72, 66, 48)`.

### Some other considerations:
- If we limited results from only the top 100. We'd likely just have to adjust the math.
- Maybe times it by 2 and some change to match the 0.00-100.00 values to equivalent 0-255 values.
