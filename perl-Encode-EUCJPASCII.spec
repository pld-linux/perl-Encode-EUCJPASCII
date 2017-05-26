#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Encode
%define		pnam	EUCJPASCII
%include	/usr/lib/rpm/macros.perl
Summary:	Encode::EUCJPASCII - eucJP-ascii, an eucJP-open mapping
Summary(pl.UTF-8):	Encode::EUCJPASCII - odwzorowanie eucJP-ascii (eucJP-open)
Name:		perl-Encode-EUCJPASCII
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5daa65f55b7c2050bb0713d9e95f239d
Patch0:		%{name}-man.patch
URL:		http://search.cpan.org/dist/Encode-EUCJPASCII/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.00
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides eucJP-ascii, one of eucJP-open mappings,
and its derivative.

%description -l pl.UTF-8
Ten moduł udostępnia eucJP-ascii - jedno z odwzorowań eucJP-open oraz
jego pochodne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Encode/EUCJPASCII.pm
%dir %{perl_vendorarch}/auto/Encode/EUCJPASCII
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/EUCJPASCII/EUCJPASCII.so
%{_mandir}/man3/Encode::EUCJPASCII.3pm*
