Name:		superlight
Version:	1.0.2
Release:	1
Summary:	System Monitor for Linux desktops
License:        GPL-3+
URL:            https://github.com/xapp-project/superlight
Source0:	https://github.com/xapp-project/superlight/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:	lib64glib2.0-devel
BuildRequires:	lib64gio-gir2.0
BuildRequires:	lib64gtk3_0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python

Requires:       lib64gtk-gir3.0
Requires:       lib64upower-glib-gir1.0
Requires:       lib64xapp-gir3.2
Requires:       python
Requires:       python-cairo
Requires:       python-gi
Requires:       python-gi-cairo
Requires:       python-setproctitle
Requires:       python-xapp
Requires:       upower
Requires:       xapp-symbolic-icons

Recommends:	lib64flatpak-gir1.0

%description
System Monitor for Linux desktops

%prep
%autosetup -p1

%files
%license LICENSES/*
%doc README.md
%{_bindir}/superlight
%{python_sitelib}/superlight/
%{_datadir}/applications/org.x.superlight.desktop
%{_datadir}/icons/hicolor/scalable/apps/superlight.svg
%{_datadir}/glib-2.0/schemas/org.x.superlight.gschema.xml
