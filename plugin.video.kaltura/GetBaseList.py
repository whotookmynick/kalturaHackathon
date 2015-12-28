#!/usr/bin/python
# Version 0.5
import sys
from KalturaClient import *
from kalturaAuthenticate import *

class GetBaseList:
    # KS = ""
    entryList = ""
    pager = 0
    kalturaConfig = ""
    client_handle = ""
    # serviceUrl = 'http://allinone-be.dev.kaltura.com'
    serviceUrl = 'http://www.kaltura.com'
    final_object_content_length = 0
    final_object_content = ""

    def __init__(self, user_email, password, service_url, page_size=500):
        # if (len (ks) == 0 ):
            # raise GetBaseList ("KS cannot be empty.")
        # self.KS = ks
        self.serviceUrl = service_url
        self.userEmail = user_email
        self.password = password
        if (page_size < 1):
            raise GetBaseList ("Pager cannot be less than 1")
        self.page_size = page_size
        self.createPartnerEntryList()


    def createPartnerEntryList(self):

        # create pager
        pager = Client.KalturaFilterPager()
        pager.pageSize = self.page_size
        pager.pageIndex = 0
        
        #getKs
        authenticator = KalturaAuthenticator(self.userEmail, self.password, self.serviceUrl)
        KS = authenticator.getKs()
        
        # set ks pm client
        kalturaConfig = KalturaConfiguration()
        kalturaConfig.serviceUrl = self.serviceUrl
        self.client_handle = KalturaClient(kalturaConfig)
        self.client_handle.setKs(KS)
        
        # get entry list
        result = self.client_handle.baseEntry.list(None, None)
        self.final_object_content = result.getObjects()
        self.final_object_content_length = len(self.final_object_content)

    def getPartnerEntryList(self):
        return self.final_object_content


# Main
if __name__=="__main__":
    try:
        if len(sys.argv) < 3:
            print "Not enough parameters were given. Must give email and password, service-url is optional"
            exit (1)
        user_email = sys.argv[1]
        password = sys.argv[2]
        service_url = "http://www.kaltura.com"
        if len(sys.argv) > 3:
            service_url = sys.argv[3]
            
        base_list = GetBaseList(user_email, password, service_url, 5)
        # base_list = GetBaseList("MjVmMDI4ZTFjMDQ4ZjA4ZTZhNDc0ZjRkMWJjMzJjYzkxNjM0ZTYyOHwxMDI7MTAyOzE0NTEyOTYzNzM7MjsxNDUxMjA5OTczLjI2NTU7a29iaS5taWNoYWVsaUBrYWx0dXJhLmNvbTsqLGRpc2FibGVlbnRpdGxlbWVudDs7", 5)
        base_list.getPartnerEntryList()

    except GetBaseList as ex_message:
        print ex_message
        exit (1)

    exit (0)
