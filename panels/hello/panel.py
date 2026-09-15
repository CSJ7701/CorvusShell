from gi.repository import Gtk
from core.panel import Panel, PanelConfig

class HelloPanel(Panel):
    name = "hello"
    description = "Example panel"
    config = PanelConfig(
        anchor="left",
        width=60,
        height=600,
        exclusive=True,
    )

    def build(self):
        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
        )
        box.append(
            Gtk.Label(label="Hello")
        )
        self.set_child(box)

# PANEL = HelloPanel
