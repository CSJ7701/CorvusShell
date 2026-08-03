import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


def run_panel(panel):

    class App(Gtk.Application):

        def do_activate(self):

            window = panel(self)
            window.present()

    App().run()
