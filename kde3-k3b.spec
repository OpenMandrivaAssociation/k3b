%define	major	3
%define	libname	%mklibname k3b %major
%define oldlibname %mklibname k3b 2

%define k3b_18n_version 1.0.5

Name: kde3-k3b
Summary: CD-Burner for KDE
Version: 1.0.5
Release: %mkrel 3
License: GPL
Group: Archiving/Cd burning
Source0: http://jaist.dl.sourceforge.net/sourceforge/k3b/k3b-%{version}.tar.bz2
Source1: http://jaist.dl.sourceforge.net/sourceforge/k3b/k3b-i18n-%{k3b_18n_version}.tar.bz2
URL: http://www.k3b.org/
Provides: k3b = %version-%release
Requires: cdrecord 
Requires: mkisofs 
Requires: cdrdao 
Requires: sox 
Requires: vcdimager 
Requires: normalize
Requires: kdebase-progs
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libcdda-devel
BuildRequires: kdelibs-devel 
BuildRequires: jpeg-devel
BuildRequires: png-devel
BuildRequires: X11-devel
BuildRequires: mad-devel
BuildRequires: arts-devel
BuildRequires: libart_lgpl-devel
BuildRequires: fam-devel
BuildRequires: audiofile-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel
BuildRequires: nas-devel 
BuildRequires: libflac++-devel
BuildRequires: libflac-devel
BuildRequires: id3lib-devel 
BuildRequires: taglib-devel 
BuildRequires: musicbrainz-devel 
BuildRequires: ffmpeg-devel
BuildRequires: libsndfile-devel 
BuildRequires: libmpcdec-devel 
BuildRequires: libsamplerate-devel
BuildRequires: libdbus-qt-1-devel
BuildRequires: GL-devel
BuildRequires: hal-devel
BuildRequires: libdvdread-devel
BuildRequires: desktop-file-utils
Obsoletes:     k3b < 1.95
Requires:      %libname = %version-%release

%description
K3b is CD-writing software which intends to be feature-rich and 
provide an easily usable interface. Features include burning 
audio CDs from .WAV and .MP3 audio files, configuring external 
programs and configuring devices. 

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f k3b.lang
%defattr (-,root,root)
%dir %_kde3_docdir/HTML/*/k3b
%doc %_kde3_docdir/HTML/*/k3b/*
%_kde3_libdir/kde3/*
%_kde3_bindir/*
%_kde3_datadir/applications/kde/*
%_kde3_appsdir/konqueror/servicemenus/*
%_kde3_datadir/mimelnk/application/*
%dir %_kde3_appsdir/k3b/
%_kde3_appsdir/k3b/*
%_kde3_datadir/sounds/*.wav
%_kde3_datadir/applnk/.hidden/*.desktop
%_kde3_iconsdir/*/*/*/*
%_kde3_appsdir/konqsidebartng/virtual_folders/services/videodvd.desktop
%_kde3_datadir/services/kfile_k3b.desktop
%_kde3_datadir/services/videodvd.protocol

#------------------------------------------------------------------

%package -n	%libname
Group: 		System/Libraries
Summary: 	Libraries for %name
Provides: 	libk3b = %version-%release
Conflicts: 	k3b <= 0.9-3mdk
Obsoletes:	%oldlibname
Obsoletes:	%mklibname k3b 3 < %version-%release
Obsoletes:	%mklibname kde3-k3b 3 < %version-%release

%description -n	%libname
The libraries from %name package

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%_kde3_libdir/libk3b.la
%_kde3_libdir/libk3b.so.%{major}*
%_kde3_libdir/libk3bdevice.so.*
%_kde3_libdir/libk3bdevice.la

#------------------------------------------------------------------

%package devel
Group: Development/Other
Summary: Libraries for %name
Requires: %libname = %version-%release
Provides: kde3-k3b-devel = %{version}-%{release}
Obsoletes: %oldlibname-devel
Obsoletes: %libname-devel
Conflicts: 	k3b <= 0.9-3mdk

%description devel
Development libraries from %name

%files devel
%defattr (-,root,root)
%_kde3_includedir/*
%_kde3_libdir/*.so

#------------------------------------------------------------------

%prep
%setup -q -c -n k3b
%setup -q -T -D -c -a 1 -n k3b

%build
export QTDIR=%qt3dir
cd %_builddir/k3b/k3b-%version

%configure_kde3 \
   --without-cdrecord-suid-root \
   --with-k3bsetup=no 

%make 

cd -

cd %_builddir/k3b/k3b-i18n-%{k3b_18n_version}
make -f admin/Makefile.common
CFLAGS="${CFLAGS} %optflags" 
CXXFLAGS="${CXXFLAGS} %optflags" 
export CFLAGS CXXFLAGS 
%configure_kde3

# Necessary to regenerate po file !!!! Otherwise it's not generated
make clean
find -name *.gmo | xargs rm -f
%make
cd -


%install
rm -rf %buildroot
mkdir -p %buildroot/%_kde3_datadir/applnk/Multimedia

cd %_builddir/k3b/k3b-%{version}
%makeinstall_std
cd -

cd %_builddir/k3b/k3b-i18n-%{k3b_18n_version}
%makeinstall_std
cd -

install -d %buildroot/%_kde3_datadir/applications/kde/
desktop-file-install --vendor='' \
	--dir %buildroot/%_kde3_datadir/applications/kde/ \
	--remove-key='Encoding' \
	--remove-category='Application' \
	--remove-category='AudioVideo' \
	--add-category='Utility' \
	%buildroot/%_kde3_datadir/applications/kde/k3b.desktop

%find_lang k3b k3b k3bsetup libk3b libk3bdevice

%clean
rm -rf %buildroot
