locals {
  cluster_name                 = "kops-cluster.xmementoit.co.uk"
  master_autoscaling_group_ids = [aws_autoscaling_group.master-eu-west-1a-masters-kops-cluster-xmementoit-co-uk.id]
  master_security_group_ids    = [aws_security_group.masters-kops-cluster-xmementoit-co-uk.id]
  masters_role_arn             = aws_iam_role.masters-kops-cluster-xmementoit-co-uk.arn
  masters_role_name            = aws_iam_role.masters-kops-cluster-xmementoit-co-uk.name
  node_autoscaling_group_ids   = [aws_autoscaling_group.nodes-eu-west-1a-kops-cluster-xmementoit-co-uk.id]
  node_security_group_ids      = [aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id]
  node_subnet_ids              = [aws_subnet.eu-west-1a-kops-cluster-xmementoit-co-uk.id]
  nodes_role_arn               = aws_iam_role.nodes-kops-cluster-xmementoit-co-uk.arn
  nodes_role_name              = aws_iam_role.nodes-kops-cluster-xmementoit-co-uk.name
  region                       = "eu-west-1"
  route_table_public_id        = aws_route_table.kops-cluster-xmementoit-co-uk.id
  subnet_eu-west-1a_id         = aws_subnet.eu-west-1a-kops-cluster-xmementoit-co-uk.id
  vpc_cidr_block               = aws_vpc.kops-cluster-xmementoit-co-uk.cidr_block
  vpc_id                       = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

output "cluster_name" {
  value = "kops-cluster.xmementoit.co.uk"
}

output "master_autoscaling_group_ids" {
  value = [aws_autoscaling_group.master-eu-west-1a-masters-kops-cluster-xmementoit-co-uk.id]
}

output "master_security_group_ids" {
  value = [aws_security_group.masters-kops-cluster-xmementoit-co-uk.id]
}

output "masters_role_arn" {
  value = aws_iam_role.masters-kops-cluster-xmementoit-co-uk.arn
}

output "masters_role_name" {
  value = aws_iam_role.masters-kops-cluster-xmementoit-co-uk.name
}

output "node_autoscaling_group_ids" {
  value = [aws_autoscaling_group.nodes-eu-west-1a-kops-cluster-xmementoit-co-uk.id]
}

output "node_security_group_ids" {
  value = [aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id]
}

output "node_subnet_ids" {
  value = [aws_subnet.eu-west-1a-kops-cluster-xmementoit-co-uk.id]
}

output "nodes_role_arn" {
  value = aws_iam_role.nodes-kops-cluster-xmementoit-co-uk.arn
}

output "nodes_role_name" {
  value = aws_iam_role.nodes-kops-cluster-xmementoit-co-uk.name
}

output "region" {
  value = "eu-west-1"
}

output "route_table_public_id" {
  value = aws_route_table.kops-cluster-xmementoit-co-uk.id
}

output "subnet_eu-west-1a_id" {
  value = aws_subnet.eu-west-1a-kops-cluster-xmementoit-co-uk.id
}

output "vpc_cidr_block" {
  value = aws_vpc.kops-cluster-xmementoit-co-uk.cidr_block
}

output "vpc_id" {
  value = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

provider "aws" {
  region = "eu-west-1"
}

provider "aws" {
  alias  = "files"
  region = "us-east-1"
}

resource "aws_autoscaling_group" "master-eu-west-1a-masters-kops-cluster-xmementoit-co-uk" {
  enabled_metrics = ["GroupDesiredCapacity", "GroupInServiceInstances", "GroupMaxSize", "GroupMinSize", "GroupPendingInstances", "GroupStandbyInstances", "GroupTerminatingInstances", "GroupTotalInstances"]
  launch_template {
    id      = aws_launch_template.master-eu-west-1a-masters-kops-cluster-xmementoit-co-uk.id
    version = aws_launch_template.master-eu-west-1a-masters-kops-cluster-xmementoit-co-uk.latest_version
  }
  max_instance_lifetime = 0
  max_size              = 1
  metrics_granularity   = "1Minute"
  min_size              = 1
  name                  = "master-eu-west-1a.masters.kops-cluster.xmementoit.co.uk"
  protect_from_scale_in = false
  tag {
    key                 = "KubernetesCluster"
    propagate_at_launch = true
    value               = "kops-cluster.xmementoit.co.uk"
  }
  tag {
    key                 = "Name"
    propagate_at_launch = true
    value               = "master-eu-west-1a.masters.kops-cluster.xmementoit.co.uk"
  }
  tag {
    key                 = "k8s.io/cluster-autoscaler/node-template/label/kops.k8s.io/kops-controller-pki"
    propagate_at_launch = true
    value               = ""
  }
  tag {
    key                 = "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/control-plane"
    propagate_at_launch = true
    value               = ""
  }
  tag {
    key                 = "k8s.io/cluster-autoscaler/node-template/label/node.kubernetes.io/exclude-from-external-load-balancers"
    propagate_at_launch = true
    value               = ""
  }
  tag {
    key                 = "k8s.io/role/master"
    propagate_at_launch = true
    value               = "1"
  }
  tag {
    key                 = "kops.k8s.io/instancegroup"
    propagate_at_launch = true
    value               = "master-eu-west-1a"
  }
  tag {
    key                 = "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"
    propagate_at_launch = true
    value               = "owned"
  }
  vpc_zone_identifier = [aws_subnet.eu-west-1a-kops-cluster-xmementoit-co-uk.id]
}

resource "aws_autoscaling_group" "nodes-eu-west-1a-kops-cluster-xmementoit-co-uk" {
  enabled_metrics = ["GroupDesiredCapacity", "GroupInServiceInstances", "GroupMaxSize", "GroupMinSize", "GroupPendingInstances", "GroupStandbyInstances", "GroupTerminatingInstances", "GroupTotalInstances"]
  launch_template {
    id      = aws_launch_template.nodes-eu-west-1a-kops-cluster-xmementoit-co-uk.id
    version = aws_launch_template.nodes-eu-west-1a-kops-cluster-xmementoit-co-uk.latest_version
  }
  max_instance_lifetime = 0
  max_size              = 2
  metrics_granularity   = "1Minute"
  min_size              = 2
  name                  = "nodes-eu-west-1a.kops-cluster.xmementoit.co.uk"
  protect_from_scale_in = false
  tag {
    key                 = "KubernetesCluster"
    propagate_at_launch = true
    value               = "kops-cluster.xmementoit.co.uk"
  }
  tag {
    key                 = "Name"
    propagate_at_launch = true
    value               = "nodes-eu-west-1a.kops-cluster.xmementoit.co.uk"
  }
  tag {
    key                 = "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/node"
    propagate_at_launch = true
    value               = ""
  }
  tag {
    key                 = "k8s.io/role/node"
    propagate_at_launch = true
    value               = "1"
  }
  tag {
    key                 = "kops.k8s.io/instancegroup"
    propagate_at_launch = true
    value               = "nodes-eu-west-1a"
  }
  tag {
    key                 = "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"
    propagate_at_launch = true
    value               = "owned"
  }
  vpc_zone_identifier = [aws_subnet.eu-west-1a-kops-cluster-xmementoit-co-uk.id]
}

resource "aws_ebs_volume" "a-etcd-events-kops-cluster-xmementoit-co-uk" {
  availability_zone = "eu-west-1a"
  encrypted         = true
  iops              = 3000
  size              = 20
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "a.etcd-events.kops-cluster.xmementoit.co.uk"
    "k8s.io/etcd/events"                                  = "a/a"
    "k8s.io/role/master"                                  = "1"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
  throughput = 125
  type       = "gp3"
}

resource "aws_ebs_volume" "a-etcd-main-kops-cluster-xmementoit-co-uk" {
  availability_zone = "eu-west-1a"
  encrypted         = true
  iops              = 3000
  size              = 20
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "a.etcd-main.kops-cluster.xmementoit.co.uk"
    "k8s.io/etcd/main"                                    = "a/a"
    "k8s.io/role/master"                                  = "1"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
  throughput = 125
  type       = "gp3"
}

resource "aws_iam_instance_profile" "masters-kops-cluster-xmementoit-co-uk" {
  name = "masters.kops-cluster.xmementoit.co.uk"
  role = aws_iam_role.masters-kops-cluster-xmementoit-co-uk.name
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "masters.kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
}

resource "aws_iam_instance_profile" "nodes-kops-cluster-xmementoit-co-uk" {
  name = "nodes.kops-cluster.xmementoit.co.uk"
  role = aws_iam_role.nodes-kops-cluster-xmementoit-co-uk.name
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "nodes.kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
}

resource "aws_iam_role" "masters-kops-cluster-xmementoit-co-uk" {
  assume_role_policy = file("${path.module}/data/aws_iam_role_masters.kops-cluster.xmementoit.co.uk_policy")
  name               = "masters.kops-cluster.xmementoit.co.uk"
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "masters.kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
}

resource "aws_iam_role" "nodes-kops-cluster-xmementoit-co-uk" {
  assume_role_policy = file("${path.module}/data/aws_iam_role_nodes.kops-cluster.xmementoit.co.uk_policy")
  name               = "nodes.kops-cluster.xmementoit.co.uk"
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "nodes.kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
}

resource "aws_iam_role_policy" "masters-kops-cluster-xmementoit-co-uk" {
  name   = "masters.kops-cluster.xmementoit.co.uk"
  policy = file("${path.module}/data/aws_iam_role_policy_masters.kops-cluster.xmementoit.co.uk_policy")
  role   = aws_iam_role.masters-kops-cluster-xmementoit-co-uk.name
}

resource "aws_iam_role_policy" "nodes-kops-cluster-xmementoit-co-uk" {
  name   = "nodes.kops-cluster.xmementoit.co.uk"
  policy = file("${path.module}/data/aws_iam_role_policy_nodes.kops-cluster.xmementoit.co.uk_policy")
  role   = aws_iam_role.nodes-kops-cluster-xmementoit-co-uk.name
}

resource "aws_internet_gateway" "kops-cluster-xmementoit-co-uk" {
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
  vpc_id = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

resource "aws_launch_template" "master-eu-west-1a-masters-kops-cluster-xmementoit-co-uk" {
  block_device_mappings {
    device_name = "/dev/sda1"
    ebs {
      delete_on_termination = true
      encrypted             = true
      iops                  = 3000
      throughput            = 125
      volume_size           = 64
      volume_type           = "gp3"
    }
  }
  iam_instance_profile {
    name = aws_iam_instance_profile.masters-kops-cluster-xmementoit-co-uk.id
  }
  image_id      = "ami-0b95c8042c84717b9"
  instance_type = "t2.micro"
  lifecycle {
    create_before_destroy = true
  }
  metadata_options {
    http_endpoint               = "enabled"
    http_protocol_ipv6          = "disabled"
    http_put_response_hop_limit = 3
    http_tokens                 = "required"
  }
  monitoring {
    enabled = false
  }
  name = "master-eu-west-1a.masters.kops-cluster.xmementoit.co.uk"
  network_interfaces {
    associate_public_ip_address = true
    delete_on_termination       = true
    ipv6_address_count          = 0
    security_groups             = [aws_security_group.masters-kops-cluster-xmementoit-co-uk.id]
  }
  tag_specifications {
    resource_type = "instance"
    tags = {
      "KubernetesCluster"                                                                                     = "kops-cluster.xmementoit.co.uk"
      "Name"                                                                                                  = "master-eu-west-1a.masters.kops-cluster.xmementoit.co.uk"
      "k8s.io/cluster-autoscaler/node-template/label/kops.k8s.io/kops-controller-pki"                         = ""
      "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/control-plane"                   = ""
      "k8s.io/cluster-autoscaler/node-template/label/node.kubernetes.io/exclude-from-external-load-balancers" = ""
      "k8s.io/role/master"                                                                                    = "1"
      "kops.k8s.io/instancegroup"                                                                             = "master-eu-west-1a"
      "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"                                                   = "owned"
    }
  }
  tag_specifications {
    resource_type = "volume"
    tags = {
      "KubernetesCluster"                                                                                     = "kops-cluster.xmementoit.co.uk"
      "Name"                                                                                                  = "master-eu-west-1a.masters.kops-cluster.xmementoit.co.uk"
      "k8s.io/cluster-autoscaler/node-template/label/kops.k8s.io/kops-controller-pki"                         = ""
      "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/control-plane"                   = ""
      "k8s.io/cluster-autoscaler/node-template/label/node.kubernetes.io/exclude-from-external-load-balancers" = ""
      "k8s.io/role/master"                                                                                    = "1"
      "kops.k8s.io/instancegroup"                                                                             = "master-eu-west-1a"
      "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"                                                   = "owned"
    }
  }
  tags = {
    "KubernetesCluster"                                                                                     = "kops-cluster.xmementoit.co.uk"
    "Name"                                                                                                  = "master-eu-west-1a.masters.kops-cluster.xmementoit.co.uk"
    "k8s.io/cluster-autoscaler/node-template/label/kops.k8s.io/kops-controller-pki"                         = ""
    "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/control-plane"                   = ""
    "k8s.io/cluster-autoscaler/node-template/label/node.kubernetes.io/exclude-from-external-load-balancers" = ""
    "k8s.io/role/master"                                                                                    = "1"
    "kops.k8s.io/instancegroup"                                                                             = "master-eu-west-1a"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"                                                   = "owned"
  }
  user_data = filebase64("${path.module}/data/aws_launch_template_master-eu-west-1a.masters.kops-cluster.xmementoit.co.uk_user_data")
}

resource "aws_launch_template" "nodes-eu-west-1a-kops-cluster-xmementoit-co-uk" {
  block_device_mappings {
    device_name = "/dev/sda1"
    ebs {
      delete_on_termination = true
      encrypted             = true
      iops                  = 3000
      throughput            = 125
      volume_size           = 128
      volume_type           = "gp3"
    }
  }
  iam_instance_profile {
    name = aws_iam_instance_profile.nodes-kops-cluster-xmementoit-co-uk.id
  }
  image_id      = "ami-0b95c8042c84717b9"
  instance_type = "t2.micro"
  lifecycle {
    create_before_destroy = true
  }
  metadata_options {
    http_endpoint               = "enabled"
    http_protocol_ipv6          = "disabled"
    http_put_response_hop_limit = 1
    http_tokens                 = "required"
  }
  monitoring {
    enabled = false
  }
  name = "nodes-eu-west-1a.kops-cluster.xmementoit.co.uk"
  network_interfaces {
    associate_public_ip_address = true
    delete_on_termination       = true
    ipv6_address_count          = 0
    security_groups             = [aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id]
  }
  tag_specifications {
    resource_type = "instance"
    tags = {
      "KubernetesCluster"                                                          = "kops-cluster.xmementoit.co.uk"
      "Name"                                                                       = "nodes-eu-west-1a.kops-cluster.xmementoit.co.uk"
      "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/node" = ""
      "k8s.io/role/node"                                                           = "1"
      "kops.k8s.io/instancegroup"                                                  = "nodes-eu-west-1a"
      "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"                        = "owned"
    }
  }
  tag_specifications {
    resource_type = "volume"
    tags = {
      "KubernetesCluster"                                                          = "kops-cluster.xmementoit.co.uk"
      "Name"                                                                       = "nodes-eu-west-1a.kops-cluster.xmementoit.co.uk"
      "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/node" = ""
      "k8s.io/role/node"                                                           = "1"
      "kops.k8s.io/instancegroup"                                                  = "nodes-eu-west-1a"
      "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"                        = "owned"
    }
  }
  tags = {
    "KubernetesCluster"                                                          = "kops-cluster.xmementoit.co.uk"
    "Name"                                                                       = "nodes-eu-west-1a.kops-cluster.xmementoit.co.uk"
    "k8s.io/cluster-autoscaler/node-template/label/node-role.kubernetes.io/node" = ""
    "k8s.io/role/node"                                                           = "1"
    "kops.k8s.io/instancegroup"                                                  = "nodes-eu-west-1a"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk"                        = "owned"
  }
  user_data = filebase64("${path.module}/data/aws_launch_template_nodes-eu-west-1a.kops-cluster.xmementoit.co.uk_user_data")
}

resource "aws_route" "route-0-0-0-0--0" {
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.kops-cluster-xmementoit-co-uk.id
  route_table_id         = aws_route_table.kops-cluster-xmementoit-co-uk.id
}

resource "aws_route" "route-__--0" {
  destination_ipv6_cidr_block = "::/0"
  gateway_id                  = aws_internet_gateway.kops-cluster-xmementoit-co-uk.id
  route_table_id              = aws_route_table.kops-cluster-xmementoit-co-uk.id
}

resource "aws_route_table" "kops-cluster-xmementoit-co-uk" {
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
    "kubernetes.io/kops/role"                             = "public"
  }
  vpc_id = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

resource "aws_route_table_association" "eu-west-1a-kops-cluster-xmementoit-co-uk" {
  route_table_id = aws_route_table.kops-cluster-xmementoit-co-uk.id
  subnet_id      = aws_subnet.eu-west-1a-kops-cluster-xmementoit-co-uk.id
}

resource "aws_s3_object" "cluster-completed-spec" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_cluster-completed.spec_content")
  key                    = "kops-cluster.xmementoit.co.uk/cluster-completed.spec"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "etcd-cluster-spec-events" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_etcd-cluster-spec-events_content")
  key                    = "kops-cluster.xmementoit.co.uk/backups/etcd/events/control/etcd-cluster-spec"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "etcd-cluster-spec-main" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_etcd-cluster-spec-main_content")
  key                    = "kops-cluster.xmementoit.co.uk/backups/etcd/main/control/etcd-cluster-spec"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-aws-cloud-controller-addons-k8s-io-k8s-1-18" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-aws-cloud-controller.addons.k8s.io-k8s-1.18_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/aws-cloud-controller.addons.k8s.io/k8s-1.18.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-aws-ebs-csi-driver-addons-k8s-io-k8s-1-17" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-aws-ebs-csi-driver.addons.k8s.io-k8s-1.17_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/aws-ebs-csi-driver.addons.k8s.io/k8s-1.17.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-bootstrap" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-bootstrap_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/bootstrap-channel.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-coredns-addons-k8s-io-k8s-1-12" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-coredns.addons.k8s.io-k8s-1.12_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/coredns.addons.k8s.io/k8s-1.12.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-dns-controller-addons-k8s-io-k8s-1-12" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-dns-controller.addons.k8s.io-k8s-1.12_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/dns-controller.addons.k8s.io/k8s-1.12.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-kops-controller-addons-k8s-io-k8s-1-16" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-kops-controller.addons.k8s.io-k8s-1.16_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/kops-controller.addons.k8s.io/k8s-1.16.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-kubelet-api-rbac-addons-k8s-io-k8s-1-9" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-kubelet-api.rbac.addons.k8s.io-k8s-1.9_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/kubelet-api.rbac.addons.k8s.io/k8s-1.9.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-leader-migration-rbac-addons-k8s-io-k8s-1-23" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-leader-migration.rbac.addons.k8s.io-k8s-1.23_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/leader-migration.rbac.addons.k8s.io/k8s-1.23.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-limit-range-addons-k8s-io" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-limit-range.addons.k8s.io_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/limit-range.addons.k8s.io/v1.5.0.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-cluster-xmementoit-co-uk-addons-storage-aws-addons-k8s-io-v1-15-0" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-cluster.xmementoit.co.uk-addons-storage-aws.addons.k8s.io-v1.15.0_content")
  key                    = "kops-cluster.xmementoit.co.uk/addons/storage-aws.addons.k8s.io/v1.15.0.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "kops-version-txt" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_kops-version.txt_content")
  key                    = "kops-cluster.xmementoit.co.uk/kops-version.txt"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "manifests-etcdmanager-events-master-eu-west-1a" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_manifests-etcdmanager-events-master-eu-west-1a_content")
  key                    = "kops-cluster.xmementoit.co.uk/manifests/etcd/events-master-eu-west-1a.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "manifests-etcdmanager-main-master-eu-west-1a" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_manifests-etcdmanager-main-master-eu-west-1a_content")
  key                    = "kops-cluster.xmementoit.co.uk/manifests/etcd/main-master-eu-west-1a.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "manifests-static-kube-apiserver-healthcheck" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_manifests-static-kube-apiserver-healthcheck_content")
  key                    = "kops-cluster.xmementoit.co.uk/manifests/static/kube-apiserver-healthcheck.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "nodeupconfig-master-eu-west-1a" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_nodeupconfig-master-eu-west-1a_content")
  key                    = "kops-cluster.xmementoit.co.uk/igconfig/master/master-eu-west-1a/nodeupconfig.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_s3_object" "nodeupconfig-nodes-eu-west-1a" {
  bucket                 = "xmementoit-kops-cluster"
  content                = file("${path.module}/data/aws_s3_object_nodeupconfig-nodes-eu-west-1a_content")
  key                    = "kops-cluster.xmementoit.co.uk/igconfig/node/nodes-eu-west-1a/nodeupconfig.yaml"
  provider               = aws.files
  server_side_encryption = "AES256"
}

resource "aws_security_group" "masters-kops-cluster-xmementoit-co-uk" {
  description = "Security group for masters"
  name        = "masters.kops-cluster.xmementoit.co.uk"
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "masters.kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
  vpc_id = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

resource "aws_security_group" "nodes-kops-cluster-xmementoit-co-uk" {
  description = "Security group for nodes"
  name        = "nodes.kops-cluster.xmementoit.co.uk"
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "nodes.kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
  vpc_id = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

resource "aws_security_group_rule" "from-0-0-0-0--0-ingress-tcp-22to22-masters-kops-cluster-xmementoit-co-uk" {
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 22
  protocol          = "tcp"
  security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port           = 22
  type              = "ingress"
}

resource "aws_security_group_rule" "from-0-0-0-0--0-ingress-tcp-22to22-nodes-kops-cluster-xmementoit-co-uk" {
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 22
  protocol          = "tcp"
  security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port           = 22
  type              = "ingress"
}

resource "aws_security_group_rule" "from-0-0-0-0--0-ingress-tcp-443to443-masters-kops-cluster-xmementoit-co-uk" {
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 443
  protocol          = "tcp"
  security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port           = 443
  type              = "ingress"
}

resource "aws_security_group_rule" "from-__--0-ingress-tcp-22to22-masters-kops-cluster-xmementoit-co-uk" {
  from_port         = 22
  ipv6_cidr_blocks  = ["::/0"]
  protocol          = "tcp"
  security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port           = 22
  type              = "ingress"
}

resource "aws_security_group_rule" "from-__--0-ingress-tcp-22to22-nodes-kops-cluster-xmementoit-co-uk" {
  from_port         = 22
  ipv6_cidr_blocks  = ["::/0"]
  protocol          = "tcp"
  security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port           = 22
  type              = "ingress"
}

resource "aws_security_group_rule" "from-__--0-ingress-tcp-443to443-masters-kops-cluster-xmementoit-co-uk" {
  from_port         = 443
  ipv6_cidr_blocks  = ["::/0"]
  protocol          = "tcp"
  security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port           = 443
  type              = "ingress"
}

resource "aws_security_group_rule" "from-masters-kops-cluster-xmementoit-co-uk-egress-all-0to0-0-0-0-0--0" {
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 0
  protocol          = "-1"
  security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port           = 0
  type              = "egress"
}

resource "aws_security_group_rule" "from-masters-kops-cluster-xmementoit-co-uk-egress-all-0to0-__--0" {
  from_port         = 0
  ipv6_cidr_blocks  = ["::/0"]
  protocol          = "-1"
  security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port           = 0
  type              = "egress"
}

resource "aws_security_group_rule" "from-masters-kops-cluster-xmementoit-co-uk-ingress-all-0to0-masters-kops-cluster-xmementoit-co-uk" {
  from_port                = 0
  protocol                 = "-1"
  security_group_id        = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  source_security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port                  = 0
  type                     = "ingress"
}

resource "aws_security_group_rule" "from-masters-kops-cluster-xmementoit-co-uk-ingress-all-0to0-nodes-kops-cluster-xmementoit-co-uk" {
  from_port                = 0
  protocol                 = "-1"
  security_group_id        = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  source_security_group_id = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  to_port                  = 0
  type                     = "ingress"
}

resource "aws_security_group_rule" "from-nodes-kops-cluster-xmementoit-co-uk-egress-all-0to0-0-0-0-0--0" {
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 0
  protocol          = "-1"
  security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port           = 0
  type              = "egress"
}

resource "aws_security_group_rule" "from-nodes-kops-cluster-xmementoit-co-uk-egress-all-0to0-__--0" {
  from_port         = 0
  ipv6_cidr_blocks  = ["::/0"]
  protocol          = "-1"
  security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port           = 0
  type              = "egress"
}

resource "aws_security_group_rule" "from-nodes-kops-cluster-xmementoit-co-uk-ingress-all-0to0-nodes-kops-cluster-xmementoit-co-uk" {
  from_port                = 0
  protocol                 = "-1"
  security_group_id        = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  source_security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port                  = 0
  type                     = "ingress"
}

resource "aws_security_group_rule" "from-nodes-kops-cluster-xmementoit-co-uk-ingress-tcp-1to2379-masters-kops-cluster-xmementoit-co-uk" {
  from_port                = 1
  protocol                 = "tcp"
  security_group_id        = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  source_security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port                  = 2379
  type                     = "ingress"
}

resource "aws_security_group_rule" "from-nodes-kops-cluster-xmementoit-co-uk-ingress-tcp-2382to4000-masters-kops-cluster-xmementoit-co-uk" {
  from_port                = 2382
  protocol                 = "tcp"
  security_group_id        = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  source_security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port                  = 4000
  type                     = "ingress"
}

resource "aws_security_group_rule" "from-nodes-kops-cluster-xmementoit-co-uk-ingress-tcp-4003to65535-masters-kops-cluster-xmementoit-co-uk" {
  from_port                = 4003
  protocol                 = "tcp"
  security_group_id        = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  source_security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port                  = 65535
  type                     = "ingress"
}

resource "aws_security_group_rule" "from-nodes-kops-cluster-xmementoit-co-uk-ingress-udp-1to65535-masters-kops-cluster-xmementoit-co-uk" {
  from_port                = 1
  protocol                 = "udp"
  security_group_id        = aws_security_group.masters-kops-cluster-xmementoit-co-uk.id
  source_security_group_id = aws_security_group.nodes-kops-cluster-xmementoit-co-uk.id
  to_port                  = 65535
  type                     = "ingress"
}

resource "aws_subnet" "eu-west-1a-kops-cluster-xmementoit-co-uk" {
  availability_zone                           = "eu-west-1a"
  cidr_block                                  = "172.20.32.0/19"
  enable_resource_name_dns_a_record_on_launch = true
  private_dns_hostname_type_on_launch         = "resource-name"
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "eu-west-1a.kops-cluster.xmementoit.co.uk"
    "SubnetType"                                          = "Public"
    "kops.k8s.io/instance-group/master-eu-west-1a"        = "true"
    "kops.k8s.io/instance-group/nodes-eu-west-1a"         = "true"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
    "kubernetes.io/role/elb"                              = "1"
    "kubernetes.io/role/internal-elb"                     = "1"
  }
  vpc_id = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

resource "aws_vpc" "kops-cluster-xmementoit-co-uk" {
  assign_generated_ipv6_cidr_block = true
  cidr_block                       = "172.20.0.0/16"
  enable_dns_hostnames             = true
  enable_dns_support               = true
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
}

resource "aws_vpc_dhcp_options" "kops-cluster-xmementoit-co-uk" {
  domain_name         = "eu-west-1.compute.internal"
  domain_name_servers = ["AmazonProvidedDNS"]
  tags = {
    "KubernetesCluster"                                   = "kops-cluster.xmementoit.co.uk"
    "Name"                                                = "kops-cluster.xmementoit.co.uk"
    "kubernetes.io/cluster/kops-cluster.xmementoit.co.uk" = "owned"
  }
}

resource "aws_vpc_dhcp_options_association" "kops-cluster-xmementoit-co-uk" {
  dhcp_options_id = aws_vpc_dhcp_options.kops-cluster-xmementoit-co-uk.id
  vpc_id          = aws_vpc.kops-cluster-xmementoit-co-uk.id
}

terraform {
  required_version = ">= 0.15.0"
  required_providers {
    aws = {
      "configuration_aliases" = [aws.files]
      "source"                = "hashicorp/aws"
      "version"               = ">= 4.0.0"
    }
  }
}
