Summary: NethServer Dummy RPM
Name: nethserver-dummy-rpm
Version: 1.0.7
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-base
BuildRequires: nethserver-devtools 

%description
NethServer dummy rpm package.

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Oct 04 2022 Tommaso Bailetti <tommaso.bailetti@nethesis.it> - 1.0.7-1
- Enable RPM build on GitHub Actions - NethServer/dev#6700

* Fri Sep 30 2022 Tommaso Bailetti <tommaso.bailetti@nethesis.it> - 1.0.6-1
- Enable RPM build on GitHub Actions - NethServer/dev#6700

* Fri Sep 30 2022 Tommaso Bailetti <tommaso.bailetti@nethesis.it> - 1.0.5-1
- Enable RPM build on GitHub Actions - NethServer/dev#6700

* Wed Sep 28 2022 Tommaso Bailetti <tommaso.bailetti@nethesis.it> - 1.0.4-1
- Enable RPM build on GitHub Actions - NethServer/dev#6700

* Wed Sep 21 2022 Tommaso Bailetti <tommaso.bailetti@nethesis.it> - 1.0.3-1
- Enable RPM build on GitHub Actions - NethServer/dev#6700

* Wed Sep 21 2022 Tommaso Bailetti <tommaso.bailetti@nethesis.it> - 1.0.2-1
- Enable RPM build on GitHub Actions - NethServer/dev#6700

