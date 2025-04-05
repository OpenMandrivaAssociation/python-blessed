Name:		python-blessed
Version:	1.20.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/blessed/blessed-%{version}.tar.gz
Summary:	Easy, practical library for making terminal apps, by providing an elegant, well-documented interface to Colors, Keyboard input, and screen Positioning capabilities.
URL:		https://pypi.org/project/blessed/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Easy, practical library for making terminal apps, by providing an elegant, well-documented interface to Colors, Keyboard input, and screen Positioning capabilities.

%files
%{py_sitedir}/blessed
%{py_sitedir}/blessed-*.*-info
