%define version  1.68.0
%define release  %mkrel 0.%revision.1
%define revision alpha3

Name:            k3b
Version:         %{version}
Release:         %{release}
Epoch:           4
License:         GPLv2+
Url:             http://www.k3b.org/
Group:           Archiving/Cd burning
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:         http://jaist.dl.sourceforge.net/sourceforge/k3b/%{name}-%version%revision.tar.bz2
Source1:         k3b-19.5-po-files.tar.bz2 
Patch1:          k3b-1.95-add-po.patch
Patch3:          k3b-1.66-always-use-growisofs-for-dvd.patch
Summary:         CD-Burner for KDE4
BuildRequires:   kdelibs4-devel
BuildRequires:   kdemultimedia4-devel
BuildRequires:   libdvdread-devel
BuildRequires:   libogg-devel
BuildRequires:   libvorbis-devel
BuildRequires:   libflac++-devel
BuildRequires:   libflac-devel
BuildRequires:   ffmpeg-devel
BuildRequires:   mad-devel
BuildRequires:   libmpcdec-devel
BuildRequires:   sndfile-devel
BuildRequires:   taglib-devel
BuildRequires:   doxygen
BuildRequires:   libsamplerate-devel
BuildRequires:   polkit-qt-devel
Requires:        cdrecord
Requires:        mkisofs
Requires:        cdrdao
Requires:        sox
Requires:        vcdimager
Requires:        normalize
Requires:        dvd+rw-tools
Requires:        kdebase4-runtime >= 1:4.1.70

Obsoletes:       kde4-k3b < 1.95-0.766860.2
Provides:        kde4-k3b

%description
K3b is CD-writing software which intends to be feature-rich and
provide an easily usable interface. Features include burning
audio CDs from .WAV and .MP3 audio files, configuring external
programs and configuring devices.

%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%_kde_bindir/k3b
%_kde_bindir/k3bsetup
%_kde_libdir/kde4/kcm_k3bsetup.so
%_kde_libdir/kde4/kcm_k3boggvorbisencoder.so
%_kde_libdir/kde4/kio_videodvd.so
%_kde_libdir/kde4/k3bffmpegdecoder.so
%_kde_libdir/kde4/k3bflacdecoder.so
%_kde_libdir/kde4/k3bmaddecoder.so
%_kde_libdir/kde4/k3boggvorbisdecoder.so
%_kde_libdir/kde4/k3boggvorbisencoder.so
%_kde_libdir/kde4/k3bmpcdecoder.so
%_kde_libdir/kde4/k3blibsndfiledecoder.so
%_kde_libdir/kde4/k3baudiometainforenamerplugin.so
%_kde_libdir/kde4/k3baudioprojectcddbplugin.so
%_kde_libdir/kde4/k3bexternalencoder.so
%_kde_libdir/kde4/k3bsoxencoder.so
%_kde_libdir/kde4/k3bwavedecoder.so
%_kde_libdir/kde4/kcm_k3bexternalencoder.so
%_kde_datadir/applications/kde4/k3b.desktop
%_kde_appsdir/k3b
%_kde_appsdir/konqsidebartng/virtual_folders/services/videodvd.desktop
%_kde_appsdir/solid/actions/*
%_kde_iconsdir/hicolor/*/apps/k3b.png
%_kde_datadir/kde4/services/ServiceMenus/*.desktop
%_kde_datadir/kde4/services/*.desktop
%_kde_datadir/kde4/servicetypes/k3bplugin.desktop
%_kde_datadir/kde4/services/videodvd.protocol
%dir %_kde_datadir/sounds
%_kde_datadir/sounds/*.wav
%_sysconfdir/dbus-1/system.d/org.k3b.setup.conf
%_kde_libdir/kde4/libexec/k3bsetup_worker
%_kde_datadir/PolicyKit/policy/org.k3b.setup.policy
%_kde_datadir/dbus-1/interfaces/org.k3b.setup.xml
%_kde_datadir/dbus-1/system-services/org.k3b.setup.service

#------------------------------------------------

%define libk3b_major 6
%define libk3b %mklibname k3b %libk3b_major

%package -n %libk3b
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}k3b4 < 4:1.66.0

%description -n %libk3b
KDE 4 core library.

%files -n %libk3b
%defattr(-,root,root)
%_kde_libdir/libk3b.so.%{libk3b_major}*

#------------------------------------------------

%define libk3bdevice_major 6
%define libk3bdevice %mklibname k3bdevice %libk3bdevice_major

%package -n %libk3bdevice
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libk3bdevice
KDE 4 core library.

%files -n %libk3bdevice
%defattr(-,root,root)
%_kde_libdir/libk3bdevice.so.%{libk3bdevice_major}*

#------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Development libraries from %name
Requires: %libk3bdevice = %epoch:%version-%release
Requires: %libk3b = %epoch:%version-%release

Obsoletes:       kde4-k3b-devel < 1.95-0.766860.2
Provides:        kde4-k3b-devel
Conflicts:       k3b < 3:1.0.4-4mdv

%description devel
Development libraries from %name

%files devel
%defattr(-,root,root,-)
%_kde_includedir/*.h
%_kde_libdir/libk3b.so
%_kde_libdir/libk3bdevice.so
#------------------------------------------------

%prep
%setup -q -n %name-%version -a 1
%patch1 -p1
%patch3 -p1

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build
%find_lang k3b k3b k3bsetup libk3b libk3bdevice

%clean
rm -rf %buildroot
