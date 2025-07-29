from screeninfo import get_monitors

for m in get_monitors():
    print(f"Display: {m.name}, x={m.x}, y={m.y}, width={m.width}, height={m.height}")
