import sys
import xbmcgui
import xbmcplugin

from addOnSettings import *
from GetBaseList import *
from itemInfo import *

addon_handle    = int(sys.argv[1])
addon_settings  = addOnSettings()
addon_ks        = addon_settings.getKS()

xbmcplugin.setContent(addon_handle, 'movies')
play_list = GetBaseList(addon_ks).getPartnerEntryList()
info_list = ItemInfoList(play_list);

for i in range(len(play_list)):
    item_info = info_list.getItemInfo(i);
    url = item_info.downloadUrl
    li = xbmcgui.ListItem(item_info.name, iconImage='DefaultVideo.png')
    li.setArt({'thumb': item_info.thumbUrl})
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=item_info.downloadUrl, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)

