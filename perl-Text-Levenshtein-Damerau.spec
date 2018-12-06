#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Levenshtein-Damerau
Version  : 0.41
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/U/UG/UGEXE/Text-Levenshtein-Damerau-0.41.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/U/UG/UGEXE/Text-Levenshtein-Damerau-0.41.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-levenshtein-damerau-perl/libtext-levenshtein-damerau-perl_0.41-1.debian.tar.xz
Summary  : 'Damerau Levenshtein edit distance.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Levenshtein-Damerau-license = %{version}-%{release}
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

%description dev
dev components for the perl-Text-Levenshtein-Damerau package.


%package license
Summary: license components for the perl-Text-Levenshtein-Damerau package.
Group: Default

%description license
license components for the perl-Text-Levenshtein-Damerau package.


%prep
%setup -q -n Text-Levenshtein-Damerau-0.41
cd ..
%setup -q -T -D -n Text-Levenshtein-Damerau-0.41 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Text-Levenshtein-Damerau-0.41/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Levenshtein-Damerau
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Levenshtein-Damerau/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/Text/Levenshtein/Damerau.pm
/usr/lib/perl5/vendor_perl/5.28.1/Text/Levenshtein/Damerau/PP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Levenshtein::Damerau.3
/usr/share/man/man3/Text::Levenshtein::Damerau::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Levenshtein-Damerau/LICENSE
