import csv
from pathlib import Path
import html

def format_number(value):
    value = value.strip()

    if value == "" or value.lower() == "nan":
        return ""
    try:
        return f"{float(value):,.0f}"
    except ValueError:
        return html.escape(value)

def csv_to_pluto_table(csv_path, output_path, col1_name, col2_name):
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))

    header = rows[0]
    years = header[1:]

    col1_values = None
    col2_values = None

    col1_key = col1_name.strip().lower()
    col2_key = col2_name.strip().lower()

    for row in rows[1:]:
        label = row[0].strip().lower()

        if label == col1_key:
            col1_values = row[1:]

        elif label == col2_key:
            col2_values = row[1:]

    if col1_values is None:
        raise ValueError(f"Could not find row: {col1_name}")

    if col2_values is None:
        raise ValueError(f"Could not find row: {col2_name}")

    html_rows = [
        'html"""',
        '<table class="lecture-table">',
        "  <thead>",
        "    <tr>",
        "      <th>Year</th>",
        f"      <th>{html.escape(col1_name)}</th>",
        f"      <th>{html.escape(col2_name)}</th>",
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]

    for year, v1, v2 in zip(years, col1_values, col2_values):
        html_rows.append("    <tr>")
        html_rows.append(f"      <td>{html.escape(year)}</td>")
        html_rows.append(f"      <td>{format_number(v1)}</td>")
        html_rows.append(f"      <td>{format_number(v2)}</td>")
        html_rows.append("    </tr>")

    html_rows += [
        "  </tbody>",
        "</table>",
        '"""'
    ]

    table_html = "\n".join(html_rows)
    Path(output_path).write_text(table_html, encoding="utf-8")

    return table_html

if __name__ == "__main__":
    csv_to_pluto_table(
        csv_path = "DATA/GDPGDI.csv",
        output_path = "table_helper_output.txt",
        col1_name = "Gross domestic product",
        col2_name = "Gross domestic income"
        # col1_name = "Total assets",
        # col2_name = "Total liabilities"
    )
    print("Created table in table_helper_output.txt")