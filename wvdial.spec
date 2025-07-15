Summary:	A heuristic autodialer for PPP connections
Summary(pl.UTF-8):	Heurystyczny "autowydzwaniacz" dla połączeń PPP
Name:		wvdial
Version:	1.61
Release:	2
License:	LGPL v2
Group:		Networking/Daemons
Source0:	http://wvstreams.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	acd3b2050c9b65fff2aecda6576ee7bc
Patch0:		%{name}-link.patch
URL:		http://alumnit.ca/wiki/index.php?page=WvDial
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	wvstreams-devel >= 4.5
Requires:	ppp >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WvDial automatically locates and configures modems and can log into
almost any ISP's server without special configuration. You need to
input the username, password, and phone number, and then WvDial will
negotiate the PPP connection using any mechanism needed.

%description -l pl.UTF-8
WvDial automatycznie wyszukuje i konfiguruje modem, i potrafi się
zalogować do praktycznie każdego serwera dostawcy usług internetowych
(ISP). Trzeba wprowadzić nazwę użytkownika, hasło i numer telefonu, a
WvDial wynegocjuje połączenie PPP używając potrzebnych mechanizmów.

%prep
%setup -q
%patch -P0 -p1

%build
# not autoconf generated, no arguments used
./configure
%{__make} -j1 \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CPPOPTS="%{rpmcppflags}" \
	COPTS="%{rpmcflags}" \
	CXXOPTS="%{rpmcppflags}" \
	VERBOSE=1 \
	WVSTREAMS_LIB=. \
	enable_debug=no

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	PPPDIR=$RPM_BUILD_ROOT%{_sysconfdir}/ppp/peers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES ChangeLog FAQ MENUS README TODO
%attr(755,root,root) %{_bindir}/wvdial
%attr(755,root,root) %{_bindir}/wvdialconf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ppp/peers/wvdial
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ppp/peers/wvdial-pipe
%{_mandir}/man1/wvdial.1*
%{_mandir}/man1/wvdialconf.1*
%{_mandir}/man5/wvdial.conf.5*
