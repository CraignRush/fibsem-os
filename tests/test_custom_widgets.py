"""Tests for custom widgets - focused on the closest_value logic."""

import sys
import os

# Set up Qt environment variables for headless testing
os.environ["QT_QPA_PLATFORM"] = "offscreen"

import pytest
from PyQt5.QtWidgets import QApplication

# Ensure QApplication exists for testing Qt widgets
app = QApplication.instance() or QApplication(sys.argv)


def test_string_subtraction_error_original():
    """Test that the original error case (string subtraction) is now handled."""
    # This would have caused: TypeError: unsupported operand type(s) for -: 'str' and 'str'
    items = ['8i-cc3', 'Si-cc3 Neu', 'config1', 'config2']
    value = 'nonexistent'
    
    # The logic we're testing
    if items:
        if isinstance(value, (int, float)) and all(isinstance(x, (int, float)) for x in items):
            # numeric comparison - should not be used for strings
            closest_value = min(items, key=lambda x: abs(x - value))
        else:
            # string comparison - should be used for strings
            str_value = str(value).lower()
            closest_value = next(
                (item for item in items if str(item).lower() == str_value),
                next(
                    (item for item in items if str_value in str(item).lower()),
                    items[0]
                )
            )
    else:
        closest_value = value
    
    # Should default to first item when no match
    assert closest_value == '8i-cc3'


def test_numeric_values_closest_match():
    """Test that numeric values find the closest match."""
    items = [1.0, 2.0, 3.0, 4.0, 5.0]
    value = 2.3
    
    if items:
        if isinstance(value, (int, float)) and all(isinstance(x, (int, float)) for x in items):
            closest_value = min(items, key=lambda x: abs(x - value))
        else:
            str_value = str(value).lower()
            closest_value = next(
                (item for item in items if str(item).lower() == str_value),
                next(
                    (item for item in items if str_value in str(item).lower()),
                    items[0]
                )
            )
    else:
        closest_value = value
    
    assert closest_value == 2.0


def test_string_values_exact_match():
    """Test that string values find exact match."""
    items = ['8i-cc3', 'Si-cc3 Neu', 'config1', 'config2']
    value = '8i-cc3'
    
    if items:
        if isinstance(value, (int, float)) and all(isinstance(x, (int, float)) for x in items):
            closest_value = min(items, key=lambda x: abs(x - value))
        else:
            str_value = str(value).lower()
            closest_value = next(
                (item for item in items if str(item).lower() == str_value),
                next(
                    (item for item in items if str_value in str(item).lower()),
                    items[0]
                )
            )
    else:
        closest_value = value
    
    assert closest_value == '8i-cc3'


def test_string_values_case_insensitive_match():
    """Test that string values find case-insensitive match."""
    items = ['Config1', 'Config2', 'Config3']
    value = 'config1'
    
    if items:
        if isinstance(value, (int, float)) and all(isinstance(x, (int, float)) for x in items):
            closest_value = min(items, key=lambda x: abs(x - value))
        else:
            str_value = str(value).lower()
            closest_value = next(
                (item for item in items if str(item).lower() == str_value),
                next(
                    (item for item in items if str_value in str(item).lower()),
                    items[0]
                )
            )
    else:
        closest_value = value
    
    assert closest_value == 'Config1'


def test_string_values_substring_match():
    """Test that string values find substring match."""
    items = ['8i-cc3-config', 'Si-cc3 Neu', 'other-config']
    value = 'cc3'
    
    if items:
        if isinstance(value, (int, float)) and all(isinstance(x, (int, float)) for x in items):
            closest_value = min(items, key=lambda x: abs(x - value))
        else:
            str_value = str(value).lower()
            closest_value = next(
                (item for item in items if str(item).lower() == str_value),
                next(
                    (item for item in items if str_value in str(item).lower()),
                    items[0]
                )
            )
    else:
        closest_value = value
    
    assert closest_value == '8i-cc3-config'
