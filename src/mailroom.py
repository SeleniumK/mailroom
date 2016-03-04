# -*- coding: utf-8 -*-


def thank_you():
    print("thank you selected")


def create_report():
    print("create report selected")




menus = {
    "main": {
        "message": "Please enter thank you or report:\n",
        "menu_options": {
            "thank you": thank_you,
            "report": create_report,
        },
    },
}


def menu_info(menu):
    return menu["message"], menu["menu_options"]


def get_menu(menu_name):
    return menus[menu_name]


def end_program():
    print("ending!")


def check_quit(user_answer):
    if user_answer == "quit":
        confirm = raw_input("Are you sure? \n")
        return confirm


def get_input(prompt, options):
    user_answer = raw_input(prompt)
    if user_answer not in options:
        get_input(prompt, options)
    return user_answer


def prompt_user(active_menu="main", hardcode_input=""):
    choice = hardcode_input
    message, options = menu_info(get_menu(active_menu))
    if not hardcode_input:
        choice = get_input(message, options)
    if check_quit(choice) == "y":
        end_program(active_menu)
    options[choice]()
    return choice


prompt_user("main")
