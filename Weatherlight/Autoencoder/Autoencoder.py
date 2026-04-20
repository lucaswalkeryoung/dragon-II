# -------------------------------------------------------------------------------------------------
# --------------------------- Weatherlight :: Autoencoder :: Autoencoder --------------------------
# -------------------------------------------------------------------------------------------------
from Dragon import Embedding
from Dragon import Node

from .. import Nodes

import torch
import torch.nn as nn


# -------------------------------------------------------------------------------------------------
# ------------------------------------- Module :: Autoencoder -------------------------------------
# -------------------------------------------------------------------------------------------------
class Autoencoder(nn.Module):

	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, height: int, width: int) -> None:

		nodes = vars(Nodes).values()

		nodes = filter(lambda item: isinstance(item, type), nodes)
		nodes = filter(lambda item: issubclass(item, Node), nodes)

		self.embeddings = Embedding(width, nodes)
		self.height = height
		self.width  = width