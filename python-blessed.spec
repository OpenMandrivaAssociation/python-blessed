%define module blessed

Name:		python-blessed
Version:	1.38.0
Release:	1
Summary:	An easy, practical library for making python terminal apps
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/blessed/
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Blessed is an easy, practical library for making terminal apps, by providing
an elegant, well-documented interface to Colors, Keyboard input, and screen
position and Location capabilities.

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
