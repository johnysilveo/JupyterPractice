WIDTH = 90
INNER_WIDTH = WIDTH - 2

def border() -> str:
    pattern = "<>"
    middle = (pattern * WIDTH)[:WIDTH - 2]
    return f"*{middle}*"

def centered(text: str = "") -> str:
    return f"|{text:^{INNER_WIDTH}}|"

def show_header(title: str) -> None:
  print(border())
  print(centered())
  print(centered(title))
  print(centered())
  print(border())

def result_border() -> str:
    return "+" + "-" * INNER_WIDTH + "+"

def show_result(value) -> None:
    print(result_border())
    for line in str(value).splitlines():
        print(centered(line))
    print(result_border())


def show_markdown_table(headers, rows, align=None):
    if align is None:
        align = ["left"] * len(headers)
    #find required width for every column
    widths = []
    for i, header in enumerate(headers):
        width = len(str(header))
        for row in rows:
            width = max(width, len(str(row[i])))
        widths.append(max(width, 5))

    #format normal cells
    def format_cell(value, width, alignment):
        text = str(value)
        if alignment == "center":
            return text.center(width)
        if alignment == "right":
            return text.rjust(width)
        return text.ljust(width)

    #create markdown separator
    def make_separator(width, alignment):
        if alignment == "center":
            return ":" + "-" * (width - 2) + ":"
        if alignment == "right":
            return "-" * (width - 1) + ":"
        return ":" + "-" * (width - 1)
    table = []

    #header
    table.append(
        "| " + " | ".join(
            format_cell(headers[i], widths[i], align[i])
            for i in range(len(headers))
        ) + " |"
    )
    #markdown separator
    table.append(
        "| " + " | ".join(
            make_separator(widths[i], align[i])
            for i in range(len(headers))
        ) + " |"
    )
    #rows
    for row in rows:
        table.append(
            "| " + " | ".join(
                format_cell(row[i], widths[i], align[i])
                for i in range(len(headers))
            ) + " |"
        )
    print(result_border())
    for line in table:
        print(centered(line))
    print(result_border())
