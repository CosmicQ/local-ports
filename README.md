# local-ports
This is an example repository for the RPM build process and releases
 
This was built using mostly David Both's guide on opensource.com (https://opensource.com/article/18/9/how-build-rpm-packages)
 
This is a simple script called `local-ports` that uses nmap to interrogate the primary interface and log the results to /var/log/local-port.log
 
This was created so there would be a dependency on a package that was unlikely to be installed (at least by default).  This also uses a config file to define the log file and directory to show how one might install a script with multiple parts.  The `.cron` and `.logroate` files are also used to highlight this ability.
