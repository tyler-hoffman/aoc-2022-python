class HumanService:
    """Asks a question and gets returns a response
    from them as a string
    """

    query_start_string = "[START QUERY]"
    query_end_string = "[START QUERY]"

    def query(self, prompt: str) -> str:
        print(self.get_start_line(prompt))
        print(prompt)
        print(self.get_end_line(prompt))
        print("answer plz: ", end="")
        return input()

    def get_start_line(self, prompt: str) -> str:
        return self.end_with_line(self.query_start_string, prompt)

    def get_end_line(self, prompt: str) -> str:
        return self.end_with_line(self.query_end_string, prompt)

    def end_with_line(self, start: str, prompt: str) -> str:
        start = self.query_start_string + " "
        desired_len = self.get_prompt_length(prompt)
        start_len = len(start)
        return start + "=" * (desired_len - start_len)

    def get_prompt_length(self, prompt: str) -> int:
        lines = prompt.split("\n")
        lengths = [len(line) for line in lines]
        return max(lengths)
