Summary:	Easy configurable node/gateway (AX25)
Summary(pl):	Prosto konfigurowalny przekaznik/brama (AX25)
Name:		awznode
Version:	v0.4pre2
Release:	1
License:	GNU
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ftp.icm.edu.pl/vol/rzm0/ham/unix/Linux/packet/awznode/%{name}-v0.4-pre2.tar.gz
Patch0:		http://zolw.eu.org/~djrzulf/PLD/patch/%{name}-configure.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	zlib-devel
BuildRequires:	libax25-devel
Requires:	zlib >= 1.1.3
Requires:	libax25 >= 0.0.9
Requires:	ax25-tools >= 0.0.8

%description
Easy node/gateway software for AX25 procotole. It's usable tool if you
want create gateway packetradio <> internet (both sides).

%description -l pl
Prosty przekaznik/brama dla protokolu AX25. Przydatne narzedzie przy
budowaniu bramek packetradio <> internet.

%prep
%setup -q -n awznode-v0.4-pre2
%patch0 -p0

%build
%configure2_13
%{__make} CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/ax25/node
install -d $RPM_BUILD_ROOT/var/ax25/flex
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/ax25/node/help
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man5
install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ax25

install etc/loggedin   $RPM_BUILD_ROOT/var/ax25/node       
install etc/lastlog    $RPM_BUILD_ROOT/var/ax25/node       
install etc/gateways   $RPM_BUILD_ROOT/var/ax25/flex

install node $RPM_BUILD_ROOT%{_sbindir}
install nodeusers $RPM_BUILD_ROOT%{_sbindir}
install flexd $RPM_BUILD_ROOT%{_sbindir}

install etc/help/*.hlp $RPM_BUILD_ROOT%{_libdir}/ax25/node/help

install etc/node.conf.ex $RPM_BUILD_ROOT%{_sysconfdir}/ax25
install etc/node.perms.ex $RPM_BUILD_ROOT%{_sysconfdir}/ax25
install etc/node.info.ex $RPM_BUILD_ROOT%{_sysconfdir}/ax25
install etc/node.motd.ex $RPM_BUILD_ROOT%{_sysconfdir}/ax25
install etc/node.users.ex $RPM_BUILD_ROOT%{_sysconfdir}/ax25
install etc/node.routes.ex $RPM_BUILD_ROOT%{_sysconfdir}/ax25
install etc/flexd.conf.ex $RPM_BUILD_ROOT%{_sysconfdir}/ax25

install man/nodeusers.1  $RPM_BUILD_ROOT%{_mandir}/man1
install man/node.conf.5  $RPM_BUILD_ROOT%{_mandir}/man5
install man/node.perms.5 $RPM_BUILD_ROOT%{_mandir}/man5
install man/node.8       $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_sbindir}/nodeusers
%attr(755,root,root)%{_sbindir}/flexd
%attr(4775,root,root)%{_sbindir}/node
%attr(600,root,root)%{_sysconfdir}/ax25/*
%{_mandir}/man?/*
/var/ax25/*

%doc CHANGES COPYING INSTALL README
