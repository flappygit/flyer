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
        return Elijah.login(user_id, password)

    def getUserDetails(self):
        self.user_id = self.root.ids.user_id.text
        self.password = self.root.ids.password.text

        #print self.user_id
        #print self.password

        self.userIsValid = self.login(self.user_id, self.password)

        #print self.userIsValid

        if self.userIsValid:
            self.changeLayout()
        else:
            self.showError()

    def changeLayout(self):
        self.flyer_open_panel = Factory.FlyerOpenPanel()
        self.root.clear_widgets()
        self.root.add_widget(self.flyer_open_panel)
        quote = Elijah.getQuote()
        self.putReports()
        #print quote
        #Use the random quote this gets and use it as the "quote_space" label text.
        self.flyer_open_panel.ids.quote_space.text = quote
        self.flyer_open_panel.ids.flyer_password_changer.ids.reset_password_button.bind(on_press=self.changePassword)
    def showError(self):
        self.root.ids.password.text = ""

    def putReports(self):        
        reports = Elijah.fetchLatestReports()
        #print reports
        report_dict = {
            "Performance": {"Text": "", "Time Stamp":""},
            "OrgDev": {"Text": "", "Time Stamp":""},
            "Rewards": {"Text": "", "Time Stamp":""}
        }
        for report in reports:
            report_dict[report["report_type"]]["Text"] = report["report_text"]
            report_dict[report["report_type"]]["Time Stamp"] = report["time_stamp"]
        self.flyer_open_panel.ids.perf_report.text = report_dict["Performance"]["Text"]
        self.flyer_open_panel.ids.orgdev.text = report_dict["OrgDev"]["Text"]
        self.flyer_open_panel.ids.rewards.text = report_dict["Rewards"]["Text"]


    def changePassword(self, *args):
        password_field_1 = self.flyer_open_panel.ids.flyer_password_changer.ids.password_new_1.text
        password_field_2 = self.flyer_open_panel.ids.flyer_password_changer.ids.password_new_2.text
        if password_field_1 == password_field_2:
            self.password = password_field_1
            Elijah.changePassword(self.user_id, self.password)
            #print "Changed password to %s" %self.password

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#0088D6')
    regular_font = os.path.join('fonts', 'RionaSans-Regular.ttf')
    bold_font = os.path.join('fonts', 'RionaSans-Bold.ttf')
    italic_font = os.path.join('fonts', 'RionaSans-Italic.ttf')
    LabelBase.register(name='Riona',
                       fn_regular=regular_font,
                       fn_bold=bold_font,
                       fn_italic=italic_font)
    FlyerApp().run()
