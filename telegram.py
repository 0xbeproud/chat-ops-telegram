#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests

from properties import ENV_TELEGRAM_BOT_TOKEN

__author__ = 'Logan. 81k'


def send_telegram_to(chat_id, message):
    print('chat_id: {}, message: {}'.format(chat_id, message))
    requests.post(
        url='https://api.telegram.org/bot{0}/sendMessage'.format(ENV_TELEGRAM_BOT_TOKEN),
        data={
            'chat_id': '{}'.format(chat_id),
            'text': '{}'.format('{}'.format(message))
        },
        timeout=10
    )
