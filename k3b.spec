%define git %{nil}

Summary:	CD-Burner for KDE4
Name:		k3b
Epoch:		6
Version:	2.0.3
%if "%{git}" != ""
Release:	0.%{git}.4
Source0:	%{name}-%git.tar.xz
%else
Release:	1
Source0:	ftp://ftp.kde.org/pub/kde/stable/k3b/%{name}-%version.tar.xz
%endif
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		http://k3b.sourceforge.net/
Patch3:		k3b-1.69-always-use-growisofs-for-dvd.patch
Patch6:		k3b-20140211-ffmpeg_check.patch
BuildRequires:	doxygen
BuildRequires:	kdelibs4-devel
BuildRequires:	libkcddb-devel
BuildRequires:	libmpcdec-devel
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
Requires:	cdrecord
Requires:	mkisofs
Requires:	cdrdao
Requires:	sox
Requires:	vcdimager
Requires:	normalize
Requires:	dvd+rw-tools
Requires:	kdebase4-runtime
# (tpg) needed for bug https://issues.openmandriva.org/show_bug.cgi?id=876
Requires:	%{_lib}cdio_paranoia-devel

%description
K3b is CD-writing software which intends to be feature-rich and
provide an easily usable interface. Features include burning
audio CDs from .WAV and .MP3 audio files, configuring external
programs and configuring devices.

%files
%{_kde_bindir}/k3b
%{_kde_libdir}/kde4/kcm_k3boggvorbisencoder.so
%{_kde_libdir}/kde4/kio_videodvd.so
%{_kde_libdir}/kde4/k3bffmpegdecoder.so
%{_kde_libdir}/kde4/k3bflacdecoder.so
%{_kde_libdir}/kde4/k3bmaddecoder.so
%{_kde_libdir}/kde4/k3boggvorbisdecoder.so
%{_kde_libdir}/kde4/k3boggvorbisencoder.so
%{_kde_libdir}/kde4/k3bmpcdecoder.so
%{_kde_libdir}/kde4/k3blibsndfiledecoder.so
%{_kde_libdir}/kde4/k3baudiometainforenamerplugin.so
%{_kde_libdir}/kde4/k3baudioprojectcddbplugin.so
%{_kde_libdir}/kde4/k3bexternalencoder.so
%{_kde_libdir}/kde4/k3bsoxencoder.so
%{_kde_libdir}/kde4/k3bwavedecoder.so
%{_kde_libdir}/kde4/kcm_k3bexternalencoder.so
%{_kde_libdir}/kde4/kcm_k3bsoxencoder.so
%{_kde_datadir}/applications/kde4/k3b.desktop
%{_kde_datadir}/mime/packages/x-k3b.xml
%{_kde_appsdir}/k3b
%{_kde_appsdir}/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_kde_appsdir}/solid/actions/*
%{_kde_datadir}/kde4/services/ServiceMenus/*.desktop
%{_kde_datadir}/kde4/services/*.desktop
%{_kde_datadir}/kde4/servicetypes/k3bplugin.desktop
%{_kde_datadir}/kde4/services/videodvd.protocol
%{_kde_iconsdir}/hicolor/*/apps/k3b.*
%optional %{_kde_datadir}/locale/*/LC_MESSAGES/*.mo
%{_kde_datadir}/doc/HTML/*
#------------------------------------------------

%define libk3b_major 6
%define libk3b %mklibname k3blib %{libk3b_major}

%package -n %{libk3b}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libk3b}
KDE 4 core library.

%files -n %{libk3b}
%{_kde_libdir}/libk3blib.so.%{libk3b_major}*

#------------------------------------------------

%define libk3bdevice_major 6
%define libk3bdevice %mklibname k3bdevice %{libk3bdevice_major}

%package -n %{libk3bdevice}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libk3bdevice}
KDE 4 core library.

%files -n %{libk3bdevice}
%{_kde_libdir}/libk3bdevice.so.%{libk3bdevice_major}*

#------------------------------------------------

%package devel
Group:		Development/KDE and Qt
Summary:	Development libraries from %{name}
Requires:	%{libk3bdevice} = %{EVRD}
Requires:	%{libk3b} = %{EVRD}

%description devel
Development libraries from %{name}

%files devel
%{_kde_includedir}/*.h
%{_kde_libdir}/libk3blib.so
%{_kde_libdir}/libk3bdevice.so
#------------------------------------------------

%prep
%if "%{git}" != ""
%setup -q -n %{name}
%else
%setup -q
%endif
%apply_patches

%build
%cmake_kde4 -DK3B_ENABLE_HAL_SUPPORT:BOOL=OFF -DK3B_BUILD_K3BSETUP:BOOL=OFF
%make

%install
%makeinstall_std -C build
