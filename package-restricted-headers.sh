#!/bin/sh

sudo dnf --refresh install 'pkgconfig(x264)' 'pkgconfig(x265)' 'pkgconfig(fdk-aac)' 'pkgconfig(faad2)' 'pkgconfig(opencore-amrwb)' 'pkgconfig(opencore-amrnb)' xvid-devel
sudo dnf upgrade 'pkgconfig(x264)' 'pkgconfig(x265)' 'pkgconfig(fdk-aac)' 'pkgconfig(faad2)' 'pkgconfig(opencore-amrwb)' 'pkgconfig(opencore-amrnb)' xvid-devel
LOCALDIR=$(realpath $(dirname $0))
TMPDIR=$(mktemp -d /tmp/mmheadersXXXXXX)
mkdir -p $TMPDIR/localinc
cd /usr/include
cp -a fdk-aac neaacdec.h opencore-amrwb opencore-amrnb x264_config.h x264.h x265_config.h x265.h xvid.h $TMPDIR/localinc
cd $TMPDIR
echo "%define x264_major $(cat localinc/x264.h |grep '^#define X264_BUILD' |awk '{ print $3; }')" >$LOCALDIR/restricted-defines.macros
echo "%define x265_major $(cat localinc/x265_config.h |grep '^#define X265_BUILD' |awk '{ print $3; }')" >>$LOCALDIR/restricted-defines.macros
tar cJf $LOCALDIR/restricted-multimedia-headers.tar.xz localinc
cd $LOCALDIR
rm -rf $TMPDIR

printf '%s\n' "Now upload restricted-multimedia-headers.tar.xz to ABF and update .abf.yml file"
