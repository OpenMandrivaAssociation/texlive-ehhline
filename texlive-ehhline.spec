%global tl_name ehhline
%global tl_revision 54676

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Extend the \hhline command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ehhline
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ehhline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ehhline.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package extends the \hhline command with a !{...} token, which
allows to create lines with arbitrary LaTeX commands.

