from typing import Callable, Iterable, TypeVar, Iterator, Optional

T = TypeVar('T')


def ft_filter(function: Optional[Callable[[T], bool]],
              iterable: Iterable[T]) -> Iterator[T]:
    """
    Filters elements from an iterable based on a function.
    If function is None, filters out falsy values.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def count_in_list(lst: list, s: str):
    """
        Return the number of occurence of s in the list
    """
    return len(list(ft_filter(lambda x: x == s, lst)))
