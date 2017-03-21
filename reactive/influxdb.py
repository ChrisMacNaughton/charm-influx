from charmhelpers.core.hookenv import status_set, resource_get, open_port
from charmhelpers.core.host import service_start, service_stop
from charmhelpers.core.templating import render
from charms.reactive import when, when_not
from charms.reactive import set_state, remove_state

from subprocess import check_call, CalledProcessError

@when('admin.available')
def configure_website(website):
    website.configure(port=hookenv.config('port'))

@when_not('influxdb.configured')
@when('apt.installed.influxdb')
def install_influx():
  open_port(8083)
  open_port(8086)
  config_changed()
  service_start('influxdb')
  status_set('active', '')
  set_state('influxdb.configured')

@when('config.changed')
def config_changed():
  render(source='influxdb.conf',
         target='/etc/influxdb/influxdb.conf',
         owner='root',
         perms=0o644,
         context={
             'admin': 'true',
         })

@when('query.api.available')
def query_available(query):
  query.configure(port=8086, username='root', password='root')