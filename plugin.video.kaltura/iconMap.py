#!/usr/bin/python
import sys, os, xbmc, xbmcaddon

class iconMap:
	path = './.kodi/resources/icons'
	types = {'playlist' : 'list-numbered-256-000000.png', 'clip' : 'film.ico', 'live' : 'live.PNG', 'blank' : 'blank.PNG', 'audio':'audio.png', 'image':'image.png'}

	# def __init__(self):
	# 	# Dummy ctor

	def get_type_keys(self):
		ret_keys = self.types.keys()
		ret_keys.remove('blank')
		return ret_keys


	def get_type_from_dict (self, needed_type):
		keys = self.types.keys()
		addon = xbmcaddon.Addon('plugin.video.kaltura')
		addon_home = addon.getAddonInfo('path').decode('utf-8')
		if (needed_type in keys):
			file_name = xbmc.translatePath(os.path.join(addon_home, 'resources','icons',self.types[needed_type]))
			readable = os.access(file_name, os.R_OK)
			if (readable == True):
				return file_name
			else:
				# print "Not"
				return self.path+'/'+self.types['blank']
		else:
			return self.path+'/'+self.types['blank']


# Main
if __name__=="__main__":
	ret_type = iconMap()
	if (len(sys.argv) != 2):
		print "Must get only one paramater of the type:" + str (ret_type.get_type_keys())
		exit (1)
	print ret_type.get_type_from_dict(sys.argv[1])
	exit (0)
