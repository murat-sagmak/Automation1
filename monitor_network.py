from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
import time
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def get_device_status(task):
    result = task.run(task=netmiko_send_command, command_string="show ip interface brief")
    task.host["status"] = result.result
    print(result)
    print(result)

    

