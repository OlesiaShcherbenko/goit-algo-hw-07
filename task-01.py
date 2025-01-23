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

# Алгоритм для знаходження найбільшого значення в дереві
def find_max_in_bst(root):
    if root is None:
        return None  # Якщо дерево порожнє
    current = root
    while current.right is not None:  # Рухаємося вправо, поки є правий вузол
        current = current.right
    return current.value

# Тестування алгоритму
if __name__ == "__main__":
    # Створення дерева
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]  # Приклад значень
    for val in values:
        root = insert(root, val)

    # Пошук найбільшого значення
    max_value = find_max_in_bst(root)
    print(f"Найбільше значення в дереві: {max_value}")