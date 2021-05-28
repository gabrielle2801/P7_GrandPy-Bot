import re
from grandpy_bot.constant import PATTERN_PARSER


class MatchNotFound(Exception):
    pass


def parse_search(user_request):
    for p in PATTERN_PARSER:
        response = re.search(p, user_request)
        if response:
            result_regex = response.group(1).strip()
            return result_regex
    if not response:
        raise MatchNotFound("Oospy demande incorrect, reformulez votre demande")
