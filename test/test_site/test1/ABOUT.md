# Aim of test

The aim of this test is to check if multithread search gives a lot of profit in search speed. 

# How to test

`simple_sync_search.py` contains function with single thread search.

`simple_multithread_search.py` contains function with multithread search.

`test.py` gives you opportunity to compare speeds of two ways.

# Result

Tests have shown that a multithreaded program works 3-4 times faster. 

We need to rewrite the main search in a multithreaded format, because this will improve the user experience.
