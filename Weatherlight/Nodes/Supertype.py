# --------------------------------------------------------------------------------------------------
# ------------------------------- Weatherlight :: Nodes :: Supertype -------------------------------
# --------------------------------------------------------------------------------------------------
from Dragon import Attr
from Dragon import Node
from Dragon import Type


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Node :: Supertype ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Supertype(Node):

	# -----------------------------------------------------------------------------------------
	# --------------------------------- Embedding Annotations ---------------------------------
	# -----------------------------------------------------------------------------------------
	basic	  : Attr[None | bool]
	legendary : Attr[None | bool]
	snow	  : Attr[None | bool]
	world 	  : Attr[None | bool]
	supertype : Type


	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, *components: Node | str, **attributes: bool | int | float) -> None:
		super().__init__(*components, **attributes)

		self.blue  = attributes.get('basic')
		self.black = attributes.get('legendary')
		self.red   = attributes.get('snow')
		self.green = attributes.get('world')


Basic 	  = Supertype(basic=True)
Legendary = Supertype(legendary=True)
Snow 	  = Supertype(snow=True)
World 	  = Supertype(world=True)
