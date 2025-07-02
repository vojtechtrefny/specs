Summary:  A python module for system storage configuration
Name: python-blivet
Url: https://storageapis.wordpress.com/projects/blivet
Version: 3.12.1

#%%global prerelease .b2
# prerelease, if defined, should be something like .a1, .b1, .b2.dev1, or .c2
Release: 1%{?prerelease}%{?dist}
Epoch: 1
License: LGPL-2.1-or-later
%global realname blivet
%global realversion %{version}%{?prerelease}
Source0: http://github.com/storaged-project/blivet/releases/download/%{realname}-%{realversion}/%{realname}-%{realversion}.tar.gz
Source1: http://github.com/storaged-project/blivet/releases/download/%{realname}-%{realversion}/%{realname}-%{realversion}-tests.tar.gz


# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%global partedver 1.8.1
%global pypartedver 3.10.4
%global utillinuxver 2.15.1
%global libblockdevver 3.3.0
%global libbytesizever 0.3
%global pyudevver 0.18
%global s390utilscorever 2.31.0

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
Requires: python3-pyudev >= %{pyudevver}
Requires: parted >= %{partedver}
Requires: python3-pyparted >= %{pypartedver}
Requires: libselinux-python3
Requires: python3-libmount
Requires: python3-blockdev >= %{libblockdevver}
Recommends: libblockdev-btrfs >= %{libblockdevver}
Recommends: libblockdev-crypto >= %{libblockdevver}
Recommends: libblockdev-dm >= %{libblockdevver}
Recommends: libblockdev-fs >= %{libblockdevver}
Recommends: libblockdev-loop >= %{libblockdevver}
Recommends: libblockdev-lvm >= %{libblockdevver}
Recommends: libblockdev-mdraid >= %{libblockdevver}
Recommends: libblockdev-mpath >= %{libblockdevver}
Recommends: libblockdev-nvme >= %{libblockdevver}
Recommends: libblockdev-part >= %{libblockdevver}
Recommends: libblockdev-swap >= %{libblockdevver}
Recommends: libblockdev-s390 >= %{libblockdevver}
Recommends: s390utils-core >= %{s390utilscorever}
%endif

%if 0%{?suse_version}
Requires: python3-selinux
Recommends: libbd_btrfs3 >= %{libblockdevver}
Recommends: libbd_crypto3 >= %{libblockdevver}
Recommends: libbd_dm3 >= %{libblockdevver}
Recommends: libbd_fs3 >= %{libblockdevver}
Recommends: libbd_loop3 >= %{libblockdevver}
Recommends: libbd_lvm3 >= %{libblockdevver}
Recommends: libbd_mdraid3 >= %{libblockdevver}
Recommends: libbd_mpath3 >= %{libblockdevver}
Recommends: libbd_part3 >= %{libblockdevver}
Recommends: libbd_swap3 >= %{libblockdevver}
Requires: python3-libblockdev >= %{libblockdevver}
Requires: typelib-1_0-BlockDev-3_0 >= %{libblockdevver}
Requires: python3-libbytesize >= %{libbytesizever}
Requires: python3-parted >= %{pypartedver}
Requires: python3-gobject
Requires: python3-pyudev >= %{pyudevver}
Requires: python3-libmount
Requires: python3
Requires: udev
%endif

%if 0%{?mageia}
Requires: python3-libselinux
Recommends: lib64bd_btrfs3 >= %{libblockdevver}
Recommends: lib64bd_crypto3 >= %{libblockdevver}
Recommends: lib64bd_dm3 >= %{libblockdevver}
Recommends: lib64bd_fs3 >= %{libblockdevver}
Recommends: lib64bd_loop3 >= %{libblockdevver}
Recommends: lib64bd_lvm3 >= %{libblockdevver}
Recommends: lib64bd_mdraid3 >= %{libblockdevver}
Recommends: lib64bd_mpath3 >= %{libblockdevver}
Recommends: lib64bd_part3 >= %{libblockdevver}
Recommends: lib64bd_swap3 >= %{libblockdevver}
Requires: python3-blockdev >= %{libblockdevver}
Requires: lib64blockdev-gir3.0 >= %{libblockdevver}
Requires: python3-bytesize >= %{libbytesizever}
Requires: python3-parted >= %{pypartedver}
Requires: python3-gobject-base
Requires: python3-pyudev >= %{pyudevver}
Requires: python3-libmount
Requires: python3
Requires: systemd
%endif

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
* Wed Jul 02 2025 Vojtech Trefny <vtrefny@redhat.com> - 3.12.1-1
- Update to 3.12.1

* Thu Mar 16 2023 Vojtech Trefny <vtrefny@redhat.com> - 3.7.1-1
- Update to 3.7.1

* Fri Feb 10 2023 Vojtech Trefny <vtrefny@redhat.com> - 3.7.0-1
- Update to 3.7.0

* Mon Nov 28 2022 Vojtech Trefny <vtrefny@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 20 2022 Vojtech Trefny <vtrefny@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Tue Jul 19 2022 Vojtech Trefny <vtrefny@redhat.com> - 3.5.0-1
- Update to 3.5.0

* Mon May 16 2022 Vojtech Trefny <vtrefny@redhat.com> - 3.4.4-1
- Update to 3.4.4

* Tue Feb 01 2022 Vojtech Trefny <vtrefny@redhat.com> - 3.4.3-1
- Update to 3.4.3

* Thu Sep 30 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.4.2-1
- Update to 3.4.2

* Sun Sep 05 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.4.1-2
- Rebuild for OpenMandriva

* Thu Aug 19 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Sat Aug 07 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.4.0-1
- Initial build of 3.4.0-1
