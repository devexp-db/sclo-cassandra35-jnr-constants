%global commit_hash 2478e42 
%global tag_hash 2478e42 

Name:           jnr-constants
Version:        0.8.6
Release:        1%{?dist}
Summary:        Java Native Runtime constants 
Group:          Development/Libraries
License:        ASL 2.0
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit

%description
Provides java values for common platform C constants (e.g. errno).

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete
%mvn_file :jnr-constants constantine

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8.6-1
- Update to upstream 0.8.6.
- Start using mvn_install.

* Thu Jun 12 2014 Alexander Kurtakov <akurtako@redhat.com> 0.8.4-6
- Fix FTBFS.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.8.4-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.4-2
- Provide a constantine.jar simlink for gradle.

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.4-1
- Updated to version 0.8.4.
- Switch from ant to maven.

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
