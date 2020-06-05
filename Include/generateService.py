from random import randint
from Include.enums.Sex_enum import Sex
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
