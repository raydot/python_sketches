#user_def_docstrings.py

"""
Module documentation
***Lorem this is module documentation ipsum...
"""

spam = 40

def square(x):
	"""
	function documentation
	This is the documentation for the square function
	"""
	return x **2

class employee:
	"This is documentation for the employee class!"
	pass

print (square(4))
print (square.__doc__)