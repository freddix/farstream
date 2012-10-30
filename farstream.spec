%include	/usr/lib/rpm/macros.gstreamer

Summary:	Audio/Video Communications Framework
Name:		farstream
Version:	0.2.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://freedesktop.org/software/farstream/releases/farstream/%{name}-%{version}.tar.gz
# Source0-md5:	479c42adf5cc606abcb47d58ed542414
URL:		http://www.freedesktop.org/wiki/Software/Farstream
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	gupnp-igd-devel
BuildRequires:	libnice-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Farstream (formerly Farsight) project is an effort to create a
framework to deal with all known audio/video conferencing protocols.
On one side it offers a generic API that makes it possible to write
plugins for different streaming protocols, on the other side it offers
an API for clients to use those plugins.

The main target clients for Farstream are Instant Messaging
applications. These applications should be able to use Farstream for
all their Audio/Video conferencing needs without having to worry about
any of the lower level streaming and NAT traversal issues.

%package devel
Summary:	Header files for Farstream library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Farstream library.

%package apidocs
Summary:	Farstream API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for Farstream library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--disable-silent-rules	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libfarstream-0.2.so.2
%attr(755,root,root) %{_libdir}/libfarstream-0.2.so.*.*.*
%{_libdir}/girepository-1.0/Farstream-0.2.typelib

%dir %{_libdir}/farstream-0.2
%attr(755,root,root) %{_libdir}/farstream-0.2/libmulticast-transmitter.so
%attr(755,root,root) %{_libdir}/farstream-0.2/libnice-transmitter.so
%attr(755,root,root) %{_libdir}/farstream-0.2/librawudp-transmitter.so
%attr(755,root,root) %{_libdir}/farstream-0.2/libshm-transmitter.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libfsmsnconference.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libfsrawconference.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libfsrtcpfilter.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libfsrtpconference.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libfsvideoanyrate.so
%{_datadir}/farstream

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfarstream-0.2.so
%{_datadir}/gir-1.0/Farstream-0.2.gir
%{_includedir}/farstream-0.2
%{_pkgconfigdir}/farstream-0.2.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/farstream-libs-1.0
%{_gtkdocdir}/farstream-plugins-0.2

