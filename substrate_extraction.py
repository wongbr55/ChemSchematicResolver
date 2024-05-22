import chemschematicresolver as csr
import image-segmentation.image_segmentation as imseg


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
