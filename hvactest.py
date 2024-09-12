# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

import hvac
import sys
import os

# Authentication
client = hvac.Client(
    url='https://vault.openknowit.com',
    token=os.environ.get('VAULT_TOKEN', 's.5Y9pZ4x6y3sZ4y3s'),
)

# Writing a secret
create_response = client.secrets.kv.v2.create_or_update_secret(
    path='my-secret-password',
    secret=dict(password='Hashi123'),
)

print('Secret written successfully.')

# Reading a secret
read_response = client.secrets.kv.read_secret_version(path='my-secret-password')

password = read_response['data']['data']['password']

if password != 'Hashi123':
    sys.exit('unexpected password')

print('Access granted!')

def read_patchwindows():
    # read the and convert the file to a list
    patchwindows = []
    filename = "/UNIXDOC/PatchManagement/PatchWindowsUnix.csv"
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            patchwindows.append(line.strip())
    return patchwindows



    

