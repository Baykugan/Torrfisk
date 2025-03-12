from enum import IntEnum

import numpy as np


class PieceType(IntEnum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5


class PieceColor(IntEnum):
    WHITE = 0
    BLACK = 1


class WhitePieces(IntEnum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5


class BlackPieces(IntEnum):
    PAWN = 6
    KNIGHT = 7
    BISHOP = 8
    ROOK = 9
    QUEEN = 10
    KING = 11


class Piece(IntEnum):
    WHITE_PAWN = 0
    WHITE_KNIGHT = 1
    WHITE_BISHOP = 2
    WHITE_ROOK = 3
    WHITE_QUEEN = 4
    WHITE_KING = 5
    BLACK_PAWN = 6
    BLACK_KNIGHT = 7
    BLACK_BISHOP = 8
    BLACK_ROOK = 9
    BLACK_QUEEN = 10
    BLACK_KING = 11


class MoveType(IntEnum):
    NORMAL = 0
    CASTLE = 1
    EN_PASSANT = 2
    PROMOTION = 3


class Castle(IntEnum):
    WHITE_KING_SIDE = 0
    WHITE_QUEEN_SIDE = 1
    BLACK_KING_SIDE = 2
    BLACK_QUEEN_SIDE = 3


class Rank(IntEnum):
    R1 = np.uint64(0b0000000000000000000000000000000000000000000000000000000011111111)
    R2 = np.uint64(0b0000000000000000000000000000000000000000000000001111111100000000)
    R3 = np.uint64(0b0000000000000000000000000000000000000000111111110000000000000000)
    R4 = np.uint64(0b0000000000000000000000000000000011111111000000000000000000000000)
    R5 = np.uint64(0b0000000000000000000000001111111100000000000000000000000000000000)
    R6 = np.uint64(0b0000000000000000111111110000000000000000000000000000000000000000)
    R7 = np.uint64(0b0000000011111111000000000000000000000000000000000000000000000000)
    R8 = np.uint64(0b1111111100000000000000000000000000000000000000000000000000000000)


class File(IntEnum):
    A = np.uint64(0b1000000010000000100000001000000010000000100000001000000010000000)
    B = np.uint64(0b0100000001000000010000000100000001000000010000000100000001000000)
    C = np.uint64(0b0010000000100000001000000010000000100000001000000010000000100000)
    D = np.uint64(0b0001000000010000000100000001000000010000000100000001000000010000)
    E = np.uint64(0b0000100000001000000010000000100000001000000010000000100000001000)
    F = np.uint64(0b0000010000000100000001000000010000000100000001000000010000000100)
    G = np.uint64(0b0000001000000010000000100000001000000010000000100000001000000010)
    H = np.uint64(0b0000000100000001000000010000000100000001000000010000000100000001)


class Square(IntEnum):
    A1 = Rank.R1 & File.A
    B1 = Rank.R1 & File.B
    C1 = Rank.R1 & File.C
    D1 = Rank.R1 & File.D
    E1 = Rank.R1 & File.E
    F1 = Rank.R1 & File.F
    G1 = Rank.R1 & File.G
    H1 = Rank.R1 & File.H

    A2 = Rank.R2 & File.A
    B2 = Rank.R2 & File.B
    C2 = Rank.R2 & File.C
    D2 = Rank.R2 & File.D
    E2 = Rank.R2 & File.E
    F2 = Rank.R2 & File.F
    G2 = Rank.R2 & File.G
    H2 = Rank.R2 & File.H

    A3 = Rank.R3 & File.A
    B3 = Rank.R3 & File.B
    C3 = Rank.R3 & File.C
    D3 = Rank.R3 & File.D
    E3 = Rank.R3 & File.E
    F3 = Rank.R3 & File.F
    G3 = Rank.R3 & File.G
    H3 = Rank.R3 & File.H

    A4 = Rank.R4 & File.A
    B4 = Rank.R4 & File.B
    C4 = Rank.R4 & File.C
    D4 = Rank.R4 & File.D
    E4 = Rank.R4 & File.E
    F4 = Rank.R4 & File.F
    G4 = Rank.R4 & File.G
    H4 = Rank.R4 & File.H

    A5 = Rank.R5 & File.A
    B5 = Rank.R5 & File.B
    C5 = Rank.R5 & File.C
    D5 = Rank.R5 & File.D
    E5 = Rank.R5 & File.E
    F5 = Rank.R5 & File.F
    G5 = Rank.R5 & File.G
    H5 = Rank.R5 & File.H

    A6 = Rank.R6 & File.A
    B6 = Rank.R6 & File.B
    C6 = Rank.R6 & File.C
    D6 = Rank.R6 & File.D
    E6 = Rank.R6 & File.E
    F6 = Rank.R6 & File.F
    G6 = Rank.R6 & File.G
    H6 = Rank.R6 & File.H

    A7 = Rank.R7 & File.A
    B7 = Rank.R7 & File.B
    C7 = Rank.R7 & File.C
    D7 = Rank.R7 & File.D
    E7 = Rank.R7 & File.E
    F7 = Rank.R7 & File.F
    G7 = Rank.R7 & File.G
    H7 = Rank.R7 & File.H

    A8 = Rank.R8 & File.A
    B8 = Rank.R8 & File.B
    C8 = Rank.R8 & File.C
    D8 = Rank.R8 & File.D
    E8 = Rank.R8 & File.E
    F8 = Rank.R8 & File.F
    G8 = Rank.R8 & File.G
    H8 = Rank.R8 & File.H
