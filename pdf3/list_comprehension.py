import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from pdf2.person import Person


N = 4


def main():
    squares = [number**2 for number in range(1, N)]
    people = [Person() for _ in range(N)]
    adults = [person for person in people if person.get_age() > 18]
    for adult in adults:
        print(adult)

if __name__ == "__main__":
    main()
