Summary:	A heuristic autodialer for PPP connections
Summary(pl):	Heurystyczny "autowydzwaniacz" dla po³±czeñ PPP
Name:		wvdial
Version:	1.53
Release:	2
License:	LGPL
Group:		Networking/Daemons
Source0:	http://www.worldvisions.ca/wvdial/%{name}-%{version}.tar.gz
# Source0-md5:	e5432b4812b76e31b37cc10b6df62f5f
Patch0:		%{name}-make.patch
URL:		http://open.nit.ca/wvdial/
BuildRequires:	libstdc++-devel
BuildRequires:	wvstreams-devel
Requires:	ppp >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WvDial automatically locates and configures modems and can log into
almost any ISP's server without special configuration. You need to
input the username, password, and phone number, and then WvDial will
negotiate the PPP connection using any mechanism needed.

Install wvdial if you need a utility to configure your modem and set
up a PPP connection.

%description -l pl
WvDial automatycznie wyszukuje i konfiguruje modem, i mo¿e sie
zalogowaæ do praktycznie ka¿dego serwera dostawcy us³ug internetowych
(ISP). Potrzebujesz podaæ nazwê u¿ytkownika, has³o i numer telefonu, a
WvDial wynegocjuje po³±czenie PPP u¿ywaj±c potrzebnych mechanizmów.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	PREFIX=%{_prefix} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir} \
	COPTS="%{rpmcflags}" \
	CXXOPTS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates" \
	LDOPTS="%{rpmldflags}"

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
%doc README CHANGES ANNOUNCE src/FAQ src/TODO src/MENUS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%config %{_sysconfdir}/ppp/peers/*
