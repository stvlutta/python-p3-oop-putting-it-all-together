#!/usr/bin/env python3

import sys
import io
from lib.book import Book
from lib.shoe import Shoe

def test_book():
    # Test title and page_count
    book = Book("And Then There Were None", 272)
    assert book.page_count == 272
    assert book.title == "And Then There Were None"
    
    # Test page_count validation
    captured_out = io.StringIO()
    sys.stdout = captured_out
    book.page_count = "not an integer"
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "page_count must be an integer\n"
    
    # Test turn_page method
    captured_out = io.StringIO()
    sys.stdout = captured_out
    book.turn_page()
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"
    
    print("Book tests passed!")

def test_shoe():
    # Test brand and size
    stan_smith = Shoe("Adidas", 9)
    assert stan_smith.brand == "Adidas"
    assert stan_smith.size == 9
    
    # Test size validation
    captured_out = io.StringIO()
    sys.stdout = captured_out
    stan_smith.size = "not an integer"
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "size must be an integer\n"
    
    # Test cobble method
    captured_out = io.StringIO()
    sys.stdout = captured_out
    stan_smith.cobble()
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Your shoe is as good as new!\n"
    
    # Test cobble sets condition to New
    assert stan_smith.condition == "New"
    
    print("Shoe tests passed!")

if __name__ == "__main__":
    test_book()
    test_shoe()
    print("All tests passed!")