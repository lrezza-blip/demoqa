from pages.webtables_page import WebTables

def test_sorting_columns(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    column_headers = web_tables_page.get_column_headers()
    for header in column_headers:
        web_tables_page.wait_and_click(header)
        header_class = web_tables_page.get_header_class(header)
        assert 'sort-asc' in header_class or 'sort-desc' in header_class, f"Столбец '{header}' не отсортирован"

        web_tables_page.wait_and_click(header)
        header_class_desc = web_tables_page.get_header_class(header)
        assert 'sort-asc' in header_class_desc or 'sort-desc' in header_class_desc, f"Столбец '{header}' не отсортирован в обратном порядке"
