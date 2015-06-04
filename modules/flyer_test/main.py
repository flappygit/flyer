#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Documentation Goes Here.

Author: Bukkaraya Abinav
Last Edited: June 2015

"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import ObjectProperty


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
			changeLayout()
		else:
			showError()


	def changeLayout(self):
		pass

	def showError(self):
		pass








if __name__ == '__main__':
	Window.clearcolor = get_color_from_hex('#0088D6')
	LabelBase.register(name='Riona',
                       fn_regular='RionaSans-Regular.ttf',
                       fn_bold='RionaSans-Bold.ttf')
	FlyerApp().run()
