from dataclasses import dataclass

import importlib
import pkgutil

import panels


@dataclass
class PanelInfo:

    name: str
    description: str

    cls: type


def discover():

    registry = {}

    for module in pkgutil.iter_modules(panels.__path__):

        mod = importlib.import_module(
            f"panels.{module.name}.panel"
        )

        panel = getattr(mod, "PANEL", None)

        if panel is None:
            continue

        registry[panel.name] = PanelInfo(
            name=panel.name,
            description=panel.description,
            cls=panel,
        )

    return registry
