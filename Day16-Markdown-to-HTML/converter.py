import re
import webbrowser
import os


def convert_markdown_to_html(markdown_text):
    html = markdown_text

    # Headers
    html = re.sub(r"^## (.*)", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.*)", r"<h1>\1</h1>", html, flags=re.MULTILINE)

    # Bold
    html = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", html)

    # Italic
    html = re.sub(r"\*(.*?)\*", r"<i>\1</i>", html)

    # Links
    html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', html)

    # Lists
    lines = html.split("\n")
    in_list = False
    result = []

    for line in lines:
        if line.startswith("- "):
            if not in_list:
                result.append("<ul>")
                in_list = True
            result.append(f"<li>{line[2:]}</li>")
        else:
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(f"<p>{line}</p>")

    if in_list:
        result.append("</ul>")

    return "\n".join(result)


def main():
    with open("sample.md", "r", encoding="utf-8") as file:
        markdown_text = file.read()

    html_content = convert_markdown_to_html(markdown_text)

    output_file = "output.html"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print("✅ Markdown converted to HTML.")

    webbrowser.open(f"file://{os.path.abspath(output_file)}")


main()
