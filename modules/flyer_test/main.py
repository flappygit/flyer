#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Documentation Goes Here.

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


class FlyerApp(App):
	userIsValid = False

	def login(self, userId, password):
		return True

	def getUserDetails(self):
		self.userId = self.root.ids.userId.text
		self.password = self.root.ids.password.text

		print self.userId
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
	LabelBase.register(name='Riona',
                       fn_regular='RionaSans-Regular.ttf',
                       fn_bold='RionaSans-Bold.ttf')
	FlyerApp().run()
