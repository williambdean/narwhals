from __future__ import annotations  # pragma: no cover

from typing import TYPE_CHECKING  # pragma: no cover
from typing import Any  # pragma: no cover
from typing import Callable
from typing import TypedDict
from typing import TypeVar  # pragma: no cover

if TYPE_CHECKING:
    import sys
    from typing import Generic
    from typing import Literal

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

    import pyarrow as pa
    import pyarrow.compute as pc
    from pandas.api.extensions import ExtensionDtype as PandasExtensionDtype
    from pyarrow._stubs_typing import (  # pyright: ignore[reportMissingModuleSource]
        Indices,  # noqa: F401
    )
    from pyarrow._stubs_typing import (  # pyright: ignore[reportMissingModuleSource]
        Mask,  # noqa: F401
    )
    from pyarrow._stubs_typing import (  # pyright: ignore[reportMissingModuleSource]
        Order,  # noqa: F401
    )

    from narwhals._arrow.expr import ArrowExpr
    from narwhals._arrow.series import ArrowSeries

    IntoArrowExpr: TypeAlias = "ArrowExpr | ArrowSeries"
    TieBreaker: TypeAlias = Literal["min", "max", "first", "dense"]
    NullPlacement: TypeAlias = Literal["at_start", "at_end"]

    StringArray: TypeAlias = pc.StringArray
    ArrowChunkedArray: TypeAlias = pa.ChunkedArray[Any]
    ArrowArray: TypeAlias = pa.Array[Any]
    _AsPyType = TypeVar("_AsPyType")

    class _BasicDataType(pa.DataType, Generic[_AsPyType]): ...


Incomplete: TypeAlias = Any  # pragma: no cover
"""
Marker for working code that fails on the stubs.

Common issues:
- Annotated for `Array`, but not `ChunkedArray`
- Relies on typing information that the stubs don't provide statically
- Missing attributes
- Incorrect return types
- Inconsistent use of generic/concrete types
- `_clone_signature` used on signatures that are not identical
"""


class ArrowTableToPandasKwds(TypedDict, total=False):
    """Keyword arguments for [pyarrow.Table.to_pandas](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table.to_pandas)."""

    memory_pool: pa.MemoryPool | None
    categories: list[Any] | None
    strings_to_categorical: bool
    zero_copy_only: bool
    integer_object_nulls: bool
    date_as_object: bool
    timestamp_as_object: bool
    use_threads: bool
    deduplicate_objects: bool
    ignore_metadata: bool
    safe: bool
    split_blocks: bool
    self_destruct: bool
    maps_as_pydicts: Literal["None", "lossy", "strict"] | None
    types_mapper: Callable[[pa.DataType], PandasExtensionDtype | None] | None
    coerce_temporal_nanoseconds: bool
