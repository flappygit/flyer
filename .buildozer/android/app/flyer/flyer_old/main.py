#/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class FlyerHeader(BoxLayout):
	pass


class FlyerTabs(BoxLayout):
	tab_no = 1
	if tab_no == 2 or tab_no == 3:
		tab_no = 2(tab_no) + 1
		
	#organisation_tab = Factory.FlyerTab()
	#organisation_tab.tab_no = 1
	#organisation_tab.tab_name = '[b]Organisation Tab:[/b]'
	#self.add_widget(organisation_tab)

class FlyerIntro(BoxLayout):
	username = 'Pavan Kumar'
	status = ' In Esteem Asrani'
	last_updated = '30-04-2015 15:45'
	daily_quote = '[b]Quote of The Day:[/b]  \"The Supreme art of war is to subdue the enemy without \
fighting.\"\n [b]~ Sun Tzu[/b]'


class FlyerRoot(BoxLayout):
	pass


class FlyerApp(App):
	pass


if __name__ == '__main__':
	Window.clearcolor = get_color_from_hex('#272A3E')
	FlyerApp().run()
