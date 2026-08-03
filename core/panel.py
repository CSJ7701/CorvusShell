from __future__ import annotations
from dataclasses import dataclass

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Gtk4LayerShell", "1.0")
from gi.repository import Gtk
from gi.repository import Gtk4LayerShell as LayerShell

@dataclass
class PanelConfig:
    anchor: str = "top"

    width: int = 500
    height: int = 40

    exclusive: bool = False
    keyboard_mode: bool = False

    margin_top: int = 0
    margin_bottom: int = 0
    margin_left: int = 0
    margin_right: int = 0

class Panel(Gtk.ApplicationWindow):

    name = "panel"
    description = ""
    config = PanelConfig()
    
    def __init__(self, app):
        super().__init__(application=app)
        self.setup_window()
        self.build()

    def setup_window(self):
        cfg = self.config
        self.set_default_size(cfg.width, cfg.height)
        LayerShell.init_for_window(self)
        LayerShell.set_layer(
            self,
            LayerShell.Layer.TOP,
        )

        anchors = {
            "top": LayerShell.Edge.TOP,
            "bottom": LayerShell.Edge.BOTTOM,
            "left": LayerShell.Edge.LEFT,
            "right": LayerShell.Edge.RIGHT,
        }

        LayerShell.set_anchor(
            self,
            anchors[cfg.anchor],
            True,
        )

        if cfg.exclusive:
            LayerShell.auto_exclusive_zone_enable(self)

        LayerShell.set_margin(
            self,
            LayerShell.Edge.TOP,
            cfg.margin_top,
        )

        LayerShell.set_margin(
            self,
            LayerShell.Edge.BOTTOM,
            cfg.margin_bottom,
        )

        LayerShell.set_margin(
            self,
            LayerShell.Edge.LEFT,
            cfg.margin_left,
        )

        LayerShell.set_margin(
            self,
            LayerShell.Edge.RIGHT,
            cfg.margin_right,
        )

        if cfg.keyboard_mode:
            LayerShell.set_keyboard_mode(
                self,
                LayerShell.KeyboardMode.EXCLUSIVE,
            )

    def build(self):
        raise NotImplementedError()

    def start(self):
        self.present()
