Name:		texlive-wrapfig2
Version:	69513
Release:	1
Summary:	Wrap text around figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wrapfig2
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig2.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig2.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a fork of Donald Arseneau's wrapfig package. It
is backwards compatible with the original environments.
Therefore this package does not work with LaTeX2e kernels older
than about 2018, although a warning is issued if the LaTeX
format file is dated with a date older than 1st January 2019.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/wrapfig2
%{_texmfdistdir}/tex/latex/wrapfig2
%doc %{_texmfdistdir}/doc/latex/wrapfig2

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
