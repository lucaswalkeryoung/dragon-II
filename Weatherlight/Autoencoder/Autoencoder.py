# -------------------------------------------------------------------------------------------------
# --------------------------- Weatherlight :: Autoencoder :: Autoencoder --------------------------
# -------------------------------------------------------------------------------------------------
from Dragon import Embedding
from Dragon import Node

from .. import Nodes


# -------------------------------------------------------------------------------------------------
# ------------------------------------- Module :: Autoencoder -------------------------------------
# -------------------------------------------------------------------------------------------------
class Autoencoder(object):

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