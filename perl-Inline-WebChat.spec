#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Inline
%define		pnam	WebChat
%include	/usr/lib/rpm/macros.perl
Summary:	Inline::WebChat Perl module
Summary(cs.UTF-8):	Modul Inline::WebChat pro Perl
Summary(da.UTF-8):	Perlmodul Inline::WebChat
Summary(de.UTF-8):	Inline::WebChat Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::WebChat
Summary(fr.UTF-8):	Module Perl Inline::WebChat
Summary(it.UTF-8):	Modulo di Perl Inline::WebChat
Summary(ja.UTF-8):	Inline::WebChat Perl モジュール
Summary(ko.UTF-8):	Inline::WebChat 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::WebChat
Summary(pl.UTF-8):	Moduł Perla Inline::WebChat
Summary(pt.UTF-8):	Módulo de Perl Inline::WebChat
Summary(pt_BR.UTF-8):	Módulo Perl Inline::WebChat
Summary(ru.UTF-8):	Модуль для Perl Inline::WebChat
Summary(sv.UTF-8):	Inline::WebChat Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::WebChat
Summary(zh_CN.UTF-8):	Inline::WebChat Perl 模块
Name:		perl-Inline-WebChat
Version:	0.62
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3cbad5b19ca390fc6f160953e53d21ca
URL:		http://search.cpan.org/dist/Inline-WebChat/
BuildRequires:	perl-Inline >= 0.1
BuildRequires:	perl-WWW-Chat >= 0.62
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::WebChat - mix Perl and WebChat in a Perl script.

%description -l pl.UTF-8
Moduł Inline::WebChat - pozwalający na mieszanie kodu Perla i WebChata
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
