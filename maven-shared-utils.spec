Name:           maven-shared-utils
Version:        3.4.2
Release:        1
Summary:        Maven shared utility classes
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-shared-utils
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch:          0001-Avoid-setting-POSIX-attributes-for-symbolic-links.patch

BuildRequires:  javapackages-bootstrap

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%prep
%autosetup -p1 -C

find -name '*.java' -exec sed -i 's/\r//' {} +


%pom_remove_dep org.apache.commons:commons-text
rm src/test/java/org/apache/maven/shared/utils/CaseTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
