import json
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    parameters = json.loads('{"joint":"6930fc20e1c9963d56d36eda","control_mode":"position","limit.lower_position":0,"limit.upper_position":360,"limit.position_step":1,"limit.max_effort":10,"limit.effort_step":null,"limit.max_velocity":35,"limit.velocity_step":0}')
    configuration = json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')
    inbound_connections = json.loads('[]')
    outbound_connections = json.loads('[]')
    env = {
        "POLYFLOW_NODE_ID": "6931084c4572a135bff5b265",
        "POLYFLOW_PARAMETERS": json.dumps(parameters),
        "POLYFLOW_CONFIGURATION": json.dumps(configuration),
        "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(inbound_connections),
        "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(outbound_connections),
    }

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["python3", "workspace/src/odrive_s1/odrive_s1/node.py"],
                additional_env=env,
                output="screen",
            )
        ]
    )