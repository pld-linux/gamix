Summary:	GTK Audio Mixer for ALSA
Summary(pl):	Mikser audio w GTK dla ALSA
Name:		gamix
Version:	1.99.p14
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www1.tcnet.ne.jp/fmurata/linux/down/%{name}-%{version}.tar.gz
# Source0-md5:	a57b7954aa8e95b0a1c69a6fb06bc64b
URL:		http://www1.tcnet.ne.jp/fmurata/linux/down/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	gettext-devel
# gtk+ 1.x still needed by configure, but not used afterwards
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
GTK Audio Mixer for ALSA.

%description -l pl
Mikser Audio w GTK dla ALSA.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gtk-target=-2.0

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
