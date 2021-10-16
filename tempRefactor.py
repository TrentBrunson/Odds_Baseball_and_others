print(
    f"Temperature Conversions\n"
    f"+++++++++++++++++++++++\n"
    f"CELSIUS       FARENHEIT\n"
    f"~~~~~~~~~~~~~~~~~~~~~~~\n"
)

for c in range(-50, 51, 5):
    f = (9/5) * c + 32
    print(f"{c:>5}\t\t{round(f):>5}")