from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class WeatherApp(App):
    pass

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    def search_location(self):
        print "The answer is 42 when the location is %s." % self.search_input.text

if __name__ == "__main__":
    WeatherApp().run()