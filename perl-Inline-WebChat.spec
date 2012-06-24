#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	WebChat
Summary:	Inline::WebChat Perl module
Summary(cs):	Modul Inline::WebChat pro Perl
Summary(da):	Perlmodul Inline::WebChat
Summary(de):	Inline::WebChat Perl Modul
Summary(es):	M�dulo de Perl Inline::WebChat
Summary(fr):	Module Perl Inline::WebChat
Summary(it):	Modulo di Perl Inline::WebChat
Summary(ja):	Inline::WebChat Perl �⥸�塼��
Summary(ko):	Inline::WebChat �� ����
Summary(nb):	Perlmodul Inline::WebChat
Summary(pl):	Modu� Perla Inline::WebChat
Summary(pt):	M�dulo de Perl Inline::WebChat
Summary(pt_BR):	M�dulo Perl Inline::WebChat
Summary(ru):	������ ��� Perl Inline::WebChat
Summary(sv):	Inline::WebChat Perlmodul
Summary(uk):	������ ��� Perl Inline::WebChat
Summary(zh_CN):	Inline::WebChat Perl ģ��
Name:		perl-Inline-WebChat
Version:	0.62
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3cbad5b19ca390fc6f160953e53d21ca
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Inline >= 0.1
BuildRequires:	perl-WWW-Chat >= 0.62
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::WebChat - mix Perl and WebChat in a Perl script.

%description -l pl
Modu� Inline::WebChat - pozwalaj�cy na mieszanie kodu Perla i WebChata
w skryptach perlowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/WebChat.pm
%{_mandir}/man3/*
