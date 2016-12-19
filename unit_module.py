import animator_module 
import sprite_module
import xml.etree.ElementTree as ET

def read_units_xml(filename):
    tree = ET.parse(filename)
    units_element = tree.getroot()
    units = []
    for unit_element in units_element:
        units += [UnitType(unit_element)]
    return units
    

class UnitType:
    def __init__(self, element):
        self.hp = int(element.attrib["hp"])
        sprite = element.find("sprite").attrib
        self.sprite = sprite_module.UnitTypeSprite(sprite)
        self.attack = element.attrib["attack"]
        self.name = element.attrib["name"]
        self.id = element.attrib["id"]

class UnitInstance:
    def __init__(self, unit_type, position):
        self.unit_type = unit_type
        self.animator = animator_module.UnitAnimator(unit_type.sprite)
        self.position = position
        self.face_vector = (0,0)
        self.order_list = []

    def die(self):
        pass

    def create(self):
        pass

    def process_order(self):
        pass
    
    def animate(self, canvas, delta):
        self.animator.animate(self.position, self.face_vector, canvas, delta,
        self)
        

print read_units_xml("Data/units.xml")
