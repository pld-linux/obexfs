Summary:	ObexFTP filesystem
Summary(pl.UTF-8):   System plików ObexFTP
Name:		obexfs
Version:	0.10
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://triq.net/obexftp/%{name}-%{version}.tar.gz
# Source0-md5:	c8815a6347b0fa2d4fe1f250d88f4e58
URL:		http://openobex.triq.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.4
BuildRequires:	obexftp-devel >= 0.20
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUSE based filesystem using ObexFTP.

%description -l pl.UTF-8
System plików używający ObexFTP oparty na FUSE.

%prep
%setup -q

%{__sed} -i -e 's/-O2 //' configure.in

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
