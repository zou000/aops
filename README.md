# Aops scraper

Python scripts that scraps aops wiki site and generate printable math competition practice problem sets.

## Install

Just copy the 2 scripts anywhere on your disk. Needs `bs4` python package: `pip install bs4`

## Usage

Two steps:

1. Generate catalog for a problem category. Follow the links on `https://artofproblemsolving.com/wiki/index.php/Category:Math_Problems` until landed on a list of problems. Run the script below to download and randomize the catalog.

```python
 python aops_cat.py https://artofproblemsolving.com/wiki/index.php/Category:Introductory_Algebra_Problems > algebra_toc.html
```

This needs to be run only once per category. The links in the catalog points to a problem and its solution. See [example](examples/algebra_toc.html) 

2. Run the script to select problems from catalog and generate printable problem set. The input are catalog file generated above, start and end problem numner (inclusive). See [example](examples/algebra_1_30.html)

```python
 python aops_pset.py algebra_toc.html 1 30 > test.html
```
