{ pkgs ? import <nixpkgs> {} }:

let
  # Create a custom Python environment with our required packages
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [
    click
    pygobject3
    watchdog
  ]);
in
pkgs.mkShell {
  name = "corvus-shell-dev";

  buildInputs = [
    pythonEnv
    
    # Core system libraries needed for GObject Introspection to resolve GTK4/Astal
    pkgs.glib
    pkgs.gobject-introspection
    pkgs.gtk4
    pkgs.libadwaita
    pkgs.gtk4-layer-shell

    pkgs.pkg-config
    pkgs.ninja
    pkgs.meson
    pkgs.uv

    ];

  shellHook = ''
    # Make sure local bin is in our path while developing
    export PATH="$PWD:$PATH"

    export LD_PRELOAD="${pkgs.gtk4-layer-shell}/lib/libgtk4-layer-shell.so"
  '';
}