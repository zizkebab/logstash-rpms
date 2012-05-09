%define debug_package %{nil}

Name:           logstash
Version:        1.1.0
Release:        1%{?dist}
Summary:        logstash is a tool for managing events and logs.

Group:          System Environment/Daemons
License:        Apache 2.0
URL:            http://logstash.net
Source0:        http://semicomplete.com/files/logstash/%{name}-%{version}-monolithic.jar
Source1:        etc-rc.d-init.d-logstash
Source2:        etc-logstash-logstash.conf
Source3:        etc-logstash-log4j.properties
Source4:        usr-sbin-logstash

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       java

Requires:       chkconfig initscripts

# disable jar repackaging
%define __os_install_post %{nil}

%description
logstash is a tool for managing events and logs. You can use it to collect logs, parse them, and store them for later use (like, for searching).

%prep
cp -p %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 .
find . -type f -print0 | xargs -0 --no-run-if-empty -- sed -i -e 's/@@@version@@@/%{version}/g'

%install
rm -rf "${RPM_BUILD_ROOT}"
mkdir -p "${RPM_BUILD_ROOT}/usr/share/logstash/"
install -D -m 644 %SOURCE0 "${RPM_BUILD_ROOT}/usr/share/logstash/"
install -D -m 755 %SOURCE1 "${RPM_BUILD_ROOT}/etc/rc.d/init.d/logstash"
install -D -m 644 %SOURCE2 "${RPM_BUILD_ROOT}/etc/logstash/logstash.conf"
install -D -m 644 %SOURCE3 "${RPM_BUILD_ROOT}/etc/logstash/log4j.properties"
install -D -m 755 %SOURCE4 "${RPM_BUILD_ROOT}/usr/sbin/logstash"
mkdir -p "${RPM_BUILD_ROOT}/var/lib/logstash"

%post
/sbin/chkconfig --add logstash
/sbin/service logstash start

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/
/etc/
/var/

%changelog
