import sys
from xml.sax.saxutils import escape

maxwidth = 100
format = ".0f"

def process_options():
    global maxwidth
    global format
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("usage: {0} [maxwidth=int] [format=str] < infile.csv > outfile.html".format(sys.argv[0]))
            print("maxwidth is an optional integer; if specified, it sets the maximum\n"
                "number of characters that can be output for string fields,\n"
                "otherwise a default of 100 characters is used.\n"
                "(maxwidth - необязательное целое число. Если задано, опреедляет\n"
                "максимальное число символов для строковых полей. В противном случае\n"
                "используется значение по умолчанию 100.)\n\n"
                "format is the format to use for numbers; if not specified it\n"
                "defaults to '.0f'.\n"
                "(format - формат вывода чисел. Если не задан, по умолчанию используется\n"
                "формат '.0f'.\n\n"
                "Пример: {0} maxwidth=20 format=0.2f < mydata.csv > mydata.html".format(sys.argv[0])
            )
            sys.exit()
        else:
            try:
                maxwidth = int(sys.argv[1].strip('maxwidth='))
            except:
                maxwidth = 100
            try:
                format = str(sys.argv[2].strip('format='))
            except:
                format = ".0f"


def main():
    process_options()
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth, format)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(x, format))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = escape(field)
                else:
                    field = "{0} ...".format(
                            escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def print_end():
    print("</table>")


main()
