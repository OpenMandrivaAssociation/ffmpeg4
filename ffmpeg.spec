%define name	ffmpeg
%define version	0.6.1
%define svn 22960
%define prerel	0
%define release %mkrel 3
%define major	52

%define libname %mklibname %name %major
%define develname %mklibname %name -d
%define staticname %mklibname %name -s -d

%define avfmajor 52
%define avflibname %mklibname avformats %avfmajor
%define postprocmajor 51
%define postproclibname %mklibname postproc %postprocmajor

%define avumajor 50
%define avulibname %mklibname avutil %avumajor
%define swsmajor 0
%define swslibname %mklibname swscaler %swsmajor

%define build_swscaler 1
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%endif
%define build_faac	0
%{?_with_faac: %{expand: %%global build_faac 1}}
%{?_without_faac: %{expand: %%global build_faac 0}}
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}%{?extrarelsuffix}
Summary: 	Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Source0: 	http://ffmpeg.org/releases/%{name}-%version.tar.bz2
Patch1:		ffmpeg-linkage_fix.diff
%if %build_plf
License: 	GPLv3+
%else
License: 	GPLv2+
%endif
Group: 	 	Video
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:  texi2html
BuildRequires:	SDL-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libjack-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libschroedinger-devel
BuildRequires:	libvpx-devel
BuildRequires:	jpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	bzip2-devel
BuildRequires:	rtmp-devel
%if %{mdkversion} >= 200900
BuildRequires:	vdpau-devel
%endif
%if %{mdkversion} >= 200910
BuildRequires:	libva-devel
%endif
URL:		http://ffmpeg.org/
%if %build_plf
BuildRequires: libfaad2-devel
BuildRequires: x264-devel >= 0.83
BuildRequires: liblame-devel
BuildRequires: opencore-amr-devel
%endif
%if %build_faac
BuildRequires: libfaac-devel
%endif
Requires:	%postproclibname = %version-%release
Requires:	%libname = %version-%release
Requires:	%avflibname = %version-%release
Requires:	%avulibname = %version-%release
%if %build_swscaler
Requires:       %{swslibname} = %{version}-%release
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
Conflicts: %mklibname ffmpeg 51

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

%setup -q -n %{name}-%version

%if %build_swscaler
%endif
%patch1 -p0 -b .linkage_fix

#find -name Makefile | xargs perl -pi -e "s|\\\$\(prefix\)/lib|\\\$\(libdir\)|g"

%build
export CFLAGS="%optflags -FPIC"
export LDFLAGS="%{ldflags}"

./configure --prefix=%_prefix \
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
%if %build_plf
	--enable-libmp3lame \
	--enable-libfaad \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	--enable-version3 \
	--enable-libx264 \
%else
	--disable-decoder=aac --disable-encoder=aac \
%endif
%if %build_faac
	--enable-nonfree --enable-libfaac
%endif

%make

%install
rm -rf %{buildroot}

%makeinstall_std SRC_PATH=`pwd`

# compat symlink
install -d %buildroot/%_libdir/libavcodec
pushd %buildroot/%_libdir/libavcodec && ln -sf ../libavcodec.a && popd
install -d %buildroot/%_libdir/libavformat
pushd %buildroot/%_libdir/libavformat && ln -sf ../libavformat.a && popd

%clean
rm -rf %{buildroot}

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
%_mandir/man1/*
%_datadir/ffmpeg

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


