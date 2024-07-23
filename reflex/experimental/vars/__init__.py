"""Experimental Immutable-Based Var System."""

from .base import ArrayVar as ArrayVar
from .base import ImmutableVar as ImmutableVar
from .base import LiteralArrayVar as LiteralArrayVar
from .base import LiteralObjectVar as LiteralObjectVar
from .base import LiteralVar as LiteralVar
from .base import ObjectVar as ObjectVar
from .base import var_operation as var_operation
from .function import FunctionStringVar as FunctionStringVar
from .function import FunctionVar as FunctionVar
from .function import VarOperationCall as VarOperationCall
from .number import BooleanVar as BooleanVar
from .number import LiteralBooleanVar as LiteralBooleanVar
from .number import LiteralNumberVar as LiteralNumberVar
from .number import NumberVar as NumberVar
from .string import ConcatVarOperation as ConcatVarOperation
from .string import LiteralStringVar as LiteralStringVar
from .string import StringVar as StringVar
