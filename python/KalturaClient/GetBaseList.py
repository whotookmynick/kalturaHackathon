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

    def __init__(self, ks, page_size=10):
        if (len (ks) == 0 ):
            raise GetBaseList ("KS cannot be empty.")
        self.KS = ks
        if (page_size < 1):
            raise GetBaseList ("Pager cannot be less than 1")
        self.page_size = page_size
        self.createPartnerEntryList()


    def createPartnerEntryList(self):

        # create pager
        pager = KalturaFilterPager()
        pager.pageSize = self.page_size
        pager.pageIndex = 0
        
        # set ks pm client
        kalturaConfig = KalturaConfiguration()
        kalturaConfig.serviceUrl = self.serviceUrl
        self.client_handle = KalturaClient(kalturaConfig)
        self.client_handle.setKs(self.KS)
        
        # get entry list
        result = self.client_handle.baseEntry.list(None, pager)
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
