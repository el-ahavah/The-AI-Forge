import sys
import unittest
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_DIR))

from main import (  # noqa: E402
    Record,
    batches,
    best_time,
    dot,
    fit_standardizer,
    load_records,
    make_dataset,
    save_records,
    train_test_split,
)


class DataPreparationTests(unittest.TestCase):
    def test_seeded_split_is_repeatable(self):
        items = list(range(30))
        self.assertEqual(train_test_split(items, seed=7), train_test_split(items, seed=7))

    def test_split_has_no_overlap_and_keeps_all_items(self):
        items = list(range(30))
        train, test = train_test_split(items, test_fraction=0.2, seed=7)
        self.assertEqual(set(train) & set(test), set())
        self.assertEqual(sorted(train + test), items)

    def test_split_does_not_change_input(self):
        items = list(range(10))
        train_test_split(items, seed=2)
        self.assertEqual(items, list(range(10)))

    def test_invalid_split_fraction_raises(self):
        with self.assertRaises(ValueError):
            train_test_split([1, 2, 3], test_fraction=1.0)


class BatchTests(unittest.TestCase):
    def test_partial_final_batch_is_kept(self):
        self.assertEqual([len(batch) for batch in batches(range(10), 4)], [4, 4, 2])

    def test_drop_last_discards_partial_batch(self):
        self.assertEqual(list(batches(range(10), 4, drop_last=True)), [[0, 1, 2, 3], [4, 5, 6, 7]])

    def test_generator_input(self):
        self.assertEqual(list(batches((x for x in range(5)), 2)), [[0, 1], [2, 3], [4]])


class FileTests(unittest.TestCase):
    def test_csv_and_json_round_trip(self):
        import tempfile

        records = make_dataset(12, seed=4)
        with tempfile.TemporaryDirectory() as folder:
            for extension in ("csv", "json"):
                path = Path(folder) / f"records.{extension}"
                self.assertEqual(load_records(save_records(records, path)), records)

    def test_missing_or_unsupported_file_raises(self):
        with self.assertRaises(ValueError):
            load_records("missing.txt")


class NumericTests(unittest.TestCase):
    def test_dot_product(self):
        self.assertEqual(dot([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]), 32.0)

    def test_dot_product_rejects_different_lengths(self):
        with self.assertRaises(ValueError):
            dot([1.0, 2.0], [3.0])

    def test_standardizer_uses_fitted_training_statistics(self):
        transform = fit_standardizer([(1.0, 10.0), (3.0, 30.0)])
        self.assertEqual(transform((5.0, 50.0)), [3.0, 3.0])

    def test_constant_feature_does_not_divide_by_zero(self):
        transform = fit_standardizer([(2.0, 1.0), (2.0, 3.0)])
        self.assertEqual(transform((2.0, 2.0)), [0.0, 0.0])

    def test_best_time_rejects_nonpositive_repeats(self):
        with self.assertRaises(ValueError):
            best_time(sum, [1, 2, 3], repeats=0)


class RecordTests(unittest.TestCase):
    def test_records_are_immutable_and_comparable(self):
        first = Record((1.0, 2.0), 1)
        second = Record((1.0, 2.0), 1)
        self.assertEqual(first, second)
        with self.assertRaises((AttributeError, TypeError)):
            first.label = 0


if __name__ == "__main__":
    unittest.main()
