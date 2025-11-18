output "instance_id" {
  description = "ID of EC2 instance"
  value       = aws_instance.iris_ml.id
}

output "instance_public_ip" {
  description = "Public IP of EC2 instance"
  value       = aws_eip.iris_ml.public_ip
}

output "instance_public_dns" {
  description = "Public DNS of EC2 instance"
  value       = aws_instance.iris_ml.public_dns
}

output "security_group_id" {
  description = "ID of security group"
  value       = aws_security_group.iris_ml.id
}

output "vpc_id" {
  description = "ID of VPC"
  value       = aws_vpc.main.id
}

output "api_url" {
  description = "URL to access the API"
  value       = "http://${aws_eip.iris_ml.public_ip}:5000"
}
