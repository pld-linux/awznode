#
# Conditional build:
%bcond_with	non_hams	# allow to connect non hams stations
#
Summary:	Easy configurable node/gateway (AX25)
Summary(pl):	Prosto konfigurowalny przeka¼nik/brama (AX25)
Name:		awznode
%define		_pre	pre2
Version:	0.4
Release:	0.%{_pre}%{?with_non_hams:nonhams}
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.funet.fi/pub/ham/unix/Linux/packet/awznode/%{name}-v%{version}-%{_pre}.tar.gz
# Source0-md5:	02f26da4c4db0260c297e1cac6c9d1f5
Patch0:		%{name}-configure.patch
Patch1:		%{name}-fhs.patch
Patch2:		%{name}-non_hams.patch
BuildRequires:	libax25-devel
BuildRequires:	zlib-devel
Requires:	ax25-tools >= 0.0.8
Requires:	libax25 >= 0.0.9
Requires:	zlib >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib

%description
Easy node/gateway software for AX25 procotole. It's usable tool if you
want create gateway packetradio <> Internet (both sides).

%description -l pl
Prosty przeka¼nik/brama dla protoko³u AX25. Przydatne narzêdzie przy
budowaniu bramek packetradio <> Internet.

%prep
%setup -q -n %{name}-v%{version}-%{_pre}
%patch0 -p0
%patch1 -p1
%{?with_non_hams:%patch2 -p1}

%build
# not autoconf-generated, it doesn't take any parameters
./configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/ax25/{node,flex} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_libdir}/ax25/node/help} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,5,8} \
	$RPM_BUILD_ROOT%{_sysconfdir}/ax25

install etc/loggedin   $RPM_BUILD_ROOT%{_localstatedir}/ax25/node
install etc/lastlog    $RPM_BUILD_ROOT%{_localstatedir}/ax25/node
install etc/gateways   $RPM_BUILD_ROOT%{_localstatedir}/ax25/flex

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
%doc CHANGES README
%attr(755,root,root) %{_sbindir}/nodeusers
%attr(755,root,root) %{_sbindir}/flexd
%attr(4775,root,root) %{_sbindir}/node
%attr(600,root,root) %{_sysconfdir}/ax25/*
%{_libdir}/ax25
%{_mandir}/man?/*
%{_localstatedir}/ax25/*
