provider "aws" {
  region = "${var.region}"
}

resource "aws_s3_bucket" "BIGBUCKET" {
  bucket = "this-is-my-biggest-bucket"
  acl = "private"
  count = 3
}

resource "aws_instance" "MYBIGINSTANCE" {
  ami = "${lookup(var.amis, var.region)}"
  instance_type = "t2.micro"
  tags = {
      Name = "MYBIGINSTANCE"
  }

  depends_on = ["aws_s3_bucket.BIGBUCKET"]
}

output "ip" {
  value = "${aws_instance.MYBIGINSTANCE.public_ip}"
}
