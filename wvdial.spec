Summary:	A heuristic autodialer for PPP connections.
Summary(pl):	Heurystyczny "autowydzwaniacz" dla po³±czeñ PPP
Name:		wvdial
Version:	1.41
Release:	3
License:	LGPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Demony
Source0:	http://www.worldvisions.ca/wvdial/%{name}-%{version}.tar.gz
Patch0:		%{name}-libs.patch
Requires:	ppp >= 2.3.7
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WvDial automatically locates and configures modems and can log into almost
any ISP's server without special configuration. You need to input the
username, password, and phone number, and then WvDial will negotiate the
PPP connection using any mechanism needed.

Install wvdial if you need a utility to configure your modem and set up a
PPP connection.

%description -l pl
WvDial automatycznie wyszukuje i konfiguruje modem, i mo¿e sie zalogowaæ
do praktycznie ka¿dego serwera dostawcy us³ug internetowych (ISP).
Potrzebujesz podaæ nazwê u¿ytkownika, has³o i numer telefonu, a WvDial
wynegocjuje po³±czenie PPP u¿ywaj±c potrzebnych mechanizmów.

%prep
%setup -q
%patch0 -p1

%build
make PREFIX=%{_prefix} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make install PREFIX=${RPM_BUILD_ROOT}%{_prefix} PPPDIR=${RPM_BUILD_ROOT}%{_sysconfdir}/ppp/peers

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root)	%{_bindir}/*
%attr(0644,root,root)	%{_prefix}/man/man1/*
%attr(0600,root,daemon) %config %{_sysconfdir}/ppp/peers/wvdial
