%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-shared-utils
Version:        0.7
Release:        1.2
Summary:        Maven shared utility classes
Group:		Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-utils
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-rat
BuildRequires:  maven-shared
BuildRequires:  maven-shade-plugin

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%package javadoc
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

%build
# XXX temporarly skip running tests
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-1
- Update to upstream version 0.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.6-1
- Update to upstream version 0.6

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.5-2
- Fix unowned directory

* Mon Dec 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.5-1
- Update to upstream version 0.5
- Remove patch for MSHARED-285 (accepted upstream)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Tomas Radej <tradej@redhat.com> - 0.4-1
- Updated to latest upstream version
- Fixed and reenabled tests

* Mon Apr 08 2013 Michal Srb <msrb@redhat.com> - 0.3-2
- Disable tests (they don't work with junit >= 4.11)

* Fri Mar 15 2013 Michal Srb <msrb@redhat.com> - 0.3-1
- Update to upstream version 0.3

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.2-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Tomas Radej <tradej@redhat.com> - 0.2-1
- Initial version

