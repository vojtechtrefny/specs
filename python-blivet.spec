Summary:  A python module for system storage configuration
Name: python-blivet
Url: https://storageapis.wordpress.com/projects/blivet
Version: 3.4.1

Release: 1%{?dist}
Epoch: 1
License: LGPLv2+
%global realname blivet
%global realversion %{version}
Source0: http://github.com/storaged-project/blivet/archive/%{realname}-%{realversion}.tar.gz
Source1: http://github.com/storaged-project/blivet/archive/%{realname}-%{realversion}-tests.tar.gz

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%global partedver 3.2
%global pypartedver 3.10.4
%global utillinuxver 2.15.1
%global libblockdevver 2.24
%global libbytesizever 0.3
%global pyudevver 0.18

BuildArch: noarch

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%package -n %{realname}-data
Summary: Data for the %{realname} python module.

BuildRequires: make
BuildRequires: systemd

%description -n %{realname}-data
The %{realname}-data package provides data files required by the %{realname}
python module.

%package -n python3-%{realname}
Summary: A python3 package for examining and modifying storage configuration.

%{?python_provide:%python_provide python3-%{realname}}

BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%if 0%{?fedora}
Requires: python3-libselinux
Recommends: libblockdev-btrfs >= %{libblockdevver}
Recommends: libblockdev-crypto >= %{libblockdevver}
Recommends: libblockdev-dm >= %{libblockdevver}
Recommends: libblockdev-fs >= %{libblockdevver}
Recommends: libblockdev-kbd >= %{libblockdevver}
Recommends: libblockdev-loop >= %{libblockdevver}
Recommends: libblockdev-lvm >= %{libblockdevver}
Recommends: libblockdev-mdraid >= %{libblockdevver}
Recommends: libblockdev-mpath >= %{libblockdevver}
Recommends: libblockdev-nvdimm >= %{libblockdevver}
Recommends: libblockdev-part >= %{libblockdevver}
Recommends: libblockdev-swap >= %{libblockdevver}
Recommends: libblockdev-s390 >= %{libblockdevver}
Requires: python3-blockdev >= %{libblockdevver}
Requires: python3-bytesize >= %{libbytesizever}
Requires: python3-pyparted >= %{pypartedver}
Requires: python3-gobject-base
Requires: systemd-udev
%endif

%if 0%{?suse_version}
Requires: python3-selinux
Recommends: libbd_btrfs2 >= %{libblockdevver}
Recommends: libbd_crypto2 >= %{libblockdevver}
Recommends: libbd_dm2 >= %{libblockdevver}
Recommends: libbd_fs2 >= %{libblockdevver}
Recommends: libbd_kbd2 >= %{libblockdevver}
Recommends: libbd_loop2 >= %{libblockdevver}
Recommends: libbd_lvm2 >= %{libblockdevver}
Recommends: libbd_mdraid2 >= %{libblockdevver}
Recommends: libbd_mpath2 >= %{libblockdevver}
Recommends: libbd_part2 >= %{libblockdevver}
Recommends: libbd_swap2 >= %{libblockdevver}
Recommends: libbd_utils2 >= %{libblockdevver}
Requires: python3-libblockdev >= %{libblockdevver}
Requires: typelib-1_0-BlockDev-2_0 >= %{libblockdevver}
Requires: python3-libbytesize >= %{libbytesizever}
Requires: python3-parted >= %{pypartedver}
Requires: python3-gobject
Requires: udev
%endif

%if 0%{?mageia}
Requires: python3-libselinux
Recommends: libblockdev-plugins-all >= %{libblockdevver}
Requires: python3-blockdev >= %{libblockdevver}
Requires: lib64blockdev-gir2.0 >= %{libblockdevver}
Requires: python3-bytesize >= %{libbytesizever}
Requires: python3-parted >= %{pypartedver}
Requires: python3-gobject-base
Requires: systemd
%endif

Requires: python3
Requires: python3-six
Requires: python3-pyudev >= %{pyudevver}
Requires: parted >= %{partedver}
Requires: util-linux >= %{utillinuxver}
Requires: lsof
Requires: %{realname}-data = %{epoch}:%{version}-%{release}

%description -n python3-%{realname}
The python3-%{realname} is a python3 package for examining and modifying storage
configuration.

%prep
%autosetup -n %{realname}-%{realversion} -N
%autosetup -n %{realname}-%{realversion} -b1 -p1

%build
make PYTHON=%{__python3}

%install
make PYTHON=%{__python3} DESTDIR=%{buildroot} install

%find_lang %{realname}

%files -n %{realname}-data -f %{realname}.lang
%{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/dbus-1/system-services/*
%{_libexecdir}/*
%{_unitdir}/*

%files -n python3-%{realname}
%license COPYING
%doc README.md ChangeLog examples
%{python3_sitelib}/*

%changelog
* Thu Aug 19 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Sat Aug 07 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.4.0-1
- Initial build of 3.4.0-1
