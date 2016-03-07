# -*- coding: utf-8 -*-
import sys
from math import trunc

try:
    input = raw_input
except NameError:
    pass


def list_options():
    for key in main_menu:
        print(key)
    for glob in global_menu:
        print(glob)
    main_prompt()


def end_program():
    print("Goodbye!")
    sys.exit()


def write_email(name, donor_hist):
    if len(donor_hist) > 1:
        don_amt = "We noticed you've donated {} times before. We hope that you will choose to donate again soon.".format(len(donor_hist))
    else:
        don_amt = "We appreciate your first donation!"
    print("""Hello {},\n
        Thank your for your most recent donation of ${}.
        {}\n
        Have a great day!\n
        Selena and Rick
        """.format(name, donor_hist[-1], don_amt))


def get_donation(donor_hist, hardcode_input=""):
    amt = hardcode_input
    if not amt:
        amt = input(PROMPTS["donation"])
    amt = int(amt)
    donor_hist.append(amt)
    return donor_hist


def list_donors():
    for name in donors:
        print(name)
    thank_you()


def thank_you():
    name = input(PROMPTS["letter"]).lower()
    if name == "list":
        list_donors()
    elif name in global_menu:
        global_menu[name]()
    else:
        if name not in donors:
            donors.setdefault(name, [])
        this_donation = get_donation(donors[name])
        write_email(name, this_donation)
        main_prompt()


def sort_donors():
    sorted_donors = sorted(donors, key=lambda donor: sum(donors[donor]), reverse=True)
    return sorted_donors


def create_report():
    print("create report selected")
    for donor in sort_donors():
        value = donors[donor]
        ave = sum(value) / len(value)
        print("""Name: {},\n Donations: {},\n Total Donations:{},\n Number of Donations: {},\n Average Donations: {}\n
        """.format(donor, value, sum(value), len(value), trunc(ave)))
    main_prompt()


def get_input(prompt, options):
    user_answer = input(prompt).lower()
    if user_answer == "quit":
        end_program()
    elif user_answer not in options:
        user_answer = get_input(prompt, options)
    return user_answer


def main_prompt(hardcode_input=""):
    choice = hardcode_input
    if not choice:
        choice = get_input(PROMPTS["main"], main_menu)
    main_menu[choice]()
    return choice


def start_program():
    print('welcome message')
    main_prompt()


donors = {
    "selena": [25, 10, 15],
    "patricia": [100, 200, 300],
    "disa": [15, 15, 15],
    "terry": [5, 30, 5],
}


PROMPTS = {
    "main": "Letter or Report? \n Enter 'options' to see all options: \n",
    "letter": "Enter Name of Donor, Enter 'list' to see all, or enter 'back' to go to main menu: \n",
    "donation": "How much did they donate? Please enter a whole dollar amount: \n",
}

global_menu = {
    "back": main_prompt,
    "quit": end_program,
}


main_menu = {
    "letter": thank_you,
    "report": create_report,
    "options": list_options,
    "quit": end_program,
}

start_program()
