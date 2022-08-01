# Ansible Deployment of Todoapp

This project uses ansible on a **control node** to deploy the **To Do App** and dependencies to **host virtual machines**.

## Control Node Prerequisites
- `Unix like O/S (e.g. Linux, NOT Windows)`  
- `Python3` 
- `Ansible` 
- `private SSH key` of a private/public pair generated on the controller
## Host Node Prerequisites
- `Linux based O/S`  
- `Internet conection` for communicating with the Controller Node and Trello  
- `public SSH key` from the private/public pair (e.g. copy using ssh-copy-id)
## Misc prerequisites
- `An active Trello account` - with various security assets (tokens etc) identified as follows...
    - Trello API key
    - Trello token
    - Trello Member ID
    - Trello Board ID
    - Three Trello lists within the board with appropriate names e.g. 'To Do', 'Doing', 'Done'  

## Content

- `playbook.yaml` 
    - prompts for Trello API security assets and list names to use
    - installs prereqisites
    - checks out the latest To Do app from github
    - amends the host local .env with the security assets
    - creates and starts the service  
 - `hosts` - standart ansible hosts with the targets you must define as IP addresses [managed]
 - `.env.j2` - template for host local .env
 - `.gitignore` - borrowed off the net from an ansible suggested template
 - `todoapp.service` - defines the app as a 'systemd' service
 - `playbook.sh` bash script to simplify running the playbook  

## Secret Key
On running the script you will be prompted for the security assets as described, but first you will be prompted for a 'secret key'.  This identified the web session cookie and can be any suitably strong key (string of random characters suggest at least 16 chars long) for your production server use.

