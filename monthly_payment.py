def calculate_monthly_payment(P, rate, years):
    r = ((rate/100)/12)
    n = 12 * years
    A = ((P * r * ((1+r) ** n))/(((1+r) ** n) -1))
    return A

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")

# A = avbetalning per månad i kronor
# P = totala lånebeloppet
# r = räntan per period (t.ex. om räntan är 9% blir det r = 0.09 / 12)
# n = totalt antal betalningsperioder