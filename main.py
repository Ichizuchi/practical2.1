
y = float(input("Введите угол наклона часовой стрелки (0 < y < 360): "))

hours = int(y // 30)  # Каждый час равен 30 градусам (360 градусов / 12 часов)

remaining_angle = y % 30
minutes = int((remaining_angle / 30) * 60)

print("Полных часов:", hours, "часа")
print("ПОлных минут:", minutes, "минут")
