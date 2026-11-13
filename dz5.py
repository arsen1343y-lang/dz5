class Task:
    def __init__(self, title: str, description: str, deadline: str):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Виконано" if self.is_completed else "Не виконано"
        return f"[{status}] {self.title} (Дедлайн: {self.deadline}) — {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, title: str):
        self.tasks = [task for task in self.tasks if task.title != title]

    def complete_task(self, title: str):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")


manager = TaskManager()
manager.add_task(Task("Звіт", "Підготувати квартальний звіт", "15.11.2026"))
manager.add_task(Task("Код-рев'ю", "Перевірити гілку feature/auth", "16.11.2026"))
manager.complete_task("Звіт")
manager.show_tasks()



class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} — {self.price:.2f} грн (В наявності: {self.stock} шт.)"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            print("Кількість має бути більшою за нуль.")
            return
        if product.stock < quantity:
            print(f"Недостатньо товару '{product.name}' на складі.")
            return

        self.items[product] = self.items.get(product, 0) + quantity
        product.stock -= quantity

    def remove_product(self, product: Product, quantity: int = None):
        if product not in self.items:
            return
        if quantity is None or quantity >= self.items[product]:
            product.stock += self.items.pop(product)
        else:
            self.items[product] -= quantity
            product.stock += quantity

    def get_total_price(self) -> float:
        return sum(product.price * qty for product, qty in self.items.items())

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
            return
        for product, qty in self.items.items():
            print(f"{product.name}: {qty} шт. x {product.price:.2f} грн = {product.price * qty:.2f} грн")
        print(f"Загальна вартість: {self.get_total_price():.2f} грн")


laptop = Product("Ноутбук", 32000.0, 5)
mouse = Product("Мишка", 850.0, 10)

cart = Cart()
cart.add_product(laptop, 1)
cart.add_product(mouse, 2)
cart.show_cart()








class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float = 0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Рахунок {self.account_number} ({self.owner}): {self.balance:.2f} грн"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: BankAccount):
        self.accounts[account.account_number] = account

    def deposit(self, account_number: str, amount: float):
        account = self.accounts.get(account_number)
        if not account or amount <= 0:
            print("Помилка поповнення.")
            return
        account.balance += amount

    def withdraw(self, account_number: str, amount: float) -> bool:
        account = self.accounts.get(account_number)
        if not account or amount <= 0 or account.balance < amount:
            print("Недостатньо коштів або невірний рахунок.")
            return False
        account.balance -= amount
        return True

    def transfer(self, from_acc_num: str, to_acc_num: str, amount: float):
        if to_acc_num not in self.accounts:
            print("Рахунок отримувача не знайдено.")
            return
        if self.withdraw(from_acc_num, amount):
            self.deposit(to_acc_num, amount)
            print(f"Переказ {amount:.2f} грн виконано успішно.")


bank = Bank()
acc1 = BankAccount("Олена Коваль", "UA1001", 5000.0)
acc2 = BankAccount("Ігор Мельник", "UA1002", 1200.0)

bank.add_account(acc1)
bank.add_account(acc2)
bank.transfer("UA1001", "UA1002", 1500.0)
print(acc1)
print(acc2)




class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} — {self.position} ({self.salary:.2f} грн)"


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, name: str):
        self.employees = [emp for emp in self.employees if emp.name != name]

    def calculate_total_salary(self) -> float:
        return sum(emp.salary for emp in self.employees)

    def show_department_info(self):
        print(f"Відділ: {self.name}")
        for emp in self.employees:
            print(f" - {emp}")
        print(f"Загальний фонд зарплати: {self.calculate_total_salary():.2f} грн")


it_dept = Department("Розробка ПЗ")
it_dept.add_employee(Employee("Андрій Савченко", "Python Developer", 65000.0))
it_dept.add_employee(Employee("Марія Бойко", "QA Engineer", 42000.0))
it_dept.show_department_info()
