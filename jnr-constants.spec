Name:           jnr-constants
Version:        0.7
Release:        6%{?dist}
Summary:        Java Native Runtime constants 
Group:          Development/Libraries
License:        MIT
URL:            http://github.com/wmeissner/jnr-constants/
Source0:        http://download.github.com/wmeissner-jnr-constants-0.7-0-g8b45ca7.tar.gz
# remove wagon-svn & wagon-webdav deps
Patch0:         jnr-constants-0.7-pom_xml.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils

%description
Provides java values for common platform C constants (e.g. errno).

%prep
%setup -q -n wmeissner-%{name}-8b45ca7
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete
%patch0 -p0

%build
ant jar

%install

mkdir -p %{buildroot}%{_javadir}

# project was renamed from 'constantine' to jnr-constants, but jar has
# yet to be renamed http://fedoraproject.org/wiki/Packaging/Java#Jar_file_naming
cp -p dist/constantine.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/constantine.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_javadir}/constantine.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> 0.7-6
- add maven pom
- adapt to current guideline

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 02 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.7-2
- Fixed incorrect Source0 url

* Fri Jan 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.7-1
- Unorphaned / updated package

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 6 2008 Conrad Meyer <konrad@tylerc.org> - 0.4-2
- Include LICENSE in rpm.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 0.4-1
- Include symlink from non-versioned jar to versioned jar.
- Bump to 0.4.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 0.1-1
- Initial package (needed for jruby 1.1.5).

