%define upstream_name    Test-Inter
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Framework for more readable interactive test scripts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Basename)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is another framework for writing test scripts. It is loosely inspired
by Test::More, and has most of it's functionality, but it is not a drop-in
replacement.

Test::More (and other existing test frameworks) suffer from two weaknesses,
both of which have prevented me from ever using them:

   None offer the ability to access specific tests in
   a reasonably interactive fashion

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE ChangeLog META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-3mdv2012.0
+ Revision: 765680
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-2
+ Revision: 764230
- rebuilt for perl-5.14.x

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.0-1
+ Revision: 688830
- update to new version 1.03

* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.0-1
+ Revision: 687002
- update to new version 1.02

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2
+ Revision: 658407
- rebuild for updated rpm-setup

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 551988
- import perl-Test-Inter


* Tue Jul 13 2010 cpan2dist 1.01-1mdv
- initial mdv release, generated with cpan2dist
