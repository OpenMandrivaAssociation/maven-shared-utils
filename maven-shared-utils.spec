Name:		maven-shared-utils
Version:	3.5.0
Release:	1
Summary:	Shared utility classes for Maven
Group:		Development/Java
License:	ASL 2.0
URL:		https://maven.apache.org/shared/maven-shared-utils/
Source0:	https://github.com/apache/maven-shared-utils/archive/refs/tags/maven-shared-utils-%{version}.tar.gz#/maven-shared-utils-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	mvn(org.apache:apache:pom::)
BuildRequires:	mvn(org.apache.maven:maven-parent:pom::)
BuildRequires:	mvn(org.apache.maven.shared:maven-shared-components:pom::)
BuildRequires:	mvn(org.slf4j:slf4j-api)
BuildRequires:	mvn(commons-io:commons-io)
# Optional, so the dependency generator skips it, but the main sources import it.
BuildRequires:	mvn(org.fusesource.jansi:jansi)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
Shared utility classes used by Maven core and plugins.
3.5.0 is the first release since 3.4.2. The Java 8 and Maven 3
baseline is unchanged. It fixes process handling, string and path
helpers, and copying a symbolic link whose target is missing.
Commandline and Shell no longer implement Cloneable.
Tests are skipped.

%prep
%setup -q -n maven-shared-utils-maven-shared-utils-%{version}

%files -f .mfiles
%doc LICENSE README.md
