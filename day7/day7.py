from pathlib import Path

if __name__ == "__main__":

    data = Path(__file__).with_name("example.txt").read_text().splitlines()
    # print(data)
    for hand, str_bid in map(str.split ,data):
       
        # print(hand , str_bid)
        print(
    sum(
        (rank0 + 1) * bid
        for rank0, (*_, bid) in enumerate(
            sorted(
                (
                    max(map(hand.count, hand)),
                    -len(set(hand)),
                    *map("23456789TJQKA".index, hand),
                    int(str_bid),
                )
                for hand, str_bid in map(str.split, data)
            )
        )
    )
)
    # for  val in enumerate(data):
    #     print(val)
    #     hand = val[1].split()[0]
    #     print(hand)