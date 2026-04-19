# -------------------------------------------------------------------------------------------------
# ------------------------------ Dragon :: Autoencoder :: Annotations -----------------------------
# -------------------------------------------------------------------------------------------------
from . Annotations import Annotation
from . Schematics  import Schematics

from typing import Annotated
from typing import Any
from typing import get_args
from typing import get_origin

import collections
import torch
import torch.nn as nn


# -------------------------------------------------------------------------------------------------
# ----------------------------- Metaclass :: Embeddings Tables Manager ----------------------------
# -------------------------------------------------------------------------------------------------
class Embeddings(nn.Module, metaclass=Schematics):

	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, width: int) -> None:

		self.embeddings = {}

		for annotation, schematic in self.schematics.items():
			self.embeddings[annotation] = schematic(width)


	# -----------------------------------------------------------------------------------------
	# ---------------------------------- Operator :: Get Item ---------------------------------
	# -----------------------------------------------------------------------------------------
	def __getitem__(self, key: type) -> Embedding:

		match get_origin(key), get_args(key):

			case Annotated, [_, Annotation() as key]:
				return self.embeddings[key]

			case _:
				...

		return self.embeddings[key]