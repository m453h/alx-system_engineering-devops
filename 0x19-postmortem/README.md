# Postmortem report for services outage incident on 13th August 2023

## Issue summary

From 13/08/2023 06:00 AM GMT+3 to 13/08/2023 07:11 AM GMT+3, all requests to the web server hosting our company website resulted in an internal error message. The impact of this incident affected 100% of traffic to the website as all users could not view any content of the website. The root cause of this outage was a misspelling of the name of the website configuration file which was pushed along routine website updates.


## Timeline (all times GMT+3)

* 05:50 AM: Migration of changes to the company website begins
* 06:00 AM: Outage beings
* 06:00 AM: The DevOps team alerted of the outage through e-mail by  a monitoring agent
* 06:30 AM: Attempted to restart the web server and database server, the outage persisted
* 06:40 AM: Attempted to check web server logs to identify the root cause, but no logs were found
* 06:50 AM: Attempted to connect to the web server process to view system calls
* 07:00 AM: Identified a misspelling of the name of the website configuration file that caused the internal server error
* 07:10 AM: Renamed the configuration file to the appropriate name
* 07:11 AM: Server restart begins
* 07:11 AM: 100% of traffic is restored

## Root Cause
At 05:50 AM GMT+3 changes to the company website were released in production without being thoroughly tested. The changes contained a misspelling of the name of a critical website configuration file. This caused the webserver to fail to successfully load  essential files required for the proper functioning of the website. Whenever a user visited the website the webserver continuously failed to load the configuration file and returned a response which indicated that there was an internal server error.

## Resolution and Recovery
At 06:00 AM GMT+3, the DevOps team was alerted by our monitoring agent on a persistent internal server error being returned whenever there is an incoming request.

At 06:30 AM GMT+3, the DevOps team attempted to restart the webserver and database server but the internal server error persisted.

At 06:40 AM GMT+3, the DevOps team attempted to investigate the webserver logs but nothing was being logged by the webserver.  

At 06:50 AM GMT+3, the DevOps team attempted to connect to the web server process to view system calls.

At 07:00 AM GM+3, the DevOps team identified a misspelling of the name of the website configuration file that caused the outage. The name of this file was supposed to be “wp-settings.php” and was instead written as “wp-settings.phpp”. 

At 07:10 AM GM+3, the DevOps team renamed the configuration file to the appropriate name.

At 07:11 AM GMT+3, the server was restarted.

At 07:11 AM GMT+3, 100% of traffic to the website is restored and the error was resolved.

## Corrective and Preventative Measures
After an internal review of the incident was conducted the following recommendations were made:

* Ensure thorough testing is done in the development server before deploying changes in production.
* Develop a better mechanism for reviewing and approving changes made to the website codebase before rolling them into production.
* Automate the monitoring of critical web server processes to ensure timely resolution of incidents.
