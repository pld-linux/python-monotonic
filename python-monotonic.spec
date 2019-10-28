#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	An implementation of time.monotonic() for Python 2 & < 3.3
Name:		python-monotonic
Version:	1.3
Release:	3
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/m/monotonic/monotonic-%{version}.tar.gz
# Source0-md5:	34351251d1a67667a25cd7673d2e44bf
URL:		https://pypi.python.org/pypi/monotonic
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a monotonic() function which returns the value
(in fractional seconds) of a clock which never goes backwards.

On Python 3.3 or newer, monotonic will be an alias of time.monotonic
from the standard library. On older versions, it will fall back to an
equivalent implementation.

%description -l pl.UTF-8

%package -n python3-monotonic
Summary:	An implementation of time.monotonic() for Python 2 & < 3.3
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-monotonic
This module provides a monotonic() function which returns the value
(in fractional seconds) of a clock which never goes backwards.

On Python 3.3 or newer, monotonic will be an alias of time.monotonic
from the standard library. On older versions, it will fall back to an
equivalent implementation.

%prep
%setup -q -n monotonic-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
%{py_sitescriptdir}/monotonic.py[co]
%{py_sitescriptdir}/monotonic-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-monotonic
%defattr(644,root,root,755)
%{py3_sitescriptdir}/monotonic.py
%{py3_sitescriptdir}/__pycache__/*
%{py3_sitescriptdir}/monotonic-%{version}-py*.egg-info
%endif
