#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
FLYER: The Flipkart HR Communications App.

Author: Vinay Keerthi KT
Last Edited: June 2015
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.factory import Factory

import Elijah

class FlyerApp(App):
	userIsValid = False

	def login(self, user_id, password):
		return True

	def getUserDetails(self):
		self.user_id = self.root.ids.userId.text
		self.password = self.root.ids.password.text

		print self.user_id
		print self.password

		self.userIsValid = self.login(self.userId, self.password)

		print self.userIsValid

		if self.userIsValid:
			self.changeLayout()
		else:
			self.showError()

	def changeLayout(self):
		self.flyerTabs = Factory.FlyerTab()

		self.root.clear_widgets()
		self.root.add_widget(self.flyerTabs)

	def showError(self):
		pass

if __name__ == '__main__':
	Window.clearcolor = get_color_from_hex('#0088D6')
	regular_font = os.path.join('fonts', 'RionaSans-Regular.ttf')
	bold_font = os.path.join('fonts', 'RionaSans-Bold.ttf')
	LabelBase.register(name='Riona',
                       fn_regular=regular_font,
                       fn_bold=bold_font)
	FlyerApp().run()
