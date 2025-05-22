from typing import Iterable

def ft_tqdm(lst: Iterable) -> Iterable:
    """
    tqdm-like progress bar.
    Yields items from lst while displaying a progress bar in the terminal.
    """
    total = len(lst)
    bar_length = 60

    for i, item in enumerate(lst, 1):
        percent = i / total
        filled_length = int(bar_length * percent)
        bar = '=' * (filled_length - 1) + '>' + ' ' * (bar_length - filled_length)
        print(f'\r{int(percent * 100)}%|[{bar}]| {i}/{total}', end='', flush=True)
        yield item
    print()
