# Taken from kf5 branch in git://anongit.kde.org/k3b.git
%define git 20161201

Summary:	CD-Burner for Plasma 5
Name:		k3b
Epoch:		6
Version:	2.9.90
%if "%{git}" != ""
Release:	0.%{git}.3
Source0:	%{name}-%git.tar.xz
%else
Release:	2
Source0:	ftp://ftp.kde.org/pub/kde/stable/k3b/%{name}-%version.tar.xz
%endif
Source100:	%{name}.rpmlintrc
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		http://k3b.sourceforge.net/
Patch3:		k3b-1.69-always-use-growisofs-for-dvd.patch
Patch7:		k3b-ffmpeg3.patch
# infinite loop when burning an iso
Patch8:		k3b-invalid_url.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(polkit-qt-1)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	cmake
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
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	ninja
BuildRequires:	shared-mime-info
# Both KDE4 and KDE5's libkcddb provide cmake(Libkcddb) -- so let's use the old-style name
BuildRequires:	kcddb5-devel
Requires:	cdrecord
Requires:	mkisofs
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

%files
%{_bindir}/k3b
%{_libdir}/lib*.so.7*
%{_libdir}/qt5/plugins/k3b*.so
%{_libdir}/qt5/plugins/kcm_*.so
%{_libdir}/qt5/plugins/kio_videodvd.so
%{_datadir}/appdata/org.kde.k3b.appdata.xml
%{_datadir}/applications/org.kde.k3b.desktop
%{_datadir}/icons/*/*/*/k3b.*
%{_datadir}/icons/*/*/*/application-x-k3b.*
%{_datadir}/k3b
%{_datadir}/knotifications5/k3b.notifyrc
%{_datadir}/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/kservices5/ServiceMenus/k3b*.desktop
%{_datadir}/kservices5/k3b*.desktop
%{_datadir}/kservices5/kcm*.desktop
%{_datadir}/kservices5/videodvd.protocol
%{_datadir}/kservicetypes5/k3bplugin.desktop
%{_datadir}/kxmlgui5/k3b
%{_datadir}/mime/packages/x-k3b.xml
%{_datadir}/solid/actions/k3b*
%doc %{_docdir}/HTML/en/k3b

%package devel
Group:		Development/KDE and Qt
Summary:	Development libraries from %{name}

%description devel
Development libraries from %{name}

%files devel
%{_includedir}/*
%{_libdir}/libk3b*.so

%prep
%if "%{git}" != ""
%setup -q -n %{name}
%else
%setup -q
%endif
%apply_patches

# Workaround build failure with cmake 3.4
#sed -e "s|^cmake_minimum_required|#cmake_minimum_required|" -i CMakeLists.txt

%cmake_kde5 -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
