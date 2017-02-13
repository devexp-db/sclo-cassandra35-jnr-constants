%{?scl:%scl_package jnr-constants}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jnr-constants
Version:	0.9.6
Release:	3%{?dist}
Summary:	Java Native Runtime constants
License:	ASL 2.0
URL:		http://github.com/jnr/%{pkg_name}/
Source0:	https://github.com/jnr/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	%{?scl_prefix_java_common}junit
BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:	%{?scl_prefix_maven}maven-source-plugin
BuildRequires:	%{?scl_prefix_maven}sonatype-oss-parent
%{?scl:Requires: %scl_runtime}

%description
Provides java values for common platform C constants (e.g. errno).

%package javadoc
Summary:	Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_file : %{pkg_name}/%{pkg_name} %{pkg_name} constantine
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Feb 13 2017 Tomas Repik <trepik@redhat.com> - 0.9.6-3
- scl conversion

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.9.6-1
- Update to upstream 0.9.6.

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 0.9.2-2
- Add missing BuildRequires to fix FTBFS (BZ#1405569).

* Thu May 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.9.2-1
- Update to upstream 0.9.2 release.

* Mon Apr 18 2016 Alexander Kurtakov <akurtako@redhat.com> 0.9.1-1
- Update to upstream 0.9.1 with osgification.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Alexander Kurtakov <akurtako@redhat.com> 0.9.0-1
- Update to upstream 0.9.0.

* Thu Jun 18 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8.8-2
- Add MANIFEST.MF.

* Tue Jun 16 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8.8-1
- Update to upstream 0.8.8.
- Switch to mvn() style BRs.

* Mon May 11 2015 Michal Srb <msrb@redhat.com> - 0.8.7-2
- Restore symlinks for backward compatibility

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8.7-1
- Update to upstream 0.8.7.

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
