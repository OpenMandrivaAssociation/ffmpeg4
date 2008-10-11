%define name	ffmpeg
%define version	0.4.9
%define svn 15593
%define pre	pre1.%svn
%define rel	1
%define release %mkrel 3.%pre.%rel
%define major	52

%define libname %mklibname %name %major
%define develname %mklibname %name -d
%define staticname %mklibname %name -s -d

%define avfmajor 52
%define avflibname %mklibname avformats %avfmajor
%define postprocmajor 51
%define postproclibname %mklibname postproc %postprocmajor

%define avumajor 49
%define avulibname %mklibname avutil %avumajor
%define swsmajor 0
%define swslibname %mklibname swscaler %swsmajor

%define build_swscaler 1
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif
%define build_amr	0
%{?_with_amr: %{expand: %%global build_amr 1}}
%{?_without_amr: %{expand: %%global build_amr 0}}
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Source0: 	%{name}-r%{svn}.tar.bz2
#gw WARNING: reenabling libavcodec's deprecated image resampler
#anssi discussion and debian patch:
# http://permalink.gmane.org/gmane.comp.video.ffmpeg.devel/69238
# http://svn.debian.org/wsvn/pkg-multimedia/unstable/ffmpeg/debian/patches/015_reenable-img_convert.diff?op=file&rev=1234
Patch:		ffmpeg-reenable-imgresample.patch
License: 	GPLv2+
Group: 	 	Video
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:  imlib2-devel
BuildRequires:  tetex-texi2html
BuildRequires:	SDL-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
URL:		http://ffmpeg.sourceforge.net
%if %build_plf
BuildRequires: libfaac-devel libfaad2-devel
BuildRequires: x264-devel >= 0.54
BuildRequires: liblame-devel
%endif
%if %build_amr
BuildRequires: libamrnb-devel
BuildRequires: libamrwb-devel
%endif

%description
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

%if %build_plf
This package is in PLF as it violates several patents.
%endif

%package -n %{libname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg
Provides:       libffmpeg = %{version}-%{release}

%description -n %{libname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %{postproclibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{postproclibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.


%package -n %{avflibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{avflibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %{avulibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{avulibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %{swslibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg
Requires:	%{avulibname} = %{version}-%release

%description -n %{swslibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %develname
Group:          Development/C
Summary:        Header files for the ffmpeg codec library
Requires:       %{libname} = %{version}-%release
Requires:       %{avflibname} = %{version}-%release
Requires:       %{avulibname} = %{version}-%release
Requires:       %{postproclibname} = %{version}-%release
%if %build_swscaler
Requires:       %{swslibname} = %{version}-%release
%endif
Provides:       libffmpeg-devel = %{version}-%{release}
Provides:	ffmpeg-devel = %{version}-%{release}
Obsoletes: %mklibname -d %name 51

%description -n %develname
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg-devel if you want to compile apps with ffmpeg support.

%package -n %staticname
Group:          Development/C
Summary:        Static library for the ffmpeg codec library
Requires:       %develname = %{version}-%release
Provides:       libffmpeg-static-devel = %{version}-%{release}
Obsoletes: %mklibname -s -d %name 51

%description -n %staticname
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg-devel if you want to compile apps with ffmpeg support.

%prep

%setup -q -n %{name}
%if %build_swscaler
%patch -p1 -b .reenable-imgresample
%endif

#find -name Makefile | xargs perl -pi -e "s|\\\$\(prefix\)/lib|\\\$\(libdir\)|g"

%build
export CFLAGS="%optflags -FPIC"
./configure --prefix=%_prefix \
	--enable-shared \
	--libdir=%{_libdir} \
	--shlibdir=%{_libdir} \
	--incdir=%{_includedir} \
	--enable-postproc \
	--enable-gpl \
	--enable-pthreads \
	--enable-libtheora \
	--enable-libvorbis \
	--enable-x11grab \
%if %build_swscaler
	--enable-swscale \
%endif
%if %build_plf
	--enable-libmp3lame \
	--enable-libfaad \
	--enable-libfaac \
	--enable-libx264 \
%endif
%if %build_amr
	--enable-libamr_nb --enable-libamr_wb
%endif


%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std SRC_PATH=`pwd`

# compat symlink
install -d %buildroot/%_libdir/libavcodec
pushd %buildroot/%_libdir/libavcodec && ln -sf ../libavcodec.a && popd
install -d %buildroot/%_libdir/libavformat
pushd %buildroot/%_libdir/libavformat && ln -sf ../libavformat.a && popd

# fix doc containing CVS info.
rm -rf doc/CVS

# some apps need this header to build
# gw: it was only lve which needs this
#install -m 644 libavcodec/{bitstream.h,dsputil.h,mpegaudio.h} %buildroot/%_includedir/libavcodec/

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{avflibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{avflibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{avulibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{avulibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{swslibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{swslibname} -p /sbin/ldconfig
%endif


%files
%defattr(-,root,root)
%doc Changelog INSTALL README doc/*.html doc/*.txt doc/TODO doc/*.conf
%{_bindir}/*
%_libdir/vhook/*
%_mandir/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libavcodec.so.%{major}*

%files -n %postproclibname
%defattr(-,root,root)
%{_libdir}/libpostproc.so.%{postprocmajor}*

%files -n %{avflibname}
%defattr(-,root,root)
%{_libdir}/libavformat.so.%{avfmajor}*
%{_libdir}/libavdevice.so.%{avfmajor}*

%files -n %{avulibname}
%defattr(-,root,root)
%{_libdir}/libavutil.so.%{avumajor}*

%if %build_swscaler
%files -n %{swslibname}
%defattr(-,root,root)
%{_libdir}/libswscale.so.%{swsmajor}*
%endif

%files -n %develname
%defattr(-,root,root)
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavformat
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_libdir}/libavcodec.so
%{_libdir}/libavdevice.so
%{_libdir}/libavformat.so
%{_libdir}/libavutil.so
%{_libdir}/libpostproc.so
%if %build_swscaler
%{_libdir}/libswscale.so
%{_includedir}/libswscale
%_libdir/pkgconfig/libswscale.pc
%endif
%_libdir/pkgconfig/libavcodec.pc
%_libdir/pkgconfig/libavdevice.pc
%_libdir/pkgconfig/libavformat.pc
%_libdir/pkgconfig/libavutil.pc
%_libdir/pkgconfig/libpostproc.pc


%files -n %staticname
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/libavformat/*a
%{_libdir}/libavcodec/*a


