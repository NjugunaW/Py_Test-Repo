#!/usr/bin/python3
"""
This program contains the entry point of the command intepreter
"""

import cmd
import json

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State

from models import storage


class HBNBCommand(cmd.Cmd):

    intro = "Welcome to the HBNB console"
    # intro = r"""
    #
    #
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@          #####                                                           @@
    # @@@        ##     ##                                                         @@
    # @@@       #*   ((   #              ###        ##                  ##         @@
    # @@@     ##   /( (((  ##            ###        ##                  ##         @@
    # @@@    ##    ((((((   ##           #########  #######   ########  ########   @@
    # @@@   ##    ((((       ##          ###    ##  ##    ### ###   ### ##     ##  @@
    # @@@  ##     (((((       ##         ###    ##  ##     ## ###   ### ##     ### @@
    # @@@ #         *(          #        ###    ##  ########  ###   ### ########   @@
    # @@@ ##         (((         ##                                                @@
    # @@@ ##.     ##   ##     ###                                                  @@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #
    #
    # Welcome to the hbnb console
    # """
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

    # def do_help(self, arg: str):
    #     """
    #     This method displays custom help messages
    #     Args:
    #         arg:
    #
    #     Returns:
    #
    #     """
    #     if arg:
    #         super().do_help(arg)
    #     else:
    #         help_msg = r"""
    #         Available Commands(For detailed explanation including
    #         examples, run help <command>):
    #
    #         EOF or quit :   Exits the shell
    #         help        :   Displays this list
    #         create      :   Creates a new instance
    #         show        :   Prints a string representation of an
    #                         instance based on class name
    #         destroy     :   Deletes an instance based on the class
    #                         name and ID
    #         all         :   Prints all string representation of all instances
    #         update      :   Updates an instance based on the class name and id
    #                         by adding or updating attribute (save the change into
    #                         the JSON file).
    #         """
    #
    #         print(help_msg)

    def default(self, arg):
        """
        This method handles teh default command format where the class name
        comes first before the task
        Args:
            arg: The arguments passed

        Returns:

        """
        args = arg.strip('()').split(".")
        if len(args) < 2:
            print("*** Incomplete command ***")
            return
        all_objs = storage.all()
        cls_name = args[0]
        cmd_name = args[1].lower()
        cmd_and_attrib = cmd_name.strip(')').split('(')
        cmd_name = cmd_and_attrib[0]
        if cmd_name == "all":
            HBNBCommand.do_all(self, cls_name)
        elif cmd_name == "count":
            HBNBCommand.do_count(self, cls_name)
        elif cmd_name == "show":
            if len(cmd_and_attrib) < 2:
                print('** instance id missing **')
            else:
                HBNBCommand.do_show(self, cls_name + ' ' + cmd_and_attrib[1])
        elif cmd_name == "destroy":
            if len(cmd_and_attrib) < 2:
                print("** instance id missing **")
            else:
                HBNBCommand.do_destroy(self, cls_name + ' ' + cmd_and_attrib[1])
        elif cmd_name == "update":
            update_params = cmd_and_attrib[1].split(",")
            if len(update_params) < 1:
                print("** instance id missing **")
            elif len(update_params) < 2:
                print("** attribute name missing **")
            elif len(update_params) < 3:
                print("** value missing **")
            else:
                parts = arg.split('(')
                if len(parts) == 2:
                    upd_cmd_name = parts[0].strip()
                    args_part = parts[1].rstrip(')').strip()

                    if '.' in upd_cmd_name:
                        obj_name, cmd = upd_cmd_name.split('.')
                        if ',' in args_part:
                            id_str, json_str = map(str.strip, args_part.split(',', 1))
                            obj_id = id_str.strip('"')
                            HBNBCommand.do_update(self, cls_name + ' ' + obj_id + ' ' + json_str)


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
        elif cls_name not in HBNBCommand.hbnb_cmd_list:
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
        elif args[0] not in HBNBCommand.hbnb_cmd_list:
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
        elif args[0] not in HBNBCommand.hbnb_cmd_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
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
        if len(args) > 0 and args[0] not in HBNBCommand.hbnb_cmd_list:
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
        elif args[0] not in HBNBCommand.hbnb_cmd_list:
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
            our_obj = objs[f"{args[0]}.{args[1]}"]

            if args[2][0] == "{" and args[-1][-1] == "}":
                data_str = ' '.join(args[2:])
                try:
                    data = eval(data_str)
                    if not isinstance(data, dict):
                        print("** invalid dictionary syntax **")
                        return

                    for key, value in data.items():
                        if key in our_obj.__class__.__dict__.keys():
                            attr_type = type(our_obj.__class__.__dict__[key])
                            our_obj.__dict__[key] = attr_type(value)
                        else:
                            our_obj.__dict__[key] = value

                except SyntaxError:
                    print("** invalid dictionary syntax **")
                    return
            else:
                attribute = args[2]
                value = " ".join(args[3:])

                if attribute in our_obj.__class__.__dict__.keys():
                    attr_type = type(our_obj.__class__.__dict__[attribute])
                    our_obj.__dict__[attribute] = attr_type(value)
                else:
                    our_obj.__dict__[attribute] = value
        else:
            our_obj = objs[f"{args[0]}.{args[1]}"]
            if args[2] in our_obj.__class__.__dict__.keys():
                attr_type = type(our_obj.__class__.__dict__[args[2]])
                our_obj.__dict__[args[2]] = attr_type(args[3])
            else:
                our_obj.__dict__[args[2]] = args[3]
        BaseModel.save(self)

    def do_count(self, arg):
        """
        This method counts the number of instances of a class
        Args:
            arg:

        Example:
            count UserUser f650f143-6b7a-4630-a21b-562cda8f4a04 {'first_name': 'Chris', 'age': '32'}
        Returns:

        """
        count = 0
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.hbnb_cmd_list:
            print("** class doesn't exist **")
        else:

            for i in storage.all().values():
                if len(args) == 1 and args[0] == i.__class__.__name__:
                    count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
