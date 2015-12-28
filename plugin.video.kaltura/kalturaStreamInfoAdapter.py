class KalturaStreamInfoAdapter:
    mKodiStreamInfoDict={}

    def __init__(self, kaltura_info_item):
        #self.mKodiStreamInfoDict['codec']=None
        #self.mKodiStreamInfoDict.['aspect']=None
        self.mKodiStreamInfoDict['width']=kaltura_info_item.width
        self.mKodiStreamInfoDict['height']=kaltura_info_item.height
        self.mKodiStreamInfoDict['duration']=kaltura_info_item.duration

    def addKodiStreamItemInfo(self,kodi_list_item):
        kodi_list_item.addStreamInfo("video",self.mKodiStreamInfoDict)

