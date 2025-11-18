# Terraform Configuration

## Prerequisites

1. AWS CLI configured
2. Terraform installed
3. SSH key pair generated

## Generate SSH Key
```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/iris-ml-key
```

## Usage
```bash
# Initialize
terraform init

# Copy example vars
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values

# Plan
terraform plan

# Apply
terraform apply

# Get outputs
terraform output

# Destroy
terraform destroy
```

## Outputs

- `instance_public_ip`: IP to SSH and access API
- `api_url`: Full URL to API
