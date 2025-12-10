import pulumi
from pulumi_command import local

pulumi.log.info("Deploying command 'hello' - START...")
hello = local.Command(
    "hello",
    create="echo 'Hello from Pulumi local!'"
)

pulumi.log.info("Deploying command 'hello' - END...")
pulumi.export("message", hello.stdout)
