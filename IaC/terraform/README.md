# Terraform Infrastructure

## Prerequisites

1. AWS CLI configured with credentials
2. Terraform installed (>= 1.0)
3. SSH key generated (~/.ssh/iris-ml-key)

## Quick Start
```bash
# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Apply (create infrastructure)
terraform apply

# Get outputs
terraform output

# Destroy (delete everything)
terraform destroy
```

## Costs

Using t2.micro instance in Free Tier:
- **First 750 hours/month: FREE**
- After that: ~$0.0116/hour (~$8.5/month)

**Remember to destroy resources when done to avoid charges!**
