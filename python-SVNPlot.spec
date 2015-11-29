%define _name	svnplot

%define	module	SVNPlot
Summary:	Python module to generate graphs and statistics from Subversion repository data
Name:		python-%{module}
Version:	0.7.6
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://svnplot.googlecode.com/files/%{module}-%{version}.zip
# Source0-md5:	9db5d2d3862d77c3f7b55538a19ff693
URL:		http://code.google.com/p/svnplot/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python
Requires:	python-matplotlib
Requires:	python-pysvn
Requires:	python-modules-sqlite
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to generate graphs and statistics from Subversion
repository data.

%prep
%setup  -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{_name}
%{py_sitescriptdir}/%{_name}/*.py[co]
%{py_sitescriptdir}/%{_name}/javascript
%{py_sitescriptdir}/%{module}-*.egg-info
