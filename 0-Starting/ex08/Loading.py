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
        fl = int(bar_length * percent)
        bar = '=' * (fl - 1) + '>' + ' ' * (bar_length - fl)
        print(f'\r{int(percent * 100)}%|[{bar}]| {i}/{total}', end='',
              flush=True)
        yield item
    print()
