import sys


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        print(0)
        return
    n, m, k = data[:3]
    moves = data[3:]
    # grid cells are 1-based; we'll track colored cells and check 2x2 blocks
    colored = set()

    def has_square(x, y):
        # check if (x,y) is top-left of a 2x2 fully colored square
        return (
            (x, y) in colored
            and (x + 1, y) in colored
            and (x, y + 1) in colored
            and (x + 1, y + 1) in colored
        )

    for i in range(k):
        x = moves[2 * i]
        y = moves[2 * i + 1]
        colored.add((x, y))
        # only need to check up to 4 candidate top-left corners
        for dx in (0, -1):
            for dy in (0, -1):
                tx, ty = x + dx, y + dy
                if 1 <= tx < n and 1 <= ty < m and has_square(tx, ty):
                    print(i + 1)  # 1-based index of the move
                    return
    print(0)


if __name__ == "__main__":
    main()
