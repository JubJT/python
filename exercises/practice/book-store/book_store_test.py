import unittest

from book_store import (
    total,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class BookStoreTest(unittest.TestCase):
    def test_only_a_single_book(self):
        basket = [1]
        self.assertEqual(total(basket), 8.0)

    def test_two_of_the_same_book(self):
        basket = [2, 2]
        self.assertEqual(total(basket), 16.00)

    def test_empty_basket(self):
        basket = []
        self.assertEqual(total(basket), 0)

    def test_two_different_books(self):
        basket = [1, 2]
        self.assertEqual(total(basket), 15.20)

    def test_three_different_books(self):
        basket = [1, 2, 3]
        self.assertEqual(total(basket), 21.60)

    def test_four_different_books(self):
        basket = [1, 2, 3, 4]
        self.assertEqual(total(basket), 25.60)

    def test_five_different_books(self):
        basket = [1, 2, 3, 4, 5]
        self.assertEqual(total(basket), 30.00)

    def test_two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(total(basket), 51.60)

    def test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three(self):
        basket = [1, 1, 2, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 51.60)

    def test_group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three(self):
        basket = [1, 1, 2, 2, 3, 4]
        self.assertEqual(total(basket), 40.80)

    def test_two_each_of_first_4_books_and_1_copy_each_of_rest(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        self.assertEqual(total(basket), 55.60)

    def test_two_copies_of_each_book(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 60.00)

    def test_three_copies_of_first_book_and_2_each_of_remaining(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
        self.assertEqual(total(basket), 68.00)

    def test_three_each_of_first_2_books_and_2_each_of_remaining_books(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2]
        self.assertEqual(total(basket), 75.20)

    def test_four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three(
        self,
    ):
        basket = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(total(basket), 103.20)

    # Additional tests for this track

    def test_two_groups_of_four_and_a_group_of_five(self):
        basket = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 81.60)

    def test_shuffled_book_order(self):
        basket = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
        self.assertEqual(total(basket), 81.60)


if __name__ == "__main__":
    unittest.main()
