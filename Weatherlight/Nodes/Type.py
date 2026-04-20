# --------------------------------------------------------------------------------------------------
# ---------------------------------- Weatherlight :: Nodes :: Type ---------------------------------
# --------------------------------------------------------------------------------------------------
from Dragon import Attr
from Dragon import Node
from Dragon import Type


# --------------------------------------------------------------------------------------------------
# ------------------------------------------ Node :: Type ------------------------------------------
# --------------------------------------------------------------------------------------------------
class Type(Node):

	# -----------------------------------------------------------------------------------------
	# --------------------------------- Embedding Annotations ---------------------------------
	# -----------------------------------------------------------------------------------------
	artifact	 : Attr[None | bool]
	battle 		 : Attr[None | bool]
	creature	 : Attr[None | bool]
	dungeon 	 : Attr[None | bool]
	enchantment	 : Attr[None | bool]
	instant 	 : Attr[None | bool]
	kindred 	 : Attr[None | bool]
	land 		 : Attr[None | bool]
	planeswalker : Attr[None | bool]
	sorcery 	 : Attr[None | bool]


	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, *components: Node | str, **attributes: bool | int | float) -> None:
		super().__init__(*components, **attributes)

		artifact	 = attributes.get('artifact')
		battle 		 = attributes.get('battle')
		creature	 = attributes.get('creature')
		dungeon 	 = attributes.get('dungeon')
		enchantment	 = attributes.get('enchantment')
		instant 	 = attributes.get('instant')
		kindred 	 = attributes.get('kindred')
		land 		 = attributes.get('land')
		planeswalker = attributes.get('planeswalker')
		sorcery 	 = attributes.get('sorcery')


Artifact 	 = Type(artifact=True)
Battle   	 = Type(battle=True)
Creature 	 = Type(creature=True)
Dungeon 	 = Type(dungeon=True)
Enchantment  = Type(enchantment=True)
Instant   	 = Type(instant=True)
Kindred 	 = Type(kindred=True)
Land 		 = Type(land=True)
Planeswalker = Type(planeswalker=True)
Sorcery 	 = Type(sorcery=True)

