import pygame


def load_units(path):
    unit_types = []
    with open(path) as unit_file:
        unit_types += [_load_next_unit(unit_file)]


def _load_next_unit(file):
    token = _read_next_property("Unit:")[0]
    name = _read_next_property("Name:")[0]
    img = _read_next_property("Img:")[0]

    name = file.readline().split()
    if "Name:" != name[0]:
        raise Exception("Messed up units file!!!")
    name = name[-1]

def _read_next_property(file, tag):
    words = file.readline().split()
    if tag != words[0]:
        raise Exception("Messed up units file!!!")
    return words[1:]
        

    





