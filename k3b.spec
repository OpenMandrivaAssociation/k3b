Summary:	CD-Burner for KDE4
Name:		k3b
Version:	2.0.2
Release:	8
Epoch:		4
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		http://k3b.sourceforge.net/
Source0:	http://jaist.dl.sourceforge.net/sourceforge/k3b/%{name}-%version.tar.bz2
Patch0:		k3b-2.0.2-ffmpeg.patch
Patch1:		k3b-2.0.2-libavformat54.patch
Patch3:		k3b-1.69-always-use-growisofs-for-dvd.patch
Patch4:		k3b-2.0.2-l10n-ru.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	libkcddb-devel
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(flac)
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(mad)
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	doxygen
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(polkit-qt-1)
Requires:	cdrecord
Requires:	mkisofs
Requires:	cdrdao
Requires:	sox
Requires:	vcdimager
Requires:	normalize
Requires:	dvd+rw-tools
Requires:	kdebase4-runtime

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
%{_kde_datadir}/locale/*/LC_MESSAGES/*.mo
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1 -b .dvd
%patch4 -p1 -b .l10n-ru

%build
%cmake_kde4 -DK3B_ENABLE_HAL_SUPPORT:BOOL=OFF -DK3B_BUILD_K3BSETUP:BOOL=OFF
%make

%install
%makeinstall_std -C build
%find_lang --with-html k3b k3bsetup libk3b libk3bdevice kio_videodvd k3b.lang

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 4:2.0.2-2mdv2011.0
+ Revision: 666003
- mass rebuild

* Sun Jan 16 2011 Funda Wang <fwang@mandriva.org> 4:2.0.2-1
+ Revision: 631141
- new version 2.0.2

* Fri Sep 10 2010 Funda Wang <fwang@mandriva.org> 4:2.0.1-2mdv2011.0
+ Revision: 577021
- add upstream patch to fix mdv#60896

* Thu Aug 19 2010 Funda Wang <fwang@mandriva.org> 4:2.0.1-1mdv2011.0
+ Revision: 571353
- new version 2.0.1

* Sun Jun 27 2010 Funda Wang <fwang@mandriva.org> 4:2.0.0-1mdv2010.1
+ Revision: 549195
- update URL
- 2.0.0 final

* Thu Jun 17 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.93.0-0.rc4.1mdv2010.1
+ Revision: 548202
- Update to k3b 2.0 Rc4

* Wed Jun 02 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.92.0-0.rc3.5mdv2010.1
+ Revision: 546999
- Add branch patch to fix a crash

* Thu May 27 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.92.0-0.rc3.2mdv2010.1
+ Revision: 546416
- Remove wrong po files

* Sun May 23 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.92.0-0.rc3.1mdv2010.1
+ Revision: 545733
- Update to 2.0 Rc3
- Add icons on hicolor

* Tue Mar 23 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.91.0-0.rc2.2mdv2010.1
+ Revision: 526870
- Rebuild for kdelibs4

* Fri Mar 12 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.91.0-0.rc2.1mdv2010.1
+ Revision: 518387
- Update to Rc2

* Tue Feb 02 2010 Funda Wang <fwang@mandriva.org> 4:1.70.0-0.beta1.1mdv2010.1
+ Revision: 499420
- New version 1.70 beta1

* Fri Dec 18 2009 Funda Wang <fwang@mandriva.org> 4:1.69.0-0.alpha4.2mdv2010.1
+ Revision: 479943
- fix obsoletes

* Sat Nov 28 2009 Funda Wang <fwang@mandriva.org> 4:1.69.0-0.alpha4.1mdv2010.1
+ Revision: 470763
- New version 1.69 alpha4

* Thu Oct 15 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.68.0-0.alpha3.1mdv2010.0
+ Revision: 457761
- new release

* Thu Sep 17 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.66.0-0.alpha2.3mdv2010.0
+ Revision: 444190
- Remove Unused patch
  Remove wrong conflict ( ease upgrade )

  + Arthur Renato Mello <arthur@mandriva.com>
    - Add patch to always use growisofs when burning DVDs.
      Without this burning a DVD-RW, not using MultiSession, will fail using cdrecord

* Wed May 27 2009 Funda Wang <fwang@mandriva.org> 4:1.66.0-0.alpha2.1mdv2010.0
+ Revision: 380202
- 1.66.0 alpha2
- drop k3b_write_iso_image.desktop, it was merged upstream
- use language specific file list for *.mo
- fix libmajor

* Sun May 10 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.65.0-0.alpha1.3mdv2010.0
+ Revision: 373919
- Enable polkit support

* Thu Apr 23 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.65.0-0.alpha1.2mdv2009.1
+ Revision: 368939
- Bump release

* Thu Apr 23 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4:1.65.0-0.alpha1.1mdv2009.1
+ Revision: 368931
- Update to k3b 2 Alpha1 ( Aka 1.65.0 )
  Increase Epoch  for new version

* Fri Apr 03 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.948770.1mdv2009.1
+ Revision: 363932
- Remove patch3, i merged it upstream
- New snapshot

* Fri Mar 27 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.945194.1mdv2009.1
+ Revision: 361559
- New snapshot ( Improve burning support)

* Thu Mar 26 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.944687.3mdv2009.1
+ Revision: 361272
- Use better option to close windows

* Thu Mar 26 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.944687.2mdv2009.1
+ Revision: 361252
- Disable french translation update as there is a syntax error
- Fix the close window
- New snapshot
  Fix some french translations

* Tue Mar 24 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.944027.1mdv2009.1
+ Revision: 360950
- Fix BuildRequires
- New snapshot
- New snapshot

* Sun Mar 22 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.942810.1mdv2009.1
+ Revision: 360331
- New svn snapshot
- New snapshot

* Sat Feb 21 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.928735.1mdv2009.1
+ Revision: 343771
- Fix file list
- Update translation tarball
- Really add po
- New snapshot
- Add translations
  Add service menu

* Sun Jan 25 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.916691.1mdv2009.1
+ Revision: 333559
- Fix file list
- New snapshot
  Remove merged patches
- Fix Requires (Bug #46880)

* Fri Oct 24 2008 Funda Wang <fwang@mandriva.org> 3:1.95-0.870331.3mdv2009.1
+ Revision: 296888
- fix requires of devel package

* Wed Oct 22 2008 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.870331.2mdv2009.1
+ Revision: 296562
- Fix Requires

* Sun Oct 12 2008 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:1.95-0.870331.1mdv2009.1
+ Revision: 292878
- Say hello back to k3b for kde4

* Mon Sep 29 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.0.5-9mdv2009.0
+ Revision: 289681
- Updated desktop file as requested by translation team

* Mon Sep 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3:1.0.5-8mdv2009.0
+ Revision: 278341
- rebuild for new libdvdread

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.0.5-7mdv2009.0
+ Revision: 277282
- Obsoletes kde3-k3b and kde4-k3b

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.0.5-6mdv2009.0
+ Revision: 277210
- Library required need to have epoch

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.0.5-5mdv2009.0
+ Revision: 277205
- Fixed ffmpeg build
- Restoring k3b from kde3 to main
- Restore k3b to main name

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-3mdv2009.0
+ Revision: 267755
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jun 06 2008 Funda Wang <fwang@mandriva.org> 1.0.5-2mdv2009.0
+ Revision: 216384
- obsoletes old libname

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 213979
- New version 1.0.5

* Wed May 14 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.4-4mdv2009.0
+ Revision: 207316
+ rebuild (emptylog)

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1.0.4-3mdv2009.0
+ Revision: 204740
- Put proper provides

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1.0.4-2mdv2009.0
+ Revision: 204720
- Missing obsoletes
- Make kde3 k3b available and move to /opt
- Keep old k3b due to unknown status of k3b for kde4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.0.4-2mdv2008.1
+ Revision: 137368
- Rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Funda Wang <fwang@mandriva.org> 1.0.4-1mdv2008.1
+ Revision: 105586
- New version 1.0.4

* Wed Sep 19 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.0.3-3mdv2008.0
+ Revision: 90801
- [BUGFIX] Do not display K3B on audio video (Bug #33311)

* Wed Aug 15 2007 Helio Chissini de Castro <helio@mandriva.com> 1.0.3-2mdv2008.0
+ Revision: 63818
- Removed flac as BuildRequires. Olnlu libflac and libflac++ are needed
- Recompiling to enable flac support again

* Mon Jul 23 2007 Sebastian Trueg <strueg@mandriva.com> 1.0.3-1mdv2008.0
+ Revision: 54696
- Fixed dependancies
- Removed Patch0 line since the patch has been removed from svn.
- Added K3b 1.0.3 i18n sources.
- Version bump to K3b 1.0.3.
  Removed the unicode filename patch which has alredy been included into the official K3b 1.0.3 sources.

* Wed Jul 11 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-3mdv2008.0
+ Revision: 51427
- Fix handling of filenames in utf8 (#31246)

* Tue Jul 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 47622
- add missing buildrequires

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Add Requires (bug #20728)

* Wed Jun 27 2007 Funda Wang <fwang@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 44921
- use new find_lang
  new major

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version

* Tue Jun 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-2mdv2008.0
+ Revision: 38357
- rebuild for expat

  + Helio Chissini de Castro <helio@mandriva.com>
    - Change spec layout. Fix build on i18n parts that not fit well for cd4

  + Laurent Montel <lmontel@mandriva.org>
    - Remove it

* Thu Apr 19 2007 Laurent Montel <lmontel@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 14977
- 1.0.1


* Sat Mar 31 2007 Olivier Blin <oblin@mandriva.com> 1.0-3mdv2007.1
+ Revision: 150023
- rebuild to fix corrupted hdlist header

  + Laurent Montel <lmontel@mandriva.com>
    - add patch from branch

* Sun Mar 18 2007 Olivier Blin <oblin@mandriva.com> 1.0-2mdv2007.1
+ Revision: 145763
- tag lang on HTML doc

  + Laurent Montel <lmontel@mandriva.com>
    - 1.0

* Tue Mar 13 2007 Laurent Montel <lmontel@mandriva.com> 1.0-0.rc7.2mdv2007.1
+ Revision: 142381
- rc7

* Mon Mar 05 2007 Laurent Montel <lmontel@mandriva.com> 1.0-0.rc6.2mdv2007.1
+ Revision: 133016
- k3bsetup2 not necessary

* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.rc6.1mdv2007.1
+ Revision: 125003
- regenerate P1
- own missing files
- rebuild against new libmpcdec

  + Laurent Montel <lmontel@mandriva.com>
    - rc6

* Sat Jan 27 2007 Laurent Montel <lmontel@mandriva.com> 1.0-0.rc5.1mdv2007.1
+ Revision: 114364
- rc5

* Wed Jan 17 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.0-0.rc4.2mdv2007.1
+ Revision: 110030
- Add patch2 : Add wodim support

* Tue Jan 09 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.0-0.rc4.1mdv2007.1
+ Revision: 106587
- New version 1.0rc4 (Last before 1.0)

* Sat Dec 30 2006 Laurent Montel <lmontel@mandriva.com> 1.0-0.rc3.1mdv2007.1
+ Revision: 102863
- rc3

* Wed Dec 13 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.0-0.rc2.1mdv2007.1
+ Revision: 96454
- Fix Spec
- New version 1.0rc2

* Mon Dec 11 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.0-0.rc1.1mdv2007.1
+ Revision: 95104
- Fix spec File
- New version 1.0rc1

* Fri Dec 01 2006 Laurent Montel <lmontel@mandriva.com> 1.0-0.beta1.2mdv2007.1
+ Revision: 89519
- Fix spec file
- 1.0-beta1

* Thu Nov 02 2006 Laurent Montel <lmontel@mandriva.com> 0.12.17-3mdv2007.1
+ Revision: 75817
- Fix detect autoconf2.60
- Fix bug #26843
- add %%doc

* Fri Aug 25 2006 Helio Chissini de Castro <helio@mandriva.com> 0.12.17-1mdv2007.0
+ Revision: 57930
- k3b need flac do decide wich version is using.
- Proper file list for docs
- Make proper buildrequires
- Make proper buildrequires
- Removed non used patches
- Removed reconfigure ( not needed )
- Added suffix for 64
- Removed enable-new-ldflags
- Updated for 0.12.17

* Thu Aug 03 2006 Laurent Montel <lmontel@mandriva.com> 0.12.16-5mdv2007.0
+ Revision: 43017
- Rebuild with new k3b
  (2006/08/02) 5mdv

* Fri Jul 28 2006 Laurent Montel <lmontel@mandriva.com> 0.12.16-4mdv2007.0
+ Revision: 42270
- New version 0.12.16-4mdv (2006-07-27)
  (necessary to add this info as repsys is not able to add this info)
  Don't add categorie for hidden desktop files
- Fix file list
- Requires vcdimager
- use macro
- 0.12.16
- Rebuild with new dbus
- Rebuild to generate good category
- Rebuild against xorg
- Rebuild to generate category
- 0.12.15
- 0.12.14
- 0.12.12
- Fix spec file
- 0.12.11
- Add ja message (patch from UTUMI Hirosi)
- Re-add Buildrequires: flac
- Rebuild with new lib dbus
- Reenable flac compile (now k3b fixed this support)
- 0.12.10
- 0.12.9
- use %%mkrel
- 0.12.8
- 0.12.7
- Rebuild with new dbus
- Fix spec file
- Fix buildrequires found by Christiaan Welvaart
- Add
- 0.12.5
- Fix spec file
- 0.12.4a
- New fix
- Last sync
- New diff
- New sync
- Fix compile error
- Sync with k3b branch (add all changes from this WE)
- Fix crash on x86_64
- Add diff from branch
- Fix lang
- Add enable-final
- 0.12.3
- Fix buildrequires bug found by nicolas Chipaux
- 0.12.2
- Rebuild for x86_64
- Update
- Update 0.12

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - 0.12.15-3mdk
      	- Reupload for x86_64"
    - 0.12.14-2mdk
    - remove Japanese messages (merged upstream) #21035

  + Helio Chissini de Castro <helio@mandriva.com>
    - Uploading package ./k3b

* Mon Jun 20 2005 Laurent MONTEL <lmontel@mandriva.com> 0.12.1-1mdk
- 0.12.1

* Fri May 13 2005 Laurent MONTEL <lmontel@mandriva.com> 0.12-0.beta1.1mdk
- first k3b 0.12 beta1

* Thu May 12 2005 Laurent MONTEL <lmontel@mandriva.com> 0.11.24-1mdk
- 0.11.24

* Tue May 03 2005 Laurent MONTEL <lmontel@mandriva.com> 0.11.23-2mdk
- Rebuild with new libflac

* Fri Apr 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.23-1mdk
- 0.11.23

* Thu Mar 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.20-7mdk
- Add patch14: fix welcome widget crash

* Tue Mar 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.20-6mdk
- Add patch12: "Always close DVD when writing iso image as default."
			   "Use incremental seqeuntial writing mode as default for DVD-R(W)."
- Add patch13: fix cddb crash

* Thu Mar 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.20-5mdk
- Add patch10: "fix for crash when importing session failed."
- Add patch11: fix layout

* Thu Feb 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.20-4mdk
- Add patch9: fix diskdetection

* Tue Feb 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.20-3mdk
- Add patch8: fix sound file filter (bug found by Wilman)

* Mon Feb 14 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.20-2mdk
- Add patch7: fix detect device on buggy firmwares

* Fri Feb 04 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.20-1mdk
- 0.11.20

* Fri Feb 04 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.19-7mdk
- Make clean to ensure that we regenerate all po file fix "Burn..." not translated and other po problem
- Add patch6: fix translate

* Fri Feb 04 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.19-6mdk
- Add patch5: fix kde bug #96859 fix multi session

* Thu Jan 27 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.19-5mdk
- 0.11.19

* Thu Jan 13 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.18-5mdk
- Add patch5: fix delete dvd image

* Wed Dec 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.18-4mdk
- Fix crash when we can't find a writer device

* Wed Dec 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.18-3mdk
- Add debug

* Mon Dec 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.18-2mdk
- 0.11.18

* Thu Dec 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.17-2mdk
- fix spec file

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.17-1mdk
- 0.11.17

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.16-4mdk
- Remove requires kdebase not necessary

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.16-3mdk
- Add patch6: "fixed cd-text loading in audio projects"

* Sat Sep 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.16-2mdk
- Add patch5: fix detect speed

* Sat Sep 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.16-1mdk
- 0.11.16

* Sat Aug 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.14-7mdk
- Fix %%Name -> %%name

* Sat Aug 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.14-6mdk
- Fix icons link (bug found by Fred Crozat)

* Sat Aug 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.14-5mdk
- Fix again menu :(

* Wed Aug 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.14-4mdk
- Fix menu

* Thu Aug 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.14-3mdk
- Fix url

* Wed Aug 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.14-2mdk
- Add patch4: fix k3b + kernel 2.6.8.1

* Wed Aug 11 2004 Laurent Culioli <laurent@mandrake.org> 0.11.14-1mdk
- 0.11.14
- spec cleanup

* Thu Aug 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.13-1mdk
- 0.11.13

* Thu Aug 05 2004 Götz Waschk <waschk@linux-mandrake.com> 0.11.12-4mdk
- rebuild for new flac

* Sat Jul 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.12-3mdk
- Minor spec file clean

* Sat Jul 31 2004 Laurent Culioli <laurent@mandrake.org> 0.11.12-2mdk
- Patch8 ( fix new dvd+rw-format detection )

* Sat Jun 26 2004 Laurent Culioli <laurent@mandrake.org> 0.11.12-1mdk
- 0.11.12

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.11-2mdk
- Fix obsolete

* Wed Jun 16 2004 Laurent Culioli <laurent@mandrake.org> 0.11.11-1mdk
- 0.11.11
- change major

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 0.11.10-5mdk
- Rebuild

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.10-4mdk
- Rebuild to update src.rpm

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.10-3mdk
- 0.11.10

* Sat May 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.11.9-3mdk
- don't do stuff within parantheses
- fix buildrequires

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.11.9-2mdk
- fix buildrequires

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.11.9-1mdk
- 0.11.9
- Use %%configure
- Use mdkversion

