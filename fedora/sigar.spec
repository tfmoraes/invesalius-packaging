%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           sigar
Version:        1.7.0
Release:        1.20100310svn5287%{?dist}
Summary:        The Sigar API provides a portable interface for gathering system information

Group:          Development/Libraries
License:        GPL
URL:            http://support.hyperic.com/display/SIGAR/Home
Source0:        sigar-1.7.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc

%description
 The Sigar API provides a portable interface for gathering system information such as:
 
 * System memory, swap, cpu, load average, uptime, logins
 * Per-process memory, cpu, credential info, state, arguments, environment, open files
 * File system detection and metrics
 * Network interface detection, configuration info and metrics
 * TCP and UDP connection tables
 * Network route table
 
 This information is available in most operating systems, but each OS has their
 own way(s) providing it. SIGAR provides developers with one API to access this
 information regardless of the underlying platform. The core API is implemented
 in pure C with bindings currently implemented for Java, Perl, Ruby, Python,
 Erlang, PHP and C#.


%package python
Summary: Python bindings for sigar
BuildRequires:  python-devel
Requires:       python

%description python
 Python bindings for sigar


%package devel
Summary: sigar's headers files

%description devel
 Sigar's headers files
 
%prep
%setup -q


%build
%cmake .
make VERBOSE=1 %{?_smp_mflags}

pushd bindings/python
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

pushd bindings/python
%{__python} setup.py install --root %{buildroot} 


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%post python -p /sbin/ldconfig


%postun python -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSES EXCEPTIONS COPYING README
%{_libdir}/*.so


%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h



%files python
%defattr(-,root,root,-)
%{python_sitelib}/*


%changelog
* Wed Mar 10 2010 InVesalius <invesalius@cti.gov.br>
- Packaging sigar from svn revision 5287

