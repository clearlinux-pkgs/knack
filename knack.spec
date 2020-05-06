#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : knack
Version  : 0.7.0rc4
Release  : 2
URL      : https://github.com/microsoft/knack/archive/v0.7.0rc4.tar.gz
Source0  : https://github.com/microsoft/knack/archive/v0.7.0rc4.tar.gz
Summary  : A Command-Line Interface framework
Group    : Development/Tools
License  : MIT
Requires: knack-license = %{version}-%{release}
Requires: knack-python = %{version}-%{release}
Requires: knack-python3 = %{version}-%{release}
Requires: PyYAML
Requires: Pygments
Requires: argcomplete
Requires: colorama
Requires: flake8
Requires: jmespath
Requires: pylint
Requires: python-mock
Requires: six
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : argcomplete
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : flake8
BuildRequires : jmespath
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pylint
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
Knack
=====
.. image:: https://img.shields.io/pypi/v/knack.svg
:target: https://pypi.python.org/pypi/knack

%package license
Summary: license components for the knack package.
Group: Default

%description license
license components for the knack package.


%package python
Summary: python components for the knack package.
Group: Default
Requires: knack-python3 = %{version}-%{release}

%description python
python components for the knack package.


%package python3
Summary: python3 components for the knack package.
Group: Default
Requires: python3-core
Provides: pypi(knack)
Requires: pypi(argcomplete)
Requires: pypi(colorama)
Requires: pypi(jmespath)
Requires: pypi(pygments)
Requires: pypi(pyyaml)
Requires: pypi(six)
Requires: pypi(tabulate)

%description python3
python3 components for the knack package.


%prep
%setup -q -n knack-0.7.0rc4
cd %{_builddir}/knack-0.7.0rc4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588796035
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knack
cp %{_builddir}/knack-0.7.0rc4/LICENSE %{buildroot}/usr/share/package-licenses/knack/eee5b07a657266ef6c5c20acee6685ac6732cd19
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knack/eee5b07a657266ef6c5c20acee6685ac6732cd19

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
