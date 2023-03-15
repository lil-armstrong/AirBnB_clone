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
import re
import sys
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
        "User",
        "City",
        "Amenity",
        "State",
        "Review",
        "Place",
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

        return self.parseLine(line)

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
        """Quit command to exit the program.\n"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program.\n"""
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
        """Usage: create <class>
Create a new class instance and print its id.\n"""
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
        """show model id
Print the string representation of an instance based \
on the class name and id
"""

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
        """Usage: destroy <class> <id> or <class>.destroy(<id>)\n
Delete a class instance based on the model name and id.
"""
        (cmd, id, ln) = Cmd.parseline(self, line)

        if (not self.isMissingClass(cmd)):
            if (self.isValidClass(cmd)):
                if (not self.isIdMissing(id)):
                    id = id.strip().split()[0]
                    key = storage.makeKey(cmd, id)
                    instance = self.getInstanceByKey(key)
                    if (instance is not None):

                        new = storage.remove(key)
                        storage.save()

    def do_count(self, line):
        """Usage: count <class> or <class>.count()\n
Retrieve the number of instances of a given class.
"""
        (cmd, id, ln) = Cmd.parseline(self, line)
        count = 0
        all = storage.all()

        if (not self.isMissingClass(cmd)):
            if (self.isValidClass(cmd)):
                for cls in all.values():
                    if cls.__class__.__name__ == cmd:
                        count += 1

        self.stdout.write("{}\n".format(str(count)))

    def do_fake(self, line):
        """Fake command"""
        (cmd, args, ln) = Cmd.parseline(self, line)
        print((cmd, args, ln))

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
Display string representations of all instances of a given class. 
If no class is specified, displays all instantiated objects.
"""
        (cmd, args, ln) = Cmd.parseline(self, line)
        all_obj = storage.all()
        models = args
        objs = []

        if models is not None:
            models = set(line.split())
        else:
            models = set()

        if not all([model in HBNBCommand.__classes for model in models]):
            self.stdout.write("** class doesn't exist **\n")
        else:
            if len(models) != 0:
                for model in all_obj.values():
                    cls = model.__class__.__name__
                    if cls in models:
                        objs.append(model)
            else:
                objs = all_obj.values()

            self.stdout.write("{}\n".format(str([str(v) for v in objs])))

    def do_update(self, line):
        """update
Usage: update <class name> <id> <attribute name> "<attribute value>"
Updates an instance based on the class name and id by adding or updating \
attribute.
"""
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
                            _type = str

                            # attr_value = eval(attr_value)

                            if isinstance(attr_value, (str)):
                                attr_value = str(attr_value).replace("'", "")

                            if attr_name in instance.__class__.__dict__.keys():
                                _type = type(
                                    instance.__getattribute__(attr_name))
                            instance.update(attr_name, _type(attr_value))

                        except Exception as e:
                            print(e)
                            pass

                        storage.save()

    def parseLine(self, line=""):
        """Parse line"""
        match = re.search("([A-Za-z]?=*\S*)\.([A-Za-z]?=*\S*)\((.*)\)", line)
        names = self.get_names()
        # commands = line.strip().split(".")

        if match and len(match.groups()) >= 2:
            # mtd, *args = mtd.split("(")
            cls, mtd, *args = match.groups()
            try:
                args = [eval(v) for v in ",".join(args).split(
                    ",") if isinstance(v, (str)) and len(v)]

                if mtd in [x[3:] for x in names
                           if x.startswith("do_")]:
                    command = "{} {} {}".format(mtd, cls, " ".join(args))
                    return command
            except Exception as e:
                print("\n[ERR! ({})]\n".format(e), file=sys.stderr)
                pass
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
