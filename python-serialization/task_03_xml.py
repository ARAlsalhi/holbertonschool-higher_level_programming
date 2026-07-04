#!/usr/bin/env python3
"""Module for serializing and deserializing dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.set("type", type(value).__name__)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}

    for element in root:
        value = element.text
        value_type = element.get("type")

        if value_type == "int":
            value = int(value)
        elif value_type == "float":
            value = float(value)
        elif value_type == "bool":
            value = value == "True"
        elif value_type == "NoneType":
            value = None

        dictionary[element.tag] = value

    return dictionary
