'''
Created on Feb 26, 2010

@author: ivan
'''
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

import os
import LOG
class Song:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        
        self.album = ""
        self.artist = ""
        self.title = ""
        self.date = ""
        self.genre = ""
        self.tracknumber = ""
        if os.path.isfile(self.path):
            self._getMp3Tags()
    
    def getFullDescription(self):
        return self.artist + " - ["+self.album + "]  #"+self.tracknumber + " " + self.title
    
    def getShorDescription(self):
        return self.tracknumber +" " +  self.title + " (" + self.album + ")"
                            
               
    def _getMp3Tags(self):
        if self.path[-4:].lower() == ".mp3":
            audio = MP3(self.path, ID3=EasyID3)
            LOG.debug(EasyID3.valid_keys.keys())
            if audio.has_key('album'): self.album = audio["album"][0]
            if audio.has_key('artist'): self.artist = audio["artist"][0]
            if audio.has_key('title'): self.title = audio["title"][0]
            if audio.has_key('date'): self.date = audio["date"][0]
            if audio.has_key('genre'): self.genre = audio["genre"][0]
            if audio.has_key('tracknumber'): self.tracknumber = audio["tracknumber"][0]
        
