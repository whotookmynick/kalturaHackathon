#!/usr/bin/python

import sys
from iconMap import iconMap

class kalturaToGenericTypeTranslate:
	relevant_types = {1 : 'clip', 2 : 'image', 5 : 'audio', 201 : 'live'}
	relevant_types_keys = []
	icon_mapping = ""

	def __init__(self):
		self.relevant_types_keys = self.relevant_types.keys()
		self.icon_mapping = iconMap()

	def mapKalturaType(self, type_id):
		# print "type_id "+str(type_id)+" relevant_types_keys "+str(self.relevant_types_keys)+""
		if (type_id in self.relevant_types_keys):
			# print "found "+self.relevant_types[type_id]
			ret = self.icon_mapping.get_type_from_dict(self.relevant_types[type_id])
			return ret
		else:
			# print "not found"
			return self.icon_mapping.get_type_from_dict('blank')

	def getRelevant_types_keys(self):
		return self.relevant_types_keys

# Main
if __name__=="__main__":
	type_map = kalturaToGenericTypeTranslate()
	if len(sys.argv) < 2:
	    print "No parameters were given. You must provide one of the following:."+ type_map.getRelevant_types_keys()
	    exit (1)
	print type_map.mapKalturaType(int(sys.argv[1]))
	exit (0) 
 