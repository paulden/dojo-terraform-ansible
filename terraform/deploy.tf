provider "aws" {
  region     = "eu-west-2"
}

resource "aws_instance" "dojo_test" {
  ami           = "ami-0b0a60c0a2bd40612"
  instance_type = "t2.micro"
  key_name      = "pade"
  subnet_id     = "subnet-2ba00f51"


  associate_public_ip_address = true
  vpc_security_group_ids      = ["sg-db04bdb6"]
}