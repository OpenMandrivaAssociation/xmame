%define Werror_cflags %nil
%define build_upx 0
%{?_with_upx: %{expand: %%global build_upx 1}}

%ifarch %ix86
%define enable_dynarec 1
%define enable_68k_asm 1
%else
%define enable_dynarec 0
%define enable_68k_asm 0
%endif
%{?_with_dynarec: %{expand: %%global enable_dynarec 1}}
%{?_without_dynarec: %{expand: %%global enable_dynarec 0}}
%{?_with_68k_asm: %{expand: %%global enable_68k_asm 1}}
%{?_without_68k_asm: %{expand: %%global enable_68k_asm 0}}

%define fversion 0.106

%define buildx11mame		1
%define enable_x11_gl_mame	1
%define enable_x11_fx_mame	0
%define buildSDLmame		1
%define buildsvgalibmame	0
%define buildsvgafxmame		0

%define buildx11mess		1
%define enable_x11_gl_mess	1
%define enable_x11_fx_mess	0
%define buildSDLmess		1
%define buildsvgalibmess	0
%define buildsvgafxmess		0

%define mdkversion		%(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandrake-release)

%if %mdkversion >= 200700
%define x11prefix		%{_prefix}
%else
%define x11prefix               %{_prefix}/X11R6
%endif

%define rel			5
%define distsuffix		plf
%define release			%mkrel %rel

%define name			xmame

# virtual package to enforce naming convention
#
Summary:	X-Mame Arcade Game Emulator
Name:		%{name}
Version:	%{fversion}
Release:	%{release}

Source:		http://x.mame.net/download/%name-%version.tar.bz2
Source1:	%{name}-16x16.png
Source2:	%{name}-32x32.png
Source3:	%{name}-48x48.png
Source4:	%{name}-rc-089.tar.bz2
Source5:	xmess-16x16.png
Source6:	xmess-32x32.png
Source7:	xmess-48x48.png

Source10:	http://www.mame.net/roms/polyplay.zip
Source11:	http://www.mame.net/roms/robby.zip
Source12:	http://www.mame.net/roms/gridlee.zip
Source13:	http://www.mame.net/roms/gridlee-sample.zip

Source20:	http://www.mameworld.net/highscore/uhsdat0105.zip
#note the included cheats are for 0.106
Source21:	http://cheat.retrogames.com/cheat.7z
Source22:       http://www.arcade-history.com/download/history1_06q.zip
Source23:	http://www.mameworld.net/mameinfo/update/Mameinfo0106.zip
#Source24:	Update106to106u1.zip
#Source25:	Update106u1to106u2.zip
#location of update zips:
#http://www.mameworld.net/mameinfo/update/update0<target-version>/Update.zip

#note the included catver.ini is for 0.105
Source40:	http://catver.com/catveren.zip
#for upx packages only, as its name implies:
Patch10:	xmame-0.56.1-upx.patch.bz2
Patch13:	xmame.makefile.patch

# I have no idea what this one does and if it's still necessary
Patch12:	xmame-mamex.patch.bz2

License:	Freeware
#Actual (X)MAME license : http://x.mame.net/license.html
URL:		http://x.mame.net/
Group:		Emulators
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	esound-devel XFree86-devel zlib-devel dos2unix 
BuildRequires:	libusb-devel alsa-lib-devel
BuildRequires:  libSDL-devel unzip p7zip
BuildRequires:	libexpat-devel
%ifarch %ix86
BuildRequires:	nasm
%endif
%if %build_upx
BuildRequires:  upx
%endif

%description
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.

# xmame-tools
%package -n %{name}-tools
Summary: X-Mame Arcade Game Emulator compiled for x11
Group:         Emulators
Requires:      xmame >= %{fversion}

%description -n %{name}-tools
X-Mame/Mess the UNIX/X11 are the ports of Mame/MESS projects.
This package contains tools useful when need of creating, comparing, or 
upgrading roms or compressed hard disks (.chd) comes.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.

# xmame-base
%package -n %{name}-base
Summary: X-Mame Arcade Game Emulator compiled for x11
Group:         Emulators
Requires:      xmame >= %{fversion}

%description -n %{name}-base
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This package has the high scores, the mamedat, cheats.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.

# xmess-base
%package -n xmess-base
Summary: X-Mess Emulator compiled for x11
Group:         Emulators
Requires:      xmess >= %{fversion}

%description -n xmess-base
X-Mame/Mess the UNIX/X11 are the ports of Mame/MESS projects.
It makes MESS (Multi-Emulator Super System) available on *ix machines
using the X11R6 X-Window system (and Linux ones using SVGAlib too).

M.E.S.S. is a computer and consoles emulator: it includes a Z80, 6502,
68000 and lastly I86 uP emulators.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.

# x11 target
%if %buildx11mame
%package -n %{name}-x11
Summary:	X-Mame Arcade Game Emulator compiled for x11
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
Provides:	%{name} %{name}-xgl %{name}-xfx
Provides:       %{name} = %{fversion}
Requires:	%{name}-base
Obsoletes:	%{name} <= 0.37b13.2-1mdk
Obsoletes:	%{name}-xgl <= 0.87
Obsoletes:	%{name}-xfx <= 0.87
# xgl
%if %enable_x11_gl_mame
BuildRequires: Mesa-common-devel libjpeg-devel
%endif
# Glide/X11
%if %enable_x11_fx_mame
BuildRequires: Glide_V3 Glide_V3-devel
Requires:      Glide_V3
%endif

%description -n %{name}-x11
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This version has been compiled with X11/Open GL/Glide support.
A separate binary without the 68000 asm core is provided in a separate
binary (xmame.x11). Try it if your game does not work well.
If using dga you end up with a messed-up screen, check that XF86Config-4
has 'Load "extmod"' in the module section.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

%if %buildx11mess
%package -n xmess-x11
Summary:	X-Mess Emulator compiled for x11
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
Provides:	xmess xmess-xgl xmess-xfx
Provides:       xmess = %{fversion}
Requires:	xmess-base
Obsoletes:	xmess-xgl <= 0.87
Obsoletes:	xmess-xfx <= 0.87
# xgl
%if %enable_x11_gl_mess
BuildRequires: Mesa-common-devel libjpeg-devel
%endif
# Glide/X11
%if %enable_x11_fx_mess
BuildRequires: Glide_V3 Glide_V3-devel
Requires:      Glide_V3
%endif

%description -n xmess-x11
X-Mame/Mess the UNIX/X11 are the ports of Mame/MESS projects.
It makes MESS (Multi-Emulator Super System) available on *ix machines
using the X11R6 X-Window system (and Linux ones using SVGAlib too).

M.E.S.S. is a computer and consoles emulator: it includes a Z80, 6502,
68000 and lastly I86 uP emulators.

If using dga you end up with a messed-up screen, check that XF86Config-4
has 'Load "extmod"' in the module section.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

# svgalib target
%if %buildsvgalibmame
%package -n %{name}-svgalib
Summary:	X-Mame Arcade Game Emulator compiled for SVGA lib
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
BuildRequires:	svgalib-devel
Provides:	%{name}
Provides:       %{name} = %{fversion}
Requires:	%{name}-base svgalib
Obsoletes:	xmame <= 0.37b13.2-1mdk

%description -n %{name}-svgalib
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This version has been compiled with SVGA lib support.
A separate binary without the 68000 asm core is provided in a separate
binary (xmame.svgalib). Try it if your game does not work well.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

%if %buildsvgalibmess
%package -n xmess-svgalib
Summary:	X-Mame Arcade Game Emulator compiled for SVGA lib
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
BuildRequires:	svgalib-devel
Provides:	xmess
Provides:       xmess = %{fversion}
Requires:	xmess-base svgalib

%description -n xmess-svgalib
X-Mame/Mess the UNIX/X11 are the ports of Mame/MESS projects.
It makes MESS (Multi-Emulator Super System) available on *ix machines
using the X11R6 X-Window system (and Linux ones using SVGAlib too).

M.E.S.S. is a computer and consoles emulator: it includes a Z80, 6502, 
68000 and lastly I86 uP emulators.

This version has been compiled with SVGA lib support.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

# SDL target
%if %buildSDLmame
%package -n %{name}-SDL
Summary:	X-Mame Arcade Game Emulator compiled for SDL
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
#causes problems compiling for 9.1 otherwise
#BuildRequires: SDL1.2-devel
Provides:	%{name}
Provides:       %{name} = %{fversion}
Requires:	%{name}-base
Obsoletes:	xmame <= 0.37b13.2-1mdk

%description -n %{name}-SDL
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This version has been compiled with SDL support.
A separate binary without the 68000 asm core is provided in a separate
binary (xmame.SDL). Try it if your game does not work well.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

%if %buildSDLmess
%package -n xmess-SDL
Summary:	X-Mame Arcade Game Emulator compiled for SDL
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
#BuildRequires: SDL1.2-devel
Provides:	xmess
Provides:       xmess = %{fversion}
Requires:	xmess-base 

%description -n xmess-SDL
X-Mame/Mess the UNIX/X11 are the ports of Mame/MESS projects.
It makes MESS (Multi-Emulator Super System) available on *ix machines
using the X11R6 X-Window system (and Linux ones using SVGAlib too).

M.E.S.S. is a computer and consoles emulator: it includes a Z80, 6502, 
68000 and lastly I86 uP emulators.

This version has been compiled with SDL support.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

# Glide/svgalib target
%if %buildsvgafxmame
%package -n %{name}-svgafx
Summary:	X-Mame Arcade Game Emulator compiled for 3Dfx cards with X11
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
BuildRequires:	Glide_V3 Glide_V3-devel
Provides:	%{name}
Provides:       %{name} = %{fversion}
Requires:	%{name}-base Glide_V3
Obsoletes:	xmame <= 0.37b13.2-1mdk

%description -n %{name}-svgafx
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This version has been compiled with voodoo/svgalib support.
A separate binary without the 68000 asm core is provided in a separate
binary (xmame.svgafx). Try it if your game does not work well.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

# Glide/svgalib target
%if %buildsvgafxmess
%package -n xmess-svgafx
Summary:	X-Mame Arcade Game Emulator compiled for 3Dfx cards with X11
Group:		Emulators
Requires(pre):	/usr/sbin/update-alternatives
BuildRequires:	Glide_V3 Glide_V3-devel
Provides:	xmess
Provides:       xmess = %{fversion}
Requires:	xmess-base Glide_V3

%description -n xmess-svgafx
X-Mame/Mess the UNIX/X11 are the ports of Mame/MESS projects.
It makes MESS (Multi-Emulator Super System) available on *ix machines
using the X11R6 X-Window system (and Linux ones using SVGAlib too).

M.E.S.S. is a computer and consoles emulator: it includes a Z80, 6502, 
68000 and lastly I86 uP emulators.

This version has been compiled with voodoo/svgalib support.

This package is in PLF because of Mandriva Linux policy forbidding
non-free and emulation software.
%endif

%prep
rm -rf %buildroot

%setup -q

%if %build_upx
%patch10 -p1
%endif

%patch12 -p1
%patch13 -p0

unzip -aa -o %{SOURCE20} hiscore.dat
7za x %{SOURCE21}
unzip -aa -o %{SOURCE22} history.dat
7za x %{SOURCE23}
7za x `echo $(basename %{SOURCE23}) | perl -p -e "s|zip|exe|"`

#unzip -aa -o %{SOURCE24}
#dos2unix mameinfo.dif
#patch -p1 <mameinfo.dif
dos2unix mameinfo.dat

unzip -aa -o -C %{SOURCE40} catver.ini

%build

# settings are positioned within the spec and no more with a patch
perl -pi -e "s/# SOUND/SOUND/g" makefile.unix
perl -pi -e "s/# JOY_SDL/JOY_SDL/" makefile.unix
perl -pi -e "s/# JOY_STANDARD/JOY_STANDARD/" makefile.unix
perl -pi -e "s/# XINPUT/XINPUT/" makefile.unix
perl -pi -e "s|^X11LIB.*$|X11LIB = -L%{x11prefix}/%{_lib}|" makefile.unix
perl -pi -e "s/^CFLAGS =/CFLAGS = %optflags/" makefile.unix
%if %enable_dynarec
perl -pi -e "s/# X86_MIPS3_DRC/X86_MIPS3_DRC/" makefile.unix
perl -pi -e "s/# X86_PPC_DRC/X86_PPC_DRC/" makefile.unix
perl -pi -e "s/# X86_VOODOO_DRC/X86_VOODOO_DRC/" makefile.unix
%endif

%ifarch x86_64
perl -pi -e "s/MY_CPU = i386/MY_CPU = amd64/" makefile.unix
%else
perl -pi -e "s/MY_CPU = i386/MY_CPU = %{_arch}/" makefile.unix
%endif

#detection of mmx currently works on x86 only...
%ifarch %ix86
	perl -pi -e "s/# EFFECT_MMX_ASM/EFFECT_MMX_ASM/" makefile.unix
%endif

# options from xmame not provided by our RPM variables
# -funroll-loops -fstrength-reduce  -fomit-frame-pointer -ffast-math
# -malign-functions=2 -malign-jumps=2 -malign-loops=2 -s -fno-exceptions
# -fstrict-aliasing

#Xmame compilation
# x11 target with 68k asm support
%if %enable_68k_asm
%if %buildx11mame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
	X86_ASM_68000=1 \
	X11_DGA=1 X11_XV=1 \
%if %enable_x11_gl_mame
	X11_OPENGL=1 \
%endif
%if %enable_x11_fx_mame
	X11_GLIDE=1 \
%endif
	XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=x11 \
	CC=gcc
mv xmame.x11 xmame.x11-68k
%endif

# SDL target with 68k asm support
%if %buildSDLmame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
	X86_ASM_68000=1 \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
        XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=SDL \
	CC=gcc
mv xmame.SDL xmame.SDL-68k
%endif
#SOUND_SDL=1 JOY_SDL=1 \


# svgalib target with 68k asm support
%if %buildsvgalibmame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
	X86_ASM_68000=1 \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
        XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=svgalib \
	CC=gcc
mv xmame.svgalib xmame.svgalib-68k
%endif

# Glide/svgalib target with 68k asm support
%if %buildsvgafxmame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
	X86_ASM_68000=1 \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
        XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=svgafx \
	CC=gcc
mv xmame.svgafx xmame.svgafx-68k
%endif

# won't recompile without the 68k asm core if not clean
make -f makefile.unix PREFIX=%{_prefix} TARGET=mame clean68k
%endif

# x11 target without 68k asm support
%if %buildx11mame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
	X11_DGA=1 X11_XV=1\
%if %enable_x11_gl_mame
	X11_OPENGL=1 \
%endif
%if %enable_x11_fx_mame
	X11_GLIDE=1 \
%endif
        XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=x11 \
	CC=gcc
%endif

# SDL target without 68k asm support
%if %buildSDLmame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
        XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=SDL \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
	CC=gcc
%endif
#SOUND_SDL=1 JOY_SDL=1 \

# svgalib target without 68k asm support
%if %buildsvgalibmame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
        XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=svgalib \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \

	CC=gcc
%endif

# Glide/svgalib target without 68k asm support
%if %buildsvgafxmame
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mame \
        XMAMEROOT=%{_gamesdatadir}/xmame \
	DISPLAY_METHOD=svgafx \
	CC=gcc
%endif

#Xmess compilation
#Xmess - x11 target with 68k asm support
%if %enable_68k_asm
%if %buildx11mess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
	X86_ASM_68000=1 \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
	X11_DGA=1 X11_XV=1\
%if %enable_x11_gl_mess
	X11_OPENGL=1 \
%endif
%if %enable_x11_fx_mess
	X11_GLIDE=1 \
%endif
	XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=x11 \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
	CC=gcc
mv xmess.x11 xmess.x11-68k
%endif

#Xmess - SDL target with 68k asm support
%if %buildSDLmess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
	X86_ASM_68000=1 \
        XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=SDL \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
	CC=gcc
mv xmess.SDL xmess.SDL-68k
%endif
#SOUND_SDL=1 JOY_SDL=1 \

#Xmess - svgalib target with 68k asm support
%if %buildsvgalibmess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
	X86_ASM_68000=1 \
        XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=svgalib \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
	CC=gcc
mv xmess.svgalib xmess.svgalib-68k
%endif

#Xmess - Glide/svgalib target with 68k asm support
%if %buildsvgafxmess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
	X86_ASM_68000=1 \
        XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=svgafx \
	SOUND_ARTS_TEIRA=0 \
	SOUND_ARTS_SMOTEK=0 \
	CC=gcc
mv xmess.svgafx xmess.svgafx-68k
%endif

# won't recompile without the 68k asm core if not clean
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess clean68k
%endif

#Xmess -  x11 target without 68k asm support
%if %buildx11mess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
	X11_DGA=1 X11_XV=1\
%if %enable_x11_gl_mess
	X11_OPENGL=1 \
%endif
%if %enable_x11_fx_mess
	X11_GLIDE=1 \
%endif
        XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=x11 \
	CC=gcc
%endif

#Xmess - SDL target without 68k asm support
%if %buildSDLmess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
        XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=SDL \
	CC=gcc
%endif
#SOUND_SDL=1 JOY_SDL=1 \

#Xmess -  svgalib target without 68k asm support
%if %buildsvgalibmess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
        XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=svgalib \
	CC=gcc
%endif

#Xmess - Glide/svgalib target without 68k asm support
%if %buildsvgafxmess
%make -f makefile.unix PREFIX=%{_prefix} TARGET=mess \
        XMAMEROOT=%{_gamesdatadir}/xmess \
	DISPLAY_METHOD=svgafx \
	CC=gcc
%endif

%install

#xmame
rm -rf %buildroot
mkdir -p %buildroot%{_gamesdatadir}/%{name}/{roms,cab,samples,artwork} \
	%buildroot%{_mandir}/man6 \
	%buildroot%{_bindir} \
	%buildroot%{_gamesdatadir}/%{name}/rc \
	%buildroot%{_iconsdir} \
	%buildroot%{_liconsdir} \
	%buildroot%{_miconsdir} \
	%buildroot%{_menudir} \
	%buildroot%{_gamesbindir}

#installing the free roms
cp %{SOURCE10} %buildroot%{_gamesdatadir}/%{name}/roms
cp %{SOURCE11} %buildroot%{_gamesdatadir}/%{name}/roms
cp %{SOURCE12} %buildroot%{_gamesdatadir}/%{name}/roms
cp %{SOURCE13} %buildroot%{_gamesdatadir}/%{name}/samples/gridlee.zip

# the man pages
install -m 644 doc/xmame.6 %buildroot%{_mandir}/man6/

#xmess
mkdir -p %buildroot%{_gamesdatadir}/xmess/{bios,hash,cheat,software,sysinfo} \
	%buildroot%{_gamesdatadir}/xmess/rc
install -m 644 hash/* %buildroot%{_gamesdatadir}/xmess/hash
install -m 644 doc/mess/sysinfo.dat %buildroot%{_gamesdatadir}/xmess/sysinfo
install -m 644 doc/xmess.6 %buildroot%{_mandir}/man6/

#xmame/xmess tools
install -d -m 755 %buildroot%{_bindir}
install -m 755 romcmp %buildroot%{_bindir}/
install -m 755 chdman %buildroot%{_bindir}/
install -m 755 imgtool %buildroot%{_bindir}/
install -m 755 xml2info %buildroot%{_bindir}/
install -m 755 jedutil %buildroot%{_bindir}/

# with 68k asm
%if %enable_68k_asm
# Xmame binaries
%if %buildSDLmame
install -m  755 %{name}.SDL-68k %buildroot%{_gamesbindir}
%endif

%if %buildx11mame
install -m 4755 %{name}.x11-68k %buildroot%{_gamesbindir}
%endif

%if %buildsvgalibmame
install -m 4755 %{name}.svgalib-68k %buildroot%{_gamesbindir}
%endif

%if %buildsvgafxmame
install -m 4755 %{name}.svgafx-68k %buildroot%{_gamesbindir}
%endif

#Xmess binaries
%if %buildSDLmess
install -m  755 xmess.SDL-68k %buildroot%{_gamesbindir}
%endif

%if %buildx11mess
install -m 4755 xmess.x11-68k %buildroot%{_gamesbindir}
%endif

%if %buildsvgalibmess
install -m 4755 xmess.svgalib-68k %buildroot%{_gamesbindir}
%endif

%if %buildsvgafxmess
install -m 4755 xmess.svgafx-68k %buildroot%{_gamesbindir}
%endif
%endif

#without 68k asm
# Xmame binaries
%if %buildSDLmame
install -m  755 %{name}.SDL %buildroot%{_gamesbindir}
%endif

%if %buildx11mame
install -m 4755 %{name}.x11 %buildroot%{_gamesbindir}
%endif

%if %buildsvgalibmame
install -m 4755 %{name}.svgalib %buildroot%{_gamesbindir}
%endif

%if %buildsvgafxmame
install -m 4755 %{name}.svgafx %buildroot%{_gamesbindir}
%endif

#Xmess binaries
%if %buildSDLmess
install -m  755 xmess.SDL %buildroot%{_gamesbindir}
%endif

%if %buildx11mess
install -m 4755 xmess.x11 %buildroot%{_gamesbindir}
%endif

%if %buildsvgalibmess
install -m 4755 xmess.svgalib %buildroot%{_gamesbindir}
%endif

%if %buildsvgafxmess
install -m 4755 xmess.svgafx %buildroot%{_gamesbindir}
%endif

# xmame-screensaver from contrib/tools
install -m 755 contrib/tools/xmame-screensaver %buildroot%{_bindir}

# the cab files
make -f makefile.unix XMAMEROOT=%buildroot%{_gamesdatadir}/%{name} copycab INSTALL_GROUP=`id -g` INSTALL_USER=$USER

install -m 644 ./doc/xmamerc.dist %buildroot%{_gamesdatadir}/%{name}/xmame-x11rc
install -m 644 ./cheat.dat %buildroot%{_gamesdatadir}/%{name}/cheat.dat
install -m 644 ./history.dat %buildroot%{_gamesdatadir}/%{name}/history.dat
# install -m 644 ./driverinfo.dat %buildroot%{_gamesdatadir}/%{name}/driverinfo.dat
install -m 644 ./mameinfo.dat %buildroot%{_gamesdatadir}/%{name}/mameinfo.dat
install -m 644 ./hiscore.dat  %buildroot%{_gamesdatadir}/%{name}/hiscore.dat
install -m 644 ./Catver.ini %buildroot%{_gamesdatadir}/%{name}/catver.ini
#install contrib/frontends/mamex.new %buildroot%{_bindir}/mamex #mamex.new is v1.2 as mamex is v2
install contrib/frontends/mamex %buildroot%{_bindir}/mamex


# icons
install -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_iconsdir/%name.png
install -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

#install xmess
install -m 644 %SOURCE5 %buildroot%_miconsdir/xmess.png
install -m 644 %SOURCE6 %buildroot%_iconsdir/xmess.png
install -m 644 %SOURCE7 %buildroot%_liconsdir/xmess.png

install -m 644 ./doc/xmessrc.dist %buildroot%{_gamesdatadir}/xmess/xmess-x11rc

# rc files
tar xvjf %{SOURCE4} -C %buildroot%{_gamesdatadir}/%{name}
#touch %buildroot%{_gamesdatadir}/%{name}/xmame-xfxrc
touch %buildroot%{_gamesdatadir}/%{name}/xmame-svgafxrc

# Xmame menu entries
%if %mdkversion < 1000 
%define menusection "More applications/Emulators"
%else 
%define menusection "More Applications/Emulators"
%endif

# x11 target
%if %buildx11mame
cat << EOF > %buildroot%{_menudir}/%{name}-x11
?package(%{name}-x11):command="%{_gamesbindir}/%{name}.x11" \
	icon="%{name}.png" \
	needs="X11" \
	section=%{menusection} \
	title="Xmame (X11)" \
	longtitle="Arcade emulator" \
	xdg="true"
EOF

mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-x11.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Xmame (X11)
Comment=Arcade emulator
Exec=%{_gamesbindir}/%{name}.x11
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Emulator;X-Mandrakelinux-MoreApplications-Emulators;
EOF
%endif

# svgalib / svgafx targets : no menu entries for commandline...

# xgl target
#if %enable_x11_gl_mame
#ln -sf %{_gamesdatadir}/%{name}/cab %buildroot%{_sysconfdir}/%{name}/cab
#endif

# SDL target
%if %buildSDLmame
cat << EOF > %buildroot%{_menudir}/%{name}-SDL
?package(%{name}-SDL):command="%{_gamesbindir}/%{name}.SDL" \
	icon="%{name}.png" \
	needs="X11" \
	section=%{menusection} \
	title="Xmame (SDL)" \
	longtitle="Arcade emulator" \
	xdg="true"
EOF

if [ ! -e $RPM_BUILD_ROOT%{_datadir}/applications ]; then
        mkdir $RPM_BUILD_ROOT%{_datadir}/applications
fi
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-SDL.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Xmame (SDL)
Comment=Arcade emulator
Exec=%{_gamesbindir}/%{name}.SDL
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Emulator;X-Mandrakelinux-MoreApplications-Emulators;
EOF
%endif


# Xmess menu entries
# x11 target
%if %buildx11mess
cat << EOF > %buildroot%{_menudir}/xmess-x11
?package(xmess-x11):command="%{_gamesbindir}/xmess.x11" \
	icon="xmess.png" \
	needs="X11" \
	section=%{menusection} \
	title="Xmess (X11)" \
	longtitle="Computer - Console emulator" \
	xdg="true"
EOF

if [ ! -e $RPM_BUILD_ROOT%{_datadir}/applications ]; then
        mkdir $RPM_BUILD_ROOT%{_datadir}/applications
fi
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-xmess-x11.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Xmess (X11)
Comment=Computer - Console emulator
Exec=%{_gamesbindir}/xmess.x11
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Emulator;X-Mandrakelinux-MoreApplications-Emulators;
EOF
%endif

# svgalib / svgafx targets : no menu entries for commandline...

# SDL target
%if %buildSDLmess
cat << EOF > %buildroot%{_menudir}/xmess-SDL
?package(xmess-SDL):command="%{_gamesbindir}/xmess.SDL" \
	icon="xmess.png" \
	needs="X11" \
	section=%{menusection} \
	title="Xmess (SDL)" \
	longtitle="Computer - Console emulator" \
	xdg="true"
EOF

if [ ! -e $RPM_BUILD_ROOT%{_datadir}/applications ]; then
	mkdir $RPM_BUILD_ROOT%{_datadir}/applications
fi
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-xmess-SDL.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Xmess (SDL)
Comment=Computer - Console emulator
Exec=%{_gamesbindir}/xmess.SDL
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Emulator;X-Mandrakelinux-MoreApplications-Emulators;
EOF
%endif

# don't know what to do with these yet
# xmame-screensaver does not seem to work
#rm %buildroot%{_bindir}/xmame-screensaver
# I have to check why there is such a file there
#rm %buildroot/usr/share/games/xmame/xmame-x11rc

# Xmame rc's
%if %buildx11mame
%else
rm %buildroot%{_gamesdatadir}/%{name}/xmame-x11rc
%endif

%if %buildsvgalibmame
%else
rm %buildroot%{_gamesdatadir}/%{name}/xmame-svgalibrc
%endif

%if %buildSDLmame
%else
rm %buildroot%{_gamesdatadir}/%{name}/xmame-SDLrc
%endif

%if %buildsvgafxmame
%else
rm %buildroot%{_gamesdatadir}/%{name}/xmame-svgafxrc
%endif

# Xmess rc's
%if %buildx11mess
%else
#rm %buildroot%{_gamesdatadir}/xmess/xmess-x11rc
%endif

%if %buildsvgalibmess
%else
#rm %buildroot%{_gamesdatadir}/xmess/xmess-svgalibrc
%endif
%if %buildSDLmess
%else
#rm %buildroot%{_gamesdatadir}/xmess/xmess-SDLrc
%endif

%if %buildsvgafxmess
%else
#rm %buildroot%{_gamesdatadir}/xmess/xmess-svgafxrc
%endif

cat > ReadMe.%{name} <<EOF
Complete docs are in /usr/share/doc/%{name}-%{version}
EOF

cat > ReadMe.xmess <<EOF
Complete docs are in /usr/share/doc/xmess-%{version}
EOF

export DONT_STRIP=1

# xmame tools
#
%files -n %{name}-tools
%defattr(-,root,root)
%doc ReadMe.%{name}
%attr(755,root,games) %{_bindir}/romcmp
%attr(755,root,games) %{_bindir}/chdman
%attr(755,root,games) %{_bindir}/imgtool
%attr(755,root,games) %{_bindir}/xml2info
%attr(755,root,games) %{_bindir}/jedutil

# xmame base
#
%files -n %{name}-base
%defattr(0644,root,root,0755)
%doc doc/*
%dir               %{_gamesdatadir}/%{name}
%dir               %{_gamesdatadir}/%{name}/rc
%config(noreplace) %{_gamesdatadir}/%{name}/rc/*
%attr(755,root,games) %{_bindir}/mamex
#dir %{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/roms
%dir %{_gamesdatadir}/%{name}/samples
%dir %{_gamesdatadir}/%{name}/artwork
%attr(644,root,games) %{_gamesdatadir}/%{name}/roms/*
%attr(644,root,games) %{_gamesdatadir}/%{name}/samples/*
%{_gamesdatadir}/%{name}/cheat.dat
%{_gamesdatadir}/%{name}/history.dat
%{_gamesdatadir}/%{name}/hiscore.dat
%{_gamesdatadir}/%{name}/mameinfo.dat
%{_gamesdatadir}/%{name}/catver.ini
#%{_gamesdatadir}/%{name}/driverinfo.dat
%attr(644,root,root) %{_liconsdir}/%{name}.png
%attr(644,root,root) %{_miconsdir}/%{name}.png
%attr(644,root,root) %{_iconsdir}/%{name}.png
%attr(644,root,man) %{_mandir}/man6/%{name}.*

# xmess base
#
%files -n xmess-base
%defattr(0644,root,root,0755)
%doc doc/*
%dir               %{_gamesdatadir}/xmess
#%dir               %{_gamesdatadir}/xmess/rc
#%config(noreplace) %{_gamesdatadir}/xmess/rc/*
#%attr(755,root,games) %{_bindir}/mamex
#dir %{_gamesdatadir}/xmess
%dir %{_gamesdatadir}/xmess/bios
%dir %{_gamesdatadir}/xmess/cheat
%dir %{_gamesdatadir}/xmess/hash
%dir %{_gamesdatadir}/xmess/software
%dir %{_gamesdatadir}/xmess/sysinfo
%attr(644,root,games) %{_gamesdatadir}/xmess/sysinfo/sysinfo.dat
%attr(644,root,games) %{_gamesdatadir}/xmess/hash/*
%attr(644,root,games) %{_gamesdatadir}/xmess/xmess-x11rc
#%attr(644,root,games) %{_gamesdatadir}/xmess/roms/*
#%attr(644,root,games) %{_gamesdatadir}/xmess/samples/*
#%{_gamesdatadir}/xmess/cheat.dat
#%{_gamesdatadir}/xmess/history.dat
#%{_gamesdatadir}/xmess/hiscore.dat
#%{_gamesdatadir}/xmess/mameinfo.dat
%attr(644,root,root) %{_liconsdir}/xmess.png
%attr(644,root,root) %{_miconsdir}/xmess.png
%attr(644,root,root) %{_iconsdir}/xmess.png
%attr(644,root,man) %{_mandir}/man6/xmess.*

# Xmame alternatives , post, postun, files
# x11 target
#
%if %buildx11mame
%post -n %{name}-x11
%{update_menus}
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.x11-68k 9
%endif
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.x11     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/%{name} ] || update-alternatives --auto %{name}
update-alternatives --auto %{name}

%postun -n %{name}-x11
%{clean_menus}
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.x11-68k
%endif
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.x11
  update-alternatives --auto %{name}
fi

%files -n %{name}-x11
%defattr(-,root,root)
%doc ReadMe.%{name}
%config(noreplace) %{_gamesdatadir}/%{name}/xmame-x11rc
%attr(-,root,games) %{_gamesbindir}/xmame.x11*
# %attr(-,root,games) %{_bindir}/xmame-screensaver
%attr(644,root,root) %{_menudir}/%{name}-x11
%{_datadir}/applications/mandriva-%{name}-x11.desktop
# OpenGL only?
%if %enable_x11_gl_mame
%dir %{_gamesdatadir}/%{name}/cab
%{_gamesdatadir}/%{name}/cab/*
#{_sysconfdir}/%{name}/cab
%endif
%endif

# svgalib target
#
%if %buildsvgalibmame
%post -n %{name}-svgalib
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.svgalib-68k 9
%endif
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.svgalib     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/%{name} ] || update-alternatives --auto %{name}
update-alternatives --auto %{name}

%postun -n %{name}-svgalib
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.svgalib-68k
%endif
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.svgalib
  update-alternatives --auto %{name}
fi

%files -n %{name}-svgalib
%defattr(-,root,root)
%doc ReadMe.%{name}
%dir               %{_gamesdatadir}/%{name}
%config(noreplace) %{_gamesdatadir}/%{name}/xmame-svgalibrc
%attr(-,root,games) %{_gamesbindir}/xmame.svgalib*
%endif

# SDL target
#
%if %buildSDLmame
%post -n %{name}-SDL
%{update_menus}
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.SDL-68k 9
%endif
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.SDL     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/%{name} ] || update-alternatives --auto %{name}
update-alternatives --auto %{name}

%postun -n %{name}-SDL
%{clean_menus}
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.SDL-68k
%endif
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.SDL
  update-alternatives --auto %{name}
fi

%files -n %{name}-SDL
%defattr(-,root,root)
%doc ReadMe.%{name}
#dir               %{_gamesdatadir}/%{name}
%config(noreplace) %{_gamesdatadir}/%{name}/xmame-SDLrc
%attr(-,root,games) %{_gamesbindir}/xmame.SDL*
%attr(644,root,root) %{_menudir}/%{name}-SDL
%{_datadir}/applications/mandriva-%{name}-SDL.desktop
%{_bindir}/xmame-screensaver
%endif

# Glide/svgalib target
#
%if %buildsvgafxmame
%post -n %{name}-svgafx
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.svgafx-68k 9
%endif
update-alternatives --install %{_gamesbindir}/%{name} %{name} %{_gamesbindir}/%{name}.svgafx     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/%{name} ] || update-alternatives --auto %{name}
update-alternatives --auto %{name}

%postun -n %{name}-svgafx
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.svgafx-68k
%endif
  update-alternatives --remove %{name} %{_gamesbindir}/%{name}.svgafx
  update-alternatives --auto %{name}
fi

%files -n %{name}-svgafx
%defattr(-,root,root)
%doc ReadMe.%{name}
%dir               %{_gamesdatadir}/%{name}
%config(noreplace) %{_gamesdatadir}/%{name}/xmame-svgafxrc
%attr(-,root,games) %{_gamesbindir}/xmame.svgafx*
%endif

# Xmess alternatives , post, postun, files
# x11 target
#
%if %buildx11mess
%post -n xmess-x11
%{update_menus}
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.x11-68k 9
%endif
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.x11     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/xmess ] || update-alternatives --auto xmess
update-alternatives --auto xmess

%postun -n xmess-x11
%{clean_menus}
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove xmess %{_gamesbindir}/xmess.x11-68k
%endif
  update-alternatives --remove xmess %{_gamesbindir}/xmess.x11
  update-alternatives --auto xmess
fi

%files -n xmess-x11
%defattr(-,root,root)
%doc ReadMe.xmess
#%dir               %{_gamesdatadir}/xmess
#%config(noreplace) %{_gamesdatadir}/xmess/xmess-x11rc
%attr(-,root,games) %{_gamesbindir}/xmess.x11*
%attr(644,root,root) %{_menudir}/xmess-x11
%{_datadir}/applications/mandriva-xmess-x11.desktop
%endif

# svgalib target
#
%if %buildsvgalibmess
%post -n xmess-svgalib
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.svgalib-68k 9
%endif
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.svgalib     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/xmess ] || update-alternatives --auto xmess
update-alternatives --auto xmess

%postun -n xmess-svgalib
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove xmess %{_gamesbindir}/xmess.svgalib-68k
%endif
  update-alternatives --remove xmess %{_gamesbindir}/xmess.svgalib
  update-alternatives --auto xmess
fi

%files -n xmess-svgalib
%defattr(-,root,root)
%doc ReadMe.xmess
#%dir               %{_gamesdatadir}/xmess
#%config(noreplace) %{_gamesdatadir}/xmess/xmess-svgalibrc
%attr(-,root,games) %{_gamesbindir}/xmess.svgalib*
%endif

# SDL target
#
%if %buildSDLmess
%post -n xmess-SDL
%{update_menus}
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.SDL-68k 9
%endif
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.SDL     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/xmess ] || update-alternatives --auto xmess
update-alternatives --auto xmess

%postun -n xmess-SDL
%{clean_menus}
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove xmess %{_gamesbindir}/xmess.SDL-68k
%endif
  update-alternatives --remove xmess %{_gamesbindir}/xmess.SDL
  update-alternatives --auto xmess
fi

%files -n xmess-SDL
%defattr(-,root,root)
%doc ReadMe.xmess
#%dir               %{_gamesdatadir}/xmess
#%config(noreplace) %{_gamesdatadir}/xmess/xmame-SDLrc
%attr(-,root,games) %{_gamesbindir}/xmess.SDL*
%attr(644,root,root) %{_menudir}/xmess-SDL
%{_datadir}/applications/mandriva-xmess-SDL.desktop
%endif

# Glide/svgalib target
#
%if %buildsvgafxmess
%post -n xmess-svgafx
%if %enable_68k_asm
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.svgafx-68k 9
%endif
update-alternatives --install %{_gamesbindir}/xmess xmess %{_gamesbindir}/xmess.svgafx     10
# without the following, the group stays in default manual mode,
#  and no link is created
#[ -e %{_gamesbindir}/xmess ] || update-alternatives --auto xmess
update-alternatives --auto xmess

%postun -n xmess-svgafx
if [ "$1" = 0 ]; then
  # Remove update-alternatives entries
%if %enable_68k_asm
  update-alternatives --remove xmess %{_gamesbindir}/xmess.svgafx-68k
%endif
  update-alternatives --remove xmess %{_gamesbindir}/xmess.svgafx
  update-alternatives --auto xmess
fi

%files -n xmess-svgafx
%defattr(-,root,root)
%doc ReadMe.xmess
#%dir               %{_gamesdatadir}/xmess
#%config(noreplace) %{_gamesdatadir}/xmess/xmess-svgafxrc
%attr(-,root,games) %{_gamesbindir}/xmess.svgafx*
%endif

%clean
rm -rf %buildroot

