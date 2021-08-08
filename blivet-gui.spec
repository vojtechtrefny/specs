Summary: Tool for data storage configuration
Name: blivet-gui
Version: 2.3.0
Release: 1%{?dist}
Source0: http://github.com/storaged-project/blivet-gui/releases/download/%{version}/%{name}-%{version}.tar.gz
License: GPLv2+
BuildArch: noarch
URL: http://github.com/storaged-project/blivet-gui

BuildRequires: desktop-file-utils

Requires: blivet-gui-runtime = %{version}-%{release}

%if 0%{?fedora}
BuildRequires: libappstream-glib
Requires: PolicyKit-authentication-agent
Requires: libblockdev-plugins-all
%endif

%if 0%{?suse_version}
BuildRequires: appstream-glib
Requires: polkit
Requires: libbd_btrfs2
Requires: libbd_crypto2
Requires: libbd_dm2
Requires: libbd_fs2
Requires: libbd_kbd2
Requires: libbd_loop2
Requires: libbd_lvm2
Requires: libbd_mdraid2
Requires: libbd_mpath2
Requires: libbd_part2
Requires: libbd_swap2
Requires: libbd_utils2
%endif

%if 0%{?mageia}
BuildRequires: appstream-util
Requires: polkit-agent
Requires: libblockdev-plugins-all
%endif


%description
Graphical (GTK) tool for manipulation and configuration of data storage
(disks, LVMs, RAIDs) based on blivet library.

%package -n blivet-gui-runtime
Summary: blivet-gui runtime

BuildRequires: python3-devel
BuildRequires: gettext >= 0.18.3
BuildRequires: python3-setuptools
BuildRequires: make

Requires: python3
Requires: python3-gobject
Requires: gettext
Requires: python3-blivet >= 1:3.1.2
Requires: python3-pid

%if 0%{?fedora}
Requires: libreport
Requires: gtk3
%endif

%if 0%{?suse_version}
Requires: libgtk-3-0
Requires: typelib-1_0-Gtk-3_0
Requires: gobject-introspection
Requires: python3-gobject-Gdk
Requires: typelib-1_0-Gtk-3_0
%endif

%if 0%{?mageia}
Requires: gtk+3.0
Requires: lib64gtk-gir3.0
%endif

%description -n blivet-gui-runtime
This package provides a blivet-gui runtime for applications that want to use
blivet-gui without actually installing the application itself.

%prep
%autosetup -n %{name}-%{version} -p1

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

desktop-file-validate %{buildroot}/%{_datadir}/applications/blivet-gui.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/blivet-gui.appdata.xml

mkdir -p %{buildroot}/%{_localstatedir}/log/blivet-gui

%find_lang %{name}

%files -n blivet-gui
%{_datadir}/applications/blivet-gui.desktop
%{_datadir}/appdata/blivet-gui.appdata.xml

%files -n blivet-gui-runtime -f %{name}.lang
%{_mandir}/man1/blivet-gui.1*
%{python3_sitelib}/*
%{_datadir}/polkit-1/actions/org.fedoraproject.pkexec.blivet-gui.policy
%{_datadir}/icons/hicolor/*/apps/blivet-gui.png
%{_datadir}/blivet-gui
%{_bindir}/blivet-gui
%{_bindir}/blivet-gui-daemon
%{_localstatedir}/log/blivet-gui
%{_sysconfdir}/libreport/events.d/blivet-gui_event.conf

%changelog
* Sun Aug 08 2021 Vojtech Trefny <vtrefny@redhat.com> - 2.3.0-1
- Update to latest release 2.3.0

* Sat Aug 07 2021 Vojtech Trefny <vtrefny@redhat.com> - 2.2.1-1
- Initial build of 2.2.1-1
