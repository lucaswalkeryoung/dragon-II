# -------------------------------------------------------------------------------------------------
# ------------------------------------- Dragon :: Annotations -------------------------------------
# -------------------------------------------------------------------------------------------------
from typing import Annotated
from typing import Generator
from typing import TypeVar
from typing import get_args
from typing import get_origin
from typing import get_type_hints

T = TypeVar('T')


# -------------------------------------------------------------------------------------------------
# ------------------------------------- Utility :: Annotation -------------------------------------
# -------------------------------------------------------------------------------------------------
class Annotation(type):

	# -----------------------------------------------------------------------------------------
	# ------------------------------ Operator :: Metaconstructor ------------------------------
	# -----------------------------------------------------------------------------------------
	def __new__(meta, name: str) -> 'Annotation': return super().__new__(meta, name, (), {})


	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(meta, name: str) -> None: super().__init__(name, (), {})


	# -----------------------------------------------------------------------------------------
	# ---------------------- Method :: Extract Annotation from Annotated ----------------------
	# -----------------------------------------------------------------------------------------
	@staticmethod
	def denotate(typehint: object) -> 'None | Annotation':

		match get_origin(typehint), get_args(typehint):

			case Annotated, [_, Annotation() as annotation, *_]:
				return annotation

			case _:
				...

		return None


	# -----------------------------------------------------------------------------------------
	# -------------------- Method :: Extract Annotations Mapping from Type --------------------
	# -----------------------------------------------------------------------------------------
	@staticmethod
	def extract(type: type, key: None | type = None) -> dict[str, 'Annotation']:

		annotations = {}

		for attribute, annotation in get_type_hints(type, include_extras=True).items():

			if annotation := Annotation.denotate(annotation):

				if key:

					if annotation is key:
						annotations[attribute] = annotation

				else:
					annotations[attribute] = annotation

		return annotations


Attr = Annotated[T, Annotation('Attr')]
Edge = Annotated[T, Annotation('Edge')]
Slot = Annotated[T, Annotation('Slot')]
Type = Annotated[T, Annotation('Type')]