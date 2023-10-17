# ffmpeg is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 58
%define ppmajor 55
%define avumajor 56
%define swsmajor 5
%define filtermajor 7
%define swrmajor 3
%define avrmajor 4
%define libavcodec %mklibname avcodec %{major}
%define libavdevice %mklibname avdevice %{major}
%define libavfilter %mklibname avfilter %{filtermajor}
%define libavformat %mklibname avformat %{major}
%define libavresample %mklibname avresample %{avrmajor}
%define libavutil %mklibname avutil %{avumajor}
%define libpostproc %mklibname postproc %{ppmajor}
%define libswresample %mklibname swresample %{swrmajor}
%define libswscale %mklibname swscale %{swsmajor}
%define lib32avcodec %mklib32name avcodec %{major}
%define lib32avdevice %mklib32name avdevice %{major}
%define lib32avfilter %mklib32name avfilter %{filtermajor}
%define lib32avformat %mklib32name avformat %{major}
%define lib32avresample %mklib32name avresample %{avrmajor}
%define lib32avutil %mklib32name avutil %{avumajor}
%define lib32postproc %mklib32name postproc %{ppmajor}
%define lib32swresample %mklib32name swresample %{swrmajor}
%define lib32swscale %mklib32name swscale %{swsmajor}
# Workaround for incorrect naming in previous version.
# Can be dropped on next soname bump.
%define oldlibswscale %mklibname swscaler %{swsmajor}
%define devname %mklibname %{name} -d
%define statname %mklibname %{name} -s -d
%define dev32name %mklib32name %{name} -d
%define stat32name %mklib32name %{name} -s -d

#####################
# Hardcode PLF build
%define build_plf 0
#####################

%{?_with_plf: %{expand: %%global build_plf 1}}
%if %{build_plf}
%define distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%bcond_with dlopen
%else
%bcond_without dlopen
%endif

%ifarch %{riscv}
%bcond_with opencl
%else
%bcond_without opencl
%endif

%bcond_without swscaler
%bcond_with faac

%bcond_without bootstrap

# OpenCV, Soxr and PulseAudio use ffmpeg - can't link to them
# while bootstrapping...
%if %{with bootstrap}
%bcond_with opencv
%bcond_with soxr
%bcond_with pulse
%else
%bcond_without opencv
%bcond_without soxr
%bcond_without pulse
%endif
%bcond_without swscaler

# (tpg) use OpenMP
%global optflags %{optflags} -O3 -fopenmp
%global ldflags %{ldflags} -O3 -fopenmp

# (tpg) BIG FAT WARNING !!!
# ALWAYS RUN package-restricted-headers.sh
# AND UPLOAD output file as SOURCE1
%define x264_major 161
%define x265_major 199

Summary:	Old version of the ffmpeg codec library
Name:		ffmpeg4
Version:	4.4.1
Release:	8
%if %{build_plf}
License:	GPLv3+
%else
License:	GPLv2+
%endif
Group:		Video
Url:		http://ffmpeg.org/
Source0:	http://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz
Source1:	restricted-multimedia-headers.tar.xz
Source2:	restricted-defines.macros
# Creates Source1
Source10:	package-restricted-headers.sh
Patch1:		ffmpeg-4.3-dlopen-faac-mp3lame-opencore-x264-x265-xvid.patch
Patch2:		ffmpeg-1.0.1-time.h.patch
Patch3:		ffmpeg-2.5-fix-build-with-flto-and-inline-assembly.patch
# https://ffmpeg-devel.ffmpeg.narkive.com/qPHDqDaR/patch-1-5-avformat-adding-accessors-for-externally-used-avstream-fields-which-are-after-the-public#post8
# Generally useless but harmless, but seems to be needed by some versions of Opera, so let's keep it here for now
Patch4:		ffmpeg-4.4-add-accessors-for-AVStream.patch
Patch5:		ffmpeg-ffnvcodec-headers-12.1.14.patch
BuildRequires:	texi2html
BuildRequires:	yasm
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	flite-devel
BuildRequires:	gsm-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(libgme)
BuildRequires:	gomp-devel
%ifnarch %{riscv}
BuildRequires:	pkgconfig(caca)
%endif
BuildRequires:	pkgconfig(celt)
BuildRequires:	pkgconfig(fontconfig)
%if !%{with dlopen} || "%{disttag}" == "mdk"
BuildRequires:	pkgconfig(fdk-aac)
%endif
BuildRequires:	pkgconfig(dav1d)
%ifnarch %{ix86} %{riscv} aarch64
BuildRequires:	pkgconfig(rav1e)
%endif
%ifnarch %{riscv}
BuildRequires:	pkgconfig(aom)
%endif
BuildRequires:	pkgconfig(ffnvcodec)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libavc1394)
%ifnarch %{riscv}
BuildRequires:	pkgconfig(libbluray)
%endif
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(libdc1394-2)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(libilbc)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libpng)
%if %{with pulse}
BuildRequires:	pkgconfig(libpulse)
%endif
BuildRequires:	pkgconfig(librtmp)
BuildRequires:	pkgconfig(libssh)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libzmq)
%ifarch x86_64
# intel-mediasdk -- for now, useless on anything but x86_64
# (yes, even znver1 -- AMD CPUs don't have builtin Intel GPUs)
BuildRequires:	pkgconfig(libmfx)
%endif
%ifnarch %{riscv}
BuildRequires:	pkgconfig(openal)
%endif
%if %{with opencv}
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(frei0r)
%endif
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(sdl2)
%if 0
BuildRequires:	pkgconfig(shine)
%endif
%if %{with soxr}
BuildRequires:	pkgconfig(soxr)
%endif
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(twolame)
BuildRequires:	pkgconfig(vdpau)
%ifnarch %{riscv}
BuildRequires:	pkgconfig(vidstab)
BuildRequires:	pkgconfig(vpx)
%endif
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(xavs)
%ifnarch %{riscv}
BuildRequires:	pkgconfig(zvbi-0.2)
%endif
BuildRequires:	lame-devel
%if %{build_plf} || "%{disttag}" == "mdk"
BuildRequires:	x264-devel >= 0.148
BuildRequires:	pkgconfig(x265)
BuildRequires:	opencore-amr-devel
BuildRequires:	libvo-amrwbenc-devel
BuildRequires:	xvid-devel
%endif
%if %{with faac}
BuildRequires:	faac-devel
%endif
%ifnarch %{armx} %{riscv}
BuildRequires:	crystalhd-devel >= 0-0.20121105.1
%endif
%if %{with opencl}
BuildRequires:	pkgconfig(OpenCL)
%endif
%if %{with compat32}
BuildRequires:	devel(libbz2)
BuildRequires:	devel(libjpeg)
BuildRequires:	gomp-devel
# Better use
#BuildRequires:	devel(libgomp)
# but this is currently missing in the x86_64 tree because of
# a fluke during the distro-release upgrade
BuildRequires:	devel(libfontconfig)
BuildRequires:	devel(libopenal)
BuildRequires:	devel(libogg)
BuildRequires:	devel(libvorbis)
BuildRequires:	devel(libopus)
BuildRequires:	devel(libspeex)
BuildRequires:	devel(libgnutls)
BuildRequires:	devel(libaom)
BuildRequires:	devel(libv4l2)
BuildRequires:	devel(libfreetype)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libX11-xcb)
BuildRequires:	devel(libXdmcp)
BuildRequires:	devel(libXss)
BuildRequires:	devel(libgsm)
BuildRequires:	devel(libGL)
BuildRequires:	devel(libdrm)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
%endif

%description
ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%if %{build_plf}
This package is in Restricted as it violates several patents.
%endif

%package -n %{libavcodec}
Summary:	Shared library part of ffmpeg 4.x (OLD VERSION)
Group:		System/Libraries
%if %{with dlopen}
%if "%{disttag}" == "mdk"
%if %{with faac}
Suggests:	%{dlopen_req faac}
%endif
Suggests:	%{dlopen_req x264}
Suggests:	%{dlopen_req x265}
Suggests:	%{dlopen_req opencore-amrnb}
Suggests:	%{dlopen_req opencore-amrwb}
Suggests:	%{dlopen_req mp3lame}
Suggests:	%{dlopen_req xvidcore}
%else
%if %{with faac}
Suggests:	libfaac.so.0%{_arch_tag_suffix}
%endif
Suggests:	libx264.so.%{x264_major}%{_arch_tag_suffix}
Suggests:	libx265.so.%{x265_major}%{_arch_tag_suffix}
Suggests:	libopencore-amrnb.so.0%{_arch_tag_suffix}
Suggests:	libopencore-amrwb.so.0%{_arch_tag_suffix}
Suggests:	libmp3lame.so.0%{_arch_tag_suffix}
Suggests:	libxvidcore.so.4%{_arch_tag_suffix}
Suggests:	libfdk-aac.so.2%{_arch_tag_suffix}
%endif
%endif
Obsoletes:	%{_lib}ffmpeg54 < 1.1-3

%description -n %{libavcodec}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{libavdevice}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries
Conflicts:	%{_lib}avformats54 < 1.1-3

%description -n %{libavdevice}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{libavfilter}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries

%description -n %{libavfilter}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{libavformat}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries
Obsoletes:	%{_lib}avformats54 < 1.1-3

%description -n %{libavformat}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{libavutil}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries
Obsoletes:	%{mklibname avutil 51} < 1.1

%description -n %{libavutil}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{libpostproc}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries

%description -n %{libpostproc}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{libswresample}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries

%description -n %{libswresample}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%if %{with swscaler}
%package -n %{libswscale}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries
%rename %{oldlibswscale}

%description -n %{libswscale}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.
%endif

%package -n %{libavresample}
Summary:	Shared library part of ffmpeg (OLD VERSION)
Group:		System/Libraries

%description -n %{libavresample}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{devname}
Summary:	Header files for an old version of the ffmpeg codec library
Group:		Development/C
Requires:	%{libavcodec} = %{EVRD}
Requires:	%{libavdevice} = %{EVRD}
Requires:	%{libavfilter} = %{EVRD}
Requires:	%{libavformat} = %{EVRD}
Requires:	%{libavutil} = %{EVRD}
Requires:	%{libpostproc} = %{EVRD}
Requires:	%{libswresample} = %{EVRD}
%if %{with swscaler}
Requires:	%{libswscale} = %{EVRD}
%endif
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the development files for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{statname}
Summary:	Static library for an old version of the ffmpeg codec library
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Provides:	%{name}-static-devel = %{EVRD}

%description -n %{statname}
This package contains the static libraries for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%if %{with compat32}
%package -n %{lib32avcodec}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries
%if %{with faac}
Suggests:	libfaac.so.0
%endif
Suggests:	libx264.so.%{x264_major}
Suggests:	libx265.so.%{x265_major}
Suggests:	libopencore-amrnb.so.0
Suggests:	libopencore-amrwb.so.0
Suggests:	libmp3lame.so.0
Suggests:	libxvidcore.so.4
Suggests:	libfdk-aac.so.2

%description -n %{lib32avcodec}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{lib32avdevice}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32avdevice}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{lib32avfilter}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32avfilter}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{lib32avformat}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32avformat}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{lib32avutil}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32avutil}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{lib32postproc}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32postproc}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{lib32swresample}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32swresample}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%if %{with swscaler}
%package -n %{lib32swscale}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32swscale}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.
%endif

%package -n %{lib32avresample}
Summary:	Shared library part of ffmpeg (32-bit) (OLD VERSION)
Group:		System/Libraries

%description -n %{lib32avresample}
This package contains a shared library for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{dev32name}
Summary:	Header files for the ffmpeg codec library (32-bit) (OLD VERSION)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32avcodec} = %{EVRD}
Requires:	%{lib32avdevice} = %{EVRD}
Requires:	%{lib32avfilter} = %{EVRD}
Requires:	%{lib32avformat} = %{EVRD}
Requires:	%{lib32avutil} = %{EVRD}
Requires:	%{lib32postproc} = %{EVRD}
Requires:	%{lib32swresample} = %{EVRD}
%if %{with swscaler}
Requires:	%{lib32swscale} = %{EVRD}
%endif

%description -n %{dev32name}
This package contains the development files for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.

%package -n %{stat32name}
Summary:	Static library for the ffmpeg codec library (32-bit) (OLD VERSION)
Group:		Development/C
Requires:	%{dev32name} = %{EVRD}

%description -n %{stat32name}
This package contains the static libraries for %{name}.

THIS IS AN OLD VERSION, provided for compatibility with legacy applications
only. New applications should use ffmpeg instead.
%endif

%prep
%setup -q -n ffmpeg-%{version} -a 1
%patch2 -p1 -b .timeh~
%if %{with dlopen}
%patch1 -p1 -b .dlopen~
%endif
%patch3 -p1 -b .flto_inline_asm~
%patch4 -p1 -b .accessor~
%patch5 -p1

# The debuginfo generator doesn't like non-world readable files
find . -name "*.c" -o -name "*.h" -o -name "*.asm" |xargs chmod 0644
# use headers from current packages in restricted repo

%build
%ifarch %{ix86}
%global ldflags %{ldflags} -Wl,-z,notext
%endif
export CFLAGS="%{optflags} -fPIC -I/usr/include/openjpeg-2.2"
export LDFLAGS="%{ldflags}"

%ifarch %{ix86}
# Allow the use of %xmm7 and friends in inline assembly
export CFLAGS="${CFLAGS} -mmmx -msse -msse2 -msse3"
%endif

# The build process tends to open a lot of files...
ulimit -n 102400

%if %{with compat32}
mkdir build32
cp -a $(ls -1 |grep -v build32) build32/
cd build32
# FIXME omitting some not very common 3rd party codecs
# and outputs for now. Enable them (and build 32bit
# versions of the corresponding libs) if something
# in wine breaks...
# We're also disabling some libraries for important
# codecs (but ones that have an internal implementation
# too -- such as lame/toolame).
if ! CFLAGS="$(echo $CFLAGS |sed -e 's,-m64,,g;s,-mx32,,g') -fomit-frame-pointer" LDFLAGS="$(echo $LDFLAGS |sed -e 's,-m64,,g;s,-mx32,,g') -fomit-frame-pointer" ./configure \
	--cc="gcc -m32" \
	--cxx="g++ -m32" \
	--ranlib=%{_bindir}/llvm-ranlib \
	--prefix=%{_prefix} \
	--enable-shared \
	--libdir=%{_prefix}/lib \
	--shlibdir=%{_prefix}/lib \
	--incdir=%{_includedir} \
	--disable-stripping \
	--enable-avresample \
	--enable-postproc \
	--enable-gpl \
	--enable-version3 \
	--enable-nonfree \
%ifnarch %{armx} %{arm} %{riscv}
	--enable-nvenc \
%endif
	--enable-ffplay \
	--disable-libdav1d \
	--disable-librav1e \
	--enable-libaom \
	--enable-lto \
	--enable-pthreads \
	--disable-libtheora \
	--enable-libvorbis \
	--disable-encoder=vorbis \
	--disable-libvpx \
	--enable-runtime-cpudetect \
	--disable-libdc1394 \
	--disable-librtmp \
	--enable-libspeex \
	--enable-libfreetype \
	--enable-libgsm \
	--disable-libcelt \
	--disable-libopencv \
	--disable-frei0r \
	--disable-libopenjpeg \
	--disable-libxavs \
	--disable-libmodplug \
	--disable-libass \
	--enable-gnutls \
	--disable-libcdio \
%if %{with pulse}
	--enable-libpulse \
%endif
	--enable-libv4l2 \
%ifnarch %{riscv}
	--enable-openal \
%endif
	--enable-opengl \
	--disable-libzmq \
	--disable-libzvbi \
	--disable-libssh \
%if %{with soxr}
	--enable-libsoxr \
%endif
	--disable-libtwolame \
	--enable-libopus \
	--disable-libilbc \
	--disable-libiec61883 \
	--disable-libgme \
	--disable-libbluray \
	--disable-libcaca \
	--disable-libvidstab \
	--disable-ladspa \
	--disable-libwebp \
	--enable-fontconfig \
	--enable-libxcb \
	--enable-libxcb-shm \
	--enable-libxcb-xfixes \
	--enable-libxcb-shape \
	--disable-libbs2b \
	--disable-libmp3lame \
%if %{build_plf}
	--enable-libfdk-aac \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	--enable-version3 \
	--enable-libx264 \
	--enable-libx265 \
	--enable-libvo-amrwbenc \
	--enable-libxvid \
%else
%if %{with dlopen}
	--enable-libfdk-aac-dlopen \
	--enable-libopencore-amrnb-dlopen \
	--enable-libopencore-amrwb-dlopen \
	--enable-libx264-dlopen \
	--enable-libx265-dlopen \
	--enable-libxvid-dlopen \
%if %{with faac}
	--enable-libfaac-dlopen \
%endif
%endif
%endif
%if %{with faac} && !%{with dlopen}
	--enable-nonfree \
	--enable-libfaac \
%endif
	--disable-opencl \
	--disable-asm \
	--disable-x86asm \
	; then
	cat ffbuild/config.log
	exit 1
fi
%make_build
cd ..
%endif

if ! ./configure \
	--cc=%{__cc} \
	--cxx=%{__cxx} \
	--ranlib=%{_bindir}/llvm-ranlib \
	--prefix=%{_prefix} \
	--enable-shared \
	--libdir=%{_libdir} \
	--shlibdir=%{_libdir} \
	--incdir=%{_includedir} \
	--disable-stripping \
	--enable-avresample \
	--enable-postproc \
	--enable-gpl \
	--enable-version3 \
	--enable-nonfree \
%ifnarch %{armx} %{arm} %{riscv}
	--enable-nvenc \
%endif
	--enable-ffplay \
	--enable-libdav1d \
%ifnarch %{ix86} aarch64
	--enable-librav1e \
%endif
	--enable-libaom \
%ifarch %{ix86}
	--disable-lto \
%else
	--enable-lto \
%endif
	--enable-pthreads \
	--enable-libtheora \
	--enable-libvorbis \
	--disable-encoder=vorbis \
%ifnarch %{riscv}
	--enable-libvpx \
%endif
	--enable-runtime-cpudetect \
	--enable-libdc1394 \
	--enable-librtmp \
	--enable-libspeex \
	--enable-libfreetype \
	--enable-libgsm \
	--enable-libcelt \
%ifarch x86_64
	--enable-libmfx \
%endif
%if %{with opencv}
	--enable-libopencv \
	--enable-frei0r \
%endif
	--enable-libopenjpeg \
	--enable-libxavs \
	--enable-libmodplug \
	--enable-libass \
	--enable-gnutls \
	--enable-libcdio \
%if %{with pulse}
	--enable-libpulse \
%endif
	--enable-libv4l2 \
%ifnarch %{riscv}
	--enable-openal \
%endif
	--enable-opengl \
	--enable-libzmq \
%ifnarch %{riscv}
	--enable-libzvbi \
%endif
	--enable-libssh \
%if %{with soxr}
	--enable-libsoxr \
%endif
	--enable-libtwolame \
	--enable-libopus \
	--enable-libilbc \
	--enable-libiec61883 \
	--enable-libgme \
%ifnarch %{riscv}
	--enable-libcaca \
	--enable-libbluray \
	--enable-libvidstab \
%endif
	--enable-ladspa \
	--enable-libwebp \
	--enable-fontconfig \
%if 0
	--enable-libshine \
%endif
	--enable-libflite \
	--enable-libxcb \
	--enable-libxcb-shm \
	--enable-libxcb-xfixes \
	--enable-libxcb-shape \
	--enable-libbs2b \
	--enable-libmp3lame \
%if %{build_plf}
	--enable-libfdk-aac \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	--enable-version3 \
	--enable-libx264 \
	--enable-libx265 \
	--enable-libvo-amrwbenc \
	--enable-libxvid \
%else
%if %{with dlopen}
	--enable-libfdk-aac-dlopen \
	--enable-libopencore-amrnb-dlopen \
	--enable-libopencore-amrwb-dlopen \
	--enable-libx264-dlopen \
	--enable-libx265-dlopen \
	--enable-libxvid-dlopen \
%if %{with faac}
	--enable-libfaac-dlopen \
%endif
%endif
%endif
%if %{with faac} && !%{with dlopen}
	--enable-nonfree \
	--enable-libfaac \
%endif
%if %{with opencl}
	--enable-opencl \
%else
	--disable-opencl \
%endif
%if 0
	--disable-libaacplus \
	--disable-libstagefright-h264 \
	--disable-decklink \
%endif
	; then
	cat ffbuild/config.log
	exit 1
fi

%make_build V=1

%install
%if %{with compat32}
cd build32
%make_install SRC_PATH=$(pwd)
cd ..
%endif
%make_install SRC_PATH=$(pwd)
# Don't Provides: pkgconfig(libavcodec) and friends
# That's up to ffmpeg 5.x
for i in %{buildroot}%{_libdir}/pkgconfig/*.pc; do
	sed -i -e 's,libswscale >,libswscale-4 >,g;s,libavcodec >,libavcodec-4 >,g;s,libavformat >,libavformat-4 >,g;s,libavresample >,libavresample-4 >,g;s,libavutil >,libavutil-4 >,g;s,libpostproc >,libpostproc-4 >,g;s,libavfilter >,libavfilter-4 >,g;s,libswresample >,libswresample-4 >,g' ${i}
	mv ${i} ${i/.pc/-4.pc}
done
%if %{with compat32}
for i in %{buildroot}%{_prefix}/lib/pkgconfig/*.pc; do
	sed -i -e 's,libswscale >,libswscale-4 >,g;s,libavcodec >,libavcodec-4 >,g;s,libavformat >,libavformat-4 >,g;s,libavresample >,libavresample-4 >,g;s,libavutil >,libavutil-4 >,g;s,libpostproc >,libpostproc-4 >,g;s,libavfilter >,libavfilter-4 >,g;s,libswresample >,libswresample-4 >,g' ${i}
	mv ${i} ${i/.pc/-4.pc}
done
%endif

# No executables, docs or examples for compat packages
rm -rf %{buildroot}%{_bindir} \
	%{buildroot}%{_mandir} \
	%{buildroot}%{_datadir}/ffmpeg \
	%{buildroot}%{_docdir}

%files -n %{libavcodec}
%{_libdir}/libavcodec.so.%{major}*

%files -n %{libavdevice}
%{_libdir}/libavdevice.so.%{major}*

%files -n %{libavfilter}
%{_libdir}/libavfilter.so.%{filtermajor}*

%files -n %{libavformat}
%{_libdir}/libavformat.so.%{major}*

%files -n %{libavutil}
%{_libdir}/libavutil.so.%{avumajor}*

%files -n %{libpostproc}
%{_libdir}/libpostproc.so.%{ppmajor}*

%files -n %{libswresample}
%{_libdir}/libswresample.so.%{swrmajor}*

%if %{with swscaler}
%files -n %{libswscale}
%{_libdir}/libswscale.so.%{swsmajor}*
%endif

%files -n %{libavresample}
%{_libdir}/libavresample.so.%{avrmajor}*

%files -n %{devname}
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavformat
%{_includedir}/libavresample
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libavfilter
%{_includedir}/libswresample
%{_libdir}/libavcodec.so
%{_libdir}/libavdevice.so
%{_libdir}/libavformat.so
%{_libdir}/libavresample.so
%{_libdir}/libavutil.so
%{_libdir}/libpostproc.so
%{_libdir}/libavfilter.so
%{_libdir}/libswresample.so
%if %{with swscaler}
%{_libdir}/libswscale.so
%{_includedir}/libswscale
%{_libdir}/pkgconfig/libswscale-4.pc
%endif
%{_libdir}/pkgconfig/libavcodec-4.pc
%{_libdir}/pkgconfig/libavdevice-4.pc
%{_libdir}/pkgconfig/libavformat-4.pc
%{_libdir}/pkgconfig/libavresample-4.pc
%{_libdir}/pkgconfig/libavutil-4.pc
%{_libdir}/pkgconfig/libpostproc-4.pc
%{_libdir}/pkgconfig/libavfilter-4.pc
%{_libdir}/pkgconfig/libswresample-4.pc

%files -n %{statname}
%{_libdir}/*.a

%if %{with compat32}
%files -n %{lib32avcodec}
%{_prefix}/lib/libavcodec.so.%{major}*

%files -n %{lib32avdevice}
%{_prefix}/lib/libavdevice.so.%{major}*

%files -n %{lib32avfilter}
%{_prefix}/lib/libavfilter.so.%{filtermajor}*

%files -n %{lib32avformat}
%{_prefix}/lib/libavformat.so.%{major}*

%files -n %{lib32avutil}
%{_prefix}/lib/libavutil.so.%{avumajor}*

%files -n %{lib32postproc}
%{_prefix}/lib/libpostproc.so.%{ppmajor}*

%files -n %{lib32swresample}
%{_prefix}/lib/libswresample.so.%{swrmajor}*

%if %{with swscaler}
%files -n %{lib32swscale}
%{_prefix}/lib/libswscale.so.%{swsmajor}*
%endif

%files -n %{lib32avresample}
%{_prefix}/lib/libavresample.so.%{avrmajor}*

%files -n %{dev32name}
%{_prefix}/lib/libavcodec.so
%{_prefix}/lib/libavdevice.so
%{_prefix}/lib/libavformat.so
%{_prefix}/lib/libavresample.so
%{_prefix}/lib/libavutil.so
%{_prefix}/lib/libpostproc.so
%{_prefix}/lib/libavfilter.so
%{_prefix}/lib/libswresample.so
%if %{with swscaler}
%{_prefix}/lib/libswscale.so
%{_prefix}/lib/pkgconfig/libswscale-4.pc
%endif
%{_prefix}/lib/pkgconfig/libavcodec-4.pc
%{_prefix}/lib/pkgconfig/libavdevice-4.pc
%{_prefix}/lib/pkgconfig/libavformat-4.pc
%{_prefix}/lib/pkgconfig/libavresample-4.pc
%{_prefix}/lib/pkgconfig/libavutil-4.pc
%{_prefix}/lib/pkgconfig/libpostproc-4.pc
%{_prefix}/lib/pkgconfig/libavfilter-4.pc
%{_prefix}/lib/pkgconfig/libswresample-4.pc

%files -n %{stat32name}
%{_prefix}/lib/*.a
%endif
