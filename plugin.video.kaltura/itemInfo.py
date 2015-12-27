import sys

class ItemInfoList:
    
    itemList = []
    
    def __init__(self, itemList): 
        self._itemList = itemList
        
    def getItemInfo(self,index):
        item = ItemInfo(self._itemList[index])
        return item
        
    
class ItemInfo:
        
    downloadUrl = ""
    thumbUrl = ""
    name = ""
    description = ""
    
    def __init__(self, item):
        self.downloadUrl = item.getDownloadUrl()
        self.thumbUrl = item.getThumbnailUrl()
        self.name = item.getName()
        self.description = item.getDescription()
        
    def __str__(self):
        return "Name ["+self.name+"]\n Description ["+self.description+"]\n Download-url ["+self.downloadUrl+"]\n Thumbnail-URL ["+self.thumbUrl+"]\n"


if __name__ == '__main__':
    sys.path.append("../python/")
    from KalturaClient import *
    kalturaConfig = KalturaConfiguration()
    kalturaConfig.serviceUrl = "http://allinone-be.dev.kaltura.com"
    client_handle = KalturaClient(kalturaConfig)
    client_handle.setKs("MjVmMDI4ZTFjMDQ4ZjA4ZTZhNDc0ZjRkMWJjMzJjYzkxNjM0ZTYyOHwxMDI7MTAyOzE0NTEyOTYzNzM7MjsxNDUxMjA5OTczLjI2NTU7a29iaS5taWNoYWVsaUBrYWx0dXJhLmNvbTsqLGRpc2FibGVlbnRpdGxlbWVudDs7")
    pager = Client.KalturaFilterPager()
    pager = Client.KalturaFilterPager()
    pager.pageSize = 10
    pager.pageIndex = 0
    result = client_handle.baseEntry.list(None, None)
    object_list = result.getObjects()
    infoList = ItemInfoList(object_list)
    itemInfo = infoList.getItemInfo(0)
    print str(itemInfo)
    