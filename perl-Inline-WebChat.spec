%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pnam	WebChat
Summary:	Inline::WebChat perl module
Summary(pl):	Modu³ perla Inline::WebChat
Name:		perl-Inline-WebChat
Version:	0.62
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.1
BuildRequires:	perl-WWW-Chat >= 0.62
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::WebChat - mix Perl and WebChat in a Perl script.
    
%description -l pl
Modu³ Inline::WebChat - pozwalaj±cy na mieszanie kodu Perla i WebChata
w skryptach perlowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Inline/WebChat.pm
%{_mandir}/man3/*
