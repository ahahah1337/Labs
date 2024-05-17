{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Лабораторная работа 4. Функции."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Функция в программировании представляет собой обособленный участок кода, который можно вызывать, обратившись к нему по имени, которым он был назван. При вызове происходит выполнение команд тела функции.\n",
    "\n",
    "Функции можно сравнить с небольшими программками, которые сами по себе, т. е. автономно, не исполняются, а встраиваются в обычную программу. Нередко их так и называют – подпрограммы. Других ключевых отличий функций от программ нет. Функции также при необходимости могут получать и возвращать данные. Только обычно они их получают не с ввода (клавиатуры, файла и др.), а из вызывающей программы. Сюда же они возвращают результат своей работы."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Необязательные параметры и сопоставление по ключам\n",
    "\n",
    "Чтобы сделать некоторые параметры функции необязательными, следует в определении функции присвоить этому параметру начальное значение. Сопоставление по ключам очень удобно использовать, если функция имеет несколько необязательных\n",
    "параметров. В этом случае не нужно указывать все значения, а достаточно присвоить значение нужному параметру."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "def summa (а=2, Ь=3, с=4) : # Все параметры являются необязательными\n",
    "    return а + Ь + с"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "25\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "print (summa () )        # Использование значений по умолчанию\n",
    "print (summa (2, 3, 20)) # Позиционное присваивание\n",
    "print (summa (с=20) )    # Сопоставление по ключам"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Переменное число параметров в функции\n",
    "\n",
    "Если перед параметром в определении функции указать символ *, то функции можно будет передать произвольное количество параметров. Все переданные параметры сохраняются в кортеже. Для примера напишем функцию суммирования произвольного количества чисел"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "def summa(*t):\n",
    "    res = 0\n",
    "    for i in t: # Перебираем кортеж с переданными параметрами\n",
    "        res += i\n",
    "    return res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "210\n"
     ]
    }
   ],
   "source": [
    "print(summa(10, 20)) \n",
    "print(summa(10, 20, 30, 40, 50, 60)) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Глобальные и локальные переменные\n",
    "\n",
    "Глобальные переменные — это переменные, объявленные в программе вне функции. В Python глобальные переменные видны в любой части модуля, включая функции.\n",
    "\n",
    "Локальные переменные— это переменные, объявляемые внутри функций. Если имя локальной переменной совпадает с именем глобальной переменной, то все операции внутри функции осуществляются с локальной переменной, а значение глобальной переменной не изменяется. Локальные переменные видны только внутри тела функции."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def func():\n",
    "    global globl\n",
    "    locall = 77 # Локальная переменная\n",
    "    globl = 25  # Локальная переменная\n",
    "    print (\"Значение locall внутри функции = \", locall)\n",
    "    print (\"Значение globl внутри функции = \", globl)\n",
    "#    globl = 25 # Глобальная переменная"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Значение locall внутри функции =  77\n",
      "Значение globl внутри функции =  25\n",
      "Значение globl вне функции =  25\n",
      "Переменная locall не видна вне функции\n"
     ]
    }
   ],
   "source": [
    "globl = 10\n",
    "func() # Вызываем функцию\n",
    "print (\"Значение globl вне функции = \", globl)\n",
    "try:\n",
    "    print (\"Значение locall вне функции = \", locall) # Вызовет исключение NameError\n",
    "except NameError: # Обрабатываем исключение\n",
    "    print (\"Переменная locall не видна вне функции\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Рекурсия\n",
    "\n",
    "Рекурсия — это возможность функции вызывать саму себя. Рекурсию удобно использовать для перебора объекта, имеющего заранее неизвестную структуру, или для выполнения неопределенного количества операций. \n",
    "\n",
    "Рекурсивные функции являются мощным механизмом в программировании. К сожалению, они не всегда эффективны. Также часто использование рекурсии приводит к ошибкам. Наиболее распространенная из таких ошибок – бесконечная рекурсия, когда цепочка вызовов функций никогда не завершается и продолжается, пока не кончится свободная память в компьютере. \n",
    "\n",
    "В качестве примера рассмотрим вычисление факториала."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Пример 1. Факториал.\n",
    "\n",
    "\n",
    "Факториалом числа называют произведение всех натуральных чисел до него включительно:\n",
    "\n",
    "$$ n! = 1 \\cdot 2 \\cdot ... \\cdot n. $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial_Rec(n):\n",
    "    if n == 0 or n == 1: return 1\n",
    "    else: return n * factorial_Rec(n - 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Эта программа эквивалентна следующей"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial(n):\n",
    "    factorial = 1\n",
    "    while n > 1:\n",
    "        factorial *= n\n",
    "        n -= 1\n",
    "    return factorial"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "factorial_Rec(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Протестируем корректность работы программ:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "assert factorial_Rec(0) == 1\n",
    "assert factorial_Rec(1) == 1\n",
    "assert factorial_Rec(4) == 24\n",
    "\n",
    "assert factorial(0) == 1\n",
    "assert factorial(1) == 1\n",
    "assert factorial(4) == 24"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Утверждение (ключевое слово) assert существует во многих языках программирования. Это помогает обнаруживать проблемы в начале программы, где причина ясна, а не позже, как побочный эффект какой-либо другой операции. Используя это слово вы говорите программе проверить это условие и немедленно вызвать ошибку, если условие ложно."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "n=50\n",
    "a = np.zeros(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "174 µs ± 174 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)\n",
      "100 µs ± 133 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%timeit for i in range (n): a[i] = factorial_Rec(i)\n",
    "%timeit for i in range (n): a[i] = factorial(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Функции-генераторы\n",
    "\n",
    "Функцией-генератором называется функция, которая при последовательных вызовах возвращает очередной элемент какой-либо последовательности. Приостановить выполнение функции и превратить функцию в генератор позволяет ключевое слово yield. Генератор перестает возвращать значения, когда итераций больше нет, при достижении пустой команды return или конца функции. Локальные переменные в функции-генераторе сохраняются между вызовами (в отличие от обычных функций).\n",
    "\n",
    "Одну такую функцию мы уже встречали, это функция ranged(). Рассмотрим пример с этой функцией."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Пример 2."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for x in range(5):\n",
    "    print (x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 5)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "На её основе легко написать функцию, которая возводит элементы последовательности в заданною степень:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun_xiny(x, у):\n",
    "    for i in range(1, x + 1):\n",
    "        yield i ** у"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 4 9 16 25 36 49 64 81 100 \n",
      "1 8 27 64 125 216 343 512 729 1000 "
     ]
    }
   ],
   "source": [
    "for n in fun_xiny(10, 2):\n",
    "    print(n, end=' ')\n",
    "print()\n",
    "\n",
    "for n in fun_xiny(10, 3):\n",
    "    print(n, end=' ') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Однако, функцию-генератор легко можно написать и без ranged():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def four():\n",
    "    x = 0 \n",
    "    while x < 4:\n",
    "        print(\"В генераторе, x =\", x)\n",
    "        yield x \n",
    "        x += 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "В генераторе, x = 0\n",
      "А вне ненератора, x = 0\n",
      "В генераторе, x = 1\n",
      "А вне ненератора, x = 1\n",
      "В генераторе, x = 2\n",
      "А вне ненератора, x = 2\n",
      "В генераторе, x = 3\n",
      "А вне ненератора, x = 3\n"
     ]
    }
   ],
   "source": [
    "for x in four():\n",
    "    print('А вне ненератора, x =', x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение 1. Факториал-генератор\n",
    "\n",
    "Напишите функцию-генератор возвращающую значение факториала."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial(n):\n",
    "    result = 1\n",
    "    for i in range(2, n + 1):\n",
    "        result *= i\n",
    "    return result\n",
    "\n",
    "n = int(input('Факториал какого числа вы хотите узнать?: '))\n",
    "fac = factorial(n)\n",
    "print(f'Факториал {n} равен: {fac}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Перехват ошибки.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Как мы уже знаем, программа содержащая синтактические ошибки не может работать. Хотя, это не совсем верно, любая ошибка приводит к появлению во время работы программы (интерпритатора) \"исключения\", непозволяющего продолжить программу. Если это исключение можно преодолеть (обработать), программа сможет продолжить работать. \n",
    "\n",
    "При ошибке в тексте программы в терминологии языка Python возникает исключение, принадлежащее классу SyntaxError. Согласно документации Python синтаксические ошибки все-таки принято относить к ошибкам, а все остальные – к исключениям. В некоторых языках программирования не используется слово \"исключение\", а ошибки делят на синтаксические и семантические. Нарушение семантики обычно означает, что, хотя выражения написаны верно с точки зрения синтаксиса языка, программа не работает так, как от нее ожидалось. \n",
    "\n",
    "Ишибку любого рода можно перехватить (обработать) следующим образом:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "try:\n",
    "    Блок_инструкций_1\n",
    "except:\n",
    "    Блок_инструкций_2 (выполняется в случае ошибки в Блок_инструкций_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Однако, такой универсальный перехват не всегда дает возможность правильно обработать её. Возможно, для эффективного исправления ошибки необходимо глубже понять её природу. Для этого есть ряд ключевых вариантов:\n",
    "\n",
    "1. ArithmeticError - арифметическая ошибка.\n",
    "- FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.\n",
    "- OverflowError - возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.\n",
    "- ZeroDivisionError - деление на ноль.\n",
    "2. IndexError - индекс не входит в диапазон элементов.\n",
    "3. MemoryError - недостаточно памяти.\n",
    "4. SyntaxError - синтаксическая ошибка.\n",
    "5. TypeError - операция применена к объекту несоответствующего типа.\n",
    "6. ValueError - функция получает аргумент правильного типа, но некорректного значения.\n",
    "\n",
    "У оператора обработки исключений, кроме except, могут быть еще ветки finally и else (не обязательно обе сразу). Тело finally выполняется всегда, независимо от того, выполнялись ли блоки except в ответ на возникшие исключения или нет. Тело else сработает, если исключений в try не было, т. е. не было переходов на блоки except."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Пример 3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def divide():\n",
    "    try:\n",
    "        a = float(input(\"Введите делимое: \"))\n",
    "        b = float(input(\"Введите делитель: \"))\n",
    "        c = a / b\n",
    "        print(\"Частное: %.2f\" % c)\n",
    "    except ValueError:\n",
    "        print(\"Нельзя вводить строки\")\n",
    "    except ZeroDivisionError:\n",
    "        print(\"Нельзя делить на ноль\")\n",
    "    finally: # выполняется в любом случае\n",
    "        print(\"Конец программы\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите делимое: 1\n",
      "Введите делитель: 2\n",
      "Частное: 0.50\n",
      "Конец программы\n"
     ]
    }
   ],
   "source": [
    "divide()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите делимое: 2\n",
      "Введите делитель: a\n",
      "Нельзя вводить строки\n",
      "Конец программы\n"
     ]
    }
   ],
   "source": [
    "divide()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Пример 4. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Функция для проверки чисел на чётность или не четность. \n",
    "(Разберите структуру)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Parity ():\n",
    "    \n",
    "    sf=1\n",
    "    while bool(sf):\n",
    "        s=input('Введите число ')\n",
    "        try:\n",
    "            # перхватывает любую ошибку !\n",
    "            sf=int(s)\n",
    "            f=sf%2\n",
    "            if not bool(f):\n",
    "                print('четное')\n",
    "            else:\n",
    "                print('не четное')\n",
    "        except:\n",
    "            print('Йода говорит: только целые числа нужны нам!')\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Вызов функции:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите число 4\n",
      "четное\n",
      "Введите число 5\n",
      "не четное\n",
      "Введите число f\n",
      "Йода говорит: только целые числа нужны нам!\n",
      "Введите число 6\n",
      "четное\n",
      "Введите число h\n",
      "Йода говорит: только целые числа нужны нам!\n",
      "Введите число 0\n",
      "четное\n"
     ]
    }
   ],
   "source": [
    "Parity ()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение 2. Точный перехват."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Уточните тип возможной ошибки и доработайте соответствующее уведомление пользователю."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Parity():\n",
    "    flag = True\n",
    "    while flag:\n",
    "        number = input('Введите число ')\n",
    "    try:\n",
    "        number = int(number)\n",
    "        remainder = number % 2\n",
    "    if remainder == 0:\n",
    "        print('четное')\n",
    "    else:\n",
    "        print('не четное')\n",
    "    except ValueError:\n",
    "        print('Йода говорит: только целые числа нужны нам!')\n",
    "\n",
    "Parity()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Пример 5. \n",
    "\n",
    "Пример функции: функция для перевода числа из одной системы счисления в другую в виде цикла. \n",
    "(Разберите структуру)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_base (num, to_base=10, from_base=10):\n",
    "    \n",
    "         alphabet = \"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "    \n",
    "         x = int (num, from_base)             # приведение к десятичной базе (ЗАГЛУШКА)\n",
    "    \n",
    "         # приведение к новой базе\n",
    "         it = 0\n",
    "         digit = []\n",
    "    \n",
    "         while x>0:\n",
    "                    digit.insert(0, alphabet[x % to_base])\n",
    "                    x = x // to_base\n",
    "                    it+=1\n",
    "         for i in range(it):\n",
    "                    print (digit[i], end = '')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "235"
     ]
    }
   ],
   "source": [
    "convert_base ('111', to_base=8, from_base=12)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Пример функции: функция для перевода числа из одной системы счисления в другую в рекурсивной форме. \n",
    "(Разберите структуру)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_base_R(num, to_base=10, from_base=10):\n",
    "    \n",
    "    alphabet = \"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "    \n",
    "    if isinstance(num, str):     # праверка типа, аналогично type(num) == str\n",
    "        n = int(num, from_base)  # приведение к десятичной базе (ЗАГЛУШКА)\n",
    "    else:\n",
    "        n = int(num)\n",
    "    # приведение к новой базе\n",
    "    if n < to_base:\n",
    "        return alphabet[n]\n",
    "    else:\n",
    "        return convert_base_R(n // to_base, to_base) + alphabet[n % to_base]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'235'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "convert_base_R('111', to_base=8, from_base=12)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Домашнее задание (базовое):"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 1\n",
    "\n",
    "Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е. соединение, строк. В остальных случаях введенные числа суммируются."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "value1 = input('Введите первое значение: ')\n",
    "value2 = input('Введите второе значение: ')\n",
    "\n",
    "try:\n",
    "    value1 = int(value1)\n",
    "    value2 = int(value2)\n",
    "    print(f'Результат сложения чисел {value1} и {value2}: {value1 + value2}')\n",
    "except ValueError:\n",
    "    print(f'Результат конкатенации строк: {value1 + value2}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 2. Тортик.\n",
    "\n",
    "За столом сидят n гостей (вводится с клавиатуры), перед которыми стоит пирог. Пирог и его части можно делить только пополам. Определите, сколько раз нужно делить пирог на ещё более мелкие части, чтобы: \n",
    "- каждому из гостей достался хотя бы 1 кусок;\n",
    "- как минимум половине гостей досталось по 2 куска;\n",
    "- каждому гостю досталось по 1 куску и при этом ещё хотя бы 10 кусков осталось в запасе."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_cuts(n, piece_increment):\n",
    "    piece = 1\n",
    "    cut = 0\n",
    "    while piece < n:\n",
    "        cut += 1\n",
    "        piece += piece_increment\n",
    "    return cut\n",
    "\n",
    "n = int(input('Введите количество гостей: '))\n",
    "print(f'Число разрезов: {calculate_cuts(n, 1)}')\n",
    "\n",
    "n = int(input('Введите количество гостей: '))\n",
    "print(f'Число разрезов: {n-1}')\n",
    "\n",
    "n = int(input('Введите количество гостей: '))\n",
    "print(f'Число разрезов: {calculate_cuts(n*2, 1)}')\n",
    "\n",
    "n = int(input('Введите количество гостей: '))\n",
    "print(f'Число разрезов: {n*2-1}')\n",
    "\n",
    "n = int(input('Введите количество гостей: '))\n",
    "print(f'Число разрезов: {calculate_cuts(n+10, 11)}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 3. Явный Фибоначи.\n",
    "\n",
    "Для n-го члена в последовательности Фибоначчи существует явная формула:\n",
    "\n",
    "$$x_n = \\frac{1}{2} \\left( \\left( \\frac{1 + \\sqrt{5}}{2} \\right)^{n+1} - \\left( \\frac{1 - \\sqrt{5}}{2} \\right)^{n+1} \\right) $$\n",
    "\n",
    "Поскольку операции с вещественными числами происходят с конечной точностью, то с ростом n, результат вычисления по этой формуле будет все больше отличаться от настоящего числа Фибоначчи. Найдите n, начиная с которого, отличие от истинного значения превысит 0.001."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fibonacci_sequence():\n",
    "    a, b = 0, 1\n",
    "    yield a\n",
    "    yield b\n",
    "    while True:\n",
    "        a, b = b, a + b\n",
    "        yield b\n",
    "\n",
    "           n = 0\n",
    "           generator = fibonacci_sequence()\n",
    "    while True:\n",
    "        n += 1\n",
    "        fibonacci_number = next(generator)\n",
    "        x = 1 / (5 ** 0.5) * (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n)\n",
    "        if abs(fibonacci_number - x) > 0.001:\n",
    "            print(f\"Difference occurred at {n}-th number\")\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 4. Кубики.\n",
    "\n",
    "В детском садике n детей играют в следующую игру. Перед ними гора из m кубиков, первый ребёнок вынимает из кучи 1 кубик, каждый последующий ребёнок в два раза больше предыдущего и так по кругу. Если число кубиков, которые нужно вынуть, превышает 25, из него вычитается 25 и отсчёт идёт от уменьшенного числа, например, вместо 32 кубиков будет вынуто 7, затем 14 и т. д. Проигравшим считается тот, кто не смог вытащить нужное число кубиков (в куче осталось недостаточно). Определите проигравшего."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_cube_loser(n, m):\n",
    "    count = 1\n",
    "    num = 1\n",
    "    while count <= m:\n",
    "        m -= count\n",
    "        count *= 2\n",
    "        if count > 25:\n",
    "            count -= 25\n",
    "            num += 1\n",
    "        if num > n:\n",
    "            num = 1\n",
    "    return num\n",
    "\n",
    "n, m = int(input(\"Введите количество детей: \")), int(input(\"Введите количество кубиков: \"))\n",
    "res = get_cube_loser(n, m)\n",
    "print(f'Проигравшим будет {res} ребёнок')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 5. Ханойские башни\n",
    "\n",
    "Головоломка о ханойской башне была изобретена французским математиком Эдуардом Лукасом в 1883 году. Его вдохновила легенда, рассказывающая о замке Хинду, где эту задачу поставили перед юными жрецами. В начале времён им дали три стержня и стопку из шестидесяти четырёх золотых дисков, каждый из которых немного меньше предыдущего. Требовалось переставить все диски с одного стержня на другой, соблюдая два строгих условия. Во-первых, за раз можно было перемещать только один диск. Во-вторых, нельзя класть бОльший диск поверх меньшего. Жрецы работали (и работают по сей день) очень споро, день и ночь, переставляя каждую секунду по одному диску. Легенда гласит, что когда они закончат свою работу, замок обратится в пыль, и мир исчезнет.\n",
    "\n",
    "Хотя легенда и интересна, вам не стоит беспокоиться о скором конце света. Число ходов, требующихся для правильной перестановки башни из 64 дисков, равняется $2^{64}−1=18,446,744,073,709,551,615$. Со скоростью один ход в секунду это займёт 584,942,417,355 лет! Большая цифра для такой несложной на первый взгляд головоломки.\n",
    "\n",
    "Как нам решить эту задачу рекурсивно? С чего бы вы начали? Что является здесь базовым случаем? Давайте подумаем над этим от конца к началу. Предположим, изначально на первом колышке у вас находится башня из пяти дисков. Если вы уже знаете, как передвинуть четыре из них на второй колышек, то можете с лёгкостью переложить нижний диск на стержень №3, а затем переложить туда же башню со стержня №2. Но что, если вы понятия не имеете, как переместить башню из четырёх верхних? Предположим, что известно, как передвинуть башню из трёх верхних дисков на третий колышек. Тогда с перемещением четвёртого трудностей не возникнет: переложите его на второй стержень, а затем положите сверху те, что нанизаны на третий. Но если вы не знаете как переместить три? Что ж, можно переложить башню из двух дисков на стержень №2, а третий - на стержень №3, а потом сверху положить башню из двух. Но если до сих пор не понятно, как это сделать? Уверен, что вы согласитесь: переместить один диск на третий колышек легче лёгкого - тривиальнее ничего не найдётся. Звучит как базовый случай, а?\n",
    "\n",
    "Вот общая схема того, как переместить башню с исходного стержня на заданный с использованием промежуточного:\n",
    "- Передвинуть башню из (количество дисков - 1) на промежуточный колышек, используя при этом заданный.\n",
    "- Положить оставшийся диск на заданный стержень.\n",
    "- Переместить башню из оставшихся на промежуточном стержне дисков на конечный, используя при этом первоначальный колышек.\n",
    "\n",
    "Напишите функцию move (n, x, y), которая печатает последовательность перекладываний дисков для перемещения пирамидки высоты n со стержня номер x на стержень номер y. \n",
    "\n",
    "Реализуйте алгоритм в двух вариантах: на основе цикла и на основе рекурсии."
   ]
  },
  {
   "metadata": {},
   "cell_type": "code",
   "outputs": [
    {
     "data": {
      "image/gif": "R0lGODlhMwHOAPMJAP///wAAAKr/rFb/V/8AAKqq/1ZW//+qqv9WVgAAAAAAAAAAAAAAAAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh/wtYTVAgRGF0YVhNUDw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYxIDY0LjE0MDk0OSwgMjAxMC8xMi8wNy0xMDo1NzowMSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNS4xIFdpbmRvd3MiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6Q0Q0NzQwQTQ0NTUxMTFFMzk5MDc5QkJDMUEwMDVCMDIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6Q0Q0NzQwQTU0NTUxMTFFMzk5MDc5QkJDMUEwMDVCMDIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpDRDQ3NDBBMjQ1NTExMUUzOTkwNzlCQkMxQTAwNUIwMiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpDRDQ3NDBBMzQ1NTExMUUzOTkwNzlCQkMxQTAwNUIwMiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PgH//v38+/r5+Pf29fTz8vHw7+7t7Ovq6ejn5uXk4+Lh4N/e3dzb2tnY19bV1NPS0dDPzs3My8rJyMfGxcTDwsHAv769vLu6ubi3trW0s7KxsK+urayrqqmop6alpKOioaCfnp2cm5qZmJeWlZSTkpGQj46NjIuKiYiHhoWEg4KBgH9+fXx7enl4d3Z1dHNycXBvbm1sa2ppaGdmZWRjYmFgX15dXFtaWVhXVlVUU1JRUE9OTUxLSklIR0ZFRENCQUA/Pj08Ozo5ODc2NTQzMjEwLy4tLCsqKSgnJiUkIyIhIB8eHRwbGhkYFxYVFBMSERAPDg0MCwoJCAcGBQQDAgEAACH5BAVkAAkALAAAAAAzAc4AAAT/EMhJq7046827/2AojmRpnmiqrmzrvnAsz3Rt33iu73zv/8CgcEgsGo/IpHLJbDqf0Kh0Sq1ar9isdsvter/gsHhMLpvP6LR6zW673/C4fE6v2+/4vH7P7/v/gIGCg4SFhoeIiWUEjI2NipA/jpOUlJGXMpWam4+YniecnRWhjJ+mH5sjqaesFpopr62tli60sp62MLm3iZM3vryIuzTDwX/AO8jGx46Szct+z0HS0HnU06LVdtdC3Npw3t3Z32/hQ+bkZ+jn4+lo60Tw7l7y8e3zYfVF+vhW907/+m3hty+gQCwGmyQ8SIWgEYcMlUB8uDAiwFJaKlpcMvFIx43Y/wh00QiSIsaBJEuKO8nlo8ocKaPEfNlj5hObNGHiVLgzZ42ePEX69AiUicuhL4oGRVpQ6BilTFUcDeo0qg+oS61exWqUq9YQXrtW/YojLEeWZG1MhbI2rQezYt3+QmsGrlxXdBflvduiLVu7fAEAPjs2MIvBEvcaRoE4SWO3j4kWXsw4ssnJlEtYlpx5xWaTnaUqrjs6NKrSZD4j9TuFdWDVoE1rRq0Xs+wOsMtyqEjbcG61pRe6fvkbuG3BwYt/U04soMHhNJk33+tcujbrM7z9g54Te/Z297h3751xHHjv14+DuYZW/Hj167OJcv+ejbRO9Ovbx18qv/79/RVz2/8F6OkUy4C7kZdPJQi+peCC/q32IITwNUhBhepgaOGGHHbo4YcghijiiCSWaOKJKKao4oostujiizDGKOOMIAZgYwBy3IhjHDqqMcCPQAYp5JADnKFjj20ceaMZRDbp5I9kKImkGlIuOcaTWBI5RpU2ssHljmEIKcCYZJZppplCivGll1yKEeSZcMZJZpBgfNllGnaC6QWQcvYJJ5B12kmloF+86eehY9LpRZ6Drlnoj4hGKgCgixKKBqOPDiApopR2gemllnbB56Z+dsrFp0aGysWopMpp6haomhHrFoa2eqainqpaxqy0QmrrrVB+weuWuvbq66+JvgprscQ6Cob/mLamGaizqVKbaZbYqsmsttZei62TzbaJ57aifqtllOROK64XBrTr7rvwxitvvMKmW2+3WMyr77785opvuFV2we/ABL97qr2V/ksFvAU07PDDEEcs8cPwLqtwGMNO8e7EHHfMscFZZIwxwk646/HJKDfsrhYiqxtwFhunLPPEIF/R8r3rXmHyzDxHvDIWNyecsxU792x0AT/bTPLBF0NR9NE8J21F0P4OXcXTUMssdRVUM231wlhn7XHNUy9t8ddgGyC21u2ybLbbTTsd9to+b8312yHjrQTDdNdt991xC/3yFgUX3u/Zg1eLNtGGN0523oFXnTgXjhuO8+S76n0E/wKcd+7556CHLvroCEC++MiRK0H66qy37rnSqSMupRWu12776ICf7vLsVIB+wO/ABy/88MQXXzzoVHQtu5JVeG7889BHP/zrUygPt+5JOC/99twTT30U1puOeRPad2+++Z1Xr3nZsQ/R+fnwd//9E+EDvb4P78evf/Tpg39/8v/jQf72R0DvcU4K9YMd9jbHuQI6UHj9g0IC2bdAIwzwgQWcnxMmmLvxMaF8GNxfBCUYQASWcAcgDOH5NLjBE5KwfURIoQq3x8IWwtB+NxSC72YoPeSpL4cU9KATbkfEInaQd6ACovuKyETSKVCIqKvgELjUxCp2ToonyJMWt8hFJceCoItgDKMWbyDGMppxSjM4oxrFaIM1upGLZHyjHL34gTnaEYlpvKMe71SDPe6xjX68IyADOcc4ElKOgzykGxOpSDUaspGO7CMk18jISbKxkpYEIyYzCUdJcvKSnvykJkMpyk7SoJRhfCQqx0jKVbpwA6405SljycpZ0vKVGrglB0OgS1xmoJd09AAwsZjFYeJRBsY8ZgySybxNDtOZwIRmL2lEzWpa85rYzKY2t8nNbnrzm+AMpzjHSc5ymvOc6EynOteZoggAACH5BAVkAAUALCIAGADuAJcAAAP/CLrc/jDKSat1JOvN8/1gKI5kaZ5Vp65sq6FwLM806t54/tZ87/8WHesiXAGPyORI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\n",
      "text/plain": [
       "<IPython.core.display.Image object>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 2,
   "source": [
    "# Так можно добавлять картинки\n",
    "\n",
    "from IPython.display import Image # вызов из библиотеки определённой функции\n",
    "Image(\"Ханойская башня.gif\")              # вызов функции и передача ей в качестве аргумента пути к файлу \n",
    "\n",
    "# (в данном случае фаил находится в той же папке)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {
    "jupyter": {
     "is_executing": true
    }
   },
   "source": [
    "#На основе рекурсии\n",
    "n = 3\n",
    "a = []\n",
    "\n",
    "def move(k, n, x, y, z):\n",
    "    if n % 2 == 0 and k % 2 == 0 or n % 2 != 0 and k % 2 != 0:\n",
    "        x, y, z = 1, 2, 3\n",
    "    else:\n",
    "        x, y, z = 1, 3, 2\n",
    "\n",
    "    if k < n:\n",
    "        for i in range(2**k - 1, 2**n - 1, 2**(k + 1)):\n",
    "            a[i].append(k + 1)\n",
    "            a[i].append(x)\n",
    "            a[i].append(y)\n",
    "            x, y, z = y, z, x\n",
    "        move(k + 1, n, x, y, z)\n",
    "\n",
    "for i in range(2**n - 1):\n",
    "    a.append([])\n",
    "\n",
    "move(0, n, 1, 2, 3)\n",
    "\n",
    "for i in range(len(a)):\n",
    "    print('Диск', a[i][0], ':', a[i][1], '=====>', a[i][2])\n",
    "    \n",
    "#На основе цикла\n",
    "def move(n, x, y):\n",
    "    stack = [(n, x, y, 1)]\n",
    "    while stack:\n",
    "        n, x, y, step = stack.pop()\n",
    "        if step == 1:\n",
    "            if x + y == 3:\n",
    "                z = 3\n",
    "            elif x + y == 5:\n",
    "                z = 1\n",
    "            else:\n",
    "                z = 2\n",
    "            if n == 1:\n",
    "                print(f'Переместить {n} диск на {y} пирамидку')\n",
    "            else:\n",
    "                stack.extend([(n - 1, x, z, 1), (n, x, y, 2), (n - 1, z, y, 1)])\n",
    "        elif step == 2:\n",
    "            print(f'Переместить {n} диск на {y} пирамидку')\n",
    "\n",
    "# n, x, y = int(input(\"Введите количество дисков: \")), int(input(\"С какой пирамидки передвинуть(укажите номер пирамидки: 1, 2, 3): \")), int(input(\"На какую пирамидку передвинуть(укажите номер пирамидки: 1, 2, 3): \"))\n",
    "n, x, y = 3, 1, 2\n",
    "print('Порядок действий: ')\n",
    "move(n, x, y)"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "metadata": {},
   "cell_type": "markdown",
   "source": "# Домашнее задание (дополнительное):"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание \"Вне системы\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Написать программу совершающую элементарные алгебраические операции ($A+B$, $A-B$, $A*B$, $A/B$) с числами в произвольной системе исчисления. (Подсказка: обратите внимание на устройство программы convert_base и см. рисунок с выполенеием операций + и *.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<IPython.core.display.Image object>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Так можно добавлять картинки\n",
    "\n",
    "from IPython.display import Image # вызов из библиотеки определённой функции\n",
    "Image(\"операции.png\")              # вызов функции и передача ей в качестве аргумента пути к файлу \n",
    "\n",
    "# (в данном случае фаил находится в той же папке)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание \"Быстрый обратный квадратный корень\" \n",
    "\n",
    "Быстрый обратный квадратный корень — это быстрый приближённый алгоритм вычисления обратного квадратного корня \n",
    "\n",
    "$$ y=\\frac{1}{\\sqrt{x}} $$ \n",
    "\n",
    "для положительных 32-битных чисел с плавающей запятой. Алгоритм использует целочисленные операции «вычесть» и «битовый сдвиг», а также дробные «вычесть» и «умножить» — без медленных операций «разделить» и «квадратный корень». Несмотря на «хакерство» на битовом уровне, ошибка такого метода вычисления составляет всего несколько процентов, чего обычно не хватает для настоящих численных расчётов, однако вполне достаточно для трёхмерной графики. \n",
    "\n",
    "Алгоритм был, вероятно, разработан в Silicon Graphics в 1990-х, а реализация появилась в 1999 году в исходном коде компьютерной игры Quake III Arena, но данный метод не появлялся на общедоступных форумах до 2000-х годов. \n",
    "\n",
    "Алгоритм генерирует достаточно точные результаты, используя уникальное первое приближение метода Ньютона. Основным преимуществом алгоритма является отказ от дорогих вычислительных операций с плавающей запятой в пользу целочисленных операций. Обратные квадратные корни используются для расчета углов падения и отражения для освещения и затенения в компьютерной графике. Однако, версия для double бессмысленна, так как точность вычислений не увеличится.\n",
    "\n",
    "См. подробности на https://ru.wikipedia.org/wiki/Быстрый_обратный_квадратный_корень#cite_note-7\n",
    "\n",
    "Напишите программу, реализующую этот алгоритм. Для этого напишите функцию для быстрого вычисления обратного корня Q_rsqrt(), оцените ошибку такого метода вычисления. \n",
    "\n",
    "Сделайте одну итерацию с помощью метода Ньютона, котрая в данном случае имеет вид:\n",
    "\n",
    "$$ y_{n+1}=y_{n}(1.5-0.5xy_{n}^{2}) $$.\n",
    "\n",
    "Утверждается, что после этого погрешность обычно не превышает 1%. Проверьте так ли это."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание \"Умножение Карацубы\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "(n)-числа — те числа, которые требуют не более n элементов элементарных типов (цифр) в своём представлении. Будем считать, что с такими числами умеет работать вычислитель. Однако, если необходимо перемножить числа в два раза длиннее - (2n)-числа, как это сделать?\n",
    "\n",
    "Можно воспользоваться наивным алгоритмом, основанном на правилах умножения и переносе разряжов. Однако, такой алгоритм слишком накладен... К счастью, имеется более быстрый алгоритм. Он изобретён в 1960-х годах аспирантом А. Н. Колмогорова Анатолием Карацубой и с тех пор является неизменным участником любых библиотек работы с большими числами. Нас он интересует постольку, поскольку реализует принцип разделяй и властвуй. Пусть нам требуется перемножить два (2n)-числа. Введём константу T, на единицу большую максимального числа, представляемого (n)-числом. Тогда любое (2n)-число X можно представить в виде суммы $Tx_u + x_l$. \n",
    "\n",
    "$$N_1 = Tx_1 + y_1$$\n",
    "$$N_2 = Tx_2 + y_2$$\n",
    "\n",
    "При умножении в столбик\n",
    "\n",
    "$$N_1 × N_2 = T^2x_1x_2 + T(x_1y_2 + x_2y_1) + y_1y_2.$$\n",
    "\n",
    "Это — четыре операции умножения и три операции сложения. Число T определяет, сколько нулей нужно добавить к концу числа в соответствующей системе счисления.\n",
    "\n",
    "Алгоритм Карацубы находит произведение по другой формуле:\n",
    "\n",
    "$$N_1 × N_2 = T^2x_1x_2 + T((x_1 + y_1)(x_2 + y_2) − x_1x_2 − y_1y_2) + y_1y_2.$$\n",
    "\n",
    "Напишите программу, реализующую этот алгоритм. Представьте входные и выходные данные в виде формата list хранящего значения x и y. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
