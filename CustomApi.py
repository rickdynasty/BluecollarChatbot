from rasa.core.channels.channel import InputChannel,UserMessage,RestInput,CollectingOutputChannel
from sanic import Sanic, Blueprint, response
import asyncio
import inspect
import json
import logging
import uuid
from asyncio import Queue, CancelledError
from sanic import Sanic, Blueprint, response
from sanic.request import Request
from typing import Text, List, Dict, Any, Optional, Callable, Iterable, Awaitable
import rasa.utils.endpoints
from rasa.cli import utils as cli_utils
from rasa.constants import DOCS_BASE_URL
from rasa.core import utils
from sanic.response import HTTPResponse
from typing import NoReturn

from apis.ibapi import query_by_id
from log.BCLog import log


logger = logging.getLogger(__name__)


class CustomApi(RestInput):
    @classmethod
    def name(cls) -> Text:
        return "CustomApi"

    def blueprint(self, on_new_message: Callable[[UserMessage], Awaitable[None]]) -> Blueprint:
        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            inspect.getmodule(self).__name__,
        )

        # noinspection PyUnusedLocal
        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request) -> HTTPResponse:
            return response.json({"status": "ok"})

        @custom_webhook.route("/cloudstatus", methods=["GET"])
        async def cloudstatus(request: Request) -> HTTPResponse:
            return response.json({"status": "UP"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request: Request) -> HTTPResponse:
            #todo
            # 1 参数转换 done
            # 2 请求转发 done
            # 注： 前端加上senderId
            sender_id = await self._extract_sender(request)
            text = self._extract_message(request)

            should_use_stream = rasa.utils.endpoints.bool_arg(
                request, "stream", default=False
            )
            input_channel = self._extract_input_channel(request)
            metadata = self.get_metadata(request)


            answer_id = self._extract_answer_id(request)
            problem_id = self._extract_answer_id(request)
            if answer_id is not None or problem_id is not None:
                return response.json(query_by_id(request.json))

            # rasa 处理

            if should_use_stream:
                return response.stream(
                    self.stream_response(
                        on_new_message, text, sender_id, input_channel, metadata
                    ),
                    content_type="text/event-stream",
                )
            else:
                collector = CollectingOutputChannel()
                # noinspection PyBroadException
                try:
                    await on_new_message(
                        UserMessage(
                            text,
                            collector,
                            sender_id,
                            input_channel=input_channel,
                            metadata=metadata,
                        )
                    )
                except CancelledError:
                    logger.error(
                        "Message handling timed out for "
                        "user message '{}'.".format(text)
                    )
                except Exception:
                    logger.exception(
                        "An exception occured while handling "
                        "user message '{}'.".format(text)
                    )
                return response.json(collector.messages)

        return custom_webhook

    def _extract_message(self,req:Request):
        return req.json.get('inputText')
    
    def _extract_answer_id(self,req:Request):
        ask_param = req.json.get('askParam')
        if ask_param is not None:
            return ask_param['answerId']
        return None
    
    def _extract_problem_id(self,req:Request):
        ask_param = req.json.get('askParam')
        if ask_param is not None:
            return ask_param['problemId']
        return None