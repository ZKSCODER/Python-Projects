# Form POC

This proof-of-concept reads an order number visible on a Google Form page, finds the matching row in an `.xlsx`, and fills fields based on a header->selector mapping.

## Setup

```bash
python -m pip install openpyxl playwright
python -m playwright install
```

## Capture selectors (recommended)

```bash
python -m playwright codegen https://forms.gle/hnifwUJbNPfLyDjD7
```

Use the generated selectors to update `SELECTORS` in `fill_form.py`.

## Run

```bash
python fill_form.py /path/to/your.xlsx
```

## Notes
- Update `ORDER_REGEX` in `fill_form.py` to match the visible order number text on the form (e.g., `Order #: 12345`).
- Update `FORM_URL` if the link changes.
- For dropdowns and multi-page flows, we can extend this with `page.select_option`, `page.click`, and explicit `page.wait_for_*` calls.
