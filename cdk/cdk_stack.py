from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class CdkLabNetworkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Define the VPC
        self.vpc = ec2.Vpc(self, "MyVpc",
            max_azs=2,  # Number of availability zones
            nat_gateways=1,  # Number of NAT Gateways
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="PublicSubnet",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    name="PrivateSubnet",
                    cidr_mask=24
                )
            ]
        )
