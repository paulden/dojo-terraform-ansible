resource "aws_instance" "dojo" {
  ami           = "${data.aws_ami.ubuntu.id}"
  instance_type = "${var.instance_type}"
  key_name      = "${var.key_name}"
  subnet_id     = "${var.subnet_id}"

  associate_public_ip_address = true
  vpc_security_group_ids      = ["${var.vpc_security_group_id}"]

  tags {
    Name  = "${var.polygramme}-dojo_skool"
    Polygramme = "${upper(var.polygramme)}"
  }
}