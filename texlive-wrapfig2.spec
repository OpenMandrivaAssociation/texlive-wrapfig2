%global tl_name wrapfig2
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.0.2
Release:	%{tl_revision}.1
Summary:	Wrap text around figures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wrapfig2
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig2.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig2.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(float)
Requires:	texlive(pict2e)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is a fork of Donald Arseneau's wrapfig package. It is
backwards compatible with the original environments. Therefore this
package does not work with LaTeX2e kernels older than about 2018,
although a warning is issued if the LaTeX format file is dated with a
date older than 1st January 2019.

