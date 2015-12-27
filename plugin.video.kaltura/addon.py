import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://cfvod.kaltura.com/pd/p/1875831/sp/187583100/serveFlavor/entryId/1_9aali829/v/1/flavorId/1_q9lyy0g5/fileName/Creating_together_(Source).mov/name/a.mov'
li = xbmcgui.ListItem('My First Video!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)