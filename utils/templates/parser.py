def create_parser_stub() -> str:
    return _PARSER_TEMPLATE


_PARSER_TEMPLATE = """
class Parser(object):
    @staticmethod
    def parse(input: str) -> str:
        return input.strip()

"""
