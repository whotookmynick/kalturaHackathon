#!/usr/bin/python
# Version 0.5
import sys
from KalturaClient import *


class GetBaseList:
	KS = ""
	entryList = ""
	pager = 0
	kalturaConfig = ""
	client_handle = ""
	serviceUrl = 'http://allinone-be.dev.kaltura.com'
	final_object_content_length = 0
	final_object_content = ""

	def __init__(self, KS_input, pager_input=10):
		if (len (KS_input) == 0 ):
			raise GetBaseList ("KS cannot be empty.")
		self.KS = KS_input
		if (pager_input < 1):
			raise GetBaseList ("Pager cannot be less than 1")
		self.pager = pager_input
		self.createPartnerEntryList()


	def createPartnerEntryList(self):
		kalturaConfig = KalturaConfiguration()
		kalturaConfig.serviceUrl = self.serviceUrl
		self.client_handle = KalturaClient(kalturaConfig)
		self.client_handle.setKs(self.KS)
		pager = Client.KalturaFilterPager()
		pager.pageSize = 1000
		pager.pageIndex = 0
		result = self.client_handle.baseEntry.list(None, None)
		self.final_object_content = result.getObjects()
		self.final_object_content_length = len(self.final_object_content)
		# TODO add check for empty list

	def getPartnerEntryList(self):
		return self.final_object_content

	def return_list_indexes(self, current_index, page_size):
		page_entry_list = []
		index = current_index
		if (current_index + page_size < self.final_object_content_length):
			while index < (current_index + page_size):
				# print index,
				index = index + 1
				page_entry_list.append(self.final_object_content[index])
			return page_entry_list
		else:
			print "end of array"
			while index < self.final_object_content_length:
				# print index,
				index = index + 1
				page_entry_list.append(self.final_object_content[index])
			return page_entry_list



# Main
if __name__=="__main__":
	try:
		if len(sys.argv) < 2:
			print "No parameters were given. Must have a proper KS."
		ks = sys.argv[1]
		base_list = GetBaseList(ks, 5)
		# base_list = GetBaseList("MjVmMDI4ZTFjMDQ4ZjA4ZTZhNDc0ZjRkMWJjMzJjYzkxNjM0ZTYyOHwxMDI7MTAyOzE0NTEyOTYzNzM7MjsxNDUxMjA5OTczLjI2NTU7a29iaS5taWNoYWVsaUBrYWx0dXJhLmNvbTsqLGRpc2FibGVlbnRpdGxlbWVudDs7", 5)
		base_list.getPartnerEntryList()
		temp_list = base_list.return_list_indexes(0,4)


	except GetBaseList as ex_message: 
		print ex_message
		exit (1)

	exit (0)
