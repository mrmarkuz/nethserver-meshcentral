Summary: nethserver-meshcentral sets up the MeshCentral remote monitoring server
%define name nethserver-meshcentral
Name: %{name}
%define version 0.0.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: rh-nodejs10,rh-mongodb36
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
NethServer MeshCentral configuration

%changelog

%pre
getent passwd meshcentral >/dev/null || useradd -r -d /opt/meshcentral -s /bin/bash meshcentral
#exit 0

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist

#mkdir -p %{buildroot}/opt/meshcentral
#cd %{buildroot}/opt/meshcentral
#scl enable rh-nodejs10 "npm update"
#scl enable rh-nodejs10 "npm install meshcentral"
#scl enable rh-nodejs10 "npm install mongodb"
#chown -R meshcentral:meshcentral %{buildroot}/opt/meshcentral

mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/opt/meshcentral/meshcentral-data

#mkdir -p %{buildroot}/etc/e-smith/events/nethserver-meshcentral-update

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a ui/* %{buildroot}/usr/share/cockpit/%{name}/

%{genfilelist} $RPM_BUILD_ROOT \
  --file /etc/sudoers.d/50_nsapi_nethserver_meshcentral 'attr(0440,root,root)' \
  --file /usr/libexec/nethserver/api/%{name}/read 'attr(775,root,root)' \
  --dir /opt/meshcentral/meshcentral-data 'attr(775,meshcentral,meshcentral)' \
> %{name}-%{version}-%{release}-filelist
# | grep -v '/opt/meshcentral/'
#exit 0

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
