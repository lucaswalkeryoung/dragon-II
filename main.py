# -------------------------------------------------------------------------------------------------
# ------------------------------ The Dragon Graph Autoencoder System ------------------------------
# -------------------------------------------------------------------------------------------------
from Weatherlight import Autoencoder
from Dragon import Node
from Dragon import Slot

autoencoder = Autoencoder(height=512, width=512)

def tensorize(node: Node) -> None:
	accumulator, null, padding = autoencoder.embeddings(Slot)

tensorize(None)
