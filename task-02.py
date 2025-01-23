# Реалізація вузла дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для вставки вузла в двійкове дерево пошуку
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Алгоритм для знаходження найменшого значення в дереві
def find_min_in_bst(root):
    if root is None:
        return None  # Якщо дерево порожнє
    current = root
    while current.left is not None:  # Рухаємося вліво, поки є лівий вузол
        current = current.left
    return current.value

# Тестування алгоритму
if __name__ == "__main__":
    # Створення дерева
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]  # Приклад значень
    for val in values:
        root = insert(root, val)

    # Пошук найменшого значення
    min_value = find_min_in_bst(root)
    print(f"Найменше значення в дереві: {min_value}")