%define		fversion	%(echo %{version} |tr r -)
%define		modulename	mlbench
Summary:	Machine Learning Benchmark Problems
Summary(pl):	Problemy wydajno¶ci uczenia maszyn
Name:		R-cran-%{modulename}
Version:	1.0r0
Release:	2
License:	Free for non-commercial purposes (see README and data sets help pages for details)
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	101108689bd005ef96641a8c33f17698
BuildRequires:	R-base >= 2.0.0
Provides:	R-mlbench
Obsoletes:	R-mlbench
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of artificial and real-world machine learning benchmark
problems, including, e.g., several data sets from the UCI repository.

%description -l pl
Ten podpakiet R zawiera zestaw sztucznych i prawdziwych problemów
wydajno¶ci uczenia maszyn, w tym kilka zbiorów danych z repozytorium
UCI.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,COPYING,NEWS,README}
%{_libdir}/R/library/%{modulename}
