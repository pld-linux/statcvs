# TODO
# - make package with ant?
# - javadoc subpackage
Summary:	Generate statistical HTML reports from your CVS repository logs
Summary(pl):	Generowanie statystycznych raportów HTML z logów repozytorium CVS
Name:		statcvs
Version:	0.2.2
Release:	0.2
Epoch:		0
License:	LGPL
Group:		Development/Libraries/Java
Source0:	http://dl.sourceforge.net/statcvs/%{name}-%{version}.zip
# Source0-md5:	99a0f04064d25c595b91972735a33c69
URL:		http://statcvs.sourceforge.net/
#BuildRequires:	ant >= 0:1.6
#BuildRequires:	ant-junit >= 0:1.6 
#BuildRequires:	java-devel >= 1.4
#BuildRequires:	jcommon >= 0:0.9.7
#BuildRequires:	jfreechart >= 0:0.9.20
#BuildRequires:	jpackage-utils >= 0:1.5.32
#BuildRequires:	junit >= 0:3.8.1
Requires:	cvs
#Requires:	java-devel >= 1.4
#Requires:	java-fonts
#Requires:	jcommon >= 0:0.9.7
#Requires:	jfreechart >= 0:0.9.20
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StatCvs retrieves information from a CVS repository and generates
various tables and charts describing the project development, e.g.
timeline for the lines of code, contribution of each developer etc.

%description -l pl
StatCvs wyci±ga informacje z repozytorium CVS i generuje ró¿ne tabele
i wykresy opisuj±ce rozwój projektu, np. liczbê linii kodu w
zale¿no¶ci od czasu, wk³ad ka¿dego programisty itp.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir}}

install %{name}.jar $RPM_BUILD_ROOT%{_javadir}

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << 'EOF'
#!/bin/sh
exec java -classpath %{_javadir}/statcvs.jar net.sf.statcvs.Main "$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
%{_javadir}/*
