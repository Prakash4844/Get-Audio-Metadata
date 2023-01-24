# Python3 program to illustrate
# accessing of audio metadata
# using tinytag library

# Import Tinytag method from
# tinytag library
from tinytag import TinyTag
import sys
# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable
audio = TinyTag.get(sys.argv[1])

def secToHour(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def byteToMB(bytes):
    mb = audio.filesize/1048576
    rmb = round(mb, 2)
    return rmb

# Use the attributes
# and Display
print("Title:" + audio.title)
print("Artist: " + audio.artist)
print("Genre:" + audio.genre)
print("Year Released: " + audio.year)
print("Bitrate:" + str(audio.bitrate) + " kBits/s")
print("Filesize:"+ str(byteToMB(audio.filesize)) + "MB")
print("AlbumArtist: " + audio.albumartist)
print("Duration: " + str(secToHour(audio.duration)) + " seconds")
print("TrackTotal: " + str(audio.track_total))