from pyscript import document, display

def print_grade(e):
    first = document.getElementById("firstname").value
    last = document.getElementById("lastname").value

    def get_grade(id):
        value = document.getElementById(id).value
        return float(value) if value.strip() else 0.0

    sci = get_grade("sci")
    math = get_grade("math")
    eng = get_grade("eng")
    ict = get_grade("ict")
    fil = get_grade("fil")
    pe = get_grade("pe")

    grades = [sci, math, eng, ict, fil, pe]
    avg_g = round(sum(grades) / len(grades), 2)

    grades_text = f"""
    Science: {sci}
    Math: {math}
    English: {eng}
    ICT: {ict}
    Filipino: {fil}
    PE: {pe}
    """

    display(f"Name: {first} {last}", target="name")
    display(grades_text.strip(), target="items")
    display(f"Your general weighted average is {avg_g}", target="avg_g")
