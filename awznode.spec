Summary: ax25 libraries for hamradio applications.
Name: awznode
Version: v0.4pre2
Release: 1
License: GNU
Group: Applications/Communications
Group(pl): Aplikacje/Komunikacja
Group(de): Applikationen/Kommunikation
Source0: ftp://ftp.icm.edu.pl/vol/rzm0/ham/unix/Linux/packet/awznode/awznode-v0.4-pre2.tar.gz
Patch0: http://zolw.eu.org/~djrzulf/PLD/patch/%{name}-configure.patch
BuildRoot: /tmp/%{name}-%{version}-root
BuildRequires: zlib-devel
BuildRequires: libax25-devel
Requires: zlib >= 1.1.3
Requires: libax25 >= 0.0.9
Requires: ax25-tools >= 0.0.8

%description

Easy node/gateway software for AX25

%description -l pl

Prosty przekaznik/gateway dla AX25

%prep
%setup -q -n awznode-v0.4-pre2

%patch0 -p0

%build

%configure2_13
%{__make} CC="gcc %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/var/ax25/node
mkdir -p ${RPM_BUILD_ROOT}/var/ax25/flex
mkdir -p ${RPM_BUILD_ROOT}/usr/sbin
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/ax25/node/help
mkdir -p ${RPM_BUILD_ROOT}/usr/share/man/man1
mkdir -p ${RPM_BUILD_ROOT}/usr/share/man/man5
mkdir -p ${RPM_BUILD_ROOT}/usr/share/man/man8
mkdir -p ${RPM_BUILD_ROOT}/etc/ax25

install etc/loggedin   ${RPM_BUILD_ROOT}/var/ax25/node       
install etc/lastlog    ${RPM_BUILD_ROOT}/var/ax25/node       
install etc/gateways   ${RPM_BUILD_ROOT}/var/ax25/flex

install node          ${RPM_BUILD_ROOT}/usr/sbin
install nodeusers     ${RPM_BUILD_ROOT}/usr/sbin
install flexd         ${RPM_BUILD_ROOT}/usr/sbin

install etc/help/*.hlp ${RPM_BUILD_ROOT}/usr/lib/ax25/node/help

install etc/node.conf.ex ${RPM_BUILD_ROOT}/etc/ax25
install etc/node.perms.ex ${RPM_BUILD_ROOT}/etc/ax25
install etc/node.info.ex ${RPM_BUILD_ROOT}/etc/ax25
install etc/node.motd.ex ${RPM_BUILD_ROOT}/etc/ax25
install etc/node.users.ex ${RPM_BUILD_ROOT}/etc/ax25
install etc/node.routes.ex ${RPM_BUILD_ROOT}/etc/ax25
install etc/flexd.conf.ex ${RPM_BUILD_ROOT}/etc/ax25

install man/nodeusers.1  ${RPM_BUILD_ROOT}/usr/share/man/man1
install man/node.conf.5  ${RPM_BUILD_ROOT}/usr/share/man/man5
install man/node.perms.5 ${RPM_BUILD_ROOT}/usr/share/man/man5
install man/node.8       ${RPM_BUILD_ROOT}/usr/share/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)/usr/sbin/nodeusers
%attr(755,root,root)/usr/sbin/flexd
%attr(4775,root,root)/usr/sbin/node
%attr(600,root,root)/etc/ax25/*
/usr/share/man/*
/var/ax25/*

%doc CHANGES COPYING INSTALL README

%changelog                                                                      
* %{date} PLD Team <pld-list@pld.org.pl>                                        
All persons listed below can be reached at <cvs_login>@pld.org.pl               
                                                                                
$Log: awznode.spec,v $
Revision 1.4  2001-10-24 21:18:33  djrzulf
- don't need extra configure, parms for arch done by
  %{__make} CC="gcc %{rpmcflags} -Wall", i think it's enough

Revision 1.3  2001/10/23 18:15:44  djrzulf
- created spec for PLD
- sticky arch becouse it has very poor ./configure - if someone can - please
  rewrite ./configure script of awznode, becouse it can't build for other
  arch than builder is installed on
