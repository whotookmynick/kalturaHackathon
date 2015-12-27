from KalturaClient import *
import base64
import hashlib

def sha_message(msg,do_base64=True):
    sha = hashlib.sha1()            
    sha.update(msg)
    sha1_key = sha.hexdigest() 
    
    return base64.standard_b64encode(sha1_key) if do_base64 else sha1_key

serviceUrl = 'http://allinone-be.dev.kaltura.com'
kalturaConfig = KalturaConfiguration()
kalturaConfig.serviceUrl = serviceUrl
client_handle = KalturaClient(kalturaConfig)

#Create widget session
ws = client_handle.session.startWidgetSession("_102", 999999999)
client_handle.setKs(ws.ks)
print "widget session ["+ws.ks+"]"
#get App token
appToken = client_handle.appToken.get("0_njn488zc")

#start appToken session
tokenHash = sha_message(ws.ks+appToken.token, False)
# tokenHash = sha_message(ws.ks+"110614a84acfe54c407f654e14a565a0")

# print "apptoken ["+appToken.token+"]"
print "tokenHash ["+tokenHash+"]"
aps = client_handle.appToken.startSession("0_njn488zc", tokenHash)

print "got apptoken session ["+str(aps.ks)+"]"

