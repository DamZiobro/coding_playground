provider "aws" {
  region = "${var.region}"
}

# define ECS cluster
resource "aws_ecs_cluster" "example_cluster" {
  name = "example-ecs-cluster"
}

resource "aws_autoscaling_group" "ecs_cluster_instances" {
  name                 = "ecs-cluster-instances"
  min_size             = 2
  max_size             = 5
  launch_configuration = "${aws_launch_configuration.ecs_instance.name}"
  availability_zones   = "${var.availability_zone_names}"
}

resource "aws_launch_configuration" "ecs_instance" {
  name_prefix   = "ecs-instance-"
  instance_type = "t2.micro"
  image_id      = "${var.image_id}"
}

resource "aws_ecs_task_definition" "web_container" {
  family = "web_container"

  container_definitions = <<EOF
[{
    "name": "web_container",
    "image": "macinv/flask-example:latest",
    "cpu": 1024,
    "memory": 768,
    "essential": true,
    "portMappings": [{"containerPort": 8080, "hostPort": 8080}]
}]
EOF
}

#resource "aws_ecs_task_definition" "redis_container" {
#family = "redis-container"

#container_definitions = <<EOF
#[{
#"name": "redis-container",
#"image": "redis:alpine",
#"cpu": 1024,
#"memory": 768,
#"essential": true,
#"portMappings": [{"containerPort": 6379, "hostPort": 6379}]
#}]
#EOF
#}

resource "aws_ecs_service" "web_container" {
  name            = "web_container_service"
  cluster         = "${aws_ecs_cluster.example_cluster.id}"
  task_definition = "${aws_ecs_task_definition.web_container.arn}"
  desired_count   = 1

  deployment_maximum_percent         = 100
  deployment_minimum_healthy_percent = 0

  load_balancer {
    elb_name       = "${aws_elb.web_container.id}"
    container_name = "web_container"
    container_port = 8080
  }
}

resource "aws_elb" "web_container" {
  name               = "web-container-elb"
  availability_zones = "${var.availability_zone_names}"

  listener {
    lb_port           = 80
    lb_protocol       = "http"
    instance_port     = 8080
    instance_protocol = "http"
  }
}

#resource "aws_ecs_service" "redis_container" {
#name            = "redis-container-service"
#cluster         = "${aws_ecs_cluster.example_cluster.id}"
#task_definition = "${aws_ecs_task_definition.redis_container.arn}"
#desired_count   = 2


#load_balancer {
#elb_name       = "${aws_elb.redis_container.id}"
#container_name = "redis-container"
#container_port = 6379
#}
#}


#resource "aws_elb" "redis_container" {
#name               = "redis-container-elb"
#availability_zones = "${var.availability_zone_names}"


#listener {
#lb_port           = 6379
#lb_protocol       = "http"
#instance_port     = 6379
#instance_protocol = "http"
#}
#}

