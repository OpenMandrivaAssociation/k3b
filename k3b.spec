%define version  1.95
%define release  %mkrel 0.%revision.3
%define revision 870331

Name:            k3b
Version:         %{version}
Release:         %{release}
Epoch:           3
License:         GPLv2+
Url:             http://www.k3b.org/
Group:           Archiving/Cd burning
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:         http://jaist.dl.sourceforge.net/sourceforge/k3b/%{name}-%version.%revision.tar.bz2
Patch1:          k3b-1.95-ffmpeg-headers.patch
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
Requires:        cdrecord
Requires:        mkisofs
Requires:        cdrdao
Requires:        sox
Requires:        vcdimager
Requires:        normalize

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

%files
%defattr(-,root,root)
%_kde_bindir/k3b
%_kde_bindir/k3bsetup
%_kde_libdir/kde4/kcm_k3bsetup2.so
%_kde_libdir/kde4/kcm_k3bexternalencoder.so
%_kde_libdir/kde4/kcm_k3boggvorbisencoder.so
%_kde_libdir/kde4/kio_videodvd.so
%_kde_libdir/kde4/k3bexternalencoder.so
%_kde_libdir/kde4/k3bffmpegdecoder.so
%_kde_libdir/kde4/k3bflacdecoder.so
%_kde_libdir/kde4/k3bmaddecoder.so
%_kde_libdir/kde4/k3boggvorbisdecoder.so
%_kde_libdir/kde4/k3boggvorbisencoder.so
%_kde_libdir/kde4/k3bsoxencoder.so
%_kde_libdir/kde4/k3bwavedecoder.so
%_kde_libdir/kde4/k3bmpcdecoder.so
%_kde_libdir/kde4/k3blibsndfiledecoder.so
%_kde_datadir/applications/kde4/k3b.desktop
%_kde_libdir/kde4/k3bmpcdecoder.desktop
%dir %_kde_appsdir/k3b
%dir %_kde_appsdir/k3b/cdi
%_kde_appsdir/k3b/cdi/cdi_imag.rtf
%_kde_appsdir/k3b/cdi/cdi_text.fnt
%_kde_appsdir/k3b/cdi/cdi_vcd.app
%_kde_appsdir/k3b/cdi/cdi_vcd.cfg
%_kde_appsdir/k3b/cdi/icdia.htm
%_kde_appsdir/k3b/cdi/vcd_on_cdi_41.pdf
%dir %_kde_appsdir/k3b/extra
%_kde_appsdir/k3b/extra/*.mpg
%_kde_appsdir/k3b/icons
%_kde_appsdir/k3b/k3b.notifyrc
%_kde_appsdir/k3b/k3bui.rc
%_kde_appsdir/k3b/pics
%dir %_kde_appsdir/k3b/servicemenus
%_kde_appsdir/k3b/servicemenus/*.desktop
%_kde_appsdir/k3b/tips
%_kde_appsdir/konqsidebartng/virtual_folders/services/videodvd.desktop
%_kde_iconsdir/hicolor/*/apps/k3b.png
%_kde_datadir/kde4/services/ServiceMenus/*.desktop
%_kde_datadir/kde4/services/*.desktop
%_kde_datadir/kde4/servicetypes/k3bplugin.desktop
%_kde_datadir/kde4/services/videodvd.protocol
%dir %_kde_datadir/sounds
%_kde_datadir/sounds/*.wav

#------------------------------------------------

%define libk3b %mklibname k3b 4

%package -n %libk3b
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}k3b3 < 3:1.0.4-3

%description -n %libk3b
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libk3b -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libk3b -p /sbin/ldconfig
%endif

%files -n %libk3b
%defattr(-,root,root)
%_kde_libdir/libk3b.so.*

#------------------------------------------------

%define libk3bdevice %mklibname k3bdevice 6

%package -n %libk3bdevice
Summary: KDE 4 core library
Group: System/Libraries


%description -n %libk3bdevice
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libk3bdevice -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libk3bdevice -p /sbin/ldconfig
%endif

%files -n %libk3bdevice
%defattr(-,root,root)
%_kde_libdir/libk3bdevice.so.*


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
%setup -q -n %name-%version
%patch1 -p1 -b .ffmpeg_headers

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}

%clean
rm -rf %buildroot
