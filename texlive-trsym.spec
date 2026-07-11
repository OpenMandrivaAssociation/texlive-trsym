%global tl_name trsym
%global tl_revision 18732

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Symbols for transformations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/trsym
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides Metafont source for a small font used for (e.g.)
Laplace transformations, together with a LaTeX .fd file and a package
providing commands for the symbols' use in mathematics.

