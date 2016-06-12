import ovh, json
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='INSERTAPPKEYHERE',    # Application Key
    application_secret='INSERTAPPLICATIONSECRETHERE', # Application Secret
    consumer_key='INSERTCONSUMERKEYHERE',       # Consumer Key
)
totalbill = 0
amountpaidlist = []
print("Hi", client.get('/me')['firstname']) #this is a test of if we are properly connected to OVH
# Doing fancy things and understanding your bills
bills = client.get('/me/bill')

for bill in bills:  
    billcost = client.get('/me/bill/' + bill)['priceWithTax']['text'][2:]
    amountpaidlist.append(billcost)

for number in amountpaidlist:
    totalbill = float(totalbill) + float(number)

print("You have paid OVH £",totalbill)
