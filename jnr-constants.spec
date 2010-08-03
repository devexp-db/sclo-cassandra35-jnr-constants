Name:           jnr-constants
Version:        0.7
Release:        2%{?dist}
Summary:        Java Native Runtime constants 
Group:          Development/Libraries
License:        MIT
URL:            http://github.com/wmeissner/jnr-constants/
Source0:        http://download.github.com/wmeissner-jnr-constants-0.7-0-g8b45ca7.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant jar

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}

# project was renamed from 'constantine' to jnr-constants, but jar has
# yet to be renamed http://fedoraproject.org/wiki/Packaging/Java#Jar_file_naming
cp -p dist/constantine.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/constantine.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/constantine.jar

%changelog
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

