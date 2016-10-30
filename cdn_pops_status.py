#!/usr/bin/env python

import ovh, json
from termcolor import colored, cprint

client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='INSERTAPPKEYHERE',    # Application Key
    application_secret='INSERTAPPLICATIONSECRETHERE', # Application Secret
    consumer_key='INSERTCONSUMERKEYHERE',       # Consumer Key
)
#print("Hi", client.get('/me')['firstname']) #this is a test of if we are properly connected to OVH

pops = client.get('/cdn/dedicated/pops')

for pop in pops:
    pop_details = client.get('/cdn/dedicated/pops/%s' % pop)

    print "===== %s =====" % colored(pop_details['name'], 'blue')
    print "City: %s" % pop_details['city']
    if pop_details['status'] == 'ok':
        print "Status: %s " % colored(pop_details['status'], 'green')
    else:
        print "Status: %s " % colored(pop_details['status'], 'red')
