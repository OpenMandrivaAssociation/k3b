%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	CD-Burner for Plasma 5
Name:		k3b
Version:	23.08.4
Release:	1
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%version.tar.xz
Source100:	%{name}.rpmlintrc
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		http://k3b.sourceforge.net/
Patch3:		k3b-1.69-always-use-growisofs-for-dvd.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(polkit-qt5-1)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	shared-mime-info
BuildRequires:	cmake(KF5Cddb)
BuildRequires:	lame-devel
BuildRequires:	libmpcdec-devel
Requires:	cdrskin
Requires:	cdrkit
Requires:	cdrkit-genisoimage
Requires:	cdrdao
Requires:	sox
Requires:	vcdimager
Requires:	normalize
Requires:	dvd+rw-tools
Obsoletes:	%mklibname k3blib 6
Obsoletes:	%mklibname k3bdevice 6

%description
K3b is CD-writing software which intends to be feature-rich and
provide an easily usable interface. Features include burning
audio CDs from .WAV and .MP3 audio files, configuring external
programs and configuring devices.

%files -f k3b.lang
%{_bindir}/k3b
%{_datadir}/qlogging-categories5/k3b.categories
%{_libdir}/lib*.so.8*
%{_libdir}/qt5/plugins/k3b_plugins/*.so
%{_libdir}/qt5/plugins/k3b_plugins/kcms/kcm_*.so
%{_libdir}/qt5/plugins/kf5/kio/videodvd.so
%{_datadir}/metainfo/org.kde.k3b.appdata.xml
%{_datadir}/applications/org.kde.k3b.desktop
%{_datadir}/icons/*/*/*/k3b.*
%{_datadir}/icons/*/*/*/application-x-k3b.*
%{_datadir}/k3b
%{_datadir}/knotifications5/k3b.notifyrc
%{_datadir}/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/kservices5/ServiceMenus/k3b*.desktop
%{_datadir}/kservicetypes5/k3bplugin.desktop
%{_datadir}/kxmlgui5/k3b
%{_datadir}/mime/packages/x-k3b.xml
%{_datadir}/solid/actions/k3b*
%{_datadir}/dbus-1/system-services/org.kde.k3b.service
%{_datadir}/dbus-1/system.d/org.kde.k3b.conf
%{_libdir}/libexec/kauth/k3bhelper
%{_datadir}/polkit-1/actions/org.kde.k3b.policy
%{_datadir}/knsrcfiles/k3btheme.knsrc

%package devel
Group:		Development/KDE and Qt
Summary:	Development libraries from %{name}

%description devel
Development libraries from %{name}

%files devel
%{_includedir}/*
%{_libdir}/libk3b*.so

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang k3b --with-html --all-name
