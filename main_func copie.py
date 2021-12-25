# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from math import sqrt


class Function:

    def __init__(self, f: str = None):
        """
        :param f: formule de la fonction
        """
        self.function = f

    def sup_parentheses(self):
        """
        supprime les parenthèses de la formule d'une fonction en la décomposant en une matrice
        pour chaque calcule prioritaire une nouvelle liste est créée
        :return: formule de la fonction sans les parenthèses
        """
        val = ""
        tab = [[]]
        l_index = [0]
        index = 0

        for el in self.function:

            if el == '(':

                if val != '':
                    tab[l_index[-1]].append(val)
                    val = ''

                tab[l_index[-1]].append('#')
                index += 1
                l_index.append(index)
                tab.append([])

            elif el == ')':

                if val != '':
                    tab[l_index[-1]].append(val[:-1])
                    val = ''

                l_index.pop()

            else:
                val += el + ' '

        if val != '':
            tab[0].append(val[:-1])

        return tab

    def resolve(self, x, func=None, index=0):
        """
        resoud la fonction de maniere recursive, par ordre de priorite des parathese
        :param x: valeur avec laquelle executer la fonction
        :param func: fonction a resoudre sous forme d'une liste
        :param index: index de la liste correspondant a la partie de la fonction en cours de resolution
        :return: result: resultat du calcul
                 index: index de la liste correspondant a la partie de la fonction a resoudre lors du prochain appel de
                 la fonction
        """
        func = self.sup_parentheses() if func is None else func
        expression = ''

        if '#' not in func[index]:
            result = self.regroup(f[index], x)
            return result, index

        else:

            while '#' in func[index]:
                ret = self.resolve(x, func, index + 1)
                expression += ret[0]
                index = ret[1]
                result = self.regroup(expression, x)
                func[index].remove("#")

            return result, index

    @staticmethod
    def regroup(expression, x):
        last = None
        num = ''
        ret = []
        power_of = ''

        for i in range(len(expression)):  # parcourt tous les elements de la liste

            print(f"exp : {expression[i]}")  # debug
            match expression[i]:  # expression[i] : valeur d'entree pour les condition

                case ' ':
                    print('space')  # debug
                    pass

                case 'x':

                    print('x')  # debug
                    if last is None:
                        ret.append(str(x))

                    elif last.isdigit():
                        ret.append(num)
                        ret.append('*')
                        ret.append(str(x))

                    elif last == 'x':
                        ret.append('*')
                        ret.append(str(x))

                    elif last == '&':
                        ret.append(str(sqrt(float(x))))

                    elif last == '^':
                        ret.append(str(float(num) ** float(power_of)))
                        power_of = ''

                    else:
                        ret.append(str(x))

                    last = 'x'
                    num = ''

                case '+':

                    print('+')  # debug
                    if last is None:
                        pass

                    elif last == '&':

                        if num == '' or not num[-1].isdigit():
                            pass

                        else:
                            ret.append(str(sqrt(float(num))))
                            ret.append('+')
                            last = '+'
                            num = ''

                    elif last == '^':

                        if power_of == '' or not power_of[-1].isdigit():
                            pass

                        else:
                            ret.append(str(float(num) ** float(power_of)))
                            ret.append('+')
                            last = '+'
                            num = ''
                            power_of = ''

                    elif last.isdigit():
                        ret.append(num)
                        ret.append('+')
                        last = '+'
                        num = ''

                    elif last == 'x':
                        ret.append('+')
                        last = ''

                    else:
                        pass

                case '-':

                    print('-')  # debug
                    if last is None:
                        num += '-'

                    elif last == '&':

                        if num == '' or not num[-1].isdigit():
                            num += '-'

                        else:
                            ret.append(str(sqrt(float(num))))
                            ret.append('-')
                            last = '-'
                            num = ''

                    elif last == '^':

                        if num == '' or not num[-1].isdigit():
                            num += '-'

                        else:
                            ret.append(str(float(num) ** float(power_of)))
                            ret.append('-')
                            last = '-'
                            num = ''
                            power_of = ''

                    elif last.isdigit():
                        ret.append(num)
                        ret.append('-')
                        last = '-'
                        num = ''

                    elif last == 'x':
                        ret.append('-')
                        last = '-'

                    else:
                        num += '-'

                case '&':

                    print('&')  # debug
                    if last is None:
                        last = '&'

                    elif last.isdigit():
                        ret.append(num)
                        ret.append('*')
                        last = '&'
                        num = ''

                    elif last == 'x':
                        ret.append('*')
                        last = '&'

                    elif last == '^':

                        if power_of == '' or not power_of[-1].isdigit():
                            return "Error 238"  # a completer flemme

                        else:
                            ret.append(str(float(num) ** float(power_of)))
                            ret.append('*')
                            last = '&'
                            num = ''
                            power_of = ''

                    elif last == '&':

                        if num == '' or not num[-1].isdigit():
                            return "Error 249"  # a completer flemme

                        else:
                            ret.append(str(sqrt(float(num))))
                            ret.append('*')
                            last = '&'
                            num = ''

                    else:
                        ret.append(last)
                        last = '&'

                case '^':

                    print('^')  # debug
                    if last is None:
                        return "Error None power of_"  # Error

                    elif last.isdigit():
                        last = '^'

                    elif last == 'x':
                        num = ret.pop()
                        last = '^'

                    elif last == '^':

                        if power_of == '' or not power_of[-1].isdigit():
                            return "Error 274"  # Error

                        else:
                            return "sah flemme"  # a completer flemme pour le moment

                    elif last == '&':

                        if num == '' or not num[-1].isdigit():
                            return "Error 282"  # Error

                        else:
                            num = str(sqrt(float(num)))
                            last = '^'

                    else:
                        return "Error 288"  # Error

                case '*':

                    print('*')  # debug
                    if last is None:
                        return "Error None *"

                    if last.isdigit():
                        ret.append(num)
                        ret.append('*')
                        last = '*'
                        num = ''

                    elif last == 'x':
                        ret.append('*')
                        last = '*'

                    elif last == '^':

                        if power_of == '' or not power_of[-1].isdigit():
                            return "Error 308"  # Error

                        else:
                            ret.append(str(float(num) ** float(power_of)))
                            ret.append('*')
                            last = '*'
                            num = ''
                            power_of = ''

                    elif last == '&':

                        if num == '' or not num[-1].isdigit():
                            return "Error 320"  # Error

                        else:
                            ret.append(str(sqrt(float(num))))
                            ret.append('*')
                            last = '*'
                            num = ''

                    else:
                        return "Error 329"  # Error

                case '/':

                    print('/')  # debug
                    if last is None:
                        return "Error divise None"  # Error

                    elif last.isdigit():
                        ret.append(num)
                        ret.append('/')
                        last = '/'
                        num = ''

                    elif last == 'x':
                        ret.append('/')
                        last = '/'

                    elif last == '^':

                        if power_of == '' or not power_of[-1].isdigit():
                            return "Error 349"  # Error

                        else:
                            ret.append(str(float(num) ** float(power_of)))
                            ret.append('/')
                            last = '/'
                            num = ''
                            power_of = ''

                    elif last == '&':

                        if num == '' or not num[-1].isdigit():
                            return "Error 361"  # Error

                        else:
                            ret.append(str(sqrt(float(num))))
                            ret.append('/')
                            last = '/'
                            num = ''
                    else:
                        return "Error 369"  # Error

                case _:

                    print('digit')  # debug
                    if last is None:
                        num += expression[i]
                        last = expression[i]

                    elif last == '^':
                        power_of += expression[i]

                    elif last == '&':
                        num += expression[i]

                    elif last == 'x':
                        ret.append('*')
                        num += expression[i]
                        last = expression[i]

                    else:
                        num += expression[i]
                        last = expression[i]

        print(f'last : {last}')
        print(f"num {num}")
        if last is None:
            pass

        elif last.isdigit():
            ret.append(num)

        elif last == 'x':
            pass

        elif last == '&':
            ret.append(str(sqrt(float(num))))

        elif last == '^':
            ret.append(str(float(num) ** float(power_of)))

        else:
            return "Error 396"  # Error

        return ret


# Programme principal

f = Function("&(3x)")
func = f.sup_parentheses()
print(func)
print(f.regroup("2&3", 3))
