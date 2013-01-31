%define svn %nil
%define major	54

%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

%define avfmajor 54
%define avflibname %mklibname avformats %{avfmajor}
%define postprocmajor 52
%define postproclibname %mklibname postproc %{postprocmajor}

%define avumajor 52
%define avulibname %mklibname avutil %{avumajor}
%define swsmajor 2
%define swslibname %mklibname swscaler %{swsmajor}

%define filtermajor 3
%define filterlibname %mklibname avfilter %{filtermajor}

%define swresamplemajor 0
%define swresamplelibname %mklibname swresample %{swresamplemajor}

#####################
# Hardcode PLF build
%define build_plf 0
#####################

%{?_with_plf: %{expand: %%global build_plf 1}}
%if %{build_plf}
%define distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%bcond_with	dlopen
%else
%bcond_without	dlopen
%endif

%bcond_without	swscaler
%bcond_with	faac

Summary:	Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Name:		ffmpeg
Version:	1.1
Release:	1%{?extrarelsuffix}
%if %{build_plf}
License:	GPLv3+
%else
License:	GPLv2+
%endif
Group:		Video
URL:		http://ffmpeg.org/
Source0:	http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
Patch1:		ffmpeg-1.0-dlopen-faac-mp3lame-opencore-x264-xvid.patch
Patch2:		ffmpeg-1.0.1-time.h.patch

BuildRequires:	texi2html
BuildRequires:	yasm
BuildRequires:	bzip2-devel
BuildRequires:	gsm-devel
BuildRequires:	jpeg-devel
BuildRequires:	libnut-devel
BuildRequires:	pkgconfig(celt)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gnutls) >= 3.0
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(libdc1394-2)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(librtmp)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(schroedinger-1.0)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(xavs)
%if %{build_plf}
BuildRequires:	x264-devel >= 0.118
BuildRequires:	lame-devel
BuildRequires:	opencore-amr-devel
BuildRequires:	libvo-aacenc-devel
BuildRequires:	libvo-amrwbenc-devel
BuildRequires:	xvid-devel
%endif
%if %{with faac}
BuildRequires:	libfaac-devel
%endif
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
This package is in Restricted as it violates several patents.
%endif

%package -n	%{libname}
Group:		System/Libraries
Summary:	Shared library part of ffmpeg
%if %{with dlopen}
%endif
Suggests:	libfaac.so.0%{_arch_tag_suffix}
Suggests:	libx264.so.124%{_arch_tag_suffix}
Suggests:	libopencore-amrnb.so.0%{_arch_tag_suffix}
Suggests:	libopencore-amrwb.so.0%{_arch_tag_suffix}
Suggests:	libmp3lame.so.0%{_arch_tag_suffix}
Suggests:	libxvidcore.so.4%{_arch_tag_suffix}
%endif

%description -n	%{libname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{postproclibname}
Summary:	Shared library part of ffmpeg
Group:		System/Libraries
Conflicts:	%mklibname ffmpeg 51

%description -n	%{postproclibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.


%package -n	%{avflibname}
Summary:	Shared library part of ffmpeg
Group:		System/Libraries

%description -n %{avflibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{avulibname}
Summary:	Shared library part of ffmpeg
Group:		System/Libraries

%description -n %{avulibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{swslibname}
Summary:	Shared library part of ffmpeg
Group:		System/Libraries

%description -n %{swslibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{filterlibname}
Summary:	Shared library part of ffmpeg
Group:		System/Libraries

%description -n	%{filterlibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n	%{swresamplelibname}
Summary:	Shared library part of ffmpeg
Group:		System/Libraries

%description -n %{swresamplelibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

%package -n	%{develname}
Summary:	Header files for the ffmpeg codec library
Group:		Development/C
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
Summary:	Static library for the ffmpeg codec library
Group:		Development/C
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
%if %{with dlopen}
%patch1 -p1 -b .dlopen~
%endif
%patch2 -p1 -b .timeh~

%build
export CFLAGS="%{optflags} -fPIC -I%{_includedir}/openjpeg-1.5/"
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
	--enable-libvorbis \
	--disable-encoder=vorbis \
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
	--enable-libvo-aacenc \
	--enable-libvo-amrwbenc \
	--enable-libxvid \
%else
	--disable-decoder=aac \
	--disable-encoder=aac \
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
	--enable-nonfree \
	--enable-libfaac
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

