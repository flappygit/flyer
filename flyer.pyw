import os.path
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from modules.flyerapp import FlyerApp
from modules import Elijah

if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#0088D6')
    regular_font = os.path.join('fonts', 'RionaSans-Regular.ttf')
    bold_font = os.path.join('fonts', 'RionaSans-Bold.ttf')
    italic_font = os.path.join('fonts', 'RionaSans-Italic.ttf')
    LabelBase.register(name='Riona',
                       fn_regular=regular_font,
                       fn_bold=bold_font,
                       fn_italic=italic_font)
    FlyerApp().run()