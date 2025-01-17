Name:		texlive-trsym
Version:	18732
Release:	2
Summary:	Symbols for transformations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/trsym
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides MetaFont sources for a small font used for
(e.g.) Laplace transformations, together with a LaTeX .fd file
and a package providing commands for the symbols' use in
mathematics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/trsym/trsy.mf
%{_texmfdistdir}/fonts/source/public/trsym/trsy10.mf
%{_texmfdistdir}/fonts/source/public/trsym/trsy12.mf
%{_texmfdistdir}/fonts/tfm/public/trsym/trsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/trsym/trsy12.tfm
%{_texmfdistdir}/tex/latex/trsym/trsym.sty
%{_texmfdistdir}/tex/latex/trsym/utrsy.fd
%doc %{_texmfdistdir}/doc/latex/trsym/README
%doc %{_texmfdistdir}/doc/latex/trsym/manifest.txt
%doc %{_texmfdistdir}/doc/latex/trsym/trsym.pdf
#- source
%doc %{_texmfdistdir}/source/latex/trsym/trsym.dtx
%doc %{_texmfdistdir}/source/latex/trsym/trsym.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
