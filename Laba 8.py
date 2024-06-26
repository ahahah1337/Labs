{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Лабораторная работа 8. ООП."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pylab\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. Создание классов и объектов\n",
    "В языке программирования Python классы создаются с помощью инструкции class, за которой следует произвольное имя класса, после которого ставится двоеточие, далее с новой строки и с отступом реализуется тело класса:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class A:    #  class ИмяКласса:\n",
    "    pass    #  тело_класса"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Создание экземпляра класса:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "a = A()     #  имя_переменной = ИмяКласса()"
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
      "<__main__.A object at 0x000001AF88680A58> объект класса <class '__main__.A'>\n"
     ]
    }
   ],
   "source": [
    "print(a, 'объект класса', type(a))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2. Класс как модуль (библиотека)\n",
    "Класс можно представить подобно модулю (библиотеки), в нем могут быть свои переменные со значениями и функции, у класса есть собственное пространство имен, доступ к которым возможен через имя класса:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class CLASS:\n",
    "    const = 5              # атрибут класса\n",
    "    def adder(v):          # функция-метод\n",
    "        return v + CLASS.const"
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
       "5"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CLASS.const"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CLASS.adder(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3. Класс как создатель объектов\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Object = CLASS()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Object.const"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "adder() takes 1 positional argument but 2 were given",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-9-1977c88ed4b9>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mObject\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0madder\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;36m100\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m: adder() takes 1 positional argument but 2 were given"
     ]
    }
   ],
   "source": [
    "Object.adder(100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Дело в том, что классы и объекты не просто модули. Класс создает объекты, которые в определенном смысле являются его наследниками (копиями). \n",
    "\n",
    "Это значит, что если у объекта нет собственного поля const, то интерпретатор ищет его уровнем выше, то есть в классе. Таким образом, если мы присваиваем объекту поле с таким же именем как в классе, то оно перекрывает, т. е. переопределяет, поле класса:"
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
       "5"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Object.const"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Object.const = 10\n",
    "Object.const"
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
       "5"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CLASS.const"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Видно что Object.const и CLASS.const – это разные переменные. \n",
    "\n",
    "Object.const находится в пространстве имен объекта Object. \n",
    "\n",
    "CLASS.const – в пространстве класса CLASS. \n",
    "\n",
    "Если не задовать поле const объекту Object, то интерпретатор бы поднялся выше по дереву наследования и пришел бы в класс, где бы и нашел это поле.\n",
    "\n",
    "Методы также наследуются объектами класса. В данном случае у объекта Object нет своего собственного метода adder, значит, он ищется в классе CLASS. Однако, от класса B может быть порождено множество объектов. И методы предназначаются для обработки объектов. Таким образом, когда вызывается метод, в него надо передать конкретный объект, который он будет обрабатывать.\n",
    "\n",
    "\n",
    "Выражение Object.adder(100) выполняется интерпретатором следующим образом:\n",
    "\n",
    "- Ищу атрибут adder() у объекта Object. Не нахожу.\n",
    "\n",
    "- Тогда иду искать в класс CLASS, так как он создал объект Object.\n",
    "\n",
    "- Здесь нахожу искомый метод. Передаю ему объект, к которому этот метод надо применить, и аргумент, указанный в скобках.\n",
    "\n",
    "Другими словами, выражение Object.adder(100) преобразуется в выражение CLASS.adder(Object, 100).\n",
    "\n",
    "Таким образом, интерпретатор попытался передать в метод adder() класса CLASS два параметра – объект Object и число 100. Но мы запрограммировали метод adder() так, что он принимает только один параметр. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Однако:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "adder() missing 1 required positional argument: 'v'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-30-c3adf6ca135c>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mObject\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0madder\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m: adder() missing 1 required positional argument: 'v'"
     ]
    }
   ],
   "source": [
    "Object.adder()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Получается странная ситуация. Ведь adder() вызывается не только через класса, но и через порожденные от него объекты. Однако в последнем случае всегда будет возникать ошибка. \n",
    "\n",
    "Может понадобиться метод с параметрами, но которому не надо передавать экземпляр данного класса. Для таких ситуаций предназначены статические методы. Такие методы могут вызываться через объекты данного класса, но сам объект в качестве аргумента в них не передается.\n",
    "\n",
    "В Python острой необходимости в статических методах нет, так как код может находиться за пределами класса, и программа не начинает выполняться из класса. Если нам нужна просто какая-нибудь функция, мы можем определить ее в основной ветке. Однако в Python тоже можно реализовать подобное, то есть статические методы, с помощью декоратора @staticmethod:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class CLASS:\n",
    "    const = 5              # атрибут класса\n",
    "    @staticmethod    \n",
    "    def adder(v):          # функция-метод\n",
    "        return v + CLASS.const"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Object = CLASS()"
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
       "10"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Object.adder(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Статические методы в Python – по-сути обычные функции, помещенные в класс для удобства и находящиеся в пространстве имен этого класса. Это может быть какой-то вспомогательный код. \n",
    "\n",
    "Вообще, если в теле метода не используется self, то есть ссылка на конкретный объект, имеет смысл сделать метод статическим."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4. Изменение полей объекта\n",
    "\n",
    "В Python объекту можно не только переопределять поля и методы, унаследованные от класса, также можно добавить новые, которых нет в классе:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Object1 = CLASS()\n",
    "Object2 = CLASS()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'abcd'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Object2.str = 'abcd'\n",
    "Object2.str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'CLASS' object has no attribute 'str'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m                            Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-24-fa4dbf7c88b1>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mObject1\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0mstr\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m: 'CLASS' object has no attribute 'str'"
     ]
    }
   ],
   "source": [
    "Object1.str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "type object 'CLASS' has no attribute 'str'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m                            Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-25-758a4284ae27>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mCLASS\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0mstr\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m: type object 'CLASS' has no attribute 'str'"
     ]
    }
   ],
   "source": [
    "CLASS.str"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Однако в программировании так делать не принято, потому что тогда объекты одного класса будут отличаться между собой по набору атрибутов. Это затруднит автоматизацию их обработки, внесет в программу хаос.\n",
    "\n",
    "Поэтому принято присваивать полям, а также получать их значения, путем вызова методов (сеттеров (set – установить) и геттеров (get – получить)):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class CLASS:\n",
    "    def setName(self, n):\n",
    "        self.name = n \n",
    "    def getName(self):\n",
    "        try:\n",
    "            return self.name\n",
    "        except:\n",
    "            return \"No name\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "first = CLASS()\n",
    "second = CLASS()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Bob'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "first.setName(\"Bob\")\n",
    "first.getName()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No name\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'>' not supported between instances of 'str' and 'NoneType'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-29-8e67368b52a9>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mprint\u001B[0m\u001B[1;33m(\u001B[0m\u001B[0mmax\u001B[0m\u001B[1;33m(\u001B[0m\u001B[0msecond\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0mgetName\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m,\u001B[0m\u001B[1;34m''\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m: '>' not supported between instances of 'str' and 'NoneType'"
     ]
    }
   ],
   "source": [
    "print(second.getName())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5. Специальные методы\n",
    "\n",
    "# 5.1. Конструктор класса (метод $__init__()$)\n",
    "\n",
    "В объектно-ориентированном программировании конструктором класса называют метод, который автоматически вызывается при создании объектов. Его также можно назвать конструктором объектов класса. Имя такого метода обычно регламентируется синтаксисом конкретного языка программирования. \n",
    "\n",
    "В Python роль конструктора играет метод $__init__()$.\n",
    "\n",
    "В Python наличие пар знаков подчеркивания спереди и сзади в имени метода говорит о том, что он принадлежит к группе методов перегрузки операторов. Если подобные методы определены в классе, то объекты могут участвовать в таких операциях как сложение, вычитание, вызываться как функции и др.\n",
    "\n",
    "При этом методы перегрузки операторов не надо вызывать по имени. Вызовом для них является сам факт участия объекта в определенной операции. В случае конструктора класса – это операция создания объекта. Так как объект создается в момент вызова класса по имени, то в этот момент вызывается метод $__init__()$, если он определен в классе.\n",
    "\n",
    "Необходимость конструкторов связана с тем, что нередко объекты должны иметь собственные свойства сразу. \n",
    "\n",
    "Пусть имеется класс Person, объекты которого обязательно должны иметь имя и фамилию:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Person:\n",
    "    def setName(self, n, s):\n",
    "        self.name = n\n",
    "        self.surname = s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p1 = Person()\n",
    "p1.setName(\"Bill\", \"Ross\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ИЛИ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Person:\n",
    "    def __init__(self, n, s):\n",
    "        self.name = n\n",
    "        self.surname = s"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "В свою очередь, конструктор класса не позволит создать объект без обязательных полей:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "__init__() missing 2 required positional arguments: 'n' and 's'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-32-080148c2dc60>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mp2\u001B[0m \u001B[1;33m=\u001B[0m \u001B[0mPerson\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m: __init__() missing 2 required positional arguments: 'n' and 's'"
     ]
    }
   ],
   "source": [
    "p2 = Person()"
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
      "Sam Baker\n"
     ]
    }
   ],
   "source": [
    "p2 = Person(\"Sam\", \"Baker\")\n",
    "print(p2.name, p2.surname)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Однако бывает, что надо допустить создание объекта, даже если никакие данные в конструктор не передаются. В таком случае параметрам конструктора класса задаются значения по умолчанию:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Rectangle:\n",
    "    def __init__(self, w = 0.5, h = 1):\n",
    "        self.width = w\n",
    "        self.height = h\n",
    "    def square(self):\n",
    "        return self.width * self.height"
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
      "10\n",
      "0.5\n",
      "3\n",
      "2.0\n"
     ]
    }
   ],
   "source": [
    "rec1 = Rectangle(5, 2)\n",
    "rec2 = Rectangle()\n",
    "rec3 = Rectangle(3)\n",
    "rec4 = Rectangle(h = 4)\n",
    "\n",
    "print(rec1.square())\n",
    "print(rec2.square())\n",
    "print(rec3.square())\n",
    "print(rec4.square())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5.2. Конструктор и деструктор\n",
    "\n",
    "Помимо конструктора объектов в языках программирования есть обратный ему метод – деструктор. Он вызывается для уничтожения объекта.\n",
    "\n",
    "В языке программирования Python объект уничтожается, когда исчезают все связанные с ним переменные или им присваивается другое значение, в результате чего связь со старым объектом теряется. Удалить переменную можно с помощью команды языка del.\n",
    "\n",
    "В классах Python функцию деструктора выполняет метод $__del__()$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Student:\n",
    " \n",
    "    def __init__(self, name, surname, position=1):\n",
    "        self.name = name\n",
    "        self.surname = surname\n",
    "        self.position = position\n",
    " \n",
    "    def display(self):\n",
    "        return self.name, self.surname, self.position\n",
    " \n",
    "    def __del__(self):\n",
    "        print (\"Goodbye %s %s\" %(self.name, self.surname))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p1 = Student('big', 'dude', 3) \n",
    "p2 = Student('small', 'croon', 4)\n",
    "p3 = Student('neutral', 'guy', 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('big', 'dude', 3)\n",
      "('small', 'croon', 4)\n",
      "('neutral', 'guy', 5)\n"
     ]
    }
   ],
   "source": [
    "print (p1.display())\n",
    "print (p2.display())\n",
    "print (p3.display())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goodbye small croon\n"
     ]
    }
   ],
   "source": [
    "del p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'p2' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mNameError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-40-ed22e138fbca>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mprint\u001B[0m \u001B[1;33m(\u001B[0m\u001B[0mp2\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0mdisplay\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mNameError\u001B[0m: name 'p2' is not defined"
     ]
    }
   ],
   "source": [
    "print (p2.display())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5.3. Специальные методы"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "В Python есть ряд зарезервированных имен методов создаваемого класса - специальные (или стандартные) методы.\n",
    "\n",
    "Более подробную информацию о них вы можете найти в соответствующей документации по Python: https://docs.python.org/3/reference/datamodel.html\n",
    "\n",
    "Например:\n",
    "\n",
    "$__bool__()$\n",
    "\n",
    "Возвращает True или False.\n",
    "\n",
    "$__call__()$\n",
    "\n",
    "Позволяет использовать объект как функцию, т.е. его можно вызвать.\n",
    "\n",
    "$__len__()$\n",
    "\n",
    "Чаще всего реализуется в коллекциях и сходными с ними по логике работы типами, которые позволяют хранить наборы данных. Для списка (list) __len__() возвращает количество элементов в списке, для строки – количество символов в строке. Вызывается функцией len(), встроенной в язык Python."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Метод $__setattr__()$\n",
    "\n",
    "В Python атрибуты объекту можно назначать за пределами класса:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class A:\n",
    "    def __init__(self, v):\n",
    "        self.field1 = v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 20\n"
     ]
    }
   ],
   "source": [
    "a = A(10)\n",
    "a.field2 = 20\n",
    "print(a.field1, a.field2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Если такое поведение нежелательно, его можно запретить с помощью метода перегрузки оператора присваивания атрибуту $__setattr__()$:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class A:\n",
    "    def __init__(self, v):\n",
    "        self.field1 = v\n",
    "    def __setattr__(self, attr, value):\n",
    "        if attr == 'field1':\n",
    "            self.__dict__[attr] = value\n",
    "        else:\n",
    "            raise AttributeError('Произошло обращение к несуществующему отребуту!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = A(15)\n",
    "a.field1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "Произошло обращение к несуществующему отребуту!",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m                            Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-45-f2358415109b>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0ma\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0mfield2\u001B[0m \u001B[1;33m=\u001B[0m \u001B[1;36m30\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;32m<ipython-input-43-46da94a45054>\u001B[0m in \u001B[0;36m__setattr__\u001B[1;34m(self, attr, value)\u001B[0m\n\u001B[0;32m      6\u001B[0m             \u001B[0mself\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0m__dict__\u001B[0m\u001B[1;33m[\u001B[0m\u001B[0mattr\u001B[0m\u001B[1;33m]\u001B[0m \u001B[1;33m=\u001B[0m \u001B[0mvalue\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0;32m      7\u001B[0m         \u001B[1;32melse\u001B[0m\u001B[1;33m:\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[1;32m----> 8\u001B[1;33m             \u001B[1;32mraise\u001B[0m \u001B[0mAttributeError\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;34m'Произошло обращение к несуществующему отребуту!'\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m: Произошло обращение к несуществующему отребуту!"
     ]
    }
   ],
   "source": [
    "a.field2 = 30"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'A' object has no attribute 'field2'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m                            Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-46-535783f42773>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0ma\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0mfield2\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m: 'A' object has no attribute 'field2'"
     ]
    }
   ],
   "source": [
    "a.field2"
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
       "{'field1': 15}"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.__dict__"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Метод __setattr__(), если он присутствует в классе, вызывается всегда, когда какому-либо атрибуту выполняется присваивание. Обратите внимание, что присвоение несуществующему атрибуту также обозначает его добавление к объекту.\n",
    "\n",
    "Когда создается объект a, в конструктор передается число 15. Здесь для объекта заводится атрибут field1. Факт попытки присвоения ему значения тут же отправляет интерпретатор в метод __setattr__(), где проверяется соответствует ли имя атрибута строке 'field1'. Если так, то атрибут и соответствующее ему значение добавляется в словарь атрибутов объекта.\n",
    "\n",
    "Нельзя в __setattr__() написать просто self.field1 = value, так как это приведет к новому рекурсивному вызову метода __setattr__(). Поэтому поле назначается через словарь __dict__, который есть у всех объектов, и в котором хранятся их атрибуты со значениями.\n",
    "\n",
    "Если параметр attr не соответствует допустимым полям, то искусственно возбуждается исключение AttributeError. Мы это видим, когда в основной ветке пытаемся обзавестись полем field2."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Пример №1. Числа Фибоначчи\n",
    "\n",
    "Последовательность чисел Фибоначчи задаётся рекуррентным выражением:\n",
    "\n",
    "$$ F_n =  \\begin{cases}\n",
    "           0, n = 0, \\\\\n",
    "           1, n = 1, \\\\\n",
    "           F_{n-1}+F_{n-2}, n > 1.\n",
    "          \\end{cases} $$\n",
    "\n",
    "Что даёт следующую последовательность {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …}."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Один из способов решения, который может показаться логичным и эффективным, — решение с помощью рекурсии:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Fibonacci_Recursion(n):\n",
    "    if n == 0:\n",
    "        return 0\n",
    "    if n == 1:\n",
    "        return 1\n",
    "    return Fibonacci_Recursion (n-1) + Fibonacci_Recursion (n-2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Используя такую функцию, мы будем решать задачу «с конца» — будем шаг за шагом уменьшать n, пока не дойдем до известных значений.\n",
    "\n",
    "Но, как мы видели ранее эта реализация многократно повторяет решение одних и тех же задач. Это связано с тем, что одни и те же промежуточные данные вычисляются по несколько раз, а число операций нарастает с той же скоростью, с какой растут числа Фибоначчи — экспоненциально.\n",
    "\n",
    "Один из выходов из данной ситуации — сохранение уже найденных промежуточных результатов с целью их повторного использования (кеширование). Причём кеш должен храниться во внешней области памяти."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Fibonacci_Recursion_cache(n, cache):\n",
    "    if n == 0:\n",
    "        return 0\n",
    "    if n == 1:\n",
    "        return 1\n",
    "    if cache[n] > 0:\n",
    "        return cache[n]\n",
    "    cache[n] = Fibonacci_Recursion_cache (n-1, cache) + Fibonacci_Recursion_cache (n-2, cache)\n",
    "    return cache[n]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Приведенное решение достаточно эффективно (за исключением накладных расходов на вызов функций). Но можно поступить ещё проще:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Fibonacci(n):\n",
    "    \n",
    "    fib = [0]*max(2,n+1)\n",
    "    fib[0] = 0\n",
    "    fib[1] = 1\n",
    "    for i in range(2, n+1):\n",
    "        fib[i] = fib[i - 1] + fib[i - 2]\n",
    "        \n",
    "    return fib[n]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Такое решение можно назвать решением «с начала» — мы первым делом заполняем известные значения, затем находим первое неизвестное значение, потом следующее и т.д., пока не дойдем до нужного.\n",
    "\n",
    "Так и работает динамическое программирование: сначала решили все подзадачи (нашли все F[i] для i < n), затем, зная решения подзадач, нашли решение исходной задачи."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение №1\n",
    "\n",
    "Создайте класс для вычисления чисел Фибоначчи. Каждое число фибоначи является объектом этого класса, которое имеет атрибуты: значение и номер. Используйте функции для инициализации (вычисления) чисел Фибоначчи как сторонние по отношению к этому классу."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение №2\n",
    "\n",
    "Поместите функции для вычисления чисел Фибоначчи внутрь созданного класса как статические функции."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение №3\n",
    "\n",
    "Перегрузите опарации сложения, вычитания, умножения и деления для созданного класса как операции с номерами чисел Фибоначи."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
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
    "# Задание №1. \n",
    "\n",
    "Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных. Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит наибольшее значение из этих двух переменных."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class First:\n",
    "    def __init__(self, num1, num2):\n",
    "        self.num1 = num1\n",
    "        self.num2 = num2\n",
    "\n",
    "    def write_num(self):\n",
    "        print(f'Первое число: {self.num1}, второе число: {self.num2}')\n",
    "\n",
    "    def redact(self, num1, num2):\n",
    "        self.num1 = num1\n",
    "        self.num2 = num2\n",
    "\n",
    "    def summa(self):\n",
    "        return self.num1 + self.num2\n",
    "\n",
    "    def max_number(self):\n",
    "        if self.num1 > self.num2:\n",
    "            return '>'\n",
    "        elif self.num1 < self.num2:\n",
    "            return '<'\n",
    "        else:\n",
    "            return '='\n",
    "\n",
    "def main():\n",
    "    obj = First(int(input('Введите первое число: ')), int(input('Введите второе число: ')))\n",
    "    obj.write_num()\n",
    "    print(f'{obj.num1} + {obj.num2} = {obj.summa()}')\n",
    "    print(f'{obj.num1} {obj.max_number()} {obj.num2}')\n",
    "\n",
    "    while input('Вы хотите изменить числа? (Yes/No): ').strip().lower() == 'yes':\n",
    "        obj.redact(int(input('Введите первое изменённое число: ')), int(input('Введите второе изменённое число: ')))\n",
    "        obj.write_num()\n",
    "        print(f'{obj.num1} + {obj.num2} = {obj.summa()}')\n",
    "        print(f'{obj.num1} {obj.max_number()} {obj.num2}')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание №2. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "Составить описание класса многочленов от одной переменной, задаваемых степенью многочлена и массивом коэффициентов. Предусмотреть методы для вычисления значения многочлена для заданного аргумента, операции сложения, вычитания и умножения многочленов с получением нового объекта-многочлена, вывод на экран описания многочлена."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Polynomial:\n",
    "    def __init__(self, *terms: int):\n",
    "        self._terms = terms\n",
    "\n",
    "    def __str__(self):\n",
    "        if not self._terms:\n",
    "            return \"0\"\n",
    "        out = []\n",
    "        for p, term in enumerate(self._terms):\n",
    "            if term == 0:\n",
    "                continue\n",
    "            sign = \" + \" if term > 0 else \" - \"\n",
    "            term_str = f\"{abs(term)}\" if abs(term) != 1 or p == 0 else \"\"\n",
    "            variable_str = \"x\" if p > 0 else \"\"\n",
    "            exponent_str = f\"^{p}\" if p > 1 else \"\"\n",
    "            out.append(f\"{term_str}{variable_str}{exponent_str}\")\n",
    "        result = sign.join(out).strip()\n",
    "        return result if result[0] != \"+\" else result[2:]\n",
    "\n",
    "    def __mul__(self, other: 'Polynomial'):\n",
    "        result_terms = [0] * (len(self._terms) + len(other._terms) - 1)\n",
    "        for i, term1 in enumerate(self._terms):\n",
    "            for j, term2 in enumerate(other._terms):\n",
    "                result_terms[i + j] += term1 * term2\n",
    "        return Polynomial(*result_terms)\n",
    "\n",
    "# Пример использования\n",
    "poly1 = Polynomial(1, 2, 3)\n",
    "poly2 = Polynomial(4, 5, 6)\n",
    "result = poly1 * poly2\n",
    "print(f'({poly1}) * ({poly2}) = {result}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание №3\n",
    "\n",
    "Составить описание класса для вектора, заданного координатами его концов в трехмерном пространстве. Обеспечить операции сложения и вычитания векторов с получением нового вектора (суммы или разности), вычисления скалярного произведения двух векторов, длины вектора, косинуса угла между векторами."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Vector3D:\n",
    "    def __init__(self, x, y, z):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.z = z\n",
    "\n",
    "    def __str__(self):\n",
    "        return f\"({self.x}, {self.y}, {self.z})\"\n",
    "\n",
    "    def __add__(self, other):\n",
    "        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)\n",
    "\n",
    "    def __sub__(self, other):\n",
    "        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)\n",
    "\n",
    "    def __mul__(self, other):\n",
    "        if isinstance(other, Vector3D):  # Scalar (dot) product\n",
    "            return self.x * other.x + self.y * other.y + self.z * other.z\n",
    "        else:  # Scalar multiplication\n",
    "            return Vector3D(self.x * other, self.y * other, self.z * other)\n",
    "\n",
    "    def __abs__(self):\n",
    "        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5\n",
    "\n",
    "    def cos_angle(self, other):\n",
    "        return (self * other) / (abs(self) * abs(other))\n",
    "\n",
    "# Примеры использования\n",
    "v1 = Vector3D(1, 1, 1)\n",
    "v2 = Vector3D(1, 3, -2)\n",
    "\n",
    "v = v1 + v2\n",
    "print(\"Сумма векторов:\", v)\n",
    "\n",
    "cf = v1 * v2\n",
    "print(\"Скалярное произведение векторов:\", cf)\n",
    "\n",
    "co = v1.cos_angle(v2)\n",
    "print(\"Косинус угла между векторами:\", co)\n",
    "\n",
    "v3 = v1 * 10\n",
    "print(\"Умножение вектора на скаляр:\", v3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание №4. Поезда.\n",
    "\n",
    "Создайте структуру с именем train, содержащую поля: название пунктов отправления и назначения, время отправления и прибытия. Перегрузить операцию сложения - два поезда можно сложить, если пунк назначения первого совпадает с пунктом отправления второго и время прибытия первого раньше чем отправление второго."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Train:\n",
    "    def __init__(self, departure, destination, departure_time, arrival_time):\n",
    "        self.departure = departure\n",
    "        self.destination = destination\n",
    "        self.departure_time = departure_time\n",
    "        self.arrival_time = arrival_time\n",
    "\n",
    "    def __add__(self, other):\n",
    "        if self.destination == other.departure and self.arrival_time < other.departure_time:\n",
    "            new_departure = self.departure\n",
    "            new_destination = other.destination\n",
    "            new_departure_time = self.departure_time\n",
    "            new_arrival_time = other.arrival_time\n",
    "            return Train(new_departure, new_destination, new_departure_time, new_arrival_time)\n",
    "        else:\n",
    "            return None\n",
    "\n",
    "    def __str__(self):\n",
    "        return (f\"Train from {self.departure} to {self.destination}, \"\n",
    "                f\"departing at {self.departure_time}, arriving at {self.arrival_time}\")\n",
    "\n",
    "# Примеры использования\n",
    "train1 = Train(\"Москва\", \"Санкт-Петербург\", \"10:00\", \"14:00\")\n",
    "train2 = Train(\"Санкт-Петербург\", \"Москва\", \"15:00\", \"19:00\")\n",
    "\n",
    "combined_train = train1 + train2\n",
    "\n",
    "if combined_train:\n",
    "    print(f\"Поезда ({train1}) и ({train2}) могут быть объединены.\")\n",
    "    print(f\"Объединённый поезд: {combined_train}\")\n",
    "else:\n",
    "    print(\"Поезда не могут быть объединены.\")"
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
    "# Библиотека.\n",
    "\n",
    "Описать класс «библиотека». Предусмотреть возможность работы с произвольным числом книг, поиска книги по какому-либо признаку (например, по автору или по году издания), добавления книг в библиотеку, удаления книг из нее, сортировки книг по разным полям."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Обобщённое число.\n",
    "\n",
    "Создайте класс обобщающий понятие комплексных, двойных и дуальных чисел.\n",
    "\n",
    "Такие числа объеденены одной формой записи:\n",
    "\n",
    "$$ c = a + ib $$\n",
    "\n",
    "где c - обобщённое число (комплексное, двойное или дуальное), a и b - вещественные числа, i - некоммутирующий символ.\n",
    "\n",
    "Именно из-за наличия символа i число c не просто сумма a и b. Такие числа можно представлять как вектор на плоскости (a,b).\n",
    "\n",
    "А символ i обладает следующим свойством:\n",
    "\n",
    "- для комплексных чисел\n",
    "\n",
    "$$ i^2 = -1 $$\n",
    "\n",
    "- для двойных чисел\n",
    "\n",
    "$$ i^2 = 1 $$\n",
    "\n",
    "- для дуальных чисел\n",
    "\n",
    "$$ i^2 = 0 $$\n",
    "\n",
    "Перегрузить для них базовые операции: сложения, вычитания, умножения и деления.\n",
    "\n",
    "Например, операция умножения для таких чисел имеет вид:\n",
    "\n",
    "$$ (a_1+b_1i)\\cdot (a_2+b_2i)=a_1a_2+b_1a_2i+a_1b_2i+b_1b_2i^{2}=(a_1a_2+b_1b_2i^{2})+(b_1a_2+a_1b_2)i. $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
