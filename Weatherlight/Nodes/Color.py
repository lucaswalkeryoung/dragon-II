# --------------------------------------------------------------------------------------------------
# --------------------------------- Weatherlight :: Nodes :: Color ---------------------------------
# --------------------------------------------------------------------------------------------------
from Dragon import Attr
from Dragon import Node
from Dragon import Type


# --------------------------------------------------------------------------------------------------
# ------------------------------------------ Node :: Color -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Color(Node):

	# -----------------------------------------------------------------------------------------
	# --------------------------------- Embedding Annotations ---------------------------------
	# -----------------------------------------------------------------------------------------
	colorless : Attr[None | bool]
	white 	  : Attr[None | bool]
	blue 	  : Attr[None | bool]
	black	  : Attr[None | bool]
	red 	  : Attr[None | bool]
	green	  : Attr[None | bool]
	color 	  : Type


	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, *components: Node | str, **attributes: bool | int | float) -> None:
		super().__init__(*components, **attributes)

		self.colorless = attributes.get('colorless')
		self.white 	   = attributes.get('white')
		self.blue 	   = attributes.get('blue')
		self.black 	   = attributes.get('black')
		self.red 	   = attributes.get('red')
		self.green 	   = attributes.get('green')


Colorless = Color(colorless=True)
White 	  = Color(white=True)
Blue 	  = Color(blue=True)
Black 	  = Color(black=True)
Red 	  = Color(red=True)
Green 	  = Color(green=True)
