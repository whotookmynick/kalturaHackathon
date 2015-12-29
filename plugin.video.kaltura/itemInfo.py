import sys
from KalturaClient import *
from KalturaClient.Plugins.Caption import *

class ItemInfoList:
    
    itemList = []
    service_url = ""
    KS = ""
    captionAssets = {}
    
    def __init__(self, itemList, service_url, ks): 
        self._itemList = itemList
        self.service_url = service_url
        self.KS = ks
        
        kalturaConfig = KalturaConfiguration()
        kalturaConfig.serviceUrl = self.service_url
        self.client_handle = KalturaClient(kalturaConfig)
        self.client_handle.setKs(self.KS)
        
        #get all caption assets
        entryIds = ""
        for item in itemList:
            entryIds += item.getId() + ","
        if (entryIds != ""):
            filter = KalturaCaptionAssetFilter()
            filter.entryIdIn = entryIds
            captionAssetResult = self.client_handle.caption.captionAsset.list(filter, None)
            for captionAsset in captionAssetResult.getObjects():
                ItemInfoList.captionAssets[captionAsset.getEntryId()] = captionAsset
        
    def getItemInfo(self,index):
        item = ItemInfo(self._itemList[index], self.service_url, self.KS)
        return item
        
    
class ItemInfo:
        
    downloadUrl = ""
    thumbUrl = ""
    name = ""
    description = ""
    service_url = ""
    KS = ""
    
    '''
    KalturaBaseEntry item
    '''
    def __init__(self, item, service_url, ks):
        self.service_url = service_url
        self.KS = ks
        self.downloadUrl = self.createPlayManifestUrl(item)
        self.thumbUrl = item.getThumbnailUrl()
        self.name = item.getName()
        self.description = item.getDescription()
        self.mediaType = item.getMediaType()
        self.captionUrl = self.getCaptionUrl(item)
                
    def createPlayManifestUrl(self, item):

        ret_val = ""
        if (item.dataUrl is None or item.dataUrl == ""):
        # if (True):
            ret_val = self.service_url + "/p/" + str(item.getPartnerId()) + "/sp/"+ str(item.getPartnerId()) +"00/playManifest/entryId/"+ item.getId()+"/format/applehttp/protocol/http/a.m3u8"
            #ret_val = "http://cfvod.kaltura.com/pd/p/811441/sp/81144100/serveFlavor/entryId/1_3c0opsqp/v/21/flavorId/1_abro5rey/fileName/multi-audio_(Source).mp4/name/a.mp4"
        else:
            ret_val = item.dataUrl
            
        return ret_val
    
    def getCaptionUrl(self, item):
        ret_val = ""
        
        kalturaConfig = KalturaConfiguration()
        kalturaConfig.serviceUrl = self.service_url
        self.client_handle = KalturaClient(kalturaConfig)
        self.client_handle.setKs(self.KS)
        
        if (item.getId() in ItemInfoList.captionAssets.keys()):
            captionAssetItem = ItemInfoList.captionAssets[item.getId()]
            captionUrl = self.client_handle.caption.captionAsset.getUrl(captionAssetItem.getId())
            ret_val = captionUrl
            
        return ret_val
       
    
    def __str__(self):
        return "Name ["+self.name+"]\n Description ["+self.description+"]\n Download-url ["+self.downloadUrl+"]\n Thumbnail-URL ["+self.thumbUrl+"]\n captionUrl ["+self.captionUrl+"]"


if __name__ == '__main__':
    sys.path.append("../python/")
    from KalturaClient import *
    kalturaConfig = KalturaConfiguration()
    kalturaConfig.serviceUrl = "http://www.kaltura.com"
    client_handle = KalturaClient(kalturaConfig)
    client_handle.setKs("MGVlNTM5YjcyZjA1NTc0YWRhMWVmNjM2YWE4MDY0NWJiYjljN2Q5Ynw4MTE0NDE7ODExNDQxOzE0NTE0MTE1MDc7MjsxNDUxMzI1MTA3LjIwNjg7YWRtaW47ZGlzYWJsZWVudGl0bGVtZW50Ozs=")
    pager = Client.KalturaFilterPager()
    pager.pageSize = 10
    pager.pageIndex = 0
    result = client_handle.baseEntry.list(None, None)
    object_list = result.getObjects()
    infoList = ItemInfoList(object_list, "http://www.kaltura.com", "MGVlNTM5YjcyZjA1NTc0YWRhMWVmNjM2YWE4MDY0NWJiYjljN2Q5Ynw4MTE0NDE7ODExNDQxOzE0NTE0MTE1MDc7MjsxNDUxMzI1MTA3LjIwNjg7YWRtaW47ZGlzYWJsZWVudGl0bGVtZW50Ozs=")
    itemInfo = infoList.getItemInfo(0)
    print str(itemInfo)
    