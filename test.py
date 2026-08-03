import pkgutil
import panels
import os

path = panels.__path__
prefix = panels.__name__ + '.'

for loader, name, is_pkg in pkgutil.iter_modules(path, prefix):
    if not is_pkg:
        print(f"Module: {name}")
    else:
        print(f"Package: {name}")
