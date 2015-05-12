#/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class AddButtons(BoxLayout):
	redButton = ObjectProperty()
	def printPos(self):
		print str(self.redButton.size)
		print str(self.redButton.pos)

class ColorApp(App):
	pass

if __name__ == '__main__':
	ColorApp().run()

