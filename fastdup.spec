Name:		fastdup
Version:	0.3
Release:	1
Group:		Archiving/Backup
License:	GPLv3+
Summary:	Find copies of the same file
Url:		https://sourceforge.net/projects/fastdup/
Source0:	http://downloads.sourceforge.net/project/fastdup/fastdup/0.3%20alpha/fastdup-0.3.tar.bz2
Patch0:		fastdup-0.3-install-path.patch

%description
FastDup is a tool to find copies of the same file within directory tree(s),
designed for maximum speed and efficiency unlike most similar tools. Where
many similar tools rely on checksums or hashes of files, or simple comparisons,
fastdup uses a number of cleverly optimized tricks to reduce the number of
actual comparisons necessary, and as a result can scan large sets of data
extremely quickly compared to alternatives.

%prep
%setup -q
%patch0 -p1

%build
%make

%install
mkdir -p %{buildroot}/usr/bin
%makeinstall_std

%files
%{_bindir}/*
