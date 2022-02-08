import typer

from english_words import english_words


def is_word_valid(characters: set[str], center: str, minimum: int, word: str) -> bool:
    if len(word) < minimum:
        return False

    if center not in word:
        return False

    return characters.union(set(word)) == characters


def get_valid_words(characters: set[str], center: str, minimum: int) -> list[str]:
    words: list[str] = []

    for word in english_words:
        if is_word_valid(characters, center, minimum, word):
            words.append(word)

    return words


def sort_words(words: list[str]) -> list[str]:
    # alphabetical
    words.sort()

    # by length, longest to shortest
    words.sort(key=len, reverse=True)

    return words


def print_words(words: list[str]):
    print("\n".join(sort_words(words)))


def main(characters: str, center: str, minimum: int = typer.Option(4)):
    print_words(get_valid_words(set(characters), center, minimum))


if __name__ == "__main__":
    typer.run(main)
