#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from lambda_function import lambda_handler

__author__ = 'Logan. 81k'


def event_from_telegram(command):
    return {
        "message": {
            "from": {
                "username": "logan81k",
                "first_name": "\uae40\ud0dc\uc815",
                "last_name": "Logan K.",
                "id": "<your telegram id>",
                "language_code": "ko-KR"
            },
            "text": command,
            "entities": [
                {
                    "length": 4,
                    "type": "bot_command",
                    "offset": 0
                }
            ],
            "chat": {
                "type": "supergroup",
                "id": "<chat room id>",
                "title": "chat-ops"
            },
            "date": 1499162004,
            "message_id": 11
        },
        "update_id": 333205751
    }


lambda_handler(event_from_telegram('/aws sg prod api 124.5.119.214'), None)
# lambda_handler(event_from_telegram('/google firebase <topic>'), None)
