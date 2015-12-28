import sys, xbmcgui, xbmcplugin, xbmc, pprint, urllib, urlparse, os

from addOnSettings  		import *
from getBaseList    		import *
from itemInfo       		import *
from kalturaItemInfoAdapter 	import *
from kalturaStreamInfoAdapter   import *
from kalturaToGenericTypeTranslate import *

UTF8         	= 'utf-8'
base_url 		= sys.argv[0]
addon_handle    = int(sys.argv[1])
addon_settings  = addOnSettings()
addon_args 		= urlparse.parse_qs(sys.argv[2][1:])
                                  
addon           = xbmcaddon.Addon('plugin.video.kaltura')
addon_home      = addon.getAddonInfo('path').decode(UTF8)
addon_fanart  	= xbmc.translatePath(os.path.join(addon_home, 'fanart.jpg'))
next_icon     	= xbmc.translatePath(os.path.join(addon_home, 'resources','icons','next.png'))
type_map = kalturaToGenericTypeTranslate()

play_list_obj 	= GetBaseList(addon_settings.getEmail(), addon_settings.getPassword(), addon_settings.getServiceUrl())

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def build_pages(type):
	page_indx_list 	= addon_args.get('page', [1])
	page_indx 		= int(page_indx_list[0])
	page_size 		= 10

	xbmcplugin.setContent(addon_handle, 'movies')
	play_list_obj.createPartnerEntryList(type, page_indx, page_size)	  
	kaltura_play_list 		= play_list_obj.getPartnerEntryList()
	info_object         	= ItemInfoList(kaltura_play_list);

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
		

	if len(kaltura_play_list) == page_size:
		name = '[COLOR blue]Next Page >>' + str(((page_indx - 1) * page_size) + 1) + '-' + str(((page_indx - 1) * page_size) + page_size) + '[/COLOR]' 
		page_indx = page_indx + 1
		url = build_url({'page': page_indx, 'mode': type})
		kodi_list_item = xbmcgui.ListItem(name, '', next_icon, None)
		kodi_list_item.setProperty('fanart_image', addon_fanart)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=kodi_list_item, isFolder=True)

	xbmcplugin.endOfDirectory(addon_handle)

def build_home():
	mode = addon_args.get('mode', None)
	
	if mode is None:
		url = build_url({'mode': 'VOD'})
		iconImage = type_map.mapKalturaType(1)

		# li = xbmcgui.ListItem('VOD', iconImage='DefaultFolder.png')
		li = xbmcgui.ListItem('VOD', iconImage=iconImage)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

		url = build_url({'mode': 'Live!'})
		iconImage = type_map.mapKalturaType(201)
		li = xbmcgui.ListItem('Live!', iconImage=iconImage)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

		url = build_url({'mode': 'Audio'})
		iconImage = type_map.mapKalturaType(5)
		li = xbmcgui.ListItem('Audio', iconImage=iconImage)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
		
		url = build_url({'mode': 'Image'})
		iconImage = type_map.mapKalturaType(2)
		li = xbmcgui.ListItem('Image', iconImage=iconImage)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

		xbmcplugin.endOfDirectory(addon_handle)	
	else:
		build_pages(mode[0])
		
build_home();

