"""
Processpool Executor vereinfacht das Handling mit Processen
"""

from concurrent.futures import ProcessPoolExecutor


def quad(x):
    return x**2


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(quad, range(10))

    print(list(results))
