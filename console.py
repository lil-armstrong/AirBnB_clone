#!/usr/bin/python3
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models
import signal

storage = models.storage

"""Console module is the entry point of the command interpreter"""


class HBNBCommand (Cmd):
    """
    Class definition of the command interpreter

    Attributes:
        prompt(str): The command prompt.
    """
    __classes = {
        "BaseModel",
        "User"
    }

    def __init__(self, prompt="(hbnb) "):
        """Initializes the cmd interpreter instance.\n"""
        super().__init__()
        HBNBCommand.intro = ""
        HBNBCommand.prompt = prompt
        HBNBCommand.file = "cmd.json"
        # self.do_help()
        signal.signal(signal.SIGINT, handler=self._ctrl_c_handler)
        self._interrupted = False

    def _ctrl_c_handler(self, signal, frame):
        """Ctrl+C interrupt handler"""
        self._interrupted = True

    def precmd(self, line):
        """@Override Cmd.precmd method"""
        if self._interrupted:
            self._interrupted = False
            return ''

        if line == 'EOF':
            return 'quit'

        return line

    def isMissingClass(self, cls):
        """Check if class name is missing"""
        if cls is None:
            self.stdout.write("** class name missing **\n")
            return True
        return False

    def isValidClass(self, cls):
        """Check is class name is valid"""

        if cls in HBNBCommand.__classes:
            return True

        self.stdout.write("** class doesn't exist **\n")
        return False

    def isIdMissing(self, id):
        """Check if Id is None"""
        if id is None or len(id) == 0:
            self.stdout.write("** instance id missing **\n")
            return True
        return False

    def getInstanceByKey(self, key):
        """Check if the instance of the class name does exist for the id"""
        objs = storage.all()

        if key in objs:
            return objs[key]

        self.stdout.write("** no instance found **\n")
        return None

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """\x1b[32m\x1b[1mEOF\x1b[0m
EOF signal to exit the program.\n"""
        return 'quit'

    def emptyline(self):
        """Override Cmd.emptylines method.\n"""
        pass

    def do_help(self, line=""):
        """\x1b[32m\x1b[1mhelp\x1b[0m
\x1b[32m\x1b[1mhelp\x1b[0m\x1b[34m\x1b[1m *\x1b[0m
\x1b[32m\x1b[1mhelp\x1b[0m [\x1b[34m\x1b[1mcommand\x1b[0m...]
Without arguments, shows the list of available commands.
With arguments, shows the help for one or more commands.
Use "\x1b[34m\x1b[1mhelp *\x1b[0m" to show help for all commands at once.
The question mark "\x1b[34m\x1b[1m?\x1b[0m" can be used as an alias for
"\x1b[34m\x1b[1mhelp\x1b[0m".\n"""

        (command, args, ln) = Cmd.parseline(self, line)

        if command is None:
            Cmd.do_help(self, line)
            return False

        commands = set(line.split())
        if "*" in commands:
            commands = self.get_names()
            commands = [i[3:] for i in commands if i.startswith(("do_"))]
            commands.sort()

        for cmd in commands:
            Cmd.do_help(self, cmd)

    def do_create(self, line=""):
        """\x1b[32m\x1b[1mcreate\x1b[0m [\x1b[34m\x1b[1mmodel\x1b[0m...]
Creates a new instance of a model,
saves it and prints the id\n"""
        (cmd, args, ln) = Cmd.parseline(self, line)

        if cmd is None:
            self.stdout.write("** class name missing **\n")
            return False

        else:
            if cmd not in HBNBCommand.__classes:
                self.stdout.write("** class doesn't exist **\n")
                return False

        new = eval(cmd)()
        storage.save()
        self.stdout.write("{}\n".format(new.id))

    def do_show(self, line):
        """\x1b[32m\x1b[1mshow\x1b[0m \x1b[34m\x1b[1mmodel\x1b[0m \
\x1b[34m\x1b[1mid\x1b[0m
Print the string representation of an instance based on the \
class name and id\n"""

        (cmd, id, ln) = Cmd.parseline(self, line)

        if (not self.isMissingClass(cmd)):
            if (self.isValidClass(cmd)):
                if (not self.isIdMissing(id)):
                    id = id.strip().split()[0]
                    key = storage.makeKey(cmd, id)
                    instance = self.getInstanceByKey(key)
                    if (instance is not None):
                        self.stdout.write("{}\n".format(str(instance)))

    def do_destroy(self, line):
        """\x1b[32m\x1b[1mdestroy\x1b[0m \x1b[34m\x1b[1mmodel\x1b[0m \
\x1b[34m\x1b[1mid\x1b[0m
Delete a model instance based on the model name and id\n"""
        (cmd, id, ln) = Cmd.parseline(self, line)

        if (not self.isMissingClass(cmd)):
            if (self.isValidClass(cmd)):
                if (not self.isIdMissing(id)):
                    id = id.strip().split()[0]
                    key = storage.makeKey(cmd, id)
                    instance = self.getInstanceByKey(key)
                    if (instance is not None):

                        new = storage.remove(key)
                        storage.save(new)

    def do_all(self, line):
        """\x1b[32m\x1b[1mall\x1b[0m\x1b[34m\x1b[1m \x1b[0m
\x1b[32m\x1b[1mall\x1b[0m [\x1b[34m\x1b[1mmodel...\x1b[0m]
Without arguments, prints all the string representation of all available models
With arguments, prints the string representation of one or more models.\n"""
        (cmd, args, ln) = Cmd.parseline(self, line)
        all = storage.all()
        models = args
        objs = {}

        if isinstance(models, (str)):
            models = set(line.split())
        else:
            models = set()

        if len(models) != 0:
            for model in models:
                objs[model] = []
                if not (self.isValidClass(model)):
                    continue

                objs[model] = [str(m) for m in all.values()
                               if m.__class__.__name__ == model]
        else:
            for v in all.values():
                m = v.__class__.__name__
                if not (m in objs):
                    objs[m] = []
                else:
                    objs[m].append(str(v))

        for v in objs.values():
            if len(v) != 0:
                self.stdout.write("{}\n".format(str(v)))

    def do_update(self, line):
        """\x1b[32m\x1b[1mupdate\x1b[0m <\x1b[34m\x1b[1mclass name\x1b[0m> \
<\x1b[34m\x1b[1mid\x1b[0m> <\x1b[34m\x1b[1mattribute name\x1b[0m> \
"<\x1b[34m\x1b[1mattribute value\x1b[0m>"
Updates an instance based on the class name and id by adding or updating \
attribute\n"""
        (cmd, args, ln) = Cmd.parseline(self, line)

        if (not self.isMissingClass(cmd)):
            if (self.isValidClass(cmd)):
                if (not self.isIdMissing(args)):
                    id, *attrib = args.strip().split()
                    key = storage.makeKey(cmd, id)
                    instance = self.getInstanceByKey(key)
                    if (instance is not None):
                        if len(attrib) == 0:
                            self.stdout.write("** attribute name missing **\n")
                            return
                        if len(attrib) != 2:
                            self.stdout.write("** value missing **\n")
                            return

                        try:
                            attr_name, attr_value = attrib
                            # i_type = instance.__getattribute__(attr_name)
                            # print(id, attr_name, attr_value, i_type)
                            instance.update(attr_name, attr_value)
                        except Exception as e:
                            print(e)
                            pass
                    #     new = storage.remove(key)
                    #     print(new)
                    #     storage.save(new)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
