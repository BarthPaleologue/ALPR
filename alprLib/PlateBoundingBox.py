import xml.etree.cElementTree as ET

class PlateBoundingBox:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

        self.image_name = self.root.find('filename').text
        
        bbox = self.root.find('object').find('bndbox')
        self.xmin = int(bbox.find('xmin').text)
        self.ymin = int(bbox.find('ymin').text)
        self.xmax = int(bbox.find('xmax').text)
        self.ymax = int(bbox.find('ymax').text)
        self.width = self.xmax - self.xmin
        self.height = self.ymax - self.ymin
        self.center = (self.xmin + self.width/2, self.ymin + self.height/2)
        self.area = self.width * self.height

    def describe(self):
        print("PlateBoundingBox")
        print("xml_path: {}".format(self.xml_path))
        print("image_name: {}".format(self.image_name))
        print("xmin: {}".format(self.xmin))
        print("ymin: {}".format(self.ymin))
        print("xmax: {}".format(self.xmax))
        print("ymax: {}".format(self.ymax))
        print("width: {}".format(self.width))
        print("height: {}".format(self.height))
        print("center: {}".format(self.center))
        print("area: {}".format(self.area))
        print("")