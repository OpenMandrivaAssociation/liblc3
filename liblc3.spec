%define major 1

%define libname %mklibname liblc3
%define devname %mklibname -d liblc3

Name:           liblc3
Version:        1.0.4
Release:        1
Summary:        Low Complexity Communication Codec (LC3)
License:        Apache-2.0
Group:          System/Sound
URL:            https://github.com/google/liblc3
Source:         https://github.com/google/liblc3/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig

%description
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

%package -n %{libname}
Summary:        Low Complexity Communication Codec (LC3) - Shared library

%description -n %{libname}
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

This package provides the shared library of %{name}.

%package        tools
Summary:        Low Complexity Communication Codec (LC3) - Tools
Requires:	%{libname} = %{EVRD}

%description    tools
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

This package provides tools for %{name}.

%package -n %{devname}
Summary:        Low Complexity Communication Codec (LC3) - Development Files
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

This package provides all the necessary files for development with
%{name}.

%prep
%autosetup -p1

%build
%meson \
	--includedir=%{_includedir}/%{name} \
	-Dtools=true
%meson_build

%install
%meson_install

%files -n %{libname}
%license LICENSE
%{_libdir}/liblc3.so.%{major}*

%files tools
%{_bindir}/dlc3
%{_bindir}/elc3

%files -n %{devname}
%doc README.md
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lc3.pc
%{_libdir}/liblc3.so
