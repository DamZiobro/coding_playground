#This script does the following tasks:
#   - create AWS EC2 T2 micro instance
#   - create AWS Elastic IP
#   - assign AWS Elastic IP to AWS EC2 instance
#   - output Public IP assigned to AWS EC2 instance


provider "aws" {
  region     = "eu-west-2"
}

resource "aws_instance" "ec2_t2_micro" {
  ami           = "ami-07dc734dc14746eab"
  instance_type = "t2.micro"
}

resource "aws_eip" "ip" {
  instance = "${aws_instance.ec2_t2_micro.id}"
}

output "ip" {
  value = "${aws_eip.ip.public_ip}"
}
