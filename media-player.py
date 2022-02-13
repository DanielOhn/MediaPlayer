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

	
	def getSource(self):
		# Gets folders within the current directory
		sub_folders = [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]

		#print(sub_folders)
		#print(random.choice(sub_folders))
		
		# print([name for name in os.listdir(".") if os.path.isdir(name)])
		src = "{0}\{1}".format(dir_path, random.choice(sub_folders))
		# 	print(src)
		onlyfiles = [f for f in os.listdir(src) if isfile(join(src, f))]

		#print("src: ", src)

		if (onlyfiles):
			print("onlyfiles: ", onlyfiles)
			src = src + "\{}".format(random.choice(onlyfiles))
		
		print(src)
		return src

video = VLC_Player()
video.play()


	
# call the video method

#getSrc()
#while True:		
		# wait time
		#time.sleep(0.001)
		
		# getting the duration of the video
		# duration = player.get_length()
		# print(duration)
		#time.sleep(duration)
		# printing the duration of the video
		#print("Duration : " + str(duration))