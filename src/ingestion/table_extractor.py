import pdfplumber


def find_tables_on_page(page):
    """
    Detect tables on a pdfplumber page.

    Returns pdfplumber Table objects.
    """

    return page.find_tables()


def extract_tables_from_page(page):
    """
    Detect and extract all tables from one page.
    """

    tables = page.find_tables()

    extracted_tables = []

    for table_number, table in enumerate(tables, start=1):

        extracted_tables.append({
            "table_number": table_number,
            "bbox": table.bbox,
            "cells": table.extract()
        })

    return extracted_tables


def extract_tables_from_pdf(pdf_path):
    """
    Extract tables from every page of a PDF.
    """

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages, start=1):

            tables = extract_tables_from_page(page)

            pages.append({
                "page_number": page_number,
                "tables": tables
            })

    return pages