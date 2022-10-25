#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docutils
Version  : 0.19
Release  : 89
URL      : https://files.pythonhosted.org/packages/6b/5c/330ea8d383eb2ce973df34d1239b3b21e91cd8c865d21ff82902d952f91f/docutils-0.19.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/5c/330ea8d383eb2ce973df34d1239b3b21e91cd8c865d21ff82902d952f91f/docutils-0.19.tar.gz
Summary  : Docutils -- Python Documentation Utilities
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 Public-Domain Python-2.0
Requires: pypi-docutils-bin = %{version}-%{release}
Requires: pypi-docutils-python = %{version}-%{release}
Requires: pypi-docutils-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=======================
=======================
:Author: David Goodger
:Contact: goodger@python.org
:Date: $Date: 2022-07-05 22:04:21 +0200 (Di, 05. Jul 2022) $
:Web site: https://docutils.sourceforge.io/

%package bin
Summary: bin components for the pypi-docutils package.
Group: Binaries

%description bin
bin components for the pypi-docutils package.


%package python
Summary: python components for the pypi-docutils package.
Group: Default
Requires: pypi-docutils-python3 = %{version}-%{release}

%description python
python components for the pypi-docutils package.


%package python3
Summary: python3 components for the pypi-docutils package.
Group: Default
Requires: python3-core
Provides: pypi(docutils)

%description python3
python3 components for the pypi-docutils package.


%prep
%setup -q -n docutils-0.19
cd %{_builddir}/docutils-0.19
pushd ..
cp -a docutils-0.19 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657116320
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
ln -s rst2man.py %{buildroot}/usr/bin/rst2man
ln -s rst2html.py %{buildroot}/usr/bin/rst2html
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/docutils
/usr/bin/rst2html
/usr/bin/rst2html.py
/usr/bin/rst2html4.py
/usr/bin/rst2html5.py
/usr/bin/rst2latex.py
/usr/bin/rst2man
/usr/bin/rst2man.py
/usr/bin/rst2odt.py
/usr/bin/rst2odt_prepstyles.py
/usr/bin/rst2pseudoxml.py
/usr/bin/rst2s5.py
/usr/bin/rst2xetex.py
/usr/bin/rst2xml.py
/usr/bin/rstpep2html.py

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
