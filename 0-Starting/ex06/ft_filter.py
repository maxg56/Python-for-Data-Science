from typing import Callable, Iterable, TypeVar, Iterator, Optional

T = TypeVar('T')


def ft_filter(
        function: Optional[Callable[[T], bool]],
        iterable: Iterable[T]) -> Iterator[T]:
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
