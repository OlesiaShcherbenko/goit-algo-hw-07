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

# Алгоритм для обчислення суми всіх значень у дереві
def sum_of_tree(root):
    if root is None:
        return 0  # Порожнє дерево або вузол повертає 0
    return root.value + sum_of_tree(root.left) + sum_of_tree(root.right)

# Тестування алгоритму
if __name__ == "__main__":
    # Створення дерева
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]  # Приклад значень
    for val in values:
        root = insert(root, val)

    # Обчислення суми всіх значень
    total_sum = sum_of_tree(root)
    print(f"Сума всіх значень у дереві: {total_sum}")