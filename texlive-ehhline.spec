Name:		texlive-ehhline
Version:	54676
Release:	1
Summary:	Extend the \hhline command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ehhline
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ehhline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ehhline.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extends the \hhline command with a !{...} token,
which allows to create lines with arbitrary LaTeX commands.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ehhline
%doc %{_texmfdistdir}/doc/latex/ehhline

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
