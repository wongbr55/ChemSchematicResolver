import chemschematicresolver as csr
import argparse
import image_extraction.image_segmentation as imseg
import json


def get_yield_from_comment(comment: str):
	"""
	Gets yield information from comment
	"""
	curr_yield = ""
	seen_percent = False
	for i in range(0, len(str)):
		if comment[i] == '%':
			seen_percent = True
			curr_yield += '%'
		elif seen_percent and comment[i] != ' ':
			curr_yield += comment[i]
		elif seen_percent and comment[i] == ' ':
			break
	return yield


def get_substrates(filestr: str):
	"""
	Takes the full reaction image and segments it into reaction and substrates
	Calls chemschematicresolver on the substrate images and gets proper SMILEs and yields
	"""

	num_of_substrates = imseg.segment_reactants_and_substrates(filestr)
	smiles_and_yield = []
	for i in range(0, num_of_substrates):
		try:
			result = csr.extract_image("substrate_image_" + str(i) + ".jpeg)
			for tuple in result:
				curr_yield, smiles = get_yield_from_comment(tuple[0]), tuple[1]
				smiles_and_yield.append((smiles, curr_yield))

	# could also print to use in a shell setting
	return smiles_and_yield

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--path', type=str, required=True)

	parsed_args = parser.parse_args()
	smiles_and_yield = get_substrates(parsed_args.path)
	substrate_dict = {}
	for i in range(0, len(smiles_and_yield)):
		substrate_dict["substrate" + str(i)] = smiles_and_yield[i]
	new_json = json.dump(substrate_dict)

	with open("substrates.json", "w") as outfile:
    		outfile.write(new_json)
