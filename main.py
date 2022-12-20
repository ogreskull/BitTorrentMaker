from os import walk, path
from torf import Torrent

# os imports:
# walk and path are used to construct a folder list at the UsablePath location, and then iterate through that list
# path is used to attempt to make the script easier to use in Windows/POSIX overlap environments, ymmv

# torf imports:
# the torrent class continues some values we need, like the ability to make a torrent with assigned trackers and
# set to private by default.
# This should be part of your venv, or installed via pip install torrent

# paths:
# notice the r(aw) strings in use, this avoids having to deal with \ being treated as an escape character
# please gently massage these values in a POSIX environment
UsablePath = r"\\fileserver01\outgoing\ReadyToSeed"
OutputPath = r"\\fileserver01\outgoing\FreshlyMadeTorrents"
AnnounceUrl = "https://URLHERE/PUTYOURKEYHERE/announce"

print("Let's make some torrents!")
print("Looking in " + UsablePath)
FolderList = next(walk(UsablePath), (None, None, []))[1]

for i in FolderList:
    j = path.abspath(UsablePath + "\\" + i)  # try updating the addition here if this doesn't work for you in POSIX
    print("Making a torrent for: " + j + " ...")
    t = Torrent(path=j,
                trackers=[AnnounceUrl])
    t.private = True
    t.generate()
    t.write(OutputPath + "\\" + i + '.torrent')
