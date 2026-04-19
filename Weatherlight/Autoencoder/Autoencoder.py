# --------------------------------------------------------------------------------------------------
# --------------------------- Weatherlight :: Autoencoder :: Autoencoder ---------------------------
# --------------------------------------------------------------------------------------------------
from Dragon import Autoencoder
from Dragon import Embeddings
from Dragon import Attr
from Dragon import Edge
from Dragon import Type
from Dragon import Slot

import torch
import torch.nn as nn


# --------------------------------------------------------------------------------------------------
# ----------------------------- Autoencoder :: Weatherlight Autoencoder ----------------------------
# --------------------------------------------------------------------------------------------------
class Autoencoder(nn.Module, metaclass=Autoencoder, height=512, width=512):

	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, embeddings: Embeddings) -> None:
		self.embeddings = embeddings