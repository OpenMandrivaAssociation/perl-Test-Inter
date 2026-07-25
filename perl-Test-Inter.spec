%define modname	Test-Inter
%define modver 1.13

Summary:	Framework for more readable interactive test scripts
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/SBECK-github/Test-Inter
Source0:	https://cpan.metacpan.org/authors/id/S/SB/SBECK/Test-Inter-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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
%doc README META.yml
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*
