Files to build grok/logstash RPMs for RedHat Enterprise.

* includes log4j configuration as separate file (no need to patch jar)
* init-script included
* examples directory to get you started parting your own logfile format
* script to download sources and build RPMs

Build instructions:
-------------------
git clone git://github.com/lboynton/logstash-rpms.git
echo '%_topdir %(echo $HOME)/logstash-rpms' > ~/.rpmmacros
cd logstash-rpms
spectool --get-files SPECS/logstash.spec --directory SOURCES
mkdir BUILD
mkdir RPMS
rpmbuild -bb --buildroot ~/logstash-rpms/BUILD SPECS/logstash.spec
