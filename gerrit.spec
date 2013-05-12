Summary:	Gerrit Code Review
Name:		gerrit
Version:	2.5.2
Release:	0.1
License:	Apache v2.0
Group:		Networking/Daemons/Java/Servlets
Source0:	http://gerrit.googlecode.com/files/%{name}-full-%{version}.war
# Source0-md5:	541d11d777b08f83f4ffd188da1eb1be
URL:		https://code.google.com/p/gerrit/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapp		%{name}
%define		_appdir		%{_datadir}/%{_webapp}

%description
Gerrit is a web based code review system, facilitating online code
reviews for projects using the Git version control system.

Gerrit makes reviews easier by showing changes in a side-by-side
display, and allowing inline comments to be added by any reviewer.

Gerrit simplifies Git based project maintainership by permitting any
authorized user to submit changes to the master Git repository, rather
than requiring all approved changes to be merged in by hand by the
project maintainer. This functionality enables a more centralized
usage of Git.

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sharedstatedir}/%{name}}
cp -a . $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%postun
%tomcat_clear_cache %{name}

%files
%defattr(644,root,root,755)
%dir %{_appdir}
%{_appdir}/META-INF
%{_appdir}/LICENSES.txt
%{_appdir}/Main.class
%{_appdir}/favicon.ico
%{_appdir}/robots.txt
%{_appdir}/com
%{_appdir}/gerrit

%dir %{_appdir}/WEB-INF
%dir %{_appdir}/WEB-INF/lib
%{_appdir}/WEB-INF/lib/*.jar
%{_appdir}/WEB-INF/deploy
%{_appdir}/WEB-INF/extra
%{_appdir}/WEB-INF/plugins

%attr(2775,root,servlet) %dir %{_sharedstatedir}/%{name}

%files doc
%defattr(644,root,root,755)
%{_appdir}/Documentation
