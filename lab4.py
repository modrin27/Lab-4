# Item dictionary for Variant 2 / Словарь предметов для Варианта 2
# Format: 'name': {'size': cells, 'points': survival points} / Формат: 'название': {'size': ячейки, 'points': очки}
items = {
    'r': {'en': 'rifle', 'ru': 'винтовка', 'size': 3, 'points': 25},
    'p': {'en': 'pistol', 'ru': 'пистолет', 'size': 2, 'points': 15},
    'a': {'en': 'ammo', 'ru': 'боекомплект', 'size': 2, 'points': 15},
    'm': {'en': 'medkit', 'ru': 'аптечка', 'size': 2, 'points': 20},
    'i': {'en': 'inhaler', 'ru': 'ингалятор', 'size': 1, 'points': 5},
    'k': {'en': 'knife', 'ru': 'нож', 'size': 1, 'points': 15},
    'x': {'en': 'axe', 'ru': 'топор', 'size': 3, 'points': 20},
    't': {'en': 'talisman', 'ru': 'оберег', 'size': 1, 'points': 25},
    'f': {'en': 'flask', 'ru': 'фляжка', 'size': 1, 'points': 15},
    'd': {'en': 'antidote', 'ru': 'антидот', 'size': 1, 'points': 10},
    's': {'en': 'supplies', 'ru': 'еда', 'size': 2, 'points': 20},
    'c': {'en': 'crossbow', 'ru': 'арбалет', 'size': 2, 'points': 20}
}

# Rules for Variant 2 / Правила для Варианта 2
# 3x3 grid, asthma (need inhaler), start with 10 points / Сетка 3x3, астма (нужен ингалятор), старт 10 очков
GRID_SIZE = 3 * 3  # 9 cells total / Всего 9 ячеек
START_POINTS = 10  # Starting points / Стартовые очки
REQUIRED_ITEM = 'i' # Inhaler is required for asthma / Ингалятор обязателен из-за астмы

# Check if data is loaded / Проверка, что данные загружены
print("Items count (Количество предметов):", len(items))
print(f"Grid size (Размер рюкзака): {GRID_SIZE}")
print(f"Start points (Стартовые очки): {START_POINTS}")
import itertools # Import library to generate combinations / Импортируем библиотеку для комбинаций

# Calculate total points of all items in the game / Считаем сумму очков всех предметов в игре
total_all_points = sum(item['points'] for item in items.values())

# Variables to store our best result / Переменные для хранения лучшего результата
best_score = -9999
best_combo = []
positive_combos = [] # For the additional task / Для дополнительного задания

# Generate all possible combinations of items / Генерируем все возможные комбинации
item_keys = list(items.keys())
for r in range(len(item_keys) + 1):
    for combo in itertools.combinations(item_keys, r):
        # 1. Check if inhaler is inside (Asthma) / Проверяем наличие ингалятора (Астма)
        if REQUIRED_ITEM not in combo:
            continue
        
        # 2. Check backpack size / Проверяем размер рюкзака
        total_size = sum(items[i]['size'] for i in combo)
        if total_size > GRID_SIZE:
            continue
            
        # 3. Calculate score / Считаем очки
        taken_points = sum(items[i]['points'] for i in combo)
        left_points = total_all_points - taken_points
        current_score = START_POINTS + taken_points - left_points
        
        # Save all positive combinations (for Additional Task) / Сохраняем все комбинации с плюсом (для доп. задания)
        if current_score > 0:
            positive_combos.append((combo, current_score))
            
        # Find the best (maximum) score / Ищем лучшую (максимальную) комбинацию
        if current_score > best_score:
            best_score = current_score
            best_combo = combo

# Print the results / Печатаем результаты
print("\n--- Best Combination (Лучшая комбинация) ---")
print("Items:", best_combo)
print("Score:", best_score)
print("Total combinations with positive score (Всего комбинаций с плюсом):", len(positive_combos))

# Step 7: Format best combination as a 2D grid / Шаг 7: Форматируем лучшую комбинацию как 2D сетку
print("\n--- 2D Inventory (Двумерный инвентарь) ---")

grid_cells = []
# We take the best combo and duplicate the letter based on its size
# Берем лучшую комбинацию и дублируем букву в зависимости от ее размера
for item_code in best_combo:
    for _ in range(items[item_code]['size']):
        grid_cells.append(f"[{item_code}]")

# Print the grid row by row (3 cells per row)
# Печатаем сетку построчно (по 3 ячейки в ряд)
for i in range(0, len(grid_cells), 3):
    print(",".join(grid_cells[i:i+3]))
    # --- Additional Task 1: Check for 7 cells / Доп. задание 1: Проверка для 7 ячеек ---
print("\n--- 7 Cells Backpack Check (Проверка рюкзака на 7 ячеек) ---")

TEMP_GRID_SIZE = 7 # 7 cells for the additional task / 7 ячеек для доп. задания
found_7 = False

# Same loop, but checking for 7 cells / Тот же цикл, но проверяем 7 ячеек
for r in range(len(item_keys) + 1):
    for combo in itertools.combinations(item_keys, r):
        # Asthma check / Проверка астмы
        if REQUIRED_ITEM not in combo:
            continue
            
        total_size = sum(items[i]['size'] for i in combo)
        if total_size > TEMP_GRID_SIZE:
            continue
            
        taken_points = sum(items[i]['points'] for i in combo)
        left_points = total_all_points - taken_points
        current_score = START_POINTS + taken_points - left_points
        
        # We just need one solution to prove it exists / Нам нужно хотя бы одно решение
        if current_score > 0:
            print(f"Solution found! (Решение найдено!)")
            print(f"Items: {combo}")
            print(f"Score: {current_score}")
            found_7 = True
            break # Stop after finding one / Останавливаемся после первого найденного
    if found_7:
        break

if not found_7:
    print("No positive solution exists for 7 cells. (Нет решения с плюсом для 7 ячеек.)")
    
    # --- Additional Task 2: Print all positive combinations / Доп. задание 2: Вывести все комбинации с плюсом ---
print("\n--- All Positive Combinations (Все комбинации с плюсом) ---")

# Sort combinations by score from highest to lowest / Сортируем комбинации по очкам от большего к меньшему
positive_combos.sort(key=lambda x: x[1], reverse=True)

# Print each combination / Печатаем каждую комбинацию
for idx, (combo, score) in enumerate(positive_combos, 1):
    # Convert tuple to string for better printing / Преобразуем кортеж в строку для красивого вывода
    combo_str = ", ".join(combo)
    print(f"{idx}. Items: [{combo_str}] | Score: {score}")