# -------------------------------------------------------------------------------------------------
# ------------------------------ Dragon :: Autoencoder :: Annotations -----------------------------
# -------------------------------------------------------------------------------------------------
from . Annotations import Annotation
from . Schematic   import Schematic
from . Embedding   import Embedding

from typing import TYPE_CHECKING
from typing import Any

if TYPE_CHECKING:
	from . Embeddings import Embeddings

import collections


# -------------------------------------------------------------------------------------------------
# ---------------------------- Metaclass :: Embeddings Table Metaclass ----------------------------
# -------------------------------------------------------------------------------------------------
class Schematics(type):

	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> None:
		super().__init__(name, bases, namespace)

		self.schematics = collections.defaultdict(
			lambda : Schematic('Embedding', (Embedding, ), {})
		)


	# -----------------------------------------------------------------------------------------
	# ---------------------------------- Operator :: Get Item ---------------------------------
	# -----------------------------------------------------------------------------------------
	def __getitem__(self, key: Annotation) -> Schematic:
		return self.schematics[key]