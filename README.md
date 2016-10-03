# WellCom

WellCom enables organizations to remotely monitor their wells.  It helps them respond quickly when a well breaks, optimize operations, and quantify the impact of their work.

This is accomplished using an arduino uno, a small, inexpensive microcontroller, fitted with a FONA 800 GSM module which allows for data transfer via an HTTP request over cellular network.  Data is gathered using a temperature sensor which creates usage statistics as water travels through the pump system.  The unit is also fitted li-ion battery, which is charged using a 5v solar panel and lithium ion/polymer charger allowing constant monitoring over a 24hour period.

The graph enables users to view usage data over time for a specific well.  Users are also able to compare usage between wells by toggling them in the graph legend.  

And with multiple wells active, users can toggle between a comparison and cumulative view.

Below the graph, you’ll find cumulative data for the wells over their lifetime, which provides organizations with a couple simple metrics to measure their impact.

When a user opens the Water Test Results Dropdown, WellCom displays results of water quality tests.  The results are displayed alongside World Health Organization guidelines.  

Additionally, WellCom displays updates given by the organization about each well.  This enables a user to keep a historical log of field notes pertaining to the specific well.
