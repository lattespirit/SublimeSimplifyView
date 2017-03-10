import sublime
import sublime_plugin

class SimplifyViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        prefs = sublime.load_settings('Preferences.sublime-settings')
        view_simplified = prefs.get('view_simplified')
        
        if view_simplified == False:
            self.action(True, False)
        else:
            self.action(False, True)

    def action(self, condition, value):
        prefs = sublime.load_settings('Preferences.sublime-settings')

        if prefs.get('line_numbers') == condition:
            prefs.set('line_numbers', value)

        if self.view.window().is_minimap_visible() == condition:
            self.view.window().set_minimap_visible(value)

        if self.view.window().is_menu_visible() == condition:
            self.view.window().set_menu_visible(value)

        if self.view.window().is_sidebar_visible() == condition:
            self.view.window().set_sidebar_visible(value)

        if self.view.window().is_status_bar_visible() == condition:
            self.view.window().set_status_bar_visible(value)

        if self.view.window().get_tabs_visible() == condition:
            self.view.window().set_tabs_visible(value)

        prefs.set('view_simplified', condition)
