#/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class AddHeader(BoxLayout):
	pass

class AddIntroduction(BoxLayout):
	user = 'Pavan Kumar'
	location = 'Esteem Asrani'
	last_updated = '30-04-15 15:45'
	daily_quote = '\"The supreme art of war is \n \
to subdue the enemy without \nfighting.\" [b]~Sun Tzu[/b]'

class TabNavigation(GridLayout):
	pass

class FlyerRoot(BoxLayout):
	pass

class FlyerApp(App):
	pass

if __name__ == '__main__':
	FlyerApp().run()