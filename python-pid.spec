%global srcname pid

%global common_description %{expand:
pid provides a PidFile class that manages PID files. PidFile features:
  - stale detection
  - locking using fcntl
  - chmod (default is 0o644)
  - chown
  - custom exceptions

PidFile can also be used as a context manager or a decorator.}


Name:           python-%{srcname}
Version:        3.0.4
Release:        2%{?dist}
Summary:        PID file management library

License:        ASL 2.0
URL:            https://github.com/trbs/pid
Source0:        %{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{common_description}

%prep
# This needs to have a blank line after because of a bug in the EL6 macros
%autosetup -p1 -n %{srcname}-%{version}

rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Sep 05 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.0.4-2
- Rebuild for OpenMandriva

* Sat Aug 07 2021 Vojtech Trefny <vtrefny@redhat.com> - 3.0.4-1
- Initial build of 3.0.4-1
