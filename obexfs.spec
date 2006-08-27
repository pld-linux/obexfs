#
Summary:	ObexFTP filesystem
Summary(pl):	System plików ObexFTP
Name:		obexfs
Version:	0.10
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://triq.net/obexftp/%{name}-%{version}.tar.gz
# Source0-md5:	c8815a6347b0fa2d4fe1f250d88f4e58
URL:		http://openobex.triq.net/
BuildRequires:	libfuse-devel >= 2.4
BuildRequires:	obexftp-devel >= 0.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         filterout_ld    (-Wl,)?--as-needed

%description
FUSE based filesystem using ObexFTP.

%description -l pl
System plików u¿ywaj±cy ObexFTP oparty na FUSE.

%prep
%setup -q

%build
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
