#!/usr/bin/python3
"""
This program contains the entry point of the command intepreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class hbnb_cmd(cmd.Cmd):
    intro = "\nWelcome to the hbnb console\n\n"
    prompt = "(hbnb) "

    hbnb_cmd_list = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    ]

    def do_quit(self, arg):
        """
        Exits the interactive shell
        Args:
            arg:

        Returns:

        """
        print("Quitting... Goodbye")
        return True

    def do_EOF(self, arg):
        """
        Exits the interactive shell
        Args:
            arg:

        Returns:

        """
        print("Exiting... Goodbye")
        return True

    def emptyline(self):
        """
        This method executes nothing when there is an
        empty line
        Returns:

        """
        pass

    def do_help(self, arg: str):
        """
        This method displays custom help messages
        Args:
            arg:

        Returns:

        """
        if arg:
            super().do_help(arg)
        else:
            help_msg = r"""
            Available Commands(For detailed explanation including
            examples, run help <command>):
            
            EOF or quit :   Exits the shell
            help        :   Displays this list
            create      :   Creates a new instance
            show        :   Prints a string representation of an
                            instance based on class name
            destroy     :   Deletes an instance based on the class
                            name and ID
            all         :   Prints all string representation of all instances
            update      :   Updates an instance based on the class name and id
                            by adding or updating attribute (save the change into
                            the JSON file).
            """

            print(help_msg)

    #         Custom Commands

    def do_create(self, cls_name):
        """
        This method creates a new instance of
        Base Model, saves it to a json file and
        prints the id
        Args:
            cls_name: The class name

        Examples:
            create BaseModel

        Returns:

        """
        if len(cls_name) == 0:
            print("** class name missing **")
        elif cls_name not in hbnb_cmd.hbnb_cmd_list:
            print("** class doesn't exist **")
        else:
            print(eval(cls_name)().id)
            storage.save()

    def do_show(self, arg):
        """
        This method prints the string representation of an instance
        based on the class name and  id
        Args:
            arg

        Examples:
            show <class Name> <id>
            show BaseModel 1234-1234-1234

        Returns:

        """
        args = arg.split()
        objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in hbnb_cmd.hbnb_cmd_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
        else:
            print(objs[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """
        This method deletes an instance based on the class name
        and it's ID
        Args:
            arg

        Examples:
            destroy <class name> <id>
            destroy BaseModel 1234-1234-1234

        Returns:

        """
        args = arg.split()
        objs = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in hbnb_cmd.hbnb_cmd_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
            print(objs)
        else:
            del objs[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, cls_name):
        """
        This method prints all string representation of all
        instances either alone or by class name
        Args:
            cls_name: The class name

        Examples:
            all BaseModel
            all

        Returns:

        """
        args = cls_name.split()
        if len(args) > 0 and args[0] not in hbnb_cmd.hbnb_cmd_list:
            print("** class doesn't exist **")
        else:
            object_list = []
            for i in storage.all().values():
                if len(args) == 1 and args[0] == i.__class__.__name__:
                    object_list.append(i.__str__())
                elif len(args) == 0:
                    object_list.append(i.__str__())
            for obj in object_list:
                print(obj)

    def do_update(self, arg):
        """
        This method updates an instance based on the class name and
        id by adding or updating attributes
        Args:
            arg:

        Examples:
            update <class name> <id> <attribute> "<value>"
            update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Returns:

        """

        args = arg.split()
        objs = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in hbnb_cmd.hbnb_cmd_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) > 4:
            del args[4:]
        else:
            our_obj = objs[f"{args[0]}.{args[1]}"]
            if args[2] in our_obj.__class__.__dict__.keys():
                attr_type = type(our_obj.__class__.__dict__[args[2]])
                our_obj.__dict__[args[2]] = attr_type(args[3])
            else:
                our_obj.__dict__[args[2]] = args[3]
        storage.save()

if __name__ == "__main__":
    console = hbnb_cmd()
    console.cmdloop()
