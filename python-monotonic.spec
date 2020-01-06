#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	An implementation of time.monotonic() for Python 2
Summary(pl.UTF-8):	Implementacja time.monotinic() dla Pythona 2
Name:		python-monotonic
Version:	1.5
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/monotonic/
Source0:	https://files.pythonhosted.org/packages/source/m/monotonic/monotonic-%{version}.tar.gz
# Source0-md5:	9f81cb0e5966479754453dea2b6822f4
URL:		https://pypi.org/project/monotonic/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a monotonic() function which returns the value
(in fractional seconds) of a clock which never goes backwards.

On Python 3.3 or newer, monotonic will be an alias of time.monotonic
from the standard library. On older versions, it will fall back to an
equivalent implementation.

%description -l pl.UTF-8
Ten moduł udostępnia funkcję monotonic(), zwracającą wartość (w
ułamkach sekundy) zegara, który nigdy się nie cofa.

Dla Pythona 3.3 lub nowszego monotonic będzie aliasem dla funkcji
time.monotonic z biblioteki standardowej. Dla starszych wersji
odwołuje się do równoważnej implementacji.

%package -n python3-monotonic
Summary:	An implementation of time.monotonic() for Python < 3.3
Summary(pl.UTF-8):	Implementacja time.monotinic() dla Pythona < 3.3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-monotonic
This module provides a monotonic() function which returns the value
(in fractional seconds) of a clock which never goes backwards.

On Python 3.3 or newer, monotonic will be an alias of time.monotonic
from the standard library. On older versions, it will fall back to an
equivalent implementation.

%description -n python3-monotonic -l pl.UTF-8
Ten moduł udostępnia funkcję monotonic(), zwracającą wartość (w
ułamkach sekundy) zegara, który nigdy się nie cofa.

Dla Pythona 3.3 lub nowszego monotonic będzie aliasem dla funkcji
time.monotonic z biblioteki standardowej. Dla starszych wersji
odwołuje się do równoważnej implementacji.

%prep
%setup -q -n monotonic-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/monotonic.py[co]
%{py_sitescriptdir}/monotonic-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-monotonic
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/monotonic.py
%{py3_sitescriptdir}/__pycache__/monotonic.cpython-*.py[co]
%{py3_sitescriptdir}/monotonic-%{version}-py*.egg-info
%endif
