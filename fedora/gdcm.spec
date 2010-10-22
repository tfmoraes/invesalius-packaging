Name:           gdcm
Version:        2.0.14
Release:        1%{?dist}
Summary:        Grassroots DICOM runtime libraries

Group:          Development/Libraries
License:        BSD
URL:            http://sourceforge.net/projects/gdcm/
Source0:        %{name}-%{version}.tar.bz2
Patch0:		python_dir_package.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  expat-devel
BuildRequires:  libuuid-devel
BuildRequires:  openjpeg-devel
BuildRequires:  python-devel
BuildRequires:  vtk-devel
BuildRequires:  zlib-devel

Requires:  expat
Requires:  libuuid
Requires:  openjpeg
Requires:  python
Requires:  vtk
Requires:  vtk-python
Requires:  zlib

%description
 Grassroots DiCoM is a C++ library for DICOM medical files. It is
 automatically wrapped to python/C#/Java (using swig). It supports
 RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated. It also
 comes with DICOM Part 3,6 & 7 of the standard as XML files.
 .
 This package contains the libraries needed to run GDCM applications.

%prep
%setup -q
%patch0 -p1


%build
mkdir %{_builddir}/gdcmbin
cd %{_builddir}/gdcmbin
cmake %{_builddir}/gdcm-%{version} \
	      -DCMAKE_INSTALL_PREFIX:STRING="%{_prefix}" \
	      -DCMAKE_SKIP_RPATH=ON \
	      -DGDCM_NO_EXECUTABLE_PROPERTIES=ON \
	      -DGDCM_BUILD_APPLICATIONS=OFF \
	      -DGDCM_DOCUMENTATION:BOOL=OFF \
	      -DGDCM_PDF_DOCUMENTATION:BOOL=OFF \
	      -DGDCM_BUILD_SHARED_LIBS=ON \
	      -DGDCM_WRAP_PYTHON=ON \
	      -DGDCM_WRAP_CSHARP=OFF \
	      -DGDCM_WRAP_JAVA=OFF \
	      -DGDCM_BUILD_TESTING:BOOL=OFF \
	      -DCMAKE_BUILD_TYPE:STRING=Release \
	      -DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
	      -DGDCM_USE_SYSTEM_UUID:BOOL=ON \
	      -DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
	      -DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
	      -DGDCM_USE_SYSTEM_OPENSSL:BOOL=OFF \
	      -DGDCM_USE_SYSTEM_POPPLER:BOOL=ON \
	      -DOPENJPEG_INCLUDE_DIR:PATH=%{_includedir}/openjpeg \
	      -DGDCM_USE_VTK:BOOL=ON \
	      -DVTK_DIR:PATH=/usr/lib/vtk-5.4

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/gdcmbin
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS README.txt INSTALL.txt Copyright.txt README.Copyright.txt
%{_datadir}/gdcm-2.0/*
%{_libdir}/lib*
%{_libdir}/gdcm-2.0/*
%{_libdir}/python2.6/site-packages/*
%{_includedir}/gdcm-2.0/*


%changelog
* Mon Mar 08 2010 InVesalius <invesalius@cti.gov.br> - 2.0.14-1
- gdcm-2.0.14

