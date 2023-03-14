#!/usr/bin/python3
from cmd import Cmd
"""Console module is the entry point of the command interpreter"""


class HBNBCommand (Cmd):
    """Class definition of the command interpreter"""

    def __init__(self):
        """Initializes the cmd interpreter instance.\n"""
        super().__init__()
        self.intro = ""
        self.prompt = "(hbnb) "
        self.file = "cmd.json"
        # self.do_help()

    def do_quit(self, line):
        """\x1b[32m\x1b[1mQuit\x1b[0m
command to exit the program.\n"""
        return 'EOF'

    def do_EOF(self, line):
        """\x1b[32m\x1b[1mEOF\x1b[0m
End of file command to exit the program.\n"""
        return 'EOF'

    def emptyline(self):
        """Override Cmd.emptylines method.\n"""
        return False

    def do_help(self, line=""):
        """\x1b[32m\x1b[1mhelp\x1b[0m
\x1b[32m\x1b[1mhelp\x1b[0m \x1b[34m\x1b[1m*\x1b[0m
\x1b[32m\x1b[1mhelp\x1b[0m [\x1b[34m\x1b[1mcommand\x1b[0m...]
Without arguments, shows the list of available commands.
With arguments, shows the help for one or more commands.
Use "\x1b[34m\x1b[1mhelp *\x1b[0m" to show help for all commands at once.
The question mark "\x1b[34m\x1b[1m?\x1b[0m" can be used as an alias for \
"\x1b[34m\x1b[1mhelp\x1b[0m".\n
        """
        (command, args, ln) = Cmd.parseline(self, line)

        if command is None:
            return Cmd.do_help(self, line)

        commands = line.split()
        if "*" in commands:
            commands = self.get_names()
            commands = [i[3:] for i in commands if i.startswith(("do_"))]
            commands.sort()

        # for index, cmd in enumerate(commands):
        return Cmd.do_help(self, command)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
