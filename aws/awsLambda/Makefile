#
# Makefile
# damian, 2019-03-26 13:53
#


ZIP_PACKAGE=example.zip
S3_BUCKET=example-serverless-bucket
AWS_REGION=${AWS_DEFAULT_REGION}

all: zipsrc
	aws s3api create-bucket --bucket ${S3_BUCKET} --region ${AWS_REGION} --create-bucket-configuration LocationConstraint=${AWS_REGION}
	aws s3 cp ${ZIP_PACKAGE} s3://${S3_BUCKET}/v1.0.0/${ZIP_PACKAGE}
	terraform init
	terraform apply -auto-approve
	aws lambda invoke --region=${AWS_REGION} --function-name=ServerlessExample output.txt
	cat output.txt


clean: 
	aws s3 rb s3://${S3_BUCKET} --force
	terraform destroy -force

zipsrc:
	zip -j ${ZIP_PACKAGE} src/main*

