# Ansible Deployment

## Prerequisites

1. Ansible installed
2. SSH key configured
3. EC2 instance running (via Terraform)

## Setup
```bash
# Copy example inventory
cp inventory.ini.example inventory.ini

# Edit inventory.ini with:
# - Your EC2 IP address
# - Your Docker Hub username (saulhl07)
# - Your SSH key path
```

## Usage
```bash
# Test connection
ansible all -m ping

# Deploy application
ansible-playbook deploy.yml

# Verify deployment
ansible-playbook verify.yml

# Update application (pull new image and redeploy)
ansible-playbook deploy.yml --extra-vars "docker_tag=v1.0.1"
```

## Troubleshooting
```bash
# Check container logs
ansible iris_ml_servers -a "docker logs iris-ml-api"

# Restart container
ansible iris_ml_servers -a "docker restart iris-ml-api"

# Check Docker status
ansible iris_ml_servers -a "systemctl status docker"
```

## Variables

You can override variables when running playbooks:
```bash
# Use different Docker tag
ansible-playbook deploy.yml -e "docker_tag=v2.0.0"

# Use different port
ansible-playbook deploy.yml -e "app_port=8080"

# Deploy from different registry
ansible-playbook deploy.yml -e "docker_image=myuser/iris-ml"
```
