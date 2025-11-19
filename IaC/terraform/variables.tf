variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for tagging"
  type        = string
  default     = "iris-ml"
}

variable "environment" {
  description = "Environment (dev/staging/prod)"
  type        = string
  default     = "production"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "ami_id" {
  description = "AMI ID for Ubuntu 22.04 LTS in us-east-1"
  type        = string
  default     = "ami-0c7217cdde317cfec"
}

variable "ssh_key_name" {
  description = "Name of SSH key pair"
  type        = string
  default     = "iris-ml-key"
}

variable "my_ip" {
  description = "Your IP address for SSH access"
  type        = string
  default     = "0.0.0.0/0"  # CAMBIAR por tu IP en producción
}
