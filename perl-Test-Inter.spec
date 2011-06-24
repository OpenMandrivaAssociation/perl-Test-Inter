%define upstream_name    Test-Inter
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Framework for more readable interactive test scripts
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Basename)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE ChangeLog META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


