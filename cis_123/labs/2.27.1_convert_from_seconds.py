seconds = int(input())

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60

print(f'Seconds: {seconds}\nMinutes: {minutes}\nHours: {hours}')