# Example spec file for cdplayer app...
#
Summary: EPEL Stub Package
Name: epel-release-stub
Version: 1.0
Release: 1
License: MIT
URL: https://docs.fedoraproject.org/en-US/epel/
Packager: Brent R. Scott <brs.scottworks@gmail.com>
BuildArch: noarch
Provides: epel-release

%description
This package only provides a dependency for Fedora Environment
to allow package that require epel-release to be installed.

%build

%files

%changelog
* Thu Nov 12 2026 Brent R. Scott <brs.scottworks@gmail.com> - 1.0-1
- Create initial EPEL release stub to satisfy unnecessary dependencies.
