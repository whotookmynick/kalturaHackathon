from datetime import datetime

class KalturaItemInfoAdapter:
    mKodiInfoDict={}

    def __init__(self, kaltura_info_item):
        # self.mKodiInfoDict['genre']= None
	self.mKodiInfoDict['year']= datetime.fromtimestamp(kaltura_info_item.createdAt).strftime('%Y')
        #self.mKodiInfoDict['genre']= None
        #self.mKodiInfoDict['year']= None
        #self.mKodiInfoDict['episode']= None
        #self.mKodiInfoDict['season']= None
        #self.mKodiInfoDict['top250']= None
        #self.mKodiInfoDict['tracknumber']= None
        #self.mKodiInfoDict['rating']= None
        self.mKodiInfoDict['playcount']= kaltura_info_item.views
        #self.mKodiInfoDict['overlay']= None
        #self.mKodiInfoDict['castandrole']= None
        #self.mKodiInfoDict['director']= None
        #self.mKodiInfoDict['mpaa']= None
        self.mKodiInfoDict['plot']= kaltura_info_item.description
        #self.mKodiInfoDict['plotoutline']= None
        self.mKodiInfoDict['title']= kaltura_info_item.name
        #self.mKodiInfoDict['originaltitle']= None
        #self.mKodiInfoDict['sorttitle']= None
        self.mKodiInfoDict['duration']= kaltura_info_item.duration
        #self.mKodiInfoDict['studio']= None
        #self.mKodiInfoDict['tagline']= None
        #self.mKodiInfoDict['writer']= None
        #self.mKodiInfoDict['tvshowtitle']= None
        #self.mKodiInfoDict['premiered']= None
        #self.mKodiInfoDict['status']= None
        #self.mKodiInfoDict['code']= None
        #self.mKodiInfoDict['aired']= None
        #self.mKodiInfoDict['credits']= None
        self.mKodiInfoDict['lastplayed']= kaltura_info_item.lastPlayedAt 
        #self.mKodiInfoDict['album']= None
        #self.mKodiInfoDict['artist']= ""
        #self.mKodiInfoDict['votes']= None
        #self.mKodiInfoDict['trailer']= None
        self.mKodiInfoDict['dateadded']= datetime.fromtimestamp(kaltura_info_item.createdAt).strftime('%Y-%m-%d %H:%M:%S')
    def setKodiItemInfo(self,kodi_list_item):
        kodi_list_item.setInfo("video",self.mKodiInfoDict)
	
