


def solve_puzzle():
    for row1 in [[6,7,7],[7,6,7],[7,7,6]]:
        for row2 in [[8,3,9],[3,9,8],[9,8,3],[9,3,8],[3,8,9],[8,9,3],[4,6,9],[6,9,4],[9,4,6],[9,6,4],[6,4,9],[4,9,6]]:
            for row3 in [[3,5,9],[5,9,3],[9,3,5],[9,5,3],[5,3,9],[3,9,5]]:
                for row4 in [[2,7,7],[7,2,7],[7,7,2]]:
                    for row5 in [[8,2,7],[2,7,8],[7,8,2],[7,2,8],[2,8,7],[8,7,2],[7,4,4],[4,7,4],[4,4,7]]:
                        for row6 in [[4,3,7],[3,7,4],[7,4,3],[7,3,4],[3,4,7],[4,7,3],[2,6,7],[6,7,2],[7,2,6],[7,6,2],[6,2,7],[2,7,6]]:
                            for row7 in [[5,7,7],[7,5,7],[7,7,5]]:
                                for row8 in [[2,4,5],[4,5,2],[5,2,4],[5,4,2],[4,2,5],[2,5,4],[8,1,5],[1,5,8],[5,8,1],[5,1,8],[1,8,5],[8,5,1]]:
                                    if row1[0]*row2[0]*row3[0]*row4[0]*row5[0]*row6[0]*row7[0]*row8[0] == 8890560:
                                        if row1[1]*row2[1]*row3[1]*row4[1]*row5[1]*row6[1]*row7[1]*row8[1] == 156800:
                                            if row1[2]*row2[2]*row3[2]*row4[2]*row5[2]*row6[2]*row7[2]*row8[2] == 55566:
                                                print("Success!")
                                                print(row1)
                                                print(row2)
                                                print(row3)
                                                print(row4)
                                                print(row5)
                                                print(row6)
                                                print(row7)
                                                print(row8)

def main():
    solve_puzzle()


if __name__ == "__main__":
    main()