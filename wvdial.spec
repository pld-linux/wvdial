Summary:	A heuristic autodialer for PPP connections.
Summary(pl):	Heurystyczny "autowydzwaniacz" dla po³±czeñ PPP
Name:		wvdial
Version:	1.41
Release:	4
License:	LGPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Demony
Source0:	http://www.worldvisions.ca/wvdial/%{name}-%{version}.tar.gz
Patch0:		%{name}-libs.patch
Patch1:		%{name}-type.patch
Patch2:		%{name}-nodebug.patch
BuildRequires:	libstdc++-devel
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
WvDial automatycznie wyszukuje i konfiguruje modem, i mo¿e sie zalogowaæ do
praktycznie ka¿dego serwera dostawcy us³ug internetowych (ISP).
Potrzebujesz podaæ nazwê u¿ytkownika, has³o i numer telefonu, a WvDial
wynegocjuje po³±czenie PPP u¿ywaj±c potrzebnych mechanizmów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	PREFIX=%{_prefix} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir} \
	COPTS="$RPM_OPT_FLAGS" \
	CXXOPTS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates" \
	LDOPTS="-s"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	PPPDIR=$RPM_BUILD_ROOT%{_sysconfdir}/ppp/peers

gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man1/* README CHANGES ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config %{_sysconfdir}/ppp/peers/wvdial
