###############################################################################
# Spec file for utils
################################################################################
# Configured to be built by user student or other non-root user
################################################################################
#
Summary: Port monitor for testing RPM creation
Name: local-ports
Version: 1.0.1
Release: 1
License: MIT
URL: https://github.com/CosmicQ/local-ports
Group: MyMonitors
Packager: CosmicQ
Requires: bash
Requires: iproute
Requires: nmap
Requires: cronie
Requires: logrotate
BuildRoot: ~/rpmbuild/

# Build with the following syntax:
# rpmbuild --target noarch-unknown-linux -bb local-ports.spec

%description
A port monitor script for testing RPM creation.

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
#                                                                              #
# The %prep section is the first script that is executed during the build      #
# process. This script is not executed during the installation of the package. #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/usr/local/etc
mkdir -p $RPM_BUILD_ROOT/etc/cron.d
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d

# Copy our files in
cp ~/git/CosmicQ/local-ports/files/local-ports.sh $RPM_BUILD_ROOT/usr/local/bin
cp ~/git/CosmicQ/local-ports/files/local-ports.conf $RPM_BUILD_ROOT/usr/local/etc
cp ~/git/CosmicQ/local-ports/files/local-ports.cron $RPM_BUILD_ROOT/etc/cron.d/local-ports
cp ~/git/CosmicQ/local-ports/files/local-ports.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/local-ports

exit

################################################################################
# This would be the place to put any scripts that are required to run during   #
# installation of the rpm but prior to the installation of the files.          #
################################################################################
%pre
# Setup the cron job
if [ -e /etc/cron.d/local-ports ]; then
  mv /etc/cron.d/local-ports /etc/cron.d/local-ports.rpmorig
fi

# Make sure we rotate the log file
if [ -e /etc/logrotate.d/local-ports ]; then
  mv /etc/logrotate.d/local-ports.rpmorig
fi

################################################################################
#  This section of the spec file defines the files to be installed and their   #
#  locations in the directory tree.                                            #
################################################################################
%files
%attr(0744, root, root) /usr/local/bin/local-ports.sh
%attr(0644, root, root) /usr/local/etc/local-ports.conf
%attr(0644, root, root) /etc/cron.d/local-ports
%attr(0644, root, root) /etc/logrotate.d/local-ports

################################################################################
# This runs after the installation of files. This section can be pretty        #
# much anything you need or want it to be, including creating files, running   #
# system commands, and restarting services to reinitialize them after making   #
# configuration changes.                                                       #
################################################################################
%post

################################################################################
# This section contains a script that would be run after the rpm package is    #
# uninstalled.                                                                 #
################################################################################
%postun
if [ -e /etc/cron.d/local-ports.rpmorig ]; then
  mv /etc/cron.d/local-ports.rpmorig /etc/cron.d/local-ports
fi

if [ -e /etc/logrotate.d/local-ports.rpmorig ]; then
  mv /etc/logrotate.d/local-ports.rpmorig /etc/logrotate.d/local-ports
fi

%clean
rm -rf $RPM_BUILD_ROOT/usr/local/bin
rm -rf $RPM_BUILD_ROOT/usr/local/etc

%changelog
* Thu Jan 21 2021 Jason Qualkenbush <cosmicq@cosmicegg.net> - 1.0.1
- Update to change the group to MyMonitors
* Tue Jan 12 2021 Jason Qualkenbush <cosmicq@cosmicegg.net> - 1.0.0
- Initial build
- Example second item in the changelog for version-release 1.0.0
