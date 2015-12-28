import sys
from KalturaClient import *

class KalturaAuthenticator:
    
    def __init__(self, user_email, password, service_url):
        self.email = user_email
        self.password = password
        self.service_url = service_url
    
    
    def getKs(self):
        kalturaConfig = KalturaConfiguration()
        kalturaConfig.serviceUrl = self.service_url
        self.client_handle = KalturaClient(kalturaConfig)
        ks = self.client_handle.user.loginByLoginId(self.email, self.password)
        return ks
        
        
if __name__ == '__main__':
    ka = KalturaAuthenticator("noam.arad@kaltura.com", "C)00kies1", "http://www.kaltura.com")
    ks = ka.getKs()
    print "got KS ["+ks+"]"
   
        