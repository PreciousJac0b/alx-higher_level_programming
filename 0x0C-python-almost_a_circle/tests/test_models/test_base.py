import unittest
from models.base import Base
from models.rectangle import Rectangle

"""Defines unittests for base.py
"""

class TestBaseClass_id(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def test_four_base(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b2.id, b4.id - 2)
        self.assertEqual(b1.id, b3.id - 2)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_number(self):
        b1 = Base(12)
        self.assertEqual(12, b1.id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_string_input(self):
        self.assertEqual("I am python", Base("I am python").id)

    def test_float(self):
        self.assertEqual(8.2, Base(8.2).id)

    def test_complex_id(self):
        self.assertEqual(complex(2), Base(complex(2)).id)

    def test_dict_id(self):
        self.assertEqual({'a': 1, 'b': 2}, Base({'a': 1, 'b': 2}).id)

    def test_list_id(self):
        new_list = [1, 2, 3, 4, 5]
        self.assertEqual([1, 2, 3, 4, 5], Base(new_list).id)

    def test_tuple_id(self):
        new_tuple = (1, 2, 3, 4, 5)
        self.assertEqual(new_tuple, Base(new_tuple).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        freeze_set = frozenset({1, 2, 3})
        self.assertEqual(freeze_set, Base(freeze_set).id)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_outnumbered_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2, 3, 4, 5)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            Base(2).__nb_instances

    def test_bytecode_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'gege'), Base(bytearray(b'gege')).id)


class TestBase_to_json_string(unittest.TestCase):
    """Unittest for testing the to_json string of the Base class"""
    def test_type(self):
        r1 = Rectangle(1, 3, 4, 3, 5)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))
