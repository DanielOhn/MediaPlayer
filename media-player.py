# importing time and vlc
from inspect import getsource
import re
import time, vlc, os, msvcrt
import random
from os.path import isfile, join

dir_path = os.path.dirname(os.path.realpath(__file__))


# Plays a random video in VLC player fullscreened.
# Resets itself and keeps playing videos, uses root directory and /Videos folder
# to find subdirectories and video files.
class VLC_Player:
	def __init__(self):
		self.instance = vlc.Instance()
		self.player = vlc.MediaPlayer()
		self.media = None

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

		self.reset()

	def reset(self):
		self.media = None 
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
		onlyfiles = [f for f in os.listdir(src) if isfile(join(src, f))]

		while(onlyfiles == []):
			src = src + "\\" + self.getSubfolders(src)
			onlyfiles = [f for f in os.listdir(src) if isfile(join(src, f))]

		if (onlyfiles):
			src = src + "\{0}".format(random.choice(onlyfiles))
			print(src)
			return src
	
	def getSubfolders(self, dir):
		subfolders = os.listdir(dir)
		subfolder = random.choice(subfolders)
		return subfolder

video = VLC_Player()
video.play()
