%define _empty_manifest_terminate_build 0

Name:		doxyqml
Summary:	Doxyqml lets you use Doxygen to comment your QML classes
Version:	0.5.1
Release:	5
Group:		Development/Tools
Source0:	https://invent.kde.org/sdk/doxyqml/-/archive/%{version}/doxyqml-%{version}.tar.gz
License:	MIT
BuildRequires:	python
BuildRequires:	python-setuptools

%description
Doxyqml lets you use Doxygen to comment your QML classes

%prep
%autosetup -p1 -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/doxyqml
%{_prefix}/lib/python*/site-packages/doxyqml-*.egg-info
%{_prefix}/lib/python*/site-packages/doxyqml
