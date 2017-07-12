#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'Logan. 81k'


def parsing_command(predefined_command, chat_id, cmd, index):
    for key, v in predefined_command.items():
        print('k:{} / v:{}'.format(key, v))
        if key == cmd[index]:
            print('{} == {}'.format(key, cmd[index]))
            index += 1
            if isinstance(v, dict):
                if len(cmd) <= index:
                    return None
                return parsing_command(v, chat_id, cmd, index)
            elif isinstance(v, bool):
                print("is boolean")
                return v
            elif callable(v):
                print('-- callable: {}'.format(v.__call__))
                return predefined_command.get(key, lambda x, y: command_invalid(x, y))(chat_id, cmd)
            else:
                print('eeeeeeeeeeeeeee')
    return command_invalid(chat_id, cmd)


def command_invalid(chat_id, cmd):
    # send_telegram_to(chat_id, 'invalid command: {}'.format(cmd))
    print('invalid command: {}'.format(cmd))
