class Category:

    def __init__(self, cat):
        self.cat = cat
        self.ledger = []
        self.amount = 0

    def deposit(self, *args):
        self.amount = args[0]
        if len(args) == 2:
            description = args[1]
        else:
            description = ''
        dict = {'amount': self.amount, 'description': description}
        self.ledger.append(dict)

    def withdraw(self, *args):
        amounts = args[0]
        if len(args) == 2:
            description = args[1]
        else:
            description = ''
        if self.check_funds(amounts) == True:
            amounts = 0 - amounts
            dict = {'amount': amounts, 'description': description}
            self.ledger.append(dict)
            return True
        else:
            return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, to_cat):
        text_to = f'Transfer to {to_cat.cat}'
        for_return = self.withdraw(amount, text_to)

        text_from = f'Transfer from {self.cat}'
        to_cat.deposit(amount, text_from)
        return for_return

    def check_funds(self, amount):
        if amount <= self.amount:
            self.amount = self.amount - amount
            return True
        else:
            return False

    def __str__(self):

        len_cat = len(self.cat)
        if len_cat % 2 == 0:
            half = (30 - len_cat) / 2
            star = '*' * int(half)
            text = f'{star}{self.cat}{star}'
        else:
            half = (30 - len_cat) // 2
            star = '*' * half
            text = f'{star}{self.cat}{star}*'

        data = []
        for i in self.ledger:
            data.append(list(i.values()))

        for i in data:
            text1 = f'{i[1]:<23}'[:23]
            text2 = "%.2f" % i[0]
            text2 = f'{text2:>7}'
            line = f'\n{text1}{text2}'
            text += line

        last_line = f'\nTotal: {self.get_balance()}'
        text += last_line

        return str(text)

def create_spend_chart(list):
    values = []
    for i in list:
        sum_arg = 0
        for j in i.ledger:
            if j['amount'] < 0:
                sum_arg += abs(j['amount'])
        values.append(sum_arg)

    sum = 0
    for i in values:
        sum += i

    percents_list = []
    for i in values:
        percent = int(i / sum * 100) // 10
        percents_list.append(percent)

    for_print = []
    line1 = 'Percentage spent by category'
    line_v_1 = ['100| ', ' 90| ', ' 80| ', ' 70| ', ' 60| ', ' 50| ', ' 40| '
                , ' 30| ', ' 20| ', ' 10| ', '  0| ', '    -']
    for_print.append(line_v_1)

    for i in percents_list:
        temp = []
        for j in reversed(range(11)):
            if j == 0:
                temp.append('o  ')
                temp.append('---')
            else:
                if j > i:
                    temp.append('   ')
                elif j <= i:
                    temp.append('o  ')
        for_print.append(temp)

    final = ''
    for i in range(12):
        for j in range(len(percents_list) + 1):
            final += for_print[j][i]
        final += '\n'

    cat = []
    for i in list:
        cat.append(i.cat)

    longest = 0
    for i in cat:
        if len(i) > longest:
            longest = len(i)

    for i in range(len(cat)):
        if len(cat[i]) < longest:
            add = longest - len(cat[i])
            add_space = ' ' * add
            cat[i] = cat[i] + add_space

    final2 = ''
    print(longest)
    for i in range(longest):
        for j in range(len(cat)):
            if j == 0:
                final2 += '     '
                final2 += cat[j][i]
                final2 += '  '
            else:
                final2 += cat[j][i]
                final2 += '  '
        if i == longest - 1:
            pass
        else:
            final2 += '\n'

    result = line1 + '\n' + final + final2
    return result



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)


print(create_spend_chart([food, clothing, auto]))




food = Category('Food')
food.deposit(900, "deposit")
entertainment = Category('Entertainment')
entertainment.deposit(900, "deposit")
business = Category('Business')
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))