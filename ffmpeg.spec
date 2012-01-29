%define svn 22960
%define major	53

%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

%define avfmajor 53
%define avflibname %mklibname avformats %{avfmajor}
%define postprocmajor 52
%define postproclibname %mklibname postproc %{postprocmajor}

%define avumajor 51
%define avulibname %mklibname avutil %{avumajor}
%define swsmajor 2
%define swslibname %mklibname swscaler %{swsmajor}

%define filtermajor 2
%define filterlibname %mklibname avfilter %{filtermajor}

%define swresamplemajor 0
%define swresamplelibname %mklibname swresample %{swresamplemajor}

%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %{build_plf}
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%endif

%bcond_without	swscaler
%bcond_with	faac
%bcond_without	dlopen

Name: 	 	ffmpeg
Version: 	0.10
Release: 	1
Summary: 	Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Source0: 	http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
Patch0:		ffmpeg-0.8.7-string-format-fix.patch
Patch1:		ffmpeg-0.10-dlopen-faac-mp3lame-opencore-x264-xvid.patch
%if %{build_plf}
License: 	GPLv3+
%else
License: 	GPLv2+
%endif
Group:		Video
BuildRequires:	texi2html
BuildRequires:	SDL-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig(jack)
BuildRequires:	libdc1394-devel
BuildRequires:	libschroedinger-devel
BuildRequires:	libvpx-devel
BuildRequires:	jpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	bzip2-devel
BuildRequires:	rtmp-devel
BuildRequires:	yasm
BuildRequires:	vdpau-devel
BuildRequires:	libva-devel
URL:		http://ffmpeg.org/
%if %{build_plf}
BuildRequires:	x264-devel >= 0.118
BuildRequires:	liblame-devel
BuildRequires:	opencore-amr-devel
%endif
%if %{with faac}
BuildRequires:	libfaac-devel
%endif
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	libnut-devel
BuildRequires:	gsm-devel
BuildRequires:	pkgconfig(celt)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	openjpeg-devel
BuildRequires:	pkgconfig(xavs)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(dirac)
BuildRequires:	pkgconfig(libv4l2)
%if 0
Buildrequires:	pkgconfig(frei0r)
%endif

%description
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

%if %{build_plf}
This package is in PLF as it violates several patents.
%endif

%package -n	%{libname}
Group:		System/Libraries
Summary:	Shared library part of ffmpeg
%if %{with dlopen}
%if "%{_lib}" == "lib64"
%global	_ext	()(64bit)
%else
%global	_ext	%{nil}
%endif
Suggests:	libfaac.so.0%{_ext}
Suggests:	libx264.so.120%{_ext}
Suggests:	libopencore-amrnb.so.0%{_ext}
Suggests:	libopencore-amrwb.so.0%{_ext}
Suggests:	libmp3lame.so.0%{_ext}
Suggests:	libxvidcore.so.4%{_ext}
%endif

%description -n	%{libname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{postproclibname}
Group:		System/Libraries
Summary:	Shared library part of ffmpeg
Conflicts:	%mklibname ffmpeg 51

%description -n	%{postproclibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.


%package -n	%{avflibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{avflibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{avulibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{avulibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{swslibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{swslibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{filterlibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n	%{filterlibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{swresamplelibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{swresamplelibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

%package -n	%{develname}
Group:		Development/C
Summary:	Header files for the ffmpeg codec library
Requires:	%{libname} = %{EVRD}
Requires:	%{avflibname} = %{EVRD}
Requires:	%{avulibname} = %{EVRD}
Requires:	%{postproclibname} = %{EVRD}
%if %{with swscaler}
Requires:	%{swslibname} = %{EVRD}
%endif
Requires:	%{swresamplelibname} = %{EVRD}
Requires:	%{filterlibname} = %{EVRD}
Provides:	ffmpeg-devel = %{EVRD}
Obsoletes:	%mklibname -d %{name} 51

%description -n	%{develname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg-devel if you want to compile apps with ffmpeg support.

%package -n	%{staticname}
Group:		Development/C
Summary:	Static library for the ffmpeg codec library
Requires:	%{develname} = %{EVRD}
Provides:	ffmpeg-static-devel = %{EVRD}
Obsoletes:	%mklibname -s -d %{name} 51

%description -n	%{staticname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg-devel if you want to compile apps with ffmpeg support.

%prep
%setup -q
%patch0 -p1 -b .str_fmt~
%patch1 -p1 -b .dlopen~

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{ldflags}"

./configure --prefix=%{_prefix} \
	--enable-shared \
	--libdir=%{_libdir} \
	--shlibdir=%{_libdir} \
	--incdir=%{_includedir} \
	--disable-stripping \
	--enable-postproc \
	--enable-gpl \
	--enable-pthreads \
	--enable-libtheora \
	--enable-libvorbis --disable-encoder=vorbis \
	--enable-libvpx \
	--enable-x11grab \
	--enable-runtime-cpudetect \
	--enable-libdc1394 \
	--enable-libschroedinger \
	--enable-librtmp \
	--enable-libspeex \
	--enable-libfreetype \
	--enable-libnut \
	--enable-libgsm \
	--enable-libcelt \
	--enable-libopencv \
	--enable-libopenjpeg \
	--enable-libxavs \
	--enable-libmodplug \
	--enable-libass \
	--enable-gnutls \
	--enable-libcdio \
	--enable-libpulse \
	--enable-libdirac \
	--enable-libv4l2 \
%if 0
	--enable-frei0r \
%endif
%if %{build_plf}
	--enable-libmp3lame \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	--enable-version3 \
	--enable-libx264 \
%else
	--disable-decoder=aac --disable-encoder=aac \
%if %{with dlopen}
	--enable-libmp3lame-dlopen \
	--enable-libopencore-amrnb-dlopen \
	--enable-libopencore-amrwb-dlopen \
	--enable-libx264-dlopen \
	--enable-libxvid-dlopen \
%if !%{with faac}
	--enable-libfaac-dlopen \
%endif
%endif
%endif
%if %{with faac}
	--enable-nonfree --enable-libfaac
%endif

%make

%install
%makeinstall_std SRC_PATH=`pwd`

%files
%doc INSTALL README doc/*.html doc/*.txt doc/*.conf
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/ffmpeg

%files -n %{libname}
%{_libdir}/libavcodec.so.%{major}*

%files -n %{postproclibname}
%{_libdir}/libpostproc.so.%{postprocmajor}*

%files -n %{avflibname}
%{_libdir}/libavformat.so.%{avfmajor}*
%{_libdir}/libavdevice.so.%{avfmajor}*

%files -n %{avulibname}
%{_libdir}/libavutil.so.%{avumajor}*

%if %{with swscaler}
%files -n %{swslibname}
%{_libdir}/libswscale.so.%{swsmajor}*
%endif

%files -n %{filterlibname}
%{_libdir}/libavfilter.so.%{filtermajor}*

%files -n %{swresamplelibname}
%{_libdir}/libswresample.so.%{swresamplemajor}*

%files -n %{develname}
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavformat
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libavfilter
%{_includedir}/libswresample
%{_libdir}/libavcodec.so
%{_libdir}/libavdevice.so
%{_libdir}/libavformat.so
%{_libdir}/libavutil.so
%{_libdir}/libpostproc.so
%{_libdir}/libavfilter.so
%{_libdir}/libswresample.so
%if %{with swscaler}
%{_libdir}/libswscale.so
%{_includedir}/libswscale
%{_libdir}/pkgconfig/libswscale.pc
%endif
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/pkgconfig/libpostproc.pc
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/pkgconfig/libswresample.pc

%files -n %{staticname}
%{_libdir}/*.a
