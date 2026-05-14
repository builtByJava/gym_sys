
#this program will create a Gym Membership Management System derived from a base generic Membership System parent class.
#this program is meant to be used by a User to register with the PL Mountain Gym and perform various actions such as:
# ---> checking current gym class spot availability / schedules
# --> adding a class to their account
# --> dropping a class from their account
# --> adding a guest to their account
# --> dropping a guest from their account
# --> obtaining a detailed summary of their account
# --> updating their payment method on their account
# --> cancelling their membership
# --> exiting the membership system


### IMPORTS ###
import datetime

### CLASSES ###
class MembershipSystem:
    def __init__(self, full_name='', mailing_address='', city='', state='', zipcode=0, payment_method='', status='', cost=0.00):
        self.full_name = full_name
        self.mailing_address = mailing_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.payment_method = payment_method
        self.status = status
        self.cost = cost

    def set_membership_info(self, full_name, mailing_address, city, state, zipcode, payment_method, status, cost):
        self.full_name = full_name
        self.mailing_address = mailing_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.payment_method = payment_method
        self.status = status
        self.cost = cost

    def get_membership_info(self):
        print("-" * 100)
        print(f"{'Account Details':^100}")
        print("-" * 100)
        print(f"Name on Account:{self.full_name}")
        print(f"Home Address: {self.mailing_address}{" " * 2}{self.city}{" " * 2}{self.state}{" " * 2}{self.zipcode}")
        print(f"Current Payment Method: {self.payment_method}")
        print(f"Membership Status: {self.status} - last updated at: {datetime.datetime.now()}")
        print(f"Membership Cost Per Month: {self.cost}")

    def set_new_payment_method(self, payment_method):
        print(f"Your current payment method is: {self.get_current_payment_method()}")
        while True:
            try:
                available_payment_methods = ["cash", "credit card"]
                updated_payment_method = input("which payment method would you like to switch to - cash or credit card?:").lower()
                if updated_payment_method == 'q':
                    print("exiting...")
                    quit()
                if not updated_payment_method in available_payment_methods:
                    raise ValueError("Please select either cash or credit card")

                print(f"Please check option 6 - Detailed Account Summary to see updated information")
                self.payment_method = updated_payment_method
                break
            except ValueError as v3:
                print(v3)

    def get_current_payment_method(self):
        return self.payment_method


    def cancel_membership(self):
        MembershipSystem.set_membership_info(self, self.full_name, self.mailing_address, self.city, self.state, self.zipcode, payment_method='N/A - Cancelled Membership', status='Inactive', cost=0.00)
        print(f"Please check option 6 - Detailed Account Summary to see updated information")


class GymMembershipSystem(MembershipSystem):

    list_of_guests = []
    list_of_classes = []
    desired_day = ""
    number_of_class_spots_available_in_sunday_body_building = 10
    number_of_class_spots_available_in_monday_pilates = 10
    number_of_class_spots_available_in_tuesday_crossfit = 10
    number_of_class_spots_available_in_wednesday_kickboxing = 10
    number_of_class_spots_available_in_thursday_weight_training = 10
    number_of_class_spots_available_in_friday_spin = 10
    number_of_class_spots_available_in_saturday_crossfit = 10

    gym_class_schedule_dict = {
        "sunday":  {"body building": number_of_class_spots_available_in_sunday_body_building},
        "monday": {"pilates": number_of_class_spots_available_in_monday_pilates},
        "tuesday": {"crossfit": number_of_class_spots_available_in_tuesday_crossfit},
        "wednesday": {"kickboxing": number_of_class_spots_available_in_wednesday_kickboxing},
        "thursday": {"weight training": number_of_class_spots_available_in_thursday_weight_training},
        "friday": {"spin": number_of_class_spots_available_in_friday_spin},
        "saturday": {"crossfit advanced": number_of_class_spots_available_in_saturday_crossfit}
    }

    list_of_menu_items = ["Navigator Menu:\n",
                          "1) Check Gym Class Schedules \n",
                          "2) Add a Guest to your Account \n",
                          "3) Add a Gym Class to your Account \n",
                          "4) Drop a Gym Class from your Account \n",
                          "5) Drop a Guest from your Account \n"
                          "6) Detailed Account Summary\n",
                          "7) Change Payment Method\n",
                          "8) Cancel Membership\n",
                          "9) Exit System"]

    def __init__(self, full_name, mailing_address, city, state, zipcode, payment_method, status, cost, type_of_membership, personal_trainer_needed, list_of_classes, list_of_guests):
        MembershipSystem.__init__(self, full_name, mailing_address, city, state, zipcode, payment_method, status, cost)
        self.type_of_membership = type_of_membership
        self.personal_trainer_needed = personal_trainer_needed
        self.list_of_classes = list_of_classes
        self.list_of_guests = list_of_guests

    def check_gym_class_schedule(self):
        print("=" * 100)
        print(f"{'PL Mountain Gym Class Schedule':^50}")
        print("=" * 100)
        for key, val in self.gym_class_schedule_dict.items():
            print(f"{key}: {val}")

    def enroll_in_gym_class(self):
        days_of_the_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday","saturday"]
        gym_classes_offered = ["body building", "pilates", "crossfit", "kickboxing", "weight training", "spin", "crossfit advanced"]
        while True:
                try:
                    gs.check_gym_class_schedule()
                    my_day = input("Which day do you want to attend your class? press Q to quit:").lower()
                    if my_day == 'q':
                        print("exiting...")
                        quit()
                    if my_day.isdigit():
                       raise ValueError("Please only enter alphanumeric characters that spell a day of the week")
                    if not my_day in days_of_the_week:
                        raise ValueError("Please enter a valid day of the week")

                    my_class = input("Which class do you want to attend? press Q to quit:").lower()
                    if my_class == 'q':
                        print("exiting...")
                        quit()
                    if my_class.isdigit():
                        raise ValueError("Please only enter alphanumeric characters")
                    if not my_class in gym_classes_offered:
                        raise ValueError("Please only enter valid gym classes that are offered at PL Mountain Gym")

                    print(f"Please check option 6 - Detailed Account Summary to see updated information")
                    self.list_of_classes.append(my_class)
                    gs.set_class_spots_available(my_day, my_class)
                    for c in self.list_of_classes:
                        print(f"Your updated class list: {c}")
                    gs.menu_navigator()
                except ValueError as v3:
                    print(v3)


    def get_class_spots_available(self):
        print(f"{self.number_of_class_spots_available_in_sunday_body_building}")

    def set_class_spots_available(self,desired_day, desired_class):
        self.desired_day = desired_day
        self.desired_class = desired_class

        match self.desired_day.lower():
            case "sunday":
                self.gym_class_schedule_dict[desired_day][desired_class] = self.number_of_class_spots_available_in_sunday_body_building - 1
            case "monday":
                self.gym_class_schedule_dict[desired_day][desired_class] = self.number_of_class_spots_available_in_monday_pilates - 1
            case "tuesday":
                self.gym_class_schedule_dict[desired_day][desired_class] = self.number_of_class_spots_available_in_tuesday_crossfit - 1
            case "wednesday":
                self.gym_class_schedule_dict[desired_day][desired_class] = self.number_of_class_spots_available_in_wednesday_kickboxing - 1
            case "thursday":
                self.gym_class_schedule_dict[desired_day][desired_class] = self.number_of_class_spots_available_in_thursday_weight_training - 1
            case "friday":
                self.gym_class_schedule_dict[desired_day][desired_class] = self.number_of_class_spots_available_in_friday_spin - 1
            case "saturday":
                self.gym_class_schedule_dict[desired_day][desired_class] = self.number_of_class_spots_available_in_saturday_crossfit - 1
        gs.menu_navigator()

    def drop_a_gym_class(self):
        days_of_the_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday","saturday"]
        gym_classes_offered = ["body building", "pilates", "crossfit", "kickboxing", "weight training", "spin", "crossfit advanced"]
        while True:
            try:
                remove_day = input("Which day do you want to drop? press Q to quit:").lower()
                if remove_day == 'q':
                    print("exiting...")
                    quit()
                if remove_day.isdigit():
                    raise ValueError("Please only enter alphanumeric characters that spell a day of the week")
                if not remove_day in days_of_the_week:
                    raise ValueError("Please enter only valid days of the week")

                class_name = input("Which class would you like to drop? press Q to quit:").lower()
                if class_name == 'q':
                    print("exiting...")
                    quit()
                if class_name.isdigit():
                    raise ValueError("Please only enter alphanumeric characters")
                if not class_name in gym_classes_offered:
                    raise ValueError("Please only enter gym classes offered at PL Mountain Gym")

                match remove_day.lower():
                    case "sunday":
                        self.gym_class_schedule_dict[remove_day][class_name] = self.number_of_class_spots_available_in_sunday_body_building
                    case "monday":
                        self.gym_class_schedule_dict[remove_day][class_name] = self.number_of_class_spots_available_in_monday_pilates
                    case "tuesday":
                        self.gym_class_schedule_dict[remove_day][class_name] = self.number_of_class_spots_available_in_tuesday_crossfit
                    case "wednesday":
                        self.gym_class_schedule_dict[remove_day][class_name] = self.number_of_class_spots_available_in_wednesday_kickboxing
                    case "thursday":
                        self.gym_class_schedule_dict[remove_day][class_name] = self.number_of_class_spots_available_in_thursday_weight_training
                    case "friday":
                        self.gym_class_schedule_dict[remove_day][class_name] = self.number_of_class_spots_available_in_friday_spin
                    case "saturday":
                        self.gym_class_schedule_dict[remove_day][class_name] = self.number_of_class_spots_available_in_saturday_crossfit
                    #removing from user profile
                print(f"Please check option 6 - Detailed Account Summary to see updated information")
                self.list_of_classes.remove(class_name)
                    #looping through class list to reflect change
                for c in self.list_of_classes:
                    print(f"Your updated class list: {c}")
                gs.menu_navigator()
            except ValueError as v3:
                print(v3)
                continue

    def add_guest(self):
        while True:
            try:
                guest = input("Please enter the guest\'s full name. press Q to quit:").lower()
                if guest == 'q':
                    print("exiting...")
                    quit()

                if guest.isdigit():
                    raise ValueError("Please only enter alphanumeric characters, not numbers...")

                #adding to user profile
                self.list_of_guests.append(guest)
                print(f"Total Number of Guests on Account:{len(self.list_of_guests)}")
                print(f"Please check option 6 - Detailed Account Summary to see updated information")
                gs.menu_navigator()
            except ValueError as v3:
                print(v3)
                continue


    def drop_guest(self):
        while True:
            try:
                guest = input("Please enter the guest\'s full name. press Q to quit:").lower()
                if guest == "q":
                    print("exiting...")
                    quit()
                self.list_of_guests.remove(guest)
                print(f"Total Number of Guests on Account:{len(self.list_of_guests)}")
                print(f"Please check option 6 - Detailed Account Summary to see updated information")
                gs.menu_navigator()
            except ValueError as v3:
                print(v3)
                continue

    def show_membership_menu(self):
        for item in self.list_of_menu_items:
                print(item)

    def get_membership_info(self):
        MembershipSystem.get_membership_info(self)
        print(f"Number of Total Enrolled Classes:{len(self.list_of_classes)}")
        for my_class in self.list_of_classes:
            print(f"{my_class} - last updated at: {datetime.datetime.now()}")
        print(f"Number of Total Guests on Account:{len(self.list_of_guests)}")
        for g in self.list_of_guests:
            print(f"{g} - last updated at: {datetime.datetime.now()}")
        print("-" * 100)
        gs.menu_navigator()

    def menu_navigator(self):
        self.show_membership_menu()
        while True:
            try:
                user_input = int(input("Please select a menu option number:"))

                if user_input not in range(1, 10):
                    raise ValueError("Please enter a number between 1 and 9 as an integer")
                else:
                    if user_input == 1:
                        gs.check_gym_class_schedule()
                    elif user_input == 2:
                        gs.add_guest()
                    elif user_input == 3:
                       gs.enroll_in_gym_class()
                    elif user_input == 4:
                        gs.drop_a_gym_class()
                    elif user_input == 5:
                        gs.drop_guest()
                    elif user_input == 6:
                        gs.get_membership_info()
                    elif user_input == 7:
                        gs.set_new_payment_method(user_payment_method)
                    elif user_input == 8:
                        gs.cancel_membership()
                    elif user_input == 9:
                        print("exiting...")
                        quit()

            except ValueError as v3:
                print(v3)
                continue

### FUNCTIONS ###
def generate_cost(type_of_mem, num_of_ppl):
        total_cost = 0.00
        if type_of_mem == "basic":
            total_cost += (39.99 * num_of_ppl)
        if type_of_membership == "premier":
            total_cost += (69.99 * num_of_ppl)
        if type_of_membership == "family":
            total_cost += (132.99 * num_of_ppl)
        return total_cost


### MAIN ###

print(f"Welcome to PL Mountain Gym! To get started and use our facilities, please complete the following information")
print("\tA. General Information")
print("\tB. Payment Method")
print("\tC. Membership Type")
print("\tD. Personal Training Assignment")
print("\tE. Gym Membership Terms & Conditions")
print("." * 100)
print(f"{'General Information':^100}")
print("." * 100)


while True:
        try:
            user_fullname = input(f"Please enter your full name. press Q to quit:").lower()
            if user_fullname.isdigit() or user_fullname == "":
               raise ValueError("ERROR! This field may not be left empty and only enter alphanumeric characters please")
            if user_fullname == 'q':
                print("exiting...")
                quit()
            user_address = input(f"Please enter your street address. press Q to quit:").lower()
            if user_address == "":
               raise ValueError("ERROR! This field may not be left empty and only enter alphanumeric characters please")
            if user_address == 'q':
                print("exiting...")
                quit()
            user_city = input(f"Please enter your city. press Q to quit:").lower()
            if user_city.isdigit() or user_city == "":
               raise ValueError("ERROR! This field may not be left empty and only enter alphanumeric characters please")
            if user_city == 'q':
                print("exiting...")
                quit()
            user_state = input(f"Please enter your state. press Q to quit:").lower()
            if user_state.isdigit() or user_state == "":
               raise ValueError("ERROR! This field may not be left empty and only enter alphanumeric characters please")
            if user_state == 'q':
                print("exiting...")
                quit()
            user_zipcode = int(input(f"Please enter your zip code:"))
            if user_zipcode == "":
               raise ValueError("ERROR! This field may not be left empty and only enter numeric values please")
            break
        except ValueError as v4:
            print(v4)
print("." * 100)
print(f"{'Payment Method':^100}")
print("." * 100)

while True:
        available_payment_methods = ["cash", "credit card"]
        try:
            user_payment_method = input(f"how do you want to pay for your membership? press Q to quit:").lower()
            if user_payment_method == 'q':
                print("exiting...")
                quit()
            if user_payment_method.isdigit() or user_payment_method == "":
                  raise ValueError("ERROR! This field may not be left empty and must only contain alphanumeric characters please")
            if not user_payment_method in available_payment_methods:
                  raise ValueError("ERROR! Please enter either cash or credit card")
            else:
                break
        except ValueError as v5:
            print(v5)
            continue
print("." * 100)
print(f"{'Membership Plan':^100}")
print("." * 100)

while True:
        membership_levels = ["basic", "premier", "family"]
        try:
            type_of_membership = input(f"which type of membership plan would you like - basic, premier, or family. press Q to quit:")
            if type_of_membership == "q":
                print("exiting...")
                quit()
            if type_of_membership.isdigit() or type_of_membership == "":
               raise ValueError("ERROR! This field may not be left empty and must only contain alphanumeric characters please")
            elif not type_of_membership in membership_levels:
                raise ValueError("ERROR! Membership type must be one of the following - basic, premier, or family")
            else:
                break
        except ValueError as v8:
            print(v8)
            continue
while True:
        try:
                number_of_new_members = int(input(f"how many new members will be signing up today?:"))
                if number_of_new_members == "" or number_of_new_members < 1:
                    raise ValueError("ERROR! There must be at least 1 new member at minimum")
                else:
                    break
        except ValueError as v6:
            print(v6)
            continue

print("." * 100)
print(f"{'Personal Trainer Assignment':^100}")
print("." * 100)

while True:
        trainer_acceptance = ["y", "n"]
        try:
            user_personal_trainer_needed_choice = input("Do you need a Personal Trainer appointed for you to help reach your goals? Y for Yes or No for No. press Q to quit:").lower()
            if user_personal_trainer_needed_choice == "q":
                print("exiting...")
                quit()
            if user_personal_trainer_needed_choice.isdigit() or user_personal_trainer_needed_choice ==  "":
               raise ValueError("ERROR! This field may not be left empty and only enter alphanumeric characters please")
            elif not user_personal_trainer_needed_choice in trainer_acceptance:
               raise ValueError("ERROR! Please enter either a 'Y' or 'N' to confirm whether you need the assistance of a Personal Trainer")
            break
        except ValueError as v7:
            print(v7)
            continue

while True:
        print("processing...")
        print()
        print("." * 50)
        print(f"{'Gym Membership Terms & Conditions':^100}", end="")
        print("." * 50)
        print(f"Welcome {user_fullname}! \n"
        "At PL Mountain Gym, we strive to provide to you resort-level treatment and facilities.\n"
        "It is critically important that you take time to read over this agreement with us before agreeing to the Terms & Conditions.\n"
        "We expect all of our members to treat everyone with respect and observe the gym rules\n"
        "Gym Rules List:\n"
        "\t1) Do not slam weights on floor in the weight room\n"
        "\t2) Do not leave personal belongings unattended, it is not this gym\'s responsibility to overwatch these. It is at your own risk\n"
        "\t3) Please pay all membership fees on time\n"
        "\t4) Only 2 new guests may join you per month\n"
        "\t5) Families please use the family locker room\n")
        try:
            user_acceptance_of_terms = input("Do you accept all of the terms above? Enter Y for Yes or N for No:").lower()
            if user_acceptance_of_terms == 'y':
                number_of_guests_on_account = []
                classes_enrolled_on_account = []
                user_status_activated = "Active"
                total_cost_calculation = generate_cost(type_of_membership, number_of_new_members)
                gs = GymMembershipSystem(user_fullname, user_address, user_city, user_state, user_zipcode, user_payment_method, user_status_activated, total_cost_calculation, type_of_membership, user_personal_trainer_needed_choice, classes_enrolled_on_account, number_of_guests_on_account)
                gs.set_membership_info(user_fullname, user_address, user_city, user_state, user_zipcode, user_payment_method, user_status_activated, total_cost_calculation)
                gs.get_membership_info()
                gs.menu_navigator()
                break
            else:
                print("returning to the user acceptance agreement...")
                continue
        except ValueError as v8:
            print(v8)
            continue




