# -------------------------------------------------------------------------------------------------
# ------------------------------ Dragon :: Autoencoder :: Autoencoder -----------------------------
# -------------------------------------------------------------------------------------------------
from . Annotations import Annotation
from . Schematics  import Schematics
from . Embeddings  import Embeddings

from typing import TYPE_CHECKING
from typing import Annotated
from typing import Any
from typing import Callable
from typing import Type
from typing import Union
from typing import overload
from typing import get_args
from typing import get_origin
from typing import get_type_hints

if TYPE_CHECKING:
	from .. Node import Node

import collections
import stringcase
import toolz


# -------------------------------------------------------------------------------------------------
# -------------------------- Metaclass :: Autoencoder Node Registry Help --------------------------
# -------------------------------------------------------------------------------------------------
class Autoencoder(type):

	# -----------------------------------------------------------------------------------------
	# --------------------------------- Operator :: Allocator ---------------------------------
	# -----------------------------------------------------------------------------------------
	def  __new__(meta, name: str, bases: tuple[type, ...], namespace: dict[str, Any], *,
		height : int = 256,
		width  : int = 256,
	) -> None: return super().__new__(meta, name, bases, namespace)


	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, name: str, bases: tuple[type, ...], namespace: dict[str, Any], *,
		height : int = 256,
		width  : int = 256,
	) -> None:

		super().__init__(name, bases, namespace)

		self.height = height
		self.width  = width

		self.schematics = Schematics('Embeddings', (Embeddings, ), {})


	# -----------------------------------------------------------------------------------------
	# --------------------------- Operator :: Call (Create Instance) --------------------------
	# -----------------------------------------------------------------------------------------
	def __call__(self, *positional: Any, **named: Any) -> Autoencoder:
		return super().__call__(self.schematics(self.width), *positional, **named)


	# -----------------------------------------------------------------------------------------
	# -------------------------- Method :: Register Node Class Schema -------------------------
	# -----------------------------------------------------------------------------------------
	def embed(self, node: Type[Node]) -> Type[Node]:

		annotations = get_type_hints(node, include_extras=True)

		for annotated, annotation in get_type_hints(node, include_extras=True).items():

			match (get_origin(annotation), get_args(annotation)):

				case Annotated, [_, Annotation() as annotation]:
					index = self.schematics[annotation][annotated]

		return node