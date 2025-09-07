#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	CD-Burner for Plasma 6
Name:		k3b
Version:	25.08.0
Release:	%{?git:0.%{git}.}4
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/k3b/-/archive/%{gitbranch}/k3b-%{gitbranchd}.tar.bz2#/k3b-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/k3b-%version.tar.xz
%endif
Source100:	%{name}.rpmlintrc
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		https://k3b.sourceforge.net/
Patch:		k3b-ffmpeg-8.0.patch
Patch3:		k3b-1.69-always-use-growisofs-for-dvd.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(polkit-qt6-1)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	shared-mime-info
BuildRequires:	cmake(KCddb6)
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

%rename plasma6-k3b

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
K3b is CD-writing software which intends to be feature-rich and
provide an easily usable interface. Features include burning
audio CDs from .WAV and .MP3 audio files, configuring external
programs and configuring devices.

%files -f k3b.lang
%{_bindir}/k3b
%{_datadir}/qlogging-categories6/k3b.categories
%{_libdir}/lib*.so.8*
%{_libdir}/qt6/plugins/k3b_plugins/*.so
%{_libdir}/qt6/plugins/k3b_plugins/kcms/kcm_*.so
%{_libdir}/qt6/plugins/kf6/kio/videodvd.so
%{_datadir}/metainfo/org.kde.k3b.appdata.xml
%{_datadir}/applications/org.kde.k3b.desktop
%{_datadir}/icons/*/*/*/k3b.*
%{_datadir}/icons/*/*/*/application-x-k3b.*
%{_datadir}/k3b
%{_datadir}/knotifications6/k3b.notifyrc
%{_datadir}/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/mime/packages/x-k3b.xml
%{_datadir}/solid/actions/k3b*
%{_datadir}/dbus-1/system-services/org.kde.k3b.service
%{_datadir}/dbus-1/system.d/org.kde.k3b.conf
%{_libdir}/libexec/kf6/kauth/k3bhelper
%{_datadir}/polkit-1/actions/org.kde.k3b.policy
%{_datadir}/knsrcfiles/k3btheme.knsrc
%{_datadir}/kio/servicemenus/*.desktop

%package devel
Group:		Development/KDE and Qt
Summary:	Development libraries from %{name}

%description devel
Development libraries from %{name}

%files devel
%{_includedir}/*
%{_libdir}/libk3b*.so
