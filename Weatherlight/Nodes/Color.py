# --------------------------------------------------------------------------------------------------
# --------------------------------- Weatherlight :: Nodes :: Color ---------------------------------
# --------------------------------------------------------------------------------------------------
from .. Autoencoder import Autoencoder

from Dragon import Attr
from Dragon import Edge
from Dragon import Node
from Dragon import Slot
from Dragon import Type


# --------------------------------------------------------------------------------------------------
# ------------------------------------------ Node :: Color -----------------------------------------
# --------------------------------------------------------------------------------------------------
@Autoencoder.embed
class Color(Node):

	# -----------------------------------------------------------------------------------------
	# --------------------------------- Embedding Annotations ---------------------------------
	# -----------------------------------------------------------------------------------------
	color 	  : Type
	colorless : Attr[None | bool]
	white 	  : Attr[None | bool]
	blue 	  : Attr[None | bool]
	black	  : Attr[None | bool]
	red 	  : Attr[None | bool]
	green	  : Attr[None | bool]


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
