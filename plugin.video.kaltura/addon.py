import sys, xbmcgui, xbmcplugin, xbmc, pprint, urllib, urlparse, os

from addOnSettings  		  import *
from getBaseList    		  import *
from itemInfo       		  import *
from kalturaItemInfoAdapter   import *
from kalturaStreamInfoAdapter import *



UTF8         	= 'utf-8'
base_url 		= sys.argv[0]
addon_handle    = int(sys.argv[1])
addon_settings  = addOnSettings()
addon_args 		= urlparse.parse_qs(sys.argv[2][1:])
                                  
addon           = xbmcaddon.Addon('plugin.video.kaltura')
addon_home      = addon.getAddonInfo('path').decode(UTF8)
addon_fanart  	= xbmc.translatePath(os.path.join(addon_home, 'fanart.jpg'))
next_icon     	= xbmc.translatePath(os.path.join(addon_home, 'resources','icons','next.png'))

page_indx_list 	= addon_args.get('page', [1])
page_indx 		= int(page_indx_list[0])

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

xbmcplugin.setContent(addon_handle, 'movies')
kaltura_play_list   = GetBaseList(addon_settings.getEmail(), 
								  addon_settings.getPassword(), 
								  addon_settings.getServiceUrl(), page_indx).getPartnerEntryList()
								  
info_object         = ItemInfoList(kaltura_play_list);

for i in range(len(kaltura_play_list)):
    item_info       = info_object.getItemInfo(i);
    url             = item_info.downloadUrl
    kodi_list_item  = xbmcgui.ListItem(item_info.name, iconImage='DefaultVideo.png')
    kodi_list_item.setArt({'thumb': item_info.thumbUrl, 'fanart':addon.getAddonInfo('fanart')})
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
