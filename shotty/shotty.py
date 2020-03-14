import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "List EC2 instances"
    # See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance for more info
    for i in ec2.instances.all():
        s = ", ".join((
            i.instance_id,
            i.architecture,
            i.instance_type,
            i.state['Name'],
            i.placement['AvailabilityZone'],
            i.public_dns_name
        ))
        print( s )
    return 

if __name__ == "__main__":
    list_instances()
