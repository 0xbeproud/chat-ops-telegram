#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from cmd.command import command_invalid

__author__ = 'Logan. 81k'


def command_aws_sg(chat_id, cmd):
    print('command_aws_sg -> {} {}'.format(chat_id, cmd))
    state = cmd[2]  # search, open, close
    ip = cmd[4]  # ip address

    command_aws_sg_dict = {
        'search': aws_sg_search,
        'open': aws_sg_open,
        'close': aws_sg_close
    }

    # cmd[2] ==> ip address
    return command_aws_sg_dict.get(state, lambda x, y: command_invalid(x, y))(chat_id, cmd)


def aws_sg_search(chat_id, cmd):
    print('command_aws_sg -> aws_sg_search {} {}'.format(chat_id, cmd))


def aws_sg_open(chat_id, cmd):
    print('command_aws_sg -> aws_sg_open {} {}'.format(chat_id, cmd))


def aws_sg_close(chat_id, cmd):
    print('command_aws_sg -> aws_sg_close {} {}'.format(chat_id, cmd))
