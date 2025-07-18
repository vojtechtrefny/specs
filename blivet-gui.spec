Summary: Tool for data storage configuration
Name: blivet-gui
Version: 2.6.0
Release: 1%{?dist}
Source0: http://github.com/storaged-project/blivet-gui/releases/download/%{version}/%{name}-%{version}.tar.gz

%if 0%{?fedora}
Source1: blivet-gui_event.conf
%endif

License: GPL-2.0-or-later
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
Requires: libbd_btrfs3 >= %{libblockdevver}
Requires: libbd_crypto3 >= %{libblockdevver}
Requires: libbd_dm3 >= %{libblockdevver}
Requires: libbd_fs3 >= %{libblockdevver}
Requires: libbd_loop3 >= %{libblockdevver}
Requires: libbd_lvm3 >= %{libblockdevver}
Requires: libbd_mdraid3 >= %{libblockdevver}
Requires: libbd_mpath3 >= %{libblockdevver}
Requires: libbd_part3 >= %{libblockdevver}
Requires: libbd_swap3 >= %{libblockdevver}
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

%if 0%{?fedora}
BuildRequires: python3-devel
BuildRequires: gettext >= 0.18.3
BuildRequires: python3-setuptools
BuildRequires: make

Requires: python3
Requires: python3-gobject
Requires: python3-blivet >= 1:3.8.0
Requires: python3-pid

Requires: libreport
Requires: gtk3
%endif

%if 0%{?suse_version}
BuildRequires: python3-devel
BuildRequires: gettext >= 0.18.3
BuildRequires: python3-setuptools
BuildRequires: make

Requires: python3
Requires: python3-gobject
Requires: python3-blivet >= 1:3.8.0
Requires: python3-pid

Requires: libgtk-3-0
Requires: typelib-1_0-Gtk-3_0
Requires: gobject-introspection
Requires: python3-gobject-Gdk
Requires: typelib-1_0-Gtk-3_0
%endif

%if 0%{?mageia}
BuildRequires: python3-devel
BuildRequires: gettext >= 0.18.3
BuildRequires: python3-setuptools
BuildRequires: make

Requires: python3
Requires: python3-gobject
Requires: python3-blivet >= 1:3.8.0
Requires: python3-pid

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

%if 0%{?fedora}
mkdir -p %{buildroot}/%{_sysconfdir}/libreport/events.d/
install -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/libreport/events.d/
%endif

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

%if 0%{?fedora}
%{_sysconfdir}/libreport/events.d/blivet-gui_event.conf
%endif

%changelog
* Wed Aug 16 2023 Vojtech Trefny <vtrefny@redhat.com> - 2.4.2-1
- Update to the latest release 2.4.1

* Sun Mar 26 2023 Vojtech Trefny <vtrefny@redhat.com> - 2.4.1-1
- Update to the latest release 2.4.1

* Sun Sep 18 2022 Vojtech Trefny <vtrefny@redhat.com> - 2.4.0-1
- Update to the latest release 2.4.0

* Wed Sep 07 2022 Vojtech Trefny <vtrefny@redhat.com> - 2.3.0-3
- Fix dependencies for OpenMandriva

* Sun Sep 05 2021 Vojtech Trefny <vtrefny@redhat.com> - 2.3.0-2
- Rebuild for OpenMandriva

* Sun Aug 08 2021 Vojtech Trefny <vtrefny@redhat.com> - 2.3.0-1
- Update to latest release 2.3.0

* Sat Aug 07 2021 Vojtech Trefny <vtrefny@redhat.com> - 2.2.1-1
- Initial build of 2.2.1-1
