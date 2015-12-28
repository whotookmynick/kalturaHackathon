#!/usr/bin/python
# Version 0.5
import sys
from KalturaClient import *
from kalturaAuthenticate import *


class GetBaseList:
    KS = ""
    entryList = ""
    pager = 0
    kalturaConfig = ""
    client_handle = ""
    # serviceUrl = 'http://allinone-be.dev.kaltura.com'
    serviceUrl = 'http://www.kaltura.com'
    final_object_content_length = 0
    final_object_content = ""

    def __init__(self, user_email, password, service_url, page_index=1, page_size=10):
        self.serviceUrl = service_url
-       self.userEmail = user_email
-       self.password = password
-       self.page_size = page_size
        self.page_index = page_index
        self.createPartnerEntryList()


    def createPartnerEntryList(self):

        # create pager
        pager = Client.KalturaFilterPager()
        pager.pageSize = self.page_size
        pager.pageIndex = self.page_index
        
        # set ks pm client
        authenticator = KalturaAuthenticator(self.userEmail, self.password, self.serviceUrl)
        KS = authenticator.getKs()
+
        kalturaConfig = KalturaConfiguration()
        kalturaConfig.serviceUrl = self.serviceUrl
        self.client_handle = KalturaClient(kalturaConfig)
        self.client_handle.setKs(KS)
        
        # get entry list
        filter = Client.KalturaMediaEntryFilter()
        filter.typeEqual = Client.KalturaEntryType.MEDIA_CLIP
        result = self.client_handle.media.list(filter, pager)
        self.final_object_content = result.getObjects()
        self.final_object_content_length = len(self.final_object_content)

    def getPartnerEntryList(self):
        return self.final_object_content


# Main
if __name__=="__main__":
    try:
        if len(sys.argv) < 2:
            print "No parameters were given. Must have a proper KS."
        ks = sys.argv[1]
        base_list = GetBaseList(ks, 5)
        # base_list = GetBaseList("MjVmMDI4ZTFjMDQ4ZjA4ZTZhNDc0ZjRkMWJjMzJjYzkxNjM0ZTYyOHwxMDI7MTAyOzE0NTEyOTYzNzM7MjsxNDUxMjA5OTczLjI2NTU7a29iaS5taWNoYWVsaUBrYWx0dXJhLmNvbTsqLGRpc2FibGVlbnRpdGxlbWVudDs7", 5)
        base_list.getPartnerEntryList()

    except GetBaseList as ex_message:
        print ex_message
        exit (1)

    exit (0)
