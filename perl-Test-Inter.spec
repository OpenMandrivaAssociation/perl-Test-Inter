%define modname	Test-Inter
%define modver 1.05

Summary:	Framework for more readable interactive test scripts
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Inter-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-devel

%description
This is another framework for writing test scripts. It is loosely inspired
by Test::More, and has most of it's functionality, but it is not a drop-in
replacement.

Test::More (and other existing test frameworks) suffer from two weaknesses,
both of which have prevented me from ever using them:

   None offer the ability to access specific tests in
   a reasonably interactive fashion

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE ChangeLog META.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*


