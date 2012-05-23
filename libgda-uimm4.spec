#
# Conditional build:
%bcond_without	apidocs		# don't generate documentation with doxygen
%bcond_without	static_libs	# don't build static library
#
Summary:	C++ wrapper for libgda-ui 4.x
Summary(pl.UTF-8):	Interfejs C++ dla libgda-ui 4.x
Name:		libgda-uimm4
Version:	4.1.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgda-uimm/4.1/libgda-uimm-%{version}.tar.bz2
# Source0-md5:	2cb993c245790b9f66083557b8901f08
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	gtkmm-devel >= 2.18.0
BuildRequires:	libgda4-devel >= 4.2.0
BuildRequires:	libgda4-ui-devel >= 4.2.0
BuildRequires:	libgdamm4-devel >= 3.99.19
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.8
BuildRequires:	pkgconfig
Requires:	gtkmm >= 2.18.0
Requires:	libgda4 >= 4.2.0
Requires:	libgda4-ui >= 4.2.0
Requires:	libgdamm4 >= 3.99.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrapper for libgda-ui 4.x.

%description -l pl.UTF-8
Interfejs C++ dla libgda-ui 4.x.

%package devel
Summary:	Header files for libgda-uimm 4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgda-uimm 4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.18.0
Requires:	libgda4-devel >= 4.2.0
Requires:	libgda4-ui-devel >= 4.2.0
Requires:	libgdamm4-devel >= 3.99.19

%description devel
Header files for libgda-uimm 4 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgda-uimm 4.

%package static
Summary:	Static libgda-uimm 4 library
Summary(pl.UTF-8):	Statyczna biblioteka libgda-uimm 4
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgda-uimm 4 library.

%description static -l pl.UTF-8
Statyczna biblioteka libgda-uimm 4.

%package apidocs
Summary:	libgda-uimm 4 API documentation
Summary(pl.UTF-8):	Dokumentacja API libgda-uimm 4
Group:		Documentation

%description apidocs
libgda-uimm 4 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgda-uimm 4.

%prep
%setup -q -n libgda-uimm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	%{!?with_apidocs:--disable-documentation} \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdauimm-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdauimm-4.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdauimm-4.0.so
%{_libdir}/libgda-uimm-4.0
%{_includedir}/libgda-uimm-4.0
%{_includedir}/libgdauimm-4.0
%{_pkgconfigdir}/libgda-uimm-4.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdauimm-4.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/libgda-uimm-4.0
%{_docdir}/libgda-uimm-4.0
%endif
