import logging

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.views.generic.base import TemplateView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from gamebot.models import CommunicationCategory


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

wolfgang = ChatBot(**settings.CHATTERBOT)


class HomeView(TemplateView):
    template_name = "home.html"


def _build_response(response_text: str, is_solution: bool) -> dict:
    response_data = {}
    response_data["text"] = response_text
    response_data["isSolution"] = is_solution

    return response_data


def _get_wolfgang_response(user_input: str) -> str:
    wolfgang_response = wolfgang.get_response(user_input)
    return wolfgang_response.text


def _find_keyword(user_input: str, category: CommunicationCategory) -> bool:
    keyword_list = category.accepted_keywords.split(",")
    return user_input in keyword_list


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
def post_message(request: Request) -> Response:
    user_input = request.data.get("text").lower()
    is_solution = False
    categories = CommunicationCategory.objects.all()

    for category in categories:
        keyword_found = _find_keyword(user_input, category)

        if keyword_found:
            if category.name == "Solution":
                is_solution = True
            return Response(_build_response(category.bot_answer, is_solution), 200)

    return Response(
        _build_response(_get_wolfgang_response(user_input), is_solution), 200
    )
