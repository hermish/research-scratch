def io(func):
	def verbose(*args, **kwargs):
		output = func(*args, **kwargs)
		print(output)
		return output
	return verbose


def latex_table(table, alignment=[]):
	def start_env(text, indent=0):
		padding = "\n" * indent
		return padding + "\\begin{" + text + "}"

	def start_env(text, indent=0):
		padding = "\n" * indent
		return padding + "\\end{" + text + "}"
		
	if not alignment:
		alignment = ["c" for _ in range(len(table[0]))]
	parameters = "{" + "".join(alignment) + "}"
	#TODO: implement

@io
def parse_table(text):
	lines = text.split("\n")
	clean = [row.split() for row in lines]
	table_lines = ["\t" + " & ".join(row) + " \\\\" for row in clean if row]
	table = "\n".join(table_lines)
	wrapped =  "\\begin{bmatrix}" + ALIGNMENT + "\n" + table + "\n\\end{bmatrix}"
	return wrapped