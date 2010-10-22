PREFIX ?= /usr
LIBDIR = $(PREFIX)/lib
BINDIR = $(PREFIX)/bin
DATADIR = $(PREFIX)/share/invesalius-3.0
ICONDIR = $(PREFIX)/share/pixmaps
DESKTOPDIR = $(PREFIX)/share/applications/

LOCALE_DIR = $(shell find locale -type d -maxdepth 1 -mindepth 1)
PY_SRCDIR = $(shell find invesalius -type d)

build:
	 echo 'export INVESALIUS_LIBRARY_PATH="$(DATADIR)/invesalius"' >  invesalius-3.0
	 echo 'cd $$INVESALIUS_LIBRARY_PATH' >> invesalius-3.0
	 echo 'python invesalius.py $$@' >> invesalius-3.0

make-install-dir:
	 mkdir -p $(DESTDIR)/$(BINDIR)
	 mkdir -p $(DESTDIR)/$(DATADIR)/docs/devel
	 mkdir -p $(DESTDIR)/$(DATADIR)/icons
	 mkdir -p $(DESTDIR)/$(DATADIR)/presets/raycasting/color_list
	 mkdir -p $(DESTDIR)/$(DATADIR)/samples
	 mkdir -p $(DESTDIR)/$(DESKTOPDIR)
	 mkdir -p $(DESTDIR)/$(ICONDIR)
	 mkdir -p $(DESTDIR)/$(LIBDIR)

	 for dmo in $(LOCALE_DIR); do \
		 mkdir -p $(DESTDIR)/$(DATADIR)/$$dmo/LC_MESSAGES; done

	 for d in $(PY_SRCDIR); do \
		 mkdir -p $(DESTDIR)/$(DATADIR)/$$d; done

install: make-install-dir
	 install -m 644 docs/devel/*.py $(DESTDIR)/$(DATADIR)/docs/devel/
	 install -m 644 docs/*.pdf $(DESTDIR)/$(DATADIR)/docs
	 install -m 644 icons/* $(DESTDIR)/$(DATADIR)/icons
	 install -m 644 icons/invesalius.xpm $(DESTDIR)/$(ICONDIR)
	 install -m 644 invesalius-3.0.desktop $(DESTDIR)/$(DESKTOPDIR)
	 install -m 644 presets/raycasting/color_list/*.plist $(DESTDIR)/$(DATADIR)/presets/raycasting/color_list
	 install -m 644 presets/raycasting/*.plist $(DESTDIR)/$(DATADIR)/presets/raycasting
	 install -m 644 samples/*.inv3 $(DESTDIR)/$(DATADIR)/samples

	 for dmo in $(LOCALE_DIR); do \
		 install -m 644 $$dmo/LC_MESSAGES/*.mo  $(DESTDIR)/$(DATADIR)/$$dmo/LC_MESSAGES; done

	 for d in $(PY_SRCDIR); do \
		 install -m 644 $$d/*.py $(DESTDIR)/$(DATADIR)/$$d; done
	 
	 install -m 755 invesalius-3.0 $(DESTDIR)/$(BINDIR)
