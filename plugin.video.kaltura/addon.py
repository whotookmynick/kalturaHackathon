import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
import pprint

from addOnSettings  		import *
from getBaseList    		import *
from itemInfo       		import *
from kalturaItemInfoAdapter 	import *
from kalturaStreamInfoAdapter   import *

addon_handle        = int(sys.argv[1])
addon_settings      = addOnSettings()
kaltura_addon_ks    = addon_settings.getKS()
kaltura_addon = xbmcaddon.Addon('plugin.video.kaltura')

xbmcplugin.setContent(addon_handle, 'movies')
kaltura_play_list   = GetBaseList(kaltura_addon_ks).getPartnerEntryList()
info_list           = ItemInfoList(kaltura_play_list);

for i in range(len(kaltura_play_list)):
    item_info       = info_list.getItemInfo(i);
    url             = item_info.downloadUrl
    kodi_list_item  = xbmcgui.ListItem(item_info.name, iconImage='DefaultVideo.png')
    kodi_list_item.setArt({'thumb': item_info.thumbUrl, 'fanart':kaltura_addon.getAddonInfo('fanart')})
    kodi_item_info  = KalturaItemInfoAdapter(kaltura_play_list[i])
    kodi_item_info.setKodiItemInfo(kodi_list_item)
    kodi_stream_info = KalturaStreamInfoAdapter(kaltura_play_list[i])
    kodi_stream_info.addKodiStreamItemInfo(kodi_list_item)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=item_info.downloadUrl, listitem=kodi_list_item)
xbmcplugin.endOfDirectory(addon_handle)
