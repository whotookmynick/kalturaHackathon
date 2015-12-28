#!/usr/bin/python
# Version 0.5
import sys
from KalturaClient import *
from kalturaAuthenticate import *


class GetBaseList:

    def __init__(self, user_email, password, service_url):
        self.serviceUrl = service_url
        self.userEmail = user_email
        self.password = password
        self.serviceUrl = service_url
        authenticator = KalturaAuthenticator(self.userEmail, self.password, self.serviceUrl)
        self.KS = authenticator.getKs()
        self.buildAddonToKalturaDict()
		
    def buildAddonToKalturaDict(self):
        self.addon_to_kaltura_types = {}
        self.addon_to_kaltura_types['VOD'] 		= Client.KalturaMediaType.VIDEO
        self.addon_to_kaltura_types['Live!']	= Client.KalturaMediaType.LIVE_STREAM_FLASH
        self.addon_to_kaltura_types['Audio'] 	= Client.KalturaMediaType.AUDIO
        self.addon_to_kaltura_types['Image'] 	= Client.KalturaMediaType.IMAGE

    def createPartnerEntryList(self, type, page_index=1, page_size=10):

        # create pager
        pager = Client.KalturaFilterPager()
        pager.pageSize = page_size
        pager.pageIndex = page_index

        kalturaConfig = KalturaConfiguration()
        kalturaConfig.serviceUrl = self.serviceUrl
        self.client_handle = KalturaClient(kalturaConfig)
        self.client_handle.setKs(self.KS)
        
        # get entry list
        filter = Client.KalturaMediaEntryFilter()
        print self.addon_to_kaltura_types[type]
        filter.mediaTypeEqual = self.addon_to_kaltura_types[type]
        result = self.client_handle.baseEntry.list(filter, pager)
        self.final_object_content = result.getObjects()
        self.final_object_content_length = len(self.final_object_content)

    def getPartnerEntryList(self):
        return self.final_object_content


# Main
if __name__=="__main__":
    try:
        baseListObj = GetBaseList("moshe.maor@kaltura.com", "Sara1975*", "http://www.kaltura.com")
        baseListObj.createPartnerEntryList("VOD")
        base_list = baseListObj.getPartnerEntryList();
        for i in base_list: 
            print i.name
        baseListObj.createPartnerEntryList("Live!")
        base_list = baseListObj.getPartnerEntryList();
        for i in base_list: 
            print i.name
        baseListObj.createPartnerEntryList("Audio")
        base_list = baseListObj.getPartnerEntryList();
        for i in base_list: 
            print i.name
   
    except GetBaseList as ex_message:
        print ex_message
        exit (1)

    exit (0)
