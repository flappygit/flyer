#/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class FlyerHeader(BoxLayout):
	pass

class FlyerIntro(BoxLayout):
	username = 'Pavan Kumar'
	status = ' In Esteem Asrani'
	last_updated = '30-04-2015 15:45'
	daily_quote = 'Quote of The Day: \n\"The Supreme art of war is\n to subdue the enemy without\n \
fighting.\"\n [b]~ Sun Tzu[/b]'

class FlyerRoot(BoxLayout):
	pass


class FlyerApp(App):
	pass


if __name__ == '__main__':
	FlyerApp().run()
