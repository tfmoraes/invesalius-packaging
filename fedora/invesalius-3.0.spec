Name:           invesalius
Version:        3.0.0.beta1
Release:        1%{?dist}
Summary:        InVesalius: 3D medical imaging reconstruction software

Group:          Amusements/Graphics
License:        GPLv2
URL:            http://svn.softwarepublico.gov.br/trac/invesalius
Source0:        invesalius-3.0.0.beta1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python
Requires:       python

%description
 InVesalius generates 3D medical imaging reconstructions based on a sequence of
 2D DICOM files acquired with CT or MRI equipments.  InVesalius is
 internationalized (currently available in English, Portuguese, French and
 Spanish), multi-platform (GNU Linux, Windows and MacOS) and provides several
 tools:

  * DICOM-support including: (a) ACR-NEMA version 1 and 2; (b) DICOM version
  3.0 (including various encodings of JPEG -lossless and lossy-, RLE)

  * Image manipulation facilities (zoom, pan, rotation, brightness/contrast,
  etc)

  * Segmentation based on 2D slices

  * Pre-defined threshold ranges according to tissue of interest

  * Edition tools (similar to Paint Brush) based on 2D slices

  * 3D surface creation

  * 3D surface connectivity tools 

  * 3D surface exportation (including: binary STL, OBJ, VRML, Inventor)

  * High-quality volume rendering projection

  * Pre-defined volume rendering presets

  * Volume rendering crop plane

  * Picture exportation (including: BMP, TIFF, JPG, PostScript, POV-Ray)

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/invesalius-3.0
%{_datadir}/invesalius-3.0/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%doc



%changelog
