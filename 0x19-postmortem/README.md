# Postmortem
## Issue Summary
This is an incident report on the downtime experienced for 9 hours beginning May 26 2023 6:00 p.m. to May 27 2023 3:00 a.m. EAT. The company online services were slowed down, 100% of our users experienced system irresponsiveness and reported many system crashes. The root cause was determined to be a bug in one of the API designs.
## Timeline
* 26/05/2023 6:00 p.m. – The Senior DevOps Engineer receives a warning about high bandwidth usage for outgoing network traffic.
* 26/05/2023 6:05 p.m. – The Senior DevOps Engineer instructs other engineers still on premise to monitor the system outgoing network traffic.
* 26/05/2023 6:20 p.m. – All DevOps Engineers receive warnings that the cpu IO reads have increased to above normal, the incoming requests are above the critical limit, and high memory usage.
* 26/05/2023 6:30 p.m. – Users report multiple system crashes and slow-downs.
* 26/05/2023 6:30 p.m. – Senior DevOps Engineer logs in to server.
* 26/05/2023 6:35 p.m.  – Server is slow and unresponsive due to high memory usage.
* 26/05/2023 6:40 p.m. – All hosts are physically disconnected from the server.
* 26/05/2023 6:45 p.m. – Server is taken offline, web-server and application server logs are copied into a local file for further investigation. 
* 26/05/2023 7:20 p.m. – Server is rebooted, all hosts are re-connected and server is put back online.
* 26/05/2023 8:00 p.m. – Metrics indicate that everything is working normally. The on-call Backend Engineer is requested to arrive at company premises as the rest of the engineers close and leave for the day.
* 26/05/2023 9:30 p.m. – Backend and DevOps Engineer start going through the logs jointly.
* 26/05/2023 10:00 p.m. – Senior DevOps Engineer receives a warning about increased bandwidth usage again.
* 26/05/2023 10:05 p.m. – Server is immediately shut down. Night-shift staff are instructed to take the night off as the root cause is being investigated.
* 26/05/2023 10:30 p.m. Engineers notice the logs indicate that a large amount of data transfer from server to client occurred when a certain API was called.
* 26/05/2023 11:00 p.m. – The issue is forwarded to the software development team.
* 27/05/2023 3:00 a.m. – A hot-fix is deployed, the server is rebooted and everything is back to normal. 
## Root cause and resolution:
* A new update had been tested and deployed the previous week. This new update introduced a new feature on the frontend which required a call to the API to find all users who had bought a specific product. The issue was that the developers did not account for the different sizes of the testing and production server before deployment. The call made multiple joins across millions of rows and hundreds of tables and returned data in bulk to the frontend. When this feature was announced and emailed to all users on the evening of May 26 2023, the calls to the API started coming in in mass and the system slow-downs were evident.
* The issue was fixed by optimizing the queries to filter the data to only the rows and columns that were required by the front-end. This minimized bandwidth usage and CPU workload. 
## Corrective and preventative measures:
This issue can be avoided in future by ensuring proper software testing, and code review is carried out. 
TODO:
* Include a Beta test for every new feature, no matter how small.
* Match testing, development and production databases sizes and tables.
* Review existing and new queries to database.

