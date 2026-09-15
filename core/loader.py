import importlib
import importlib.util
import os
import pkgutil
from pathlib import Path

from core.panel import Panel
import panels


def discover() -> dict[str, type[Panel]]:
    """Discovers built-in and user-defined panels, populating Panel.registry."""

    # Built in - 'panels' module
    for module in pkgutil.iter_modules(panels.__path__):
        try:
            importlib.import_module(f"panels.{module.name}.panel")
        except ModuleNotFoundError:
            # Fallback if panel folder has no panel.py submodule
            importlib.import_module(f"panels.{module.name}")

    # User defined - XDG_CONFIG_HOME/corvus/panels
    config_dir = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser() / "corvus" / "panels"

    if config_dir.exists():
        for user_panel_file in config_dir.glob("*/panel.py"):
            panel_name = user_panel_file.parent.name
            module_name = f"corvus_user_panels.{panel_name}"

            spec = importlib.util.spec_from_file_location(module_name, user_panel_file)
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

    return Panel.registry
    


def discover_old():

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
