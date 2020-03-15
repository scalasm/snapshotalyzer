import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

def get_instances(project):
    """Get instances by tagged with a given 'Project' tag, or all instances if no project is provided"""
    instances = []
    if project:
        filters = [{'Name': 'tag:Project', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
    return instances

# Main comman group: under it we create sub-groups with specific commands
@click.group()
def cli():
    """Shotty manages snapshots"""

# Subgroup for instances commands
@cli.group('instances')
def instances():
    """Commands for instances"""

# Subgroup for volumes commands
@cli.group('volumes')
def volumes():
    """Commands for volumes"""

# Subgroup for snapshots commands
@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""

@instances.command('list')
@click.option( '--project', default=None, 
    help="Only instances for project (tag Project:<NAME>" )
def list_instances(project):
    "List EC2 instances"

    # See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance for more info
    for i in get_instances(project):
        # Convert instance tags (if present from a list of dictionaries to a dictionary)
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        s = ", ".join((
            i.instance_id,
            i.architecture,
            i.instance_type,
            i.state['Name'],
            i.placement['AvailabilityZone'],
            i.public_dns_name,
            tags.get('Project','<no project>')
        ))
        print( s )
    return 

@instances.command('stop')
@click.option( '--project', default=None, 
    help="Only instances for project (tag Project:<NAME>" )
def stop_instances(project):
    "Stop EC2 instances"

    for i in get_instances(project):
        print( "Stopping {0} ...".format(i.id) )
        i.stop()

@instances.command('start')
@click.option( '--project', default=None, 
    help="Only instances for project (tag Project:<NAME>" )
def start_instances(project):
    "Start EC2 instances"

    for i in get_instances(project):
        print( "Starting {0} ...".format(i.id) )
        i.start()

@instances.command('snapshot')
@click.option( '--project', default=None, 
    help="Only instances for project (tag Project:<NAME>" )
def snapshot_instances(project):
    "Create a snapshot of EC2 instances"

    for i in get_instances(project):
        for v in i.volumes.all():
            print( "Stopping {0} ...".format(i.id) )
            i.stop()
            i.wait_until_stopped()
            print("Creating a snapshot of {0}".format(v.id))
            v.create_snapshot(Description="Created by Snapshotalyzer")
            print( "Restarting {0} ...".format(i.id) )
            i.start()
            i.wait_until_running()

@volumes.command('list')
@click.option( '--project', default=None, 
    help="Only instances for project (tag Project:<NAME>" )
def list_volumes(project):
    "List all volumes and associated EC2 instances"

    # See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance for more info
    for i in get_instances(project):
        for v in i.volumes.all():
            print( ", ".join( ( 
                v.id,
                i.id,
                v.state,
                str(v.size)+ "GiB",
                v.encrypted and "Encrypted" or "Not encrypted"
            ) ))
    return

@snapshots.command('list')
@click.option( '--project', default=None, 
    help="Only instances for project (tag Project:<NAME>" )
def list_snapshots(project):
    "List all snapshots for EC2 volumes"

    # See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance for more info
    for i in get_instances(project):
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print( ", ".join( (
                    s.id, 
                    v.id,
                    i.id,
                    s.start_time.strftime("%c"),
                    s.state,
                    s.progress,
                    str(s.volume_size)+ "GiB",
                    s.encrypted and "Encrypted" or "Not encrypted",
                ) ))
    return

if __name__ == "__main__":
    cli()
