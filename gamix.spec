Summary:	GTK Audio Mixer for ALSA
Summary(pl):	Mikser audio w GTK dla ALSA
Name:		gamix
Version:	1.99.p13
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www1.tcnet.ne.jp/fmurata/linux/down/%{name}-%{version}.tar.gz
URL:		http://www1.tcnet.ne.jp/fmurata/linux/down/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	alsa-lib-devel >= 0.5.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.0
ExcludeArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
GTK Audio Mixer for ALSA.

%description -l pl
Mikser Audio w GTK dla ALSA.

%prep
%setup -q

%build
%{__gettextize}
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
