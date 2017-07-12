#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from cmd import command_aws, command_google
from cmd.command import parsing_command


def lambda_handler(event, context):
    chat_id = str(event['message']['chat']['id'])
    message_text = str(event['message']['text'])[1:]  # slice prefix "/"
    command = message_text.split(' ')
    print(command)

    predefined_command_dict = {
        "aws": {
            "sg": command_aws
        },
        "google": command_google
    }

    parsing_command(predefined_command_dict, chat_id, command, 0)
    return 'Ok'
