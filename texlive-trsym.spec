# revision 18732
# category Package
# catalog-ctan /fonts/trsym
# catalog-date 2007-10-24 18:05:15 +0200
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-trsym
Version:	1.0
Release:	1
Summary:	Symbols for transformations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/trsym
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trsym.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
