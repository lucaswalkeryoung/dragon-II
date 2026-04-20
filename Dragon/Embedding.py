# -------------------------------------------------------------------------------------------------
# -------------------------------------- Dragon :: Embedding --------------------------------------
# -------------------------------------------------------------------------------------------------
from Utilities import DefaultDict as DefaultKeyDict

from . Annotations import Annotation

from typing import TYPE_CHECKING
from typing import Iterable

if TYPE_CHECKING:
	from . Schema import Schema

import torch
import torch.nn as nn


# -------------------------------------------------------------------------------------------------
# ------------------------------- Utility :: Embedding Table Manager ------------------------------
# -------------------------------------------------------------------------------------------------
class Embedding(nn.Module):

	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, width: int, nodes: Iterable['Schema']) -> None:
		super().__init__()

		# self.indices = DefaultKeyDict(lambda key : len(self.indices))
		# self.schemas = DefaultKeyDict(
		# 	lambda annotation : DefaultKeyDict(lambda attr : self.indices[annotation, attr])
		# )
		#
		# for node in nodes:
		#
		# 	for attribute, annotation in Annotation.extract(node).items():
		# 		node.schema[annotation][attribute] = self.schemas[annotation][attribute]
		#
		# self.tensors = nn.Embedding(width, len(self.indices))


	# -----------------------------------------------------------------------------------------
	# ----------------------- Operator :: Call (Get Embedding Vector(s)) ----------------------
	# -----------------------------------------------------------------------------------------
	def __call__(self, annotation: type, attribute: None | str = None) -> None:
		...