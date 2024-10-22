import keyboard
from lupa import LuaRuntime

# Инициализация Lua
lua = LuaRuntime(unpack_returned_tuples=True)

# Определяем математические функции
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

# Передаем функции в Lua
lua.globals().add = add
lua.globals().subtract = subtract
lua.globals().multiply = multiply
lua.globals().divide = divide

# Lua код
lua_code = '''
function calculate(op, a, b)
    if op == "add" then
        return add(a, b)
    elseif op == "subtract" then
        return subtract(a, b)
    elseif op == "multiply" then
        return multiply(a, b)
    elseif op == "divide" then
        return divide(a, b)
    else
        return "Неизвестная операция"
    end
end

function on_input(key)
    print("Нажатая клавиша: " .. key)
end
'''

# Загружаем и выполняем Lua код
lua.execute(lua_code)

# Получаем функцию on_input из Lua
on_input = lua.globals().on_input

# Функция для обработки нажатий клавиш
def handle_key_event(event):
    on_input(event.name)

# Начинаем слушать события клавиатуры
keyboard.on_press(handle_key_event)

print("Нажмите клавиши. Нажмите ESC для выхода.")

# Бесконечный цикл, чтобы программа не завершалась
keyboard.wait('esc')