# -*- coding: utf-8 -*-
prompts = {
    "welcome": "Please enter 'thank you' to write a letter, or 'report' to create a report (or 'list' to see all options: \n",
}


def thank_you():
    print("thank you selected")


def create_report():
    print("create report selected")


def list_options():
    for key in main_menu:
        print key


def end_program():
    print("you can't quit now!")

main_menu = {
    "thank you": thank_you,
    "report": create_report,
    "list": list_options,
    "quit": end_program
}


def get_input(prompt, menu_options):
    user_answer = raw_input(prompt)
    if user_answer not in menu_options:
        get_input(prompt, menu_options)
    return user_answer


def welcome_prompt():
    print('welcome message')
    choice = get_input(prompts["welcome"], main_menu)
    main_menu[choice]()
