__author__ = 'nir.belinky'
import xbmcaddon

#
# To use:
# from addOnSettings import *
#
# addon_settings = addOnSettings();  
# ks = addon_settings.getKS();
#


class addOnSettings:

    def __init__(self):
        self.addon = xbmcaddon.Addon();

    def get(self, id):
        try:
            return self.addon.getSetting(id);
        except:
            return None;

    def set(self, id, value):
        try:
            self.addon.setSetting(id, value);
        except:
            return False;
        return True;

    def getKS(self):
        return self.get('ks');

	def getEmail(self):
		return self.get('Email');

	def getPassword(self):
		return self.get('Password');



