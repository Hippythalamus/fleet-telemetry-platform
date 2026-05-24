import json

packet_small = {
    "robot_id": "robot_1",
    "battery": 87.5,
}


def json_searilazion():

    json_str = json.dumps(packet_small)

    print(json_str)

    new_str = json.loads(json_str)

    print(new_str)
    print(packet_small)
