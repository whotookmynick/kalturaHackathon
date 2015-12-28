import sys, xbmcgui, xbmcplugin, xbmc, pprint, urllib, urlparse, os

from addOnSettings  		import *
from getBaseList    		import *
from itemInfo       		import *
from kalturaItemInfoAdapter 	import *
from kalturaStreamInfoAdapter   import *
from kalturaToGenericTypeTranslate import *

UTF8         	= 'utf-8'
base_url 		= sys.argv[0]
addon_handle        = int(sys.argv[1])
addon_settings      = addOnSettings()
addon_args          = urlparse.parse_qs(sys.argv[2][1:])
addon               = xbmcaddon.Addon('plugin.video.kaltura')
addon_home          = addon.getAddonInfo('path').decode(UTF8)
addon_fanart        = xbmc.translatePath(os.path.join(addon_home, 'fanart.jpg'))
next_icon           = xbmc.translatePath(os.path.join(addon_home, 'resources','icons','next.png'))
page_indx_list      = addon_args.get('page', [1])
page_indx           = int(page_indx_list[0])

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

kaltura_addon_ks    = addon_settings.getKS()
kaltura_addon_user_email = addon_settings.getEmail()
kaltura_addon_user_password = addon_settings.getPassword()
kaltura_addon_service_url = addon_settings.getServiceUrl()
kaltura_addon = xbmcaddon.Addon('plugin.video.kaltura')

xbmcplugin.setContent(addon_handle, 'movies')
kaltura_play_list   = GetBaseList(kaltura_addon_user_email, kaltura_addon_user_password, kaltura_addon_service_url).getPartnerEntryList()
info_list           = ItemInfoList(kaltura_play_list);

for i in range(len(kaltura_play_list)):
    item_info       = info_list.getItemInfo(i);
    url             = item_info.downloadUrl
    type_map = kalturaToGenericTypeTranslate()
    iconImage = type_map.mapKalturaType(int(item_info.mediaType.getValue()))
    # xbmcgui.Dialog().ok("status", "iconImage ["+str(iconImage)+"]")
    if iconImage == "blank":
        iconImage="DefaultVideo.png"
    # kodi_list_item  = xbmcgui.ListItem(item_info.name, iconImage='/home/kobi/.kodi/addons/plugin.video.kaltura/resources/icons/blank.PNG')
    kodi_list_item  = xbmcgui.ListItem(item_info.name)
    kodi_list_item.setArt({'thumb': item_info.thumbUrl, 'fanart':kaltura_addon.getAddonInfo('fanart')})
    kodi_list_item.setIconImage('/home/kobi/.kodi/addons/plugin.video.kaltura/resources/icons/audio.png')
    kodi_item_info  = KalturaItemInfoAdapter(kaltura_play_list[i])
    kodi_item_info.setKodiItemInfo(kodi_list_item)
    kodi_stream_info = KalturaStreamInfoAdapter(kaltura_play_list[i])
    kodi_stream_info.addKodiStreamItemInfo(kodi_list_item)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=item_info.downloadUrl, listitem=kodi_list_item)
	

	
name = '[COLOR blue]Next Page >>' + str(((page_indx - 1) * 10) + 1) + '-' + str(((page_indx - 1) * 10) + 10) + '[/COLOR]' 
page_indx = page_indx + 1
url = build_url({'page': page_indx})

kodi_list_item = xbmcgui.ListItem(name, '', next_icon, None)
kodi_list_item.setProperty('fanart_image', addon_fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=kodi_list_item, isFolder=True)

xbmcplugin.endOfDirectory(addon_handle)


#    xbmcgui.Dialog().ok("status", "before ")