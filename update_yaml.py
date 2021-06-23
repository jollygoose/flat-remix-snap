#!/usr/bin/env python3

"""checks for updates to the flat-remix icon theme release and updates the 
   snapcraft.yaml file accordingly.

   example run:

   cd flat-remix-snap
   python3 update_yaml.py
"""

import yaml
import subprocess
import ruamel.yaml
import urllib.request
import re
import tarfile
import os

repo = "daniruiz/flat-remix"
repo_url = "https://github.com/" + repo + ".git"
tags = []

# get the latest tag from GitHub
git_tags = subprocess.Popen(
    ["git", "ls-remote", "--tags", repo_url], stdout=subprocess.PIPE)
out, err = git_tags.communicate()
latest_tag = out.decode().split()[-1].split('refs/tags/')[-1]

# read the snapcraft.yaml and check the yaml version matches the latest release
yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=2, offset=2)
with open('snap/snapcraft.yaml') as file:
    snapcraft_config = yaml.load(file)

# if the tag is already the latest, exit
if snapcraft_config['version'] == latest_tag:
    print("No new updates to %s. Sources are up to date." % repo_url)
    exit(0)

# otherwise, get the lastest tar file
latest_tar_name = latest_tag+".tar.gz"
tar_url = "https://codeload.github.com/" + repo + "/tar.gz/refs/tags/" + latest_tag
urllib.request.urlretrieve(tar_url, latest_tar_name)

# update the yaml version number
snapcraft_config['version'] = latest_tag

# get the icon theme names from the tar file (folder names)
latest_tar_file = tarfile.open(latest_tar_name)
regex = re.compile(r"Flat-Remix-.+?(?=/)")
icon_theme_names = []
for line in latest_tar_file.getmembers():
    line = line.get_info()['name']
    theme_name = regex.search(line)
    try:
        icon_theme_names.append("$SNAP/share/icons/" + theme_name.group())
    except AttributeError:
        pass
# remove duplicates
icon_theme_names = set(icon_theme_names)

# update the list of available icon themes
snapcraft_config['slots']['icon-themes']['source']['read'] = list(icon_theme_names)

# finalize new yaml
os.rename('snap/snapcraft.yaml', 'snap/snapcraft.yaml.bak')
with open('snap/snapcraft.yaml', 'w') as file:
    yaml.dump(snapcraft_config, file)
