%define debug_package %{nil}
%define snapshot 20200910

Name:		doxyqml
Summary:	Doxyqml lets you use Doxygen to comment your QML classes
Version:	0.5.1
Release:	%{?snapshot:0.%{snapshot}.}1
Group:		Development/Tools
Source0:	https://github.com/agateau/doxyqml/archive/master.tar.gz
License:	MIT
BuildRequires:	python
BuildRequires:	python-setuptools

%description
Doxyqml lets you use Doxygen to comment your QML classes

%prep
%autosetup -p1 -n %{name}-master

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/doxyqml
%{_prefix}/lib/python*/site-packages/doxyqml-*.egg-info
%{_prefix}/lib/python*/site-packages/doxyqml
