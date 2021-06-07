Substract an offset to each subtitles of a .rst file

Usage:
$ chmod +x subtitles_offset.py
$ ./subtitles_offset.py [RST FILE] [MINUTES] [SECONDS]

This is a very primitive tool:
- It does not remove subtitles when their timestamp underflow
- It only takes minutes and second  as offset
- It takes offset in separate parameters

I've just quickly developed a dirty tool to adjust subtitles for videos having
an offset between sound and subtitles so big that VLC was dying when I was
setting the offset by hand.
