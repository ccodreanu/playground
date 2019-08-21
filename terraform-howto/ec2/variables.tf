variable "region" {
  default = "eu-central-1"
}

variable "amis" {
  type = "map"

  default = {
    "eu-central-1" = "ami-0eaec5838478eb0ba"
  }
}

