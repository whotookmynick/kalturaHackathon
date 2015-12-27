import sys
from KalturaClient import *
if __name__=="__main__":
	ks = sys.argv[1]
	kalturaConfig = KalturaConfiguration(102)
	kalturaConfig.serviceUrl = 'http://allinone-be.dev.kaltura.com'
	kalturaClient = KalturaClient(kalturaConfig)
	kalturaClient.setKs(ks)
	filter = None
	pager = None
	result = kalturaClient.baseEntry.list(filter, pager)
	print result
