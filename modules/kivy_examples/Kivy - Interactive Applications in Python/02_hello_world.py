#02_hello_world.py
import kivy
from kivy.app import App
from kivy.uix.button import Label
class Hello2App(App):
	def build(self):
		return Label()

if __name__ == "__main__":
	Hello2App().run()