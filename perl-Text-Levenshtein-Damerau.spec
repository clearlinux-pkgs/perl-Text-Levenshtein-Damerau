#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Levenshtein-Damerau
Version  : 0.41
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/U/UG/UGEXE/Text-Levenshtein-Damerau-0.41.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/U/UG/UGEXE/Text-Levenshtein-Damerau-0.41.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-levenshtein-damerau-perl/libtext-levenshtein-damerau-perl_0.41-1.debian.tar.xz
Summary  : 'Damerau Levenshtein edit distance.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Levenshtein-Damerau-license = %{version}-%{release}
Requires: perl-Text-Levenshtein-Damerau-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Text::Levenshtein::Damerau - Damerau Levenshtein edit distance.
SYNOPSIS
use Text::Levenshtein::Damerau;

%package dev
Summary: dev components for the perl-Text-Levenshtein-Damerau package.
Group: Development
Provides: perl-Text-Levenshtein-Damerau-devel = %{version}-%{release}
Requires: perl-Text-Levenshtein-Damerau = %{version}-%{release}

%description dev
dev components for the perl-Text-Levenshtein-Damerau package.


%package license
Summary: license components for the perl-Text-Levenshtein-Damerau package.
Group: Default

%description license
license components for the perl-Text-Levenshtein-Damerau package.


%package perl
Summary: perl components for the perl-Text-Levenshtein-Damerau package.
Group: Default
Requires: perl-Text-Levenshtein-Damerau = %{version}-%{release}

%description perl
perl components for the perl-Text-Levenshtein-Damerau package.


%prep
%setup -q -n Text-Levenshtein-Damerau-0.41
cd %{_builddir}
tar xf %{_sourcedir}/libtext-levenshtein-damerau-perl_0.41-1.debian.tar.xz
cd %{_builddir}/Text-Levenshtein-Damerau-0.41
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-Levenshtein-Damerau-0.41/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Levenshtein-Damerau
cp %{_builddir}/Text-Levenshtein-Damerau-0.41/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Levenshtein-Damerau/d04a7f689d4fb6e5fe0beba6c4b3959ad6c0dd2c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Levenshtein::Damerau.3
/usr/share/man/man3/Text::Levenshtein::Damerau::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Levenshtein-Damerau/d04a7f689d4fb6e5fe0beba6c4b3959ad6c0dd2c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
