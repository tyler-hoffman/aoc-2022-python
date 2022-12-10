class HumanService:
    """Asks a question and gets returns a response
    from them as a string
    """

    def query(self, prompt: str) -> str:
        print(prompt)
        return input()


class HumanServiceFake(HumanService):
    """Fake for HumanService.
    Probably needed for CI unless I can figure out
    how to send and recieve sms messages to/from CI.
    """

    def __init__(self, response: str) -> None:
        self.response = response

    def query(self, _: str) -> str:
        return self.response
