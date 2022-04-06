import unittest
from argparse import ArgumentTypeError

import Chat


def returnOne():
    return 1


class TestChat(unittest.TestCase):
    def test_constructor_1(self):
        chat = Chat.Chat("Minou")
        self.assertEqual(chat.nom, "Minou")
        self.assertEqual(chat.classification, Chat.Classification.MAMIFERE)
        self.assertEqual(chat.isCute, True)

    def test_constructor_2(self):
        self.assertRaises(ArgumentTypeError, Chat.Chat, 2)

    # def test_returnOne(self):
    #     self.assertEqual(returnOne(), 2)


if __name__ == "__main__":
    unittest.main()
