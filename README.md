# Fortigate ipset Blocklist
An Ansible / Python script to import some famous ipset from Firehol github : https://github.com/firehol/blocklist-ipsets and create automated blocklist on Fortigate NGFW

# How it works ?
- Download the git project
- Modify the host file and insert your credentials
- Enter the command : ansible-playbook fortigate-blacklist.yml -e url="RAW URL of the blocklist ipset"
* You can choose any of the ipset blocklist available on https://github.com/firehol/blocklist-ipsets

# Current limitations :
- You're limited by the number of host on Fortigate, you can increase the limits if you want (but you'll slow down your firewall)
- You're limited by the number of host you can add in a group (600 on most of firewalls). I'll created soon a V2 of this script to avoid the script crashing when we have + 600 entries for an addressgroup.

