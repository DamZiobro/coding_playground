variable "region" {
    default = "eu-west-2"
}

variable "availability_zone_names" {
    type    = "list"
    default = ["eu-west-2a", "eu-west-2b"]
}

variable "image_id" {
    default = "ami-037af9c254c6dc46c"
}
