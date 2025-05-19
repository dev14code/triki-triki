import unittest
from triki_triki import imprimir_tablero, movimiento_jugador, victoria, empate, tablero

class TestTrikiTriki(unittest.TestCase):

    def setUp(self):
        global tablero
        tablero = [" " for i in range(9)]

    def test_imprimir_tablero(self):
        tablero[0] = "X"
        tablero[4] = "O"
        tablero[8] = "X"
        expected_output = "\n| X |   |   |\n|   | O |   |\n|   |   | X |\n\n"
        with self.assertLogs() as log:
            imprimir_tablero()
            self.assertIn(expected_output, log.output)

    def test_movimiento_jugador(self):
        movimiento_jugador("X")
        self.assertEqual(tablero[0], "X")
        self.assertNotEqual(tablero[1], "X")

    def test_victoria(self):
        tablero[0] = "X"
        tablero[1] = "X"
        tablero[2] = "X"
        self.assertTrue(victoria("X"))
        self.assertFalse(victoria("O"))

    def test_empate(self):
        for i in range(9):
            tablero[i] = "X" if i % 2 == 0 else "O"
        self.assertTrue(empate())
        tablero[8] = " "
        self.assertFalse(empate())

if __name__ == "__main__":
    unittest.main()
