# Overview

InfluxDB is an open-source, distributed, time series database.

# Usage

Deploy the telegraf charm, and the required influxDB charm with the following:

    juju deploy telegraf
    juju deploy cs:~chris.macnaughton/influxdb

Add the relation between the two charms:

    juju add-relation influxdb telegraf

Expose the influxdb charm:

    juju expose influxdb

You can then access the influxdb interface at the public interface shown
from juju status.
