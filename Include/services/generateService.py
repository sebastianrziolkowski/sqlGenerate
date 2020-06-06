from random import randint
from Include.enums.gender_enum import Sex
from Include.resources.femaleNames import femaleNames
from Include.resources.maleNames import maleNames
from Include.resources.surnames import surnames


def generate_name(sex: Sex) -> str:
    index = randint(0, 1000)
    if sex == Sex.MALE:
        return maleNames[index]
    elif sex == Sex.FEMALE:
        return femaleNames[index]
    else:
        return "Wrong sex!"


def generate_surname() -> str:
    index = randint(0, 500)
    return surnames[index]


def generate_age() -> int:
    return randint(10, 99)


def generate_column_name(Window) -> str:
    result = "INSERT INTO "
    result += "`" + Window.input_table_name.get() + "`("
    if Window.checkboxName.instate(['selected']):
        result += "`" + Window.input_name.get() + "`, "
    if Window.checkbox_surname.instate(['selected']):
        result += "`" + Window.input_surname.get() + "`, "
    if Window.checkbox_sex.instate(['selected']):
        result += "`" + Window.input_sex.get() + "`, "
    if Window.checkbox_age.instate(['selected']):
        result += "`" + Window.input_age.get() + "`, "

    result = result[:len(result) - 2]
    result += ")"
    if len(result) == 7:
        return "NULL"
    return result + "\n"


def generate_person(window, gender: Sex) -> str:
    result = "("
    if window.checkboxName.instate(['selected']):
        result += "'" + generate_name(gender) + "', "
    if window.checkbox_surname.instate(['selected']):
        result += "'" + generate_surname() + "', "
    if window.checkbox_sex.instate(['selected']):
        result += "'" + gender.name + "', "
    if window.checkbox_age.instate(['selected']):
        result += "'" + str(generate_age()) + "', "

    result = result[:len(result) - 2]
    result += ")"
    if len(result) < 3:
        return "NULL"
    return result
