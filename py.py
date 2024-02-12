class Calculator:
    def __init__(self):
        self.results_list = []  
        self.results_dict = {} 
    def add(self, num1, num2):
        result = num1 + num2
        self.results_list.append((num1, num2, result))
        self.results_dict[(num1, num2)] = result
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.results_list.append((num1, num2, result))
        self.results_dict[(num1, num2)] = result
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.results_list.append((num1, num2, result))
        self.results_dict[(num1, num2)] = result
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            return "Nelze dělit nulou!"
        result = num1 / num2
        self.results_list.append((num1, num2, result))
        self.results_dict[(num1, num2)] = result
        return result

    def clear_results(self):
        self.results_list = []
        self.results_dict = {}


calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(10, 7))
print(calc.multiply(2, 4))
print(calc.divide(10, 5))
print(calc.results_list) 
print(calc.results_dict)  
calc.clear_results() 
