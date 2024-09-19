class MockConsole:
    def __init__(self):
        self._console_commands = []

    def _get_current_command(self):
        return self._console_commands.pop(0)

    def print(self, message):
        current_command = self._get_current_command()
        assert type(current_command) == str
        assert message == current_command, f'\nactual_output_message = "{message}"' \
                                            f'\nexpected_output_message = "{current_command}"'

    def input(self, request):
        current_command = self._get_current_command()
        assert type(current_command) in (tuple, list)
        expected_request, expected_response = current_command
        assert request == expected_request, f'\nactual_request = "{request}"' \
                                            f'\nexpected_request = "{expected_request}"'
        return expected_response

    def add_expected_request_and_response(self, request, response):
        self._console_commands.append((request, response))

    def add_expected_output_message(self, message):
        self._console_commands.append(message)

    def verify_all_calls_have_been_made(self):
        assert len(self._console_commands) == 0
