#!/usr/bin/env python3

# Import required modules
import argparse
import sys
import os



parser = argparse.ArgumentParser(prog='borfee', add_help=False, usage=argparse.SUPPRESS)
parser.add_argument('-h', '--help', nargs='?', help='Show this help message and exit.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0')
subparsers = parser.add_subparsers()

# Top level subparser's parsers
master_grp = subparsers.add_parser('master')
node_grp = subparsers.add_parser('node')
queue_grp = subparsers.add_parser('queue')
job_grp = subparsers.add_parser('job')

# Master cmd args section
subparsers = master_grp.add_subparsers()
master_action = subparsers.add_parser('init')
master_action.add_argument('master_init', nargs='?', help='Type init to start master')
master_action = subparsers.add_parser('halt')
master_action.add_argument('master_halt', nargs='?', help='Type halt to stop master')
master_action = subparsers.add_parser('remove')
master_action.add_argument('master_remove', nargs='?', help='Type remove to remove master')
master_add = subparsers.add_parser('add')
master_add.add_argument('master_hostname', help='Type master hostname')

# Node cmd args section
subparsers = node_grp.add_subparsers()
node_list = subparsers.add_parser('list')
node_list.add_argument('node_list', nargs='?', help='Type list to get list of nodes')
node_add = subparsers.add_parser('add')
node_add.add_argument('node_hostname', help='Type node hostname')
node_add.add_argument('add_node_queue_name', help='Type queue name')
node_remove = subparsers.add_parser('remove')
node_remove.add_argument('node_hostname', help='Type node hostname')
node_remove.add_argument('remove_node_queue_name', help='Type queue name')

# Queue cmd args section
subparsers = queue_grp.add_subparsers()
queue_list = subparsers.add_parser('list')
queue_list.add_argument('queue_list', nargs='?', help='Type list to get list of queues')
queue_add = subparsers.add_parser('add')
queue_add.add_argument('add_queue_name', help='Type queue name')
queue_add = subparsers.add_parser('remove')
queue_add.add_argument('remove_queue_name', help='Type queue name')

# job cmd args section
subparsers = job_grp.add_subparsers()
job_list = subparsers.add_parser('list')
job_list.add_argument('job_id_list', nargs='?', help='Type list to get list of jobs')
job_submit = subparsers.add_parser('submit')
job_submit.add_argument('submit_job', help='Type job details')
job_kill = subparsers.add_parser('kill')
job_kill.add_argument('kill_job', help='Type job id')

# Parse args
args = parser.parse_args()
#print(args)

# Display help
if len(sys.argv) == 2:
    os.system('cat /opt/borfee/conf/help.txt')
    sys.exit(0)

# Process master args
if 'master_init' in args:
    print("[MSG] Starting master")
    print(f"[MSG] Host {os.environ['HOSTNAME']} is now master")
if 'master_halt' in args:
    print("[MSG]Stopping master")
if 'master_remove' in args:
    print("[MSG] Removing master")
if 'master_hostname' in args:
    print(f"[MSG] Host {args.master_hostname} is now master")

# Process node args
if 'node_list' in args and args.node_list is None:
    print("<show table of nodes here>")
elif 'node_list' in args and args.node_list:
    print("<show details of node here>")
else:
    pass
if 'node_hostname' in args and 'add_node_queue_name' in args:
    print(f"[MSG] Node {args.node_hostname} added to {args.add_node_queue_name}")
if 'node_hostname' in args and 'remove_node_queue_name' in args:
    print(f"[MSG] Node {args.node_hostname} removed from {args.remove_node_queue_name}")

# Process queue args
if 'queue_list' in args:
    print("<show table of queues here>")
if 'add_queue_name' in args:
    print(f"[MSG] Added queue {args.add_queue_name}")
if 'remove_queue_name' in args:
    print(f"[MSG] Removed queue {args.remove_queue_name}")

# Process job args
if 'job_id_list' in args and args.job_id_list is None:
    print("<show table of jobs here>")
elif 'job_id_list' in args and args.job_id_list:
    print(f"<show details for {args.job_id_list}>")
else:
    pass
if 'submit_job' in args:
    print(f"[MSG] <job-id> submitted")
if 'kill_job' in args:
    print(f"[MSG] <job-id> killed")





