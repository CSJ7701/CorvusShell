(use-modules (guix packages)
	     (guix licenses)
	     (guix gexp)
	     (guix build-system python)
	     (guix git-download)
	     (gnu packages python)
	     (gnu packages python-xyz)
	     (gnu packages python-build)
	     (gnu packages gnome)
	     (gnu packages glib)
	     (gnu packages gtk)
	     (gnu packages build-tools)
	     (gnu packages pkg-config)
	     (gnu packages rust-apps))

(package
 (name "corvus-shell")
 (version "0.1.0-dev")
 (source (local-file "." "corvus-shell-checkout"
		     #:recursive? #t
		     #:select? (git-predicate ".")))
 (build-system python-build-system)
 (arguments
  (list
   #:phases
   #~ (modify-phases %standard-phases
		     (add-after 'install 'wrap-binary
				(lambda* (#:key outputs inputs #:allow-other-keys)
				  (let* ((out (assoc-ref outputs "out"))
					 (layer-shell (assoc-ref inputs "gtk4-layer-shell"))
					 (so-file (string-append layer-shell "/lib/libgtk4-layer-shell.so")))
				    (wrap-program (string-append out "/bin/corvus")
						  `("LD_PRELOAD" ":" prefix (,so-file)))))))))

 ;; Required at runtime
 (inputs
  (list glib
	gtk
	libadwaita
	gtk4-layer-shell
	python-click
	python-pygobject
	python-watchdog))

 ;; Required at build time
 (native-inputs
  (list pkg-config
	ninja
	meson
	gobject-introspection
	python-setuptools
	python-wheel))

 (native-search-paths
  (list (search-path-specification
	 (variable "LD_PRELOAD")
	 (files '("lib/libgtk4-layer-shell.so")))
	(search-path-specification
	 (variable "PATH")
	 (files '("bin")))))

 (home-page "https://github.com/CSJ7701/CorvusShell")
 (synopsis "Desktop shell built with gtk4 and Python")
 (description "Corvus Shell is a GTK4 layer-shell panel and desktop widget system.")
 (license gpl3+))
