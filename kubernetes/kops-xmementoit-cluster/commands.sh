# 1. Create IAM group and user for kops operations
aws iam create-group --group-name kops

aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonRoute53FullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/IAMFullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonVPCFullAccess --group-name kops

#for kops delete
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess --group-name kops
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/CloudWatchEventsFullAccess --group-name kops

aws iam create-user --user-name kops

aws iam add-user-to-group --user-name kops --group-name kops

aws iam create-access-key --user-name kops

# 2. Create S3 bucket for kops cluster state
aws s3api create-bucket --bucket xmementoit-kops-cluster --region us-east-1

# 3. Create kops cluster config - dry run - requires another command to actually create EC2 nodes - see below (xmementoit.co.uk domains is registered in AWS Route53) 
kops create cluster --name kops-cluster.xmementoit.co.uk --state s3://xmementoit-kops-cluster --zones eu-west-1a --node-count 3 --node-size t2.micro --master-size t2.micro --dns-zone xmementoit.co.uk --cloud aws

# 4. Ouptut kops cluster in terraform files
kops update cluster --name kops-cluster.xmementoit.co.uk --state s3://xmementoit-kops-cluster --out=. --target=terraform
# now we can run terraform plan && terraform apply

# 5. Run kops cluster based on config created in 3.
kops update cluster --name kops-cluster.xmementoit.co.uk --state s3://xmementoit-kops-cluster --yes

# 6. Set kops cluster user 'kops' as default user of kubectl tool
kops export kubeconfig kops-cluster.xmementoit.co.uk --state s3://xmementoit-kops-cluster --user kops

# 7. Create sshpublickey on the kops cluster nodes (so the we will be able to SSH into the cluster nodes)
kops create secret sshpublickey kops-cluster.xmementoit.co.uk --state s3://xmementoit-kops-cluster -i ~/.ssh/id_rsa.pub && kops update cluster --yes

# 8. Apply all changes using rolling update of the cluster:
kops rolling-update cluster kops-cluster.xmementoit.co.uk --state s3://xmementoit-kops-cluster --yes

# DELETE kops cluster
kops delete cluster --name kops-cluster.xmementoit.co.uk --state s3://xmementoit-kops-cluster --yes
