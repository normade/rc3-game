from django.views.generic.base import TemplateView
import logging

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.views.generic.base import TemplateView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from gamebot import models



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

wolfgang = ChatBot(**settings.CHATTERBOT)

class HomeView(TemplateView):
    template_name = "home.html"


def _get_isabot_response(user_input: str) -> dict:
    response_data = {}
    isa_response = wolfgang.get_response(user_input)
    response_data["text"] = isa_response.text

    return response_data

@api_view(["POST"])
@renderer_classes((JSONRenderer,))
def post_message(request: Request) -> Response:
    user_input = request.data.get("text").lower()

    return Response(_get_isabot_response(user_input), 200)