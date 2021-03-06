# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
This script talks to the taskcluster secrets service to obtain the
Pocket token and write it to the .pocket_key_release file in the root
directory.
"""

import os
import taskcluster

# Get JSON data from taskcluster secrets service
secrets = taskcluster.Secrets({'baseUrl': 'http://taskcluster/secrets/v1'})
data = secrets.get('project/mobile/firefox-tv/tokens')

token_file_path = os.path.join(os.path.dirname(__file__), '../../.pocket_key_release')
with open(token_file_path, 'w') as token_file:
	token_file.write(data['secret']['pocketToken'])

print("Imported pocket token from secrets service")
