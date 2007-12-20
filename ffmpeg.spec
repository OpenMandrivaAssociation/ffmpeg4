%define name	ffmpeg
%define version	0.4.9
%define svn 10833
%define pre	pre1.%svn
%define rel	2
%define release %mkrel 3.%pre.%rel
%define major	51

%define libname %mklibname %name %major
%define develname %mklibname %name -d
%define staticname %mklibname %name -s -d

%define avfmajor 51
%define avflibname %mklibname avformats %avfmajor
%define avumajor 49
%define avulibname %mklibname avutil %avumajor
%define swsmajor 0
%define swslibname %mklibname swscaler %swsmajor

%define build_swscaler 0
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Source0: 	%{name}-%{svn}.tar.bz2
Patch1:		ffmpeg-ffplay-uses-xlib.patch
# gw add experimental Dirac support, drop this if it doesn't apply anymore
# gw this patch was updated to generate a correct pkgconfig file
# http://downloads.sourceforge.net/dirac/ffmpegsvn_trunk_revision_8950-dirac-0.7.x.patch.tgz
Patch3:	ffmpegsvn_trunk_revision_10713-dirac-0.8.x.patch
License: 	GPL
Group: 	 	Video
BuildRequires:  imlib2-devel
BuildRequires:  tetex-texi2html
BuildRequires:	SDL-devel
BuildRequires:	libnut-devel
URL:		http://ffmpeg.sourceforge.net
BuildRequires: libdirac-devel >= 0.8.0
BuildRequires: liba52dec-devel
%if %build_plf
BuildRequires: libfaac-devel libfaad2-devel xvid-devel 
BuildRequires: libamrnb-devel
BuildRequires: libamrwb-devel
BuildRequires: x264-devel >= 0.54
BuildRequires: liblame-devel
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
Requires:	%{avulibname} = %{version}

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
Requires:       %{libname} = %{version}
Requires:       %{avflibname} = %{version}
Requires:       %{avulibname} = %{version}
%if %build_swscaler
Requires:       %{swslibname} = %{version}
%endif
Requires:	libnut-devel
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
Requires:       %develname = %{version}
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
%patch1 -p1 -b .ffplay-uses-xlib
%patch3 -p1 -b .dirac

#don't call ldconfig on install
find -name Makefile | xargs perl -pi -e 's/ldconfig \|\| true//'
find -name Makefile | xargs perl -pi -e "s|\\\$\(prefix\)/lib|\\\$\(libdir\)|g"

%build
export CFLAGS="%optflags -FPIC"
./configure --prefix=%_prefix \
	--enable-shared \
	--libdir=%{_libdir} \
	--enable-liba52 \
	--enable-pp \
	--enable-gpl \
	--enable-pthreads \
	--enable-libnut \
	--enable-x11grab \
	--enable-dirac \
%if %build_plf
	--enable-libmp3lame \
	--enable-libfaad \
	--enable-libfaac \
	--enable-libx264 \
	--enable-libxvid \
	--enable-libamr_nb --enable-libamr_wb
%endif


%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std SRC_PATH=`pwd`
%if %_lib != lib
mv %buildroot%_prefix/lib/* %buildroot%_libdir/
%endif

# compat symlink
install -d %buildroot/%_libdir/libavcodec
pushd %buildroot/%_libdir/libavcodec && ln -sf ../libavcodec.a && popd
install -d %buildroot/%_libdir/libavformat
pushd %buildroot/%_libdir/libavformat && ln -sf ../libavformat.a && popd

# fix doc containing CVS info.
rm -rf doc/CVS

# some apps need this header to build
install -m 644 libavcodec/mpegaudio.h %buildroot/%_includedir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n %{avflibname} -p /sbin/ldconfig
%postun -n %{avflibname} -p /sbin/ldconfig
%post -n %{avulibname} -p /sbin/ldconfig
%postun -n %{avulibname} -p /sbin/ldconfig
%post -n %{swslibname} -p /sbin/ldconfig
%postun -n %{swslibname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc Changelog INSTALL README doc/*.html doc/*.txt doc/TODO doc/*.conf
%{_bindir}/*
%_libdir/vhook/*
%_mandir/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libavcodec.so.%{major}*
%{_libdir}/libpostproc.so.%{major}*

%files -n %{avflibname}
%defattr(-,root,root)
%{_libdir}/libavformat.so.%{avfmajor}*

%files -n %{avulibname}
%defattr(-,root,root)
%{_libdir}/libavutil.so.%{avumajor}*

%if %build_swscaler
%files -n %{swslibname}
%defattr(-,root,root)
%{_libdir}/libswscale.so.0
%{_libdir}/libswscale.so.%{swsmajor}*
%endif

%files -n %develname
%defattr(-,root,root)
%{_includedir}/%{name}
%{_includedir}/postproc/
%{_libdir}/libavcodec.so
%{_libdir}/libavformat.so
%{_libdir}/libavutil.so
%{_libdir}/libpostproc.so
%if %build_swscaler
%{_libdir}/libswscale.so
%endif
%_libdir/pkgconfig/*.pc

%files -n %staticname
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/libavformat/*a
%{_libdir}/libavcodec/*a


