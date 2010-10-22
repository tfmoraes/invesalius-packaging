#
# Regular cron jobs for the invesalius package
#
0 4	* * *	root	[ -x /usr/bin/invesalius_maintenance ] && /usr/bin/invesalius_maintenance
