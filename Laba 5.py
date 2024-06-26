{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Лабораторная работа 5. Структурированные типы данных"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Строки\n",
    "\n",
    "Строки представляют собой последовательности символов. Длина строки ограничена лишь объемом оперативной памяти компьютера. \n",
    "\n",
    "Поддерживают обращение к элементу по индексу, получение среза, конкатенацию (оператор +), повторение (оператор *), а также проверку на вхождение (операторы in и not in).\n",
    "\n",
    "Относятся к неизменяемым типам данных. Практически все операция в качестве значения возвращают новую строку. Поэтому для рациональной работы со строками желательно использовать специальные строковые методы."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Например, доступны следующие манипуляции:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, World! <class 'str'> 1741085358384\n"
     ]
    }
   ],
   "source": [
    "s = \"Hello, World!\"\n",
    "print(s, type(s), id(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-2-0330678be040>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0ms\u001B[0m\u001B[1;33m[\u001B[0m\u001B[1;33m-\u001B[0m\u001B[1;36m1\u001B[0m\u001B[1;33m]\u001B[0m \u001B[1;33m=\u001B[0m \u001B[1;34m\"?\"\u001B[0m\u001B[1;33m\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m\u001B[0;32m      2\u001B[0m \u001B[0mprint\u001B[0m\u001B[1;33m(\u001B[0m\u001B[0ms\u001B[0m\u001B[1;33m,\u001B[0m \u001B[0mtype\u001B[0m\u001B[1;33m(\u001B[0m\u001B[0ms\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m,\u001B[0m \u001B[0mid\u001B[0m\u001B[1;33m(\u001B[0m\u001B[0ms\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n",
      "\u001B[1;31mTypeError\u001B[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "s[-1] = \"?\"\n",
    "print(s, type(s), id(s))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Для обозначения однострочечных символов (строк) можно использовать \" \" или ' ':"
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
      "Hello, World?..?... <class 'str'> 1741085275280\n"
     ]
    }
   ],
   "source": [
    "s = s[:-1] + \"?\" + '...'\n",
    "print(s, type(s), id(s))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Их комбинация задаёт ковычки в строке:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Кто сказал \"Hello, World!\"? <class 'str'> 1741086040112\n"
     ]
    }
   ],
   "source": [
    "s = \"Кто сказал \" + '\"Hello, World!\"' + '?'\n",
    "print(s, type(s), id(s))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Для создания многострочечных строк используйте тройные ковычки:"
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
      "Строка 1\n",
      "Строка 2\n",
      "Строка 3\n",
      " <class 'str'> 2425413148208\n"
     ]
    }
   ],
   "source": [
    "s = \"\"\"Строка 1\n",
    "Строка 2\n",
    "Строка 3\n",
    "\"\"\"\n",
    "print(s, type(s), id(s))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Если строка не присваивается переменной, то она считается строкой документирования. Такая строка сохраняется в атрибуте_doc_того объекта, в котором расположена. \n",
    "\n",
    "Например:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "def test():\n",
    "    \"\"\"Это описание функции\"\"\"\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Это описание функции\n"
     ]
    }
   ],
   "source": [
    "print (test.__doc__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Строковые методы.\n",
    "\n",
    "Для строк есть множество методов. Посмотреть их можно по команде"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__add__',\n",
       " '__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getitem__',\n",
       " '__getnewargs__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__mod__',\n",
       " '__mul__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__rmod__',\n",
       " '__rmul__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'capitalize',\n",
       " 'casefold',\n",
       " 'center',\n",
       " 'count',\n",
       " 'encode',\n",
       " 'endswith',\n",
       " 'expandtabs',\n",
       " 'find',\n",
       " 'format',\n",
       " 'format_map',\n",
       " 'index',\n",
       " 'isalnum',\n",
       " 'isalpha',\n",
       " 'isascii',\n",
       " 'isdecimal',\n",
       " 'isdigit',\n",
       " 'isidentifier',\n",
       " 'islower',\n",
       " 'isnumeric',\n",
       " 'isprintable',\n",
       " 'isspace',\n",
       " 'istitle',\n",
       " 'isupper',\n",
       " 'join',\n",
       " 'ljust',\n",
       " 'lower',\n",
       " 'lstrip',\n",
       " 'maketrans',\n",
       " 'partition',\n",
       " 'replace',\n",
       " 'rfind',\n",
       " 'rindex',\n",
       " 'rjust',\n",
       " 'rpartition',\n",
       " 'rsplit',\n",
       " 'rstrip',\n",
       " 'split',\n",
       " 'splitlines',\n",
       " 'startswith',\n",
       " 'strip',\n",
       " 'swapcase',\n",
       " 'title',\n",
       " 'translate',\n",
       " 'upper',\n",
       " 'zfill']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(str)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Получить информацию по каждому можно следующим образом"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method_descriptor:\n",
      "\n",
      "split(self, /, sep=None, maxsplit=-1)\n",
      "    Return a list of the words in the string, using sep as the delimiter string.\n",
      "    \n",
      "    sep\n",
      "      The delimiter according which to split the string.\n",
      "      None (the default value) means split according to any whitespace,\n",
      "      and discard empty strings from the result.\n",
      "    maxsplit\n",
      "      Maximum number of splits to do.\n",
      "      -1 (the default value) means no limit.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(str.split)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method_descriptor:\n",
      "\n",
      "join(self, iterable, /)\n",
      "    Concatenate any number of strings.\n",
      "    \n",
      "    The string whose method is called is inserted in between each given string.\n",
      "    The result is returned as a new string.\n",
      "    \n",
      "    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(str.join)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Рассмотрим наиболее интересные из них:\n",
    "    \n",
    "- метод split() позволяет разбить строку по указанному разделителю (по умолчанию - пробелам), в результате получается список слов;\n",
    "- метод join() выполняет обратное действие, формирует из списка строку с определённым объединителем;\n",
    "- метод format() выполняет запонение строки в зарезервированные {} места."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Например:"
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
       "['Хорошо', 'бы', 'разделить', 'эту', 'строку', 'на', 'части']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"Хорошо бы разделить эту строку на части\".split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = \"Но не каждую строку, которую надо разделить, нужно делить по пробелам!!!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Но не каждую строку',\n",
       " 'которую надо разделить',\n",
       " 'нужно делить по пробелам!!!']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.split(', ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Но не каждую строку, которую надо разделить, нужно делить по пробелам',\n",
       " '',\n",
       " '',\n",
       " '']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.split('!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Но не каждую строку, которую надо разделить, нужно делить по пробелам', '!!']"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.split('!', 1)  #  ограничем максимальное чило делений"
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
      "['Но не каждую строку', 'которую надо разделить', 'нужно делить по пробелам!!!']\n"
     ]
    }
   ],
   "source": [
    "s2 = s.split(', ')\n",
    "print(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ",  <class 'str'> 2425412618352\n"
     ]
    }
   ],
   "source": [
    "s1 = ', '\n",
    "print(s1, type(s1), id(s1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Но не каждую строку, которую надо разделить, нужно делить по пробелам!!! <class 'str'> 2425413268400\n"
     ]
    }
   ],
   "source": [
    "s1 = s1.join(s2)\n",
    "print(s1, type(s1), id(s1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Строковый метод format() позволяет создать строку форматной вставкой в неё данных:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'length - 3, width - 6, height - 2.3'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "size = \"length - {}, width - {}, height - {}\"\n",
    "size.format(3, 6, 2.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'length - 2.3, width - 3, height - 6'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "size = \"length - {2}, width - {0}, height - {1}\"\n",
    "size.format(3, 6, 2.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'length - 2.300, width - 3.333, height - 6.790'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "size = \"length - {length:5.3f}, width - {width:5.3f}, height - {height:5.3f}\"\n",
    "size.format(width=3.3333333, height=6.7896, length=2.3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Списки\n",
    "\n",
    "Список в Python - это упорядоченный набор объектов, в который могут одновременно входить объекты разных типов (числа, строки и другие структуры). Эллементы списка доступны по индексу начинающегося с 0. Список является изменяемым типом данных - любой его эллемнт можно изменить.\n",
    "\n",
    "Список задаётся перечислением его элементов в квадратных скобках через запятую или с помощью функции list(), например"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2.0, '3', [4]]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "List = [1, 2.0, '3', [4]]\n",
    "List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2.0, 'three', [4]]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "List[2] = 'three'\n",
    "List"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Списки поддерживают следующие базовые операции:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l=[0,1,2,3,4,5,6,7]\n",
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- удаление эллемента"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 4, 5, 6, 7]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del l[3]\n",
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- добавить эллемента в заданную позицию"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 0, 4, 5, 6, 7]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.insert(3,0)\n",
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- добавить эллемента в конец"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 0, 4, 5, 6, 7, 8]"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.append(8)\n",
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- добавить несколько эллементов в конец"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.extend([9,10,11])\n",
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "del l[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 9, 10, 11]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[6, 7, 4]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[6, 7] + [4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Генераторы списков\n",
    "\n",
    "Можно также воспользоваться генераторами списков:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = [i for i in range(10)]\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Генераторы списков могут иметь сложную структуру — например, состоять из нескольких вложенных циклов for и (или) содержать оператор ветвления if после цикла. Для примера получим четные элементы списка и умножим их на 10:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 20, 40, 60, 80]\n"
     ]
    }
   ],
   "source": [
    "x2 = [ i*10 for i in x if i%2 == 0 ]\n",
    "print(x2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Этот код эквивалентен коду:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 20, 40, 60, 80]\n"
     ]
    }
   ],
   "source": [
    "x2 = []\n",
    "for i in x:\n",
    "    if i % 2 == 0: \n",
    "        x2.append(i*10) \n",
    "print(x2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Копирование списков\n",
    "\n",
    "Операция копирования для листов, имеет особенности"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2425413357064 2425413357064\n"
     ]
    }
   ],
   "source": [
    "y = x # это не копирование!!!\n",
    "print(id(x), id(y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Правильное копирование:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 2425413349128\n",
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 2425413247688\n",
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 2425413354888\n"
     ]
    }
   ],
   "source": [
    "y1 = list(x)\n",
    "y2 = x.copy()\n",
    "y3 = x[:]\n",
    "\n",
    "print(y1, id(y1))\n",
    "print(y2, id(y2))\n",
    "print(y3, id(y3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Объединение листов:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 8, 9] <class 'list'> 2425413318088\n"
     ]
    }
   ],
   "source": [
    "x = x[:2] + x[-2:]\n",
    "print(x, type(x), id(x))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Кортеж\n",
    "\n",
    "Кортеж в Python - это упорядоченный набор объектов, в который могут одновременно входить объекты разных типов (числа, строки и другие структуры).\n",
    "\n",
    "Его эллементы доступны по индексу начинающегося с 0. Кортеж является не изменяемым типом данных - его эллемнты нельзя менять.\n",
    "\n",
    "Кортеж задаётся перечислением его элементов в круглых скобках через запятую или с помощью функции tuple(), например"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2.0 3 [4, 5]\n"
     ]
    }
   ],
   "source": [
    "Tuple = (1, 2.0, '3', [4, 5])\n",
    "print(Tuple[0],Tuple[1],Tuple[2],Tuple[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-87-4daf37eb5949>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mTuple\u001B[0m\u001B[1;33m[\u001B[0m\u001B[1;36m2\u001B[0m\u001B[1;33m]\u001B[0m \u001B[1;33m=\u001B[0m \u001B[1;34m'three'\u001B[0m\u001B[1;33m\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m\u001B[0;32m      2\u001B[0m \u001B[0mprint\u001B[0m\u001B[1;33m(\u001B[0m\u001B[0mTuple\u001B[0m\u001B[1;33m[\u001B[0m\u001B[1;36m0\u001B[0m\u001B[1;33m]\u001B[0m\u001B[1;33m,\u001B[0m\u001B[0mTuple\u001B[0m\u001B[1;33m[\u001B[0m\u001B[1;36m1\u001B[0m\u001B[1;33m]\u001B[0m\u001B[1;33m,\u001B[0m\u001B[0mTuple\u001B[0m\u001B[1;33m[\u001B[0m\u001B[1;36m2\u001B[0m\u001B[1;33m]\u001B[0m\u001B[1;33m,\u001B[0m\u001B[0mTuple\u001B[0m\u001B[1;33m[\u001B[0m\u001B[1;36m3\u001B[0m\u001B[1;33m]\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n",
      "\u001B[1;31mTypeError\u001B[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "Tuple[2] = 'three'\n",
    "print(Tuple[0],Tuple[1],Tuple[2],Tuple[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 5]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Tuple[3]"
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
       "4"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Tuple[3][0]"
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
       "-4"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Tuple[3][0]=-4\n",
    "Tuple[3][0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Множества\n",
    "\n",
    "Множества в Python - это упорядоченный набор объектов, в который могут одновременно входить объекты разных типов (числа, строки и другие структуры). В отличии от списков и картежей, множество не итерируется по индуксу."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2.0, '3', 4}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Set = set([2.0, 1, 2, 1, '3', 4])\n",
    "Set"
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
       "{-1, 1, 2.0, '3', 4}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Set.add(1)\n",
    "Set"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Почему пропала одна 1?\n",
    "\n",
    "Вероятно, наиболее важной операцией с множеством является операция праверки принадлежности, и для неё нужно знать только уникальные эллементы множества. По этой же причине отсутствует возможность обращаться к эллементам по индексу."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "принадлежит множеству\n"
     ]
    }
   ],
   "source": [
    "x = 1\n",
    "\n",
    "if x in Set:\n",
    "    print('принадлежит множеству')\n",
    "else:\n",
    "    print('не принадлежит множеству')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__and__',\n",
       " '__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__iand__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__ior__',\n",
       " '__isub__',\n",
       " '__iter__',\n",
       " '__ixor__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__or__',\n",
       " '__rand__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__ror__',\n",
       " '__rsub__',\n",
       " '__rxor__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__sub__',\n",
       " '__subclasshook__',\n",
       " '__xor__',\n",
       " 'add',\n",
       " 'clear',\n",
       " 'copy',\n",
       " 'difference',\n",
       " 'difference_update',\n",
       " 'discard',\n",
       " 'intersection',\n",
       " 'intersection_update',\n",
       " 'isdisjoint',\n",
       " 'issubset',\n",
       " 'issuperset',\n",
       " 'pop',\n",
       " 'remove',\n",
       " 'symmetric_difference',\n",
       " 'symmetric_difference_update',\n",
       " 'union',\n",
       " 'update']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method_descriptor:\n",
      "\n",
      "add(...)\n",
      "    Add an element to a set.\n",
      "    \n",
      "    This has no effect if the element is already present.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(set.add)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Словари\n",
    "\n",
    "Словарь в Python - структура содержит пары \"ключ\" - \"значение\" (их порядок несущественен). Это одина из наиболее полезных и гибких структур имеющихся в Python. Словари реализованы как хэш-таблицы, так что поиск даже в больших словарях очень эффективен.\n",
    "\n",
    "Например, с помощью словоря можно эмулировать работу оператора множественного выбора аналогичного switch:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def switch_dict(x):\n",
    "    return {\n",
    "        \"a\": 1,\n",
    "        \"b\": 2,\n",
    "        \"c\": 3\n",
    "    }.get(x, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "switch_dict('a')"
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
       "-1"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "switch_dict('6')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Массивы (numpy)\n",
    "\n",
    "Менее стандартной, но очень полезной является структура массив, объединяющая эллементы одинакового типа."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [3, 4]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = np.array([[1,2],[3,4]])\n",
    "A"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Очень часто возникает задача создания массива определенного размера, причем чем заполнен массив абсолютно неважно. В этом случае можно воспользоваться циклами или генераторами списков (кортежей), но NumPy для таких случаев предлагает более быстрые и менее затратные функции-заполнители.\n",
    "\n",
    "Полезными оказываются следующие функции (по умолчанию, тип создаваемого массива - float64.):\n",
    "\n",
    "- zeros() - заполняет массив нулями, "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0.],\n",
       "       [0., 0., 0.],\n",
       "       [0., 0., 0.]])"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.zeros((3,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0., 0., 0.])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.zeros(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- eye() - создаёт единичную матрицу, "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0., 0.],\n",
       "       [0., 1., 0.],\n",
       "       [0., 0., 1.]])"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.eye(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- empty - заполняет матрицу случайными числами, которые зависят от состояния памяти. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0., 0.],\n",
       "       [0., 1., 0.],\n",
       "       [0., 0., 1.]])"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.empty([3, 3])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Для создания последовательностей чисел NumPy предоставляет функции arange() и linspace(), которая возвращает одномерные массивы:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- np.arange(From, To, Step) - построить массив чисел от From (включая) до To (не включая) с шагом Step:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(10)   #  От 0 до указанного числа с шагом 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(10, 20)    #  От 10 до 20 с шагом 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([10, 20, 30, 40, 50, 60, 70, 80, 90])"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(10, 100, 10)    #  Диапазон с заданным шагом"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(0, 1, 0.1)    #  Аргументы могут иметь тип float"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- np.linspace(From, To, Num) - построить массив чисел от From (включая) до To (включая) с колличеством эллементов Num:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.  , 0.25, 0.5 , 0.75, 1.  ])"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linspace(0, 1, 5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение 1.\n",
    "\n",
    "С клавиатуры (неограниченное количество раз) вводится некоторая последовательность значений, необходимо сохранить только уникальные символы (цифры и буквы). И после окончания ввода вывести сохранённые символы."
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
    "# Упражнение 2. Эффективный размер массива (стек).\n",
    "\n",
    "Стек, дека, очередь. Массив с дополнительными параметрами (размер выделенной памяти и объём занятой памяти). Позволяют за константное время добавлять и убирать элементы в начало и конец эффективного размера массива.\n",
    "\n",
    "Напишите функцию которая реализует работу стека: \n",
    "1. внутри определён массив numpy заданного размера и целочисленный параметр фиксирующий степень заполненности массива;\n",
    "2. функция принимает значение x и индиксатор действия (0 - чтение из стека, 1 - запись в стек); в случае чтения возвращает значение из конца массива или False, если стек пуст; при записи возвращает логическую переменную индикатор успешности операции;\n",
    "3. при операциях чтения и записи должна проверяться корректность этого действия связанная с размерами стека."
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
    "# Упражнение 3. Эффективный размер массива (множество).\n",
    "\n",
    "Как мы уже поняли, множество в Python это совокупность уникальных объектов не доступных по индексу. Адаптируйте предыдущую программу к работе в таком режиме.\n",
    "\n",
    "Т.е.: \n",
    "1. дописываться могут только значения не записанные ранее;\n",
    "2. функция принимает одно значение x (True - вывод всего множества, числовое значение - запись в множество); в случае если множество пусто возвращается False; при записи возвращает логическую переменную индикатор успешности операции;\n",
    "3. при операциях чтения и записи должна проверяться корректность этого действия связанная с размерами множества.\n",
    "\n",
    "P.S. Попробуйте реализовать пункт с выводом значений по возрастанию через работу с дополнительным массивом индексов (перестановок). Или начиная запись в множество с середины массива..."
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
    "# Функции для итерируемых объектов.\n",
    "\n",
    "Наиболее полезными для итерируем объектов являются функции:\n",
    "- map() - позволяет применить заданную функцию к каждому элементу последовательности, возвращает объект, поддерживающий итерации,\n",
    "- zip() - возвращает кортеж, содержащий элементы последовательностей расположенных на одинаковом смещении,\n",
    "- filter() - позволяет выполнить проверку элементов последовательности."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11, 12, 13, 14, 15]\n"
     ]
    }
   ],
   "source": [
    "def fun(elem):\n",
    "    return elem + 10 \n",
    "\n",
    "arr = [1, 2, 3, 4, 5]\n",
    "print(list(map(fun, arr)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 4, 7), (2, 5, 8), (3, 6, 9)]"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(zip([ 1, 2, 3], [4, 5, 6], [7, 8, 9]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[111, 222, 333, 444, 555]\n"
     ]
    }
   ],
   "source": [
    "arrl = [1, 2, 3, 4, 5]\n",
    "arr2 = [10, 20, 30, 40, 50]\n",
    "arrЗ = [100, 200, 300, 400, 500]\n",
    "\n",
    "arr = [х + у + z for (х, у, z) in zip(arrl, arr2, arrЗ)]\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "или что тоже самое"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[111, 222, 333, 444, 555]\n"
     ]
    }
   ],
   "source": [
    "def fun(a,b,c):\n",
    "    return a+b+c \n",
    "\n",
    "print(list(map(fun, arrl, arr2, arrЗ)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[222, 444]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def fun(elem):\n",
    "    return elem % 2 == 0\n",
    "\n",
    "list(filter(fun, arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Генераторы словарей"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'а': 1, 'Ь': 2, 'c': 3}"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "keys = [\"а\", \"Ь\", \"c\"]\n",
    "values = [1, 2, 3] \n",
    "dict_kv = {k: v for (k, v) in zip(keys, values)}\n",
    "dict_kv"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение 4.\n",
    "\n",
    "Создайте функцию принимающую двумерную таблицу, работающую со всеми возможными итерируемыми типами данных подходящими для её хранения (лист, словарь, картеж, массив и т.д.). Функция должна выполнять вывод строк этой таблици в случайном порядке. \n",
    "\n",
    "Насколько сложно было бы сделать аналогичный вывод для столбцов?"
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
    "# Домашнее задание (базовое):"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 1.\n",
    "\n",
    "С клавиатуры вводится строка, включающая строчные и прописные буквы. Требуется вывести ту же строку в изменённом регистре, тип регистра зависит от того, каких букв больше. При равном количестве букв в заглавном и проптсном регистре - выводится оригинальная строка. \n",
    "\n",
    "Например, вводится строка \"HeLLo World\", она должна быть преобразована в \"hello world\", потому что в исходной строке малых букв больше. \n",
    "\n",
    "В программе можно использовать строковые методы: upper() (преобразование к верхнему регистру) и lower() (преобразование к нижнему регистру), isupper() и islower() (проверяющие регистр строки или символа)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def transform_string(s):\n",
    "    Up, Low = 0, 0\n",
    "    for i in s:\n",
    "        if i.isupper():\n",
    "            Up += 1\n",
    "        else:\n",
    "            Low += 1\n",
    "\n",
    "    if Up > Low:\n",
    "        return s.upper()\n",
    "    elif Up < Low:\n",
    "        return s.lower()\n",
    "    else:\n",
    "        return s\n",
    "\n",
    "# s = input('Введите строку: ')\n",
    "s = \"Hello, World!\"\n",
    "transformed_string = transform_string(s)\n",
    "print(transformed_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 2\n",
    "\n",
    "Дано слово \"объектно-ориентированный\". Используя индексацию и срезы составьте из него как можно больше слов \"объект\", \"ориентир\", \"тир\", \"кот\", \"рента\" и тд. Выведите их на экран."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def transform_string(s):\n",
    "    results = []\n",
    "    indices = [\n",
    "        [0, 6],\n",
    "        [4, 6],\n",
    "        [9, 17],\n",
    "        [16, 16, 12, 13, 14, 19],\n",
    "        [4, 7, 5],\n",
    "        [1, 7, 5],\n",
    "        [6, 8, 14, 19],\n",
    "        [18, 15, -1],\n",
    "        [0, 4, 6, 7]\n",
    "    ]\n",
    "\n",
    "    for idx in indices:\n",
    "        if len(idx) == 2:\n",
    "            results.append(s[idx[0]:idx[1]])\n",
    "        elif len(idx) == 1:\n",
    "            results.append(s[idx[0]])\n",
    "        else:\n",
    "            result = \"\"\n",
    "            for i in idx:\n",
    "                result += s[i]\n",
    "            results.append(result)\n",
    "\n",
    "    return results\n",
    "\n",
    "s = \"объектно-ориентированный\"\n",
    "transformed_results = transform_string(s)\n",
    "\n",
    "for result in transformed_results:\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 3\n",
    "\n",
    "Строковый метод isdigit() проверяет, состоит ли строка только из цифр. Напишите программу, которая запрашивает с ввода целые числа и выводит их сумму. В случае некорректного ввода программа не должна завершаться с ошибкой, а должна продолжать работу, удаляя из введённой строки все символы кроме цифр. При отсутствии цифр запрс пользователю повторяется.\n",
    "\n",
    "Обработчик исключений try-except использовать нельзя."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_input(input_str):\n",
    "    new_num = ''\n",
    "    for i in input_str:\n",
    "        if i in '123457890':\n",
    "            new_num += i\n",
    "    if not new_num:\n",
    "        return None\n",
    "    return int(new_num)\n",
    "\n",
    "num1 = input('Введите первое число: ')\n",
    "num1 = check_input(num1)\n",
    "while num1 is None:\n",
    "    num1 = input('Введите число заново: ')\n",
    "    num1 = check_input(num1)\n",
    "\n",
    "num2 = input('Введите второе число: ')\n",
    "num2 = check_input(num2)\n",
    "while num2 is None:\n",
    "    num2 = input('Введите число заново: ')\n",
    "    num2 = check_input(num2)\n",
    "\n",
    "print(num1 + num2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 4\n",
    "\n",
    "Создайте словарь, где ключами являются числа, а значениями – строки. Примените к нему метод items(), полученный объект dict_items передайте в написанную вами функцию, которая создает и возвращает новый словарь, \"обратный\" исходному, т. е. ключами являются строки, а значениями – числа. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dictionary = {\n",
    "    1: 'объект',\n",
    "    2: 'кто',\n",
    "    3: 'ориентир',\n",
    "    4: 'рента',\n",
    "    5: 'кот',\n",
    "    6: 'бот',\n",
    "    7: 'нота',\n",
    "    8: 'вор',\n",
    "    9: 'окно',\n",
    "}\n",
    "\n",
    "def sort_dict_by_value(d):\n",
    "    return {v: k for k, v in sorted(d.items(), key=lambda item: item[1])}\n",
    "\n",
    "print(sort_dict_by_value(dictionary))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 5. (Снова в школу...)\n",
    "\n",
    "Опишите структуру данных (базу данных) на основе словаря и интерфейс работы с ней (функцию). \n",
    "\n",
    "Создайте словарь school, и наполните его данными, которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т.п.). И функцию для внесения изменений в словарь в рамках следующего функционала: \n",
    "а) в одном из классов изменилось количество учащихся; \n",
    "б) в школе появился новый класс; \n",
    "с) в школе был расформирован (удален) класс, в связи с чем ученики были равномерно распределены по другим; \n",
    "d) выгрузка данных: общее количество учащихся в школе, общее колличество классав, распределение учеников по классам.\n",
    "\n",
    "P.S. Дополнительно.\n",
    "\n",
    "Подумайте как лучше всего хранить такую базу данных в файле. Попробуйте реализовать свою идею."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Исходные данные\n",
    "school = {\n",
    "    '1а' : 30,\n",
    "    '1б' : 31,\n",
    "    '1в' : 29,\n",
    "    '1г' : 30,\n",
    "    '2а' : 29,\n",
    "    '2б' : 32,\n",
    "    '2в' : 33,\n",
    "    '2г' : 30,\n",
    "    '11а': 9,\n",
    "}\n",
    "\n",
    "# Функции для операций с классами\n",
    "def append_students(dictionary):\n",
    "    class_name = input('Введите класс, в котором изменилось количество учеников: ')\n",
    "    num_students = int(input('Сколько теперь учеников в классе? '))\n",
    "    dictionary[class_name] = num_students\n",
    "    return dictionary\n",
    "\n",
    "def append_class(dictionary):\n",
    "    class_name = input('Введите название нового класса: ')\n",
    "    num_students = int(input('Введите количество учащихся в этом классе: '))\n",
    "    dictionary[class_name] = num_students\n",
    "    return dictionary\n",
    "\n",
    "def delete_class(dictionary):\n",
    "    class_name = input('Введите класс, который был расформирован: ')\n",
    "    students_in_class = dictionary.pop(class_name)\n",
    "    num_classes = len(dictionary)\n",
    "    redistributed_students = students_in_class // num_classes\n",
    "    remaining_students = students_in_class % num_classes\n",
    "\n",
    "    for class_key in dictionary:\n",
    "        dictionary[class_key] += redistributed_students\n",
    "        if remaining_students > 0:\n",
    "            dictionary[class_key] += 1\n",
    "            remaining_students -= 1\n",
    "\n",
    "    return dictionary\n",
    "\n",
    "def statistic(dictionary):\n",
    "    total_classes = len(dictionary)\n",
    "    total_students = sum(dictionary.values())\n",
    "    return total_classes, total_students, dictionary\n",
    "\n",
    "# Операции с классами\n",
    "action = input('Выберите действие:\\nа) Изменить количество учащихся\\nб) Добавить новый класс\\nв) Расформировать класс\\nг) Получить статистику\\n')\n",
    "\n",
    "if action == 'а':\n",
    "    updated_school = append_students(school)\n",
    "elif action == 'б':\n",
    "    updated_school = append_class(school)\n",
    "elif action == 'в':\n",
    "    updated_school = delete_class(school)\n",
    "elif action == 'г':\n",
    "    total_info = statistic(school)\n",
    "    print(f'Всего классов в школе: {total_info[0]}\\nВсего учеников: {total_info[1]}\\nРаспределение по классам:')\n",
    "    for class_name, num_students in total_info[2].items():\n",
    "        print(f'{class_name}: {num_students}')\n",
    "else:\n",
    "    print('Выбрано некорректное действие.')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Домашнее задание (дополнительное):"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание. Реверс словаря.\n",
    "\n",
    "Создайте словарь, где ключами являются цифры, а значениями – строки. Передайте словарь в функцию, которая создает и возвращает новый словарь, \"обратный\" исходному, при этом ключами являются буквы составляющие строки, а значениями – числа составленные из цифр в порядке соответствующем.\n",
    "\n",
    "Например: \n",
    "\n",
    "Исходный словарь: {1: 'аcc', 2: 'сab', 3: 'ccb'}\n",
    "\n",
    "Выходной словарь: {'а': 12, 'b': 23, 'c': 11233}"
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
    "# Задание. Разрезание таблиц. \n",
    "\n",
    "Заполните квадратную таблицу порядка n по спирали по часовой стрелке начиная с левого верхнего угла. В напишите функцию принимающую данную таблицу в подходящем формате, найдите строку с наибольшим количеством нулей и столбец с максимальной суммой элементов. Разрежьте по этой строке и столбцу таблицу и верните из функции получившийся результат как отдельные таблицы, после чего выведете их на печать."
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
    "# Задание. Пары.\n",
    "\n",
    "На вход программы поступает последовательность из N целых положительных чисел, все числа в последовательности различны. Рассматриваются все пары различных элементов последовательности (элементы пары не обязаны стоять в последовательности рядом, порядок элементов в паре не важен). Необходимо определить количество пар, для которых произведение элементов делится на 26.\n",
    "Описание входных и выходных данных.\n",
    "\n",
    "В первой строке входных данных задаётся количество чисел N (1 ≤ N ≤ 1000). В каждой из последующих N строк записано одно целое положительное число, не превышающее 10 000.\n",
    "\n",
    "В качестве результата программа должна напечатать одно число: количество пар, в которых произведение элементов кратно 26.\n",
    "\n",
    "Пример входных данных: 4 2 6 13 39\n",
    "\n",
    "Пример выходных данных: 4\n",
    "\n",
    "Из четырёх заданных чисел можно составить 6 попарных произведений:\n",
    "\n",
    "2·6 = 12 \n",
    "\n",
    "2·13 = 26 \n",
    "\n",
    "2·39 = 78 \n",
    "\n",
    "6·13 = 78\n",
    "\n",
    "6·39 = 234 \n",
    "\n",
    "13·39 = 507\n",
    "\n",
    "Из них на 26 делятся 4 произведения:\n",
    "\n",
    "2·13=26\n",
    "\n",
    "2·39=78\n",
    "\n",
    "6·13=78\n",
    "\n",
    "6·39=234\n",
    "\n",
    "Требуется написать эффективную по времени и по памяти программу для решения описанной задачи.\n",
    "\n",
    "(Программа считается эффективной по времени, если при увеличении количества исходных чисел N в k раз время работы программы увеличивается не более чем в k раз. Программа считается эффективной по памяти, если память, необходимая для хранения всех переменных программы, не превышает 1 Кбайт и не меняется с ростом N.)"
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
 "nbformat_minor": 4
}
