"""
Parsing json utility
"""
import json


def read_json(jsondir: str):
    """
    Parses a json file for the SMILEs
    :param jsondir:
    :return: list of smiles
    """

    smiles_so_far = []
    with open(jsondir) as json_data:
        json_file = json.load(json_data)
        for i in range(0, len(json_file)):
            smiles_so_far.append(json_file[i]["smiles"])

    return smiles_so_far
