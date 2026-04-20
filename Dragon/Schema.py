# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Dragon :: Meta ----------------------------------------
# -------------------------------------------------------------------------------------------------
from . Annotations import Annotation

from typing import TYPE_CHECKING
from typing import Any

if TYPE_CHECKING:
	from . Metaencoder import Metaencoder
	from . Node import Node

import collections


# -------------------------------------------------------------------------------------------------
# -------------------------------- Metaclass :: Base Node Metaclass -------------------------------
# -------------------------------------------------------------------------------------------------
class Schema(type):

	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, name: str, bases: tuple[type, ...], attrs: dict[str, Any]) -> None:
		super().__init__(name, bases, attrs)

		self.schema = collections.defaultdict(lambda : collections.defaultdict(dict))