class Application:
    def __init__(self, hospital_commands, dialog_with_user):
        self.hospital_commands = hospital_commands
        self.dialog_with_user = dialog_with_user

    def run(self):
        user_command = None
        while user_command not in ('stop', 'стоп'):
            user_command = self.dialog_with_user.request_user_command()
            self._execute(user_command)
        self.dialog_with_user.send_message("Сеанс завершён.")

    def _execute(self, command):
        if command in ("discharge", "выписать пациента"):
            self.hospital_commands.discharge()
        elif command in ('stop', 'стоп'):
            pass
