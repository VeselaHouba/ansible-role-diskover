# Diskover

Ansible role for deploying slightly modified docker instance of Diskover. Used for disk usage analysis. Uses sshfs to mount remote FS to docker container and then scans them.

## Dependencies
Following roles are expected to be present
- `veselahouba/docker`
- `veselahouba/docker_container`


## Note
It's **highly** recommended to generate your own ssh key-pair. There's also one attached by default, but don't use it any further than PoC.

## Usage
- Resolve dependencies

example `requirements.yml`

```YAML
---
roles:
  - name: veselahouba.docker
  - name: veselahouba.docker_container

```

```BASH
ansible-galaxy role install -r requirements.yml
```


- Generate your ssh key-pair
- Pass path to your private key to ansible role as `diskover_ssh_key` variable
- Deploy to server with playbook similar to following

```YAML
- name: Deploy
  hosts: all
  roles:
    - role: veselahouba.docker
    - role: veselahouba.docker_container
    - role: veselahouba.diskover
```

- Distribute your ssh public key part
- Scan server with:

```BASH
docker exec diskover_diskover_1 /app/scan.sh [TARGET_USER@]TARGET_HOSTNAME TARGET_PATH
```
