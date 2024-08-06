# Author: Miguel Angel Fernandez
# Course: CS361 - Software Engineering
# Description: Conversion microservice [written by teammate for Milestone #1]

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4692")

def convert(req):
    amount = float(req.get("amount"))
    unit_from = req.get("unit_from")
    unit_to = req.get("unit_to")

    if unit_from == unit_to:
        return req

    # check if it's a mass unit
    if unit_from in ["lb", "oz"]:
        match unit_from:
            case "oz":
                return amount / 16
            case "lb":
                return amount * 16

    # check if it's volume
    if unit_from in ["tsp", "tbsp", "cup", "pt", "qt", "gal", "fl oz"]:
        # convert everything to a gallon first
        match unit_from:
            case "tsp":
                amount = amount / 768
            case "tbsp":
                amount = amount / 256
            case "fl oz":
                amount = amount / 128
            case "cup":
                amount = amount / 15.7725
            case "pt":
                amount = amount / 8
            case "qt":
                amount = amount / 4

        # now convert from gallons to what we need

        match unit_to:
            case "gal":
                return amount
            case "qt":
                return amount * 4
            case "pt":
                return amount * 8
            case "cup":
                return amount * 15.7725
            case "fl oz":
                return amount * 128
            case "tbsp":
                return amount * 256
            case "tsp":
                return amount * 768

    return -1

while True:
    #  Wait for request from client
    print("Waiting for request...")
    convert_info = socket.recv_json() # a dictionary

    # Received request
    print(f'Received request: {convert_info}')
    time.sleep(1)

    conv_result = convert(convert_info)
    if conv_result == -1:
        result = "Sorry, your request could not be converted."
    else:
        input_amount = float(convert_info.get("amount"))
        input_unit = convert_info.get("unit_from")
        output_amount = conv_result
        output_unit = convert_info.get("unit_to")
        result = f"{input_amount} {input_unit} = {output_amount} {output_unit}"

    # Send response back
    print("Sending response...\n")
    time.sleep(1)
    socket.send_string(result)



