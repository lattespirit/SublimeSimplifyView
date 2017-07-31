import sublime
import sublime_plugin

class SimplifyViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().set_minimap_visible(False)
        self.view.window().set_menu_visible(False)
        self.view.window().set_sidebar_visible(False)
        self.view.window().set_status_bar_visible(False)
        self.view.window().set_tabs_visible(False)

        # hide line number
        prefs = sublime.load_settings('Preferences.sublime-settings')
        prefs.set('line_numbers', False)
