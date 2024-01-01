import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

_path = 'E:/WORKING/A-AIR_TICKET/MalaysiaVisa'

hid = pd.read_excel(f'{_path}/VisaHid.xls')
hid = hid.sort_values(by='HID')

inv = pd.read_excel(f'{_path}/VisaInvoice.xls')
inv = inv[['HID', 'Inv', 'InvDate', 'Name', 'DepDate', 'Itin', 'HidDate']]
# HID	Com	Inv	InvDate	Name	DepDate	Itin HidDate
inv['Itin'] = inv['Itin'].str[:8]
inv = inv[inv['Itin'] == 'MALAYSIA']

hid.loc[hid['HID'].isin(list(inv['HID'])), 'BackDate'] = 'Y'

hid.to_excel(f'{_path}/hid.xls', sheet_name='Sheet1', index=False)

print(inv)
print(hid)