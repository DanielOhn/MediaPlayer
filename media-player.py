# importing time and vlc
from inspect import getsource
import time, vlc, os, msvcrt
import random
from os.path import isfile, join

dir_path = os.path.dirname(os.path.realpath(__file__))
isPlaying = False 

class VLC_Player:
	def __init__(self):
		self.instance = vlc.Instance()
		self.player = vlc.MediaPlayer()
		self.media = None

		self.playing = False

	def play(self):
		source = self.getSource()
		self.media = self.setMedia(source)
		
		self.player.set_media(self.media)
		# play the video
		self.player.play()
		self.player.set_fullscreen(True)

		# Get length of the video and play its full duration
		time.sleep(0.5)
		time.sleep(self.getDuration())
		self.play()

	def getDuration(self):
		duration = self.media.get_duration()

		new_duraiton = str(duration)

		return int(new_duraiton[:-3])

	#method to play video
	def setMedia(self, source):
		# creating a media
		return vlc.Media(source)
		# setting media to the player
	
	# Need to update this to get all of the directorys within Videos and select a random video
	def getSource(self):
		# Gets folders within the current directory
		sub_folders = [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]

		# Get the Videos folder in root directory
		video = None
		for folder in sub_folders:
			if folder == "Videos":
				video = folder
				
		src = "{0}\{1}".format(dir_path, video)

		# Get list of subdirectories in Videos folder
		subfolders = os.listdir(src)
		print(subfolders)
		
		src = "{0}\{1}\{2}".format(dir_path, video, random.choice(subfolders))
		print(src)

		onlyfiles = [f for f in os.listdir(src) if isfile(join(src, f))]

		if (onlyfiles):
			print("onlyfiles: ", onlyfiles)
			src = src + "\{0}".format(random.choice(onlyfiles))
			return src
		
		print(src)
		return src

video = VLC_Player()
video.play()
