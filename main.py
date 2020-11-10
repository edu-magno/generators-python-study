import csv
import datetime


def find_profiles_between_20_and_35_years(filename):

    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        age_20 = 7299
        age_35 = 13139

        for profile in reader:
            birthdate_of_profile = profile.get('birthdate')
            year_birthdate = int(birthdate_of_profile[0:4])
            month_birthdate = int(birthdate_of_profile[5:7])
            day_birthdate = int(birthdate_of_profile[8:10])

            date_check = (datetime.date.today(
            ) - datetime.date(year_birthdate, month_birthdate, day_birthdate)).days - 9

            check_age = date_check <= age_35 and date_check >= age_20

            if check_age:

                yield profile


def find_select_blood_donors_1(filename):

    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        age_30 = 11315
        age_20 = 7300

        blood_type_a_negative = 'A-'
        blood_type_o_negative = 'O-'
        for profile in reader:

            blood_type_of_profile = profile.get('blood_group')
            birthdate_of_profile = profile.get('birthdate')

            year_birthdate = int(birthdate_of_profile[0:4])
            month_birthdate = int(birthdate_of_profile[5:7])
            day_birthdate = int(birthdate_of_profile[8:10])
            date_check = (datetime.date.today(
            ) - datetime.date(year_birthdate, month_birthdate, day_birthdate)).days

            check_age = date_check <= age_30 and date_check >= age_20
            check_blood_type_a = blood_type_of_profile == blood_type_a_negative
            check_blood_type_o = blood_type_of_profile == blood_type_o_negative

            if check_blood_type_a and check_age or check_blood_type_o:
                profile.pop('blood_group')
                profile.pop('sex')
                profile.pop('birthdate')
                yield profile


def find_select_blood_donors_2(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        age_30 = 11315
        age_50 = 18614
        blood_type_b_plus = 'B+'
        sex = 'F'

        for profile in reader:
            sex_of_profile = profile.get('sex')
            blood_type_of_profile = profile.get('blood_group')
            birthdate_of_profile = profile.get('birthdate')

            year_birthdate = int(birthdate_of_profile[0:4])
            month_birthdate = int(birthdate_of_profile[5:7])
            day_birthdate = int(birthdate_of_profile[8:10])

            date_check = (datetime.date.today(
            ) - datetime.date(year_birthdate, month_birthdate, day_birthdate)).days

            check_age = date_check <= age_50 and date_check >= age_30
            check_blood = blood_type_of_profile == blood_type_b_plus
            check_sex = sex_of_profile == sex

            if check_sex and check_age and check_blood:
                profile.pop('blood_group')
                profile.pop('sex')
                profile.pop('birthdate')
                profile.pop('residence')
                yield profile


def find_select_blood_donors_3(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        age_15 = 5475
        age_25 = 9124
        blood_type_o_plus = 'O+'
        blood_type_o_negative = 'O-'
        sex = 'M'

        for profile in reader:
            residence_of_profile = profile.get('residence')
            sex_of_profile = profile.get('sex')
            birthdate_of_profile = profile.get('birthdate')
            blood_type_of_profile = profile.get('blood_group')

            year_birthdate = int(birthdate_of_profile[0:4])
            month_birthdate = int(birthdate_of_profile[5:7])
            day_birthdate = int(birthdate_of_profile[8:10])

            date_check = (datetime.date.today(
            ) - datetime.date(year_birthdate, month_birthdate, day_birthdate)).days

            check_age = date_check <= age_25 and date_check >= age_15
            check_blood_plus = blood_type_o_plus == blood_type_of_profile
            check_blood_negative = blood_type_o_negative == blood_type_of_profile
            check_blood = check_blood_plus or check_blood_negative
            check_sex = sex_of_profile == sex

            if check_sex and check_age and check_blood:
                state_initials = ''
                splited_residence_of_profile = residence_of_profile.split(' ')

                for x in splited_residence_of_profile:
                    if len(x) == 2:
                        state_initials = x

                profile.update({'residence': state_initials})
                profile.pop('blood_group')
                profile.pop('sex')
                profile.pop('birthdate')
                yield profile
