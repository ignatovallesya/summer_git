# 2.6
distance = float(input("Сколько километров хотите проехать на автомобиле? "))
fuel_consumption = float(input("Сколько литров расходует на 100 километров? "))
fuel_in_tank = float(input("Сколько литров топлива в вашем баке? "))

fuel_needed = (distance / 100) * fuel_consumption

if fuel_in_tank >= fuel_needed:
    print("Вы сможете проехать желаемое расстояние.")
else:
    print("У вас недостаточно топлива для проезда желаемого расстояния.")
