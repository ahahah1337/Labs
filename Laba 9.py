{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Лабораторная работа 9. ООП."
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
    "# 1. Инкапсуляция\n",
    "Под инкапсуляцией в объектно-ориентированном программировании понимается упаковка данных и методов для их обработки вместе, т. е. в классе. В Python инкапсуляция реализуется как на уровне классов, так и объектов. В ряде других языков, например в Java, под инкапсуляцией также понимают сокрытие свойств и методов, в результате чего они становятся приватными. Это значит, что доступ к ним ограничен либо пределами класса, либо модуля.\n",
    "\n",
    "В Python подобной инкапсуляции нет, хотя существует способ ее имитировать. Перед тем как выяснять, как это делается, надо понять, зачем вообще что-то скрывать.\n",
    "\n",
    "Дело в том, что классы бывают большими и сложными. В них может быть множество вспомогательных полей и методов, которые не должны использоваться за его пределами. Они просто для этого не предназначены. Они своего рода внутренние шестеренки, обеспечивающие нормальную работу класса.\n",
    "\n",
    "Кроме того, в других языках программирования хорошей практикой считается сокрытие всех полей объектов, чтобы уберечь их от прямого присвоения значений из основной ветки программы. Их значения можно изменять и получать только через вызовы методов, специально определенных для этих целей.\n",
    "\n",
    "Например, если надо проверять присваиваемое полю значение на корректность, то делать это каждый раз в основном коде программы будет неправильным. Проверочный код должен быть помещен в метод, который получает данные, для присвоения полю. А само поле должно быть закрыто для доступа из вне класса. В этом случае ему невозможно будет присвоить недопустимое значение.\n",
    "\n",
    "Часто намеренно скрываются поля самого класса, а не его объектов. Например, если класс имеет счетчик своих объектов, то необходимо исключить возможность его случайного изменения из вне. Рассмотрим пример с таким счетчиком на языке Python."
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
    "class B:\n",
    "    count = 0\n",
    "    def __init__(self):\n",
    "        B.count += 1\n",
    "    def __del__(self):\n",
    "        B.count -= 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "a = B()\n",
    "b = B()\n",
    "с = B()\n",
    "print(b.count)\n",
    "print(B.count) \n",
    "del a\n",
    "print(B.count) "
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
       "2"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.count"
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
      "1\n"
     ]
    }
   ],
   "source": [
    "B.count -= 1\n",
    "print(B.count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2. Полиморфизм\n",
    "Полиморфизм в объектно-ориентированном программировании – это возможность обработки разных типов данных, т. е. принадлежащих к разным классам, с помощью \"одно и той же\" функции, или метода. На самом деле одинаковым является только имя метода, его исходный код зависит от класса. Кроме того, результаты работы одноименных методов могут существенно различаться. Поэтому в данном контексте под полиморфизмом понимается множество форм одного и того же слова – имени метода.\n",
    "\n",
    "Например, два разных класса содержат метод total, однако инструкции каждого предусматривают совершенно разные операции. Так в классе T1 – это прибавление 10 к аргументу, в T2 – подсчет длины строки символов. В зависимости от того, к объекту какого класса применяется метод total, выполняются те или иные инструкции."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class T1:\n",
    "     n=10\n",
    "     def total(self, N):\n",
    "          self.total = int(self.n) + int(N)\n",
    " \n",
    "class T2:\n",
    "     def total(self,s):\n",
    "          self.total = len(str(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "t1 = T1()\n",
    "t2 = T2()\n",
    "t1.total(45)\n",
    "t2.total(45)\n",
    "print(t1.total) \n",
    "print(t2.total) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Как видно полиморфизмом обладают классы связанные наследованием. У каждого может быть свой метод __init__() или square() или какой-нибудь другой. Какой именно из методов square() вызывается, и что он делает, зависит от принадлежности объекта к тому или иному классу.\n",
    "\n",
    "Однако классы не обязательно должны быть связанны наследованием. Полиморфизм как один из ключевых элементов ООП существует независимо от наследования. Классы могут быть не родственными, но иметь одинаковые методы.\n",
    "\n",
    "Полиморфизм дает возможность реализовывать так называемые единые интерфейсы для объектов различных классов. Например, разные классы могут предусматривать различный способ вывода той или иной информации объектов. Однако одинаковое название метода вывода позволит не запутать программу, сделать код более ясным.\n",
    "\n",
    "Рассмотрим пример полиморфизма на еще одном методе, который перегружает функцию print().\n",
    "\n",
    "Если вы создадите объект собственного класса, а потом попробуете вывести его на экран, то получите информацию о классе объекта и его адрес в памяти. Такое поведение функции print() по-умолчанию по отношению к пользовательским классам запрограммировано на самом верхнем уровне иерархии, где-то в суперклассе, от которого неявно наследуются все остальные."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class A:\n",
    "    def __init__(self, v1, v2):\n",
    "        self.field1 = v1\n",
    "        self.field2 = v2"
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
      "<__main__.A object at 0x0000021DDCE084E0>\n"
     ]
    }
   ],
   "source": [
    "a = A(3, 4)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Если же мы хотим, чтобы, когда объект передается функции print(), выводилась какая-нибудь другая более полезная информация, то в класс надо добавить специальный метод __str__(). Этот метод должен обязательно возвращать строку, которую будет выводить функция print():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class A:\n",
    "    def __init__(self, v1, v2):\n",
    "        self.field1 = v1\n",
    "        self.field2 = v2\n",
    "    def __str__(self):\n",
    "        return str(self.field1) + \" \" + str(self.field2)"
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
      "3 4\n"
     ]
    }
   ],
   "source": [
    "a = A(3, 4)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение №1\n",
    "\n",
    "Измените класс A таким образом, что объект этого класса может содержать произвольное число параметров. Пергрузите для него функции $__bool__()$ и $__len__()$."
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
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# 3. Наследование\n",
    "Наследование – важная составляющая объектно-ориентированного программирования. Так или иначе мы уже сталкивались с ним, ведь объекты наследуют атрибуты своих классов. Однако обычно под наследованием в ООП понимается наличие классов и подклассов. Также их называют супер- или надклассами и классами, а также родительскими и дочерними классами.\n",
    "\n",
    "Суть наследования здесь схожа с наследованием объектами от классов. Дочерние классы наследуют атрибуты родительских, а также могут переопредять атрибуты и добавлять свои."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# 3.1. Простое наследование"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Table:\n",
    "    def __init__(self, l, w, h):\n",
    "        self.lenght = l\n",
    "        self.width = w\n",
    "        self.height = h\n",
    " \n",
    "class KitchenTable(Table):\n",
    "    def setPlaces(self, p):\n",
    "        self.places = p\n",
    " \n",
    "class DeskTable(Table):\n",
    "    def square(self):\n",
    "        return self.width * self.lenght"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "В данном случае классы KitchenTable и DeskTable не имеют своих собственных конструкторов, поэтому наследуют его от родительского класса. При создании экземпляров этих столов, передавать аргументы для __init__() обязательно, иначе возникнет ошибка:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "__init__() missing 3 required positional arguments: 'l', 'w', and 'h'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-15-23c8571ae17e>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mt1\u001B[0m \u001B[1;33m=\u001B[0m \u001B[0mKitchenTable\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mTypeError\u001B[0m: __init__() missing 3 required positional arguments: 'l', 'w', and 'h'"
     ]
    }
   ],
   "source": [
    "t1 = KitchenTable()"
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
    "t1 = KitchenTable(2, 2, 0.7)\n",
    "t2 = DeskTable(1.5, 0.8, 0.75)\n",
    "t3 = KitchenTable(1, 1.2, 0.8)"
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
       "1"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t3.lenght"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "Несомненно можно создавать столы и от родительского класса Table. Однако он не будет, согласно неким родственным связям, иметь доступ к методам setPlaces() и square(). Точно также как объект класса KitchenTable не имеет доступа к единоличным атрибутам сестринского класса DeskTable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "t4 = Table(1, 1, 0.5)"
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
       "1.2000000000000002"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t2.width * t2.lenght"
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
       "1.2000000000000002"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t2.square()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Table' object has no attribute 'square'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m                            Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-21-7b0795c5741d>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mt4\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0msquare\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m: 'Table' object has no attribute 'square'"
     ]
    }
   ],
   "source": [
    "t4.square()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'KitchenTable' object has no attribute 'square'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m                            Traceback (most recent call last)",
      "\u001B[1;32m<ipython-input-22-ed231ab2573c>\u001B[0m in \u001B[0;36m<module>\u001B[1;34m()\u001B[0m\n\u001B[1;32m----> 1\u001B[1;33m \u001B[0mt3\u001B[0m\u001B[1;33m.\u001B[0m\u001B[0msquare\u001B[0m\u001B[1;33m(\u001B[0m\u001B[1;33m)\u001B[0m\u001B[1;33m\u001B[0m\u001B[0m\n\u001B[0m",
      "\u001B[1;31mAttributeError\u001B[0m: 'KitchenTable' object has no attribute 'square'"
     ]
    }
   ],
   "source": [
    "t3.square()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3.2. Полное переопределение метода надкласса\n",
    "Что если в подклассе нам не подходит код метода его надкласса. Допустим, мы вводим еще один класс столов, который является дочерним по отношению к DeskTable. Пусть это будут компьютерные столы, при вычислении рабочей поверхности которых надо отнимать заданную величину. Имеет смысл внести в этот новый подкласс его собственный метод square():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class ComputerTable(DeskTable):\n",
    "    def square(self, e):\n",
    "        return self.width * self.lenght - e"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "При создании объекта типа ComputerTable по-прежнему требуется указывать параметры, так как интерпретатор в поисках конструктора пойдет по дереву наследования сначала в родителя, а потом в прародителя и найдет там метод __init__().\n",
    "\n",
    "Однако когда будет вызываться метод square(), то поскольку он будет обнаружен в самом ComputerTable, то метод square() из DeskTable останется невидимым, т. е. для объектов класса ComputerTable он окажется переопределенным."
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
       "1.7"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ct = ComputerTable(2, 1, 1)\n",
    "ct.square(0.3)"
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
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class ComputerTable(DeskTable):\n",
    "    def square(self, e):\n",
    "        return DeskTable.square(self) - e "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.7"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ct = ComputerTable(2, 1, 1)\n",
    "ct.square(0.3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Допустим, в классе KitchenTable нам не нужен метод, поле places должно устанавливаться при создании объекта в конструкторе. В классе можно создать собсвенный конструктор с чистого листа, чем переопределить родительский:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class KitchenTable(Table):\n",
    "    def __init__(self, l, w, h, p):\n",
    "        self.length = l\n",
    "        self.width = w\n",
    "        self.height = h\n",
    "        self.places = p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Однако, если дублируется почти весь конструктор надкласса, проще вызвать родительский конструктор, после чего дополнить своим кодом:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class KitchenTable(Table):\n",
    "    def __init__(self, l, w, h, p):\n",
    "        Table.__init__(self, l, w, h)\n",
    "        self.places = p"
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
    "tk = KitchenTable(2, 1.5, 0.7, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tk.places"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.5"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tk.width "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3.3. Множественное наследование\n",
    "\n",
    "Для наследования от нескольких классав в определении класса-наследника достаточно указать в круглых скобках сразу несколько базовых классов через запятую.\n",
    "\n",
    "# Пример.\n",
    "\n",
    "Рассмотрим три класса:"
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
    "class Classl: \n",
    "    def funс1(self):\n",
    "        print(\"Метод funс1() класса Classl\")\n",
    "\n",
    "class Class2(Classl): # Простое наследование\n",
    "    def func2(self):\n",
    "        print(\"Метод func2() класса Class2\")\n",
    "\n",
    "class Class3(Classl): # Простое наследование\n",
    "    def funс1(self):\n",
    "        print(\"Метод funс1() класса Class3\")\n",
    "    def func2(self):\n",
    "        print(\"Метод func2() класса Class3\")\n",
    "    def func3(self):\n",
    "        print(\"Метод func3() класса Class3\")\n",
    "    def func4(self):\n",
    "        print(\"Метод func4() класса Class3\")\n",
    "\n",
    "class Class4(Class2, Class3): # Множественное наследование\n",
    "    def func4(self):\n",
    "        print(\"Метод func4() класса Class4\")"
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
      "Метод funс1() класса Class3\n",
      "Метод func2() класса Class2\n",
      "Метод func3() класса Class3\n",
      "Метод func4() класса Class4\n"
     ]
    }
   ],
   "source": [
    "c = Class4()\n",
    "c.funс1() \n",
    "c.func2() \n",
    "c.func3() \n",
    "c.func4() "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Метод func1() определен в двух классах: class1 и ciass3. Так как вначале просматриваются все базовые классы, непосредственно указанные в определении текущего класса, метод func1() будет найден в классе class3 (поскольку он указан в числе базовых классов в определении Class4), а не в классе Class1.\n",
    "\n",
    "Метод func2() также определен в двух классах: Class2 и Class3. Так как класс Class2 стоит первым в списке базовых классов, то метод будет найден именно в нем. \n",
    "\n",
    "Чтобы наследовать метод из класса Class3, следует указать это явным образом:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Class4(Class2, Class3): # Множественное наследование\n",
    "# Наследуем func2() из класса Class3, а не из класса Class2\n",
    "    func2 = Class3.func2\n",
    "    def func4(self):\n",
    "        print(\"Метод func4() класса Class4\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Метод funс1() класса Class3\n",
      "Метод func2() класса Class3\n",
      "Метод func3() класса Class3\n",
      "Метод func4() класса Class4\n"
     ]
    }
   ],
   "source": [
    "c = Class4()\n",
    "c.funс1() \n",
    "c.func2() \n",
    "c.func3() \n",
    "c.func4() "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение №2\n",
    "\n",
    "Напишите класс \"numbers\" содержащий два атрибута x и y, функцию инициализации и функции Operation и Run:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def Operation(self):\n",
    "    return self.x + self.y\n",
    "def Run(self):\n",
    "    z = self.Operation()\n",
    "    print(\"Результат операции равен \" + z.__str__())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Создайте класс наследник, и с помощью полиморфизма замените функцию Operation на любую другую в наследном классе."
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
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# 4. Композиция\n",
    "\n",
    "Еще одной особенностью объектно-ориентированного программирования является возможность реализовывать так называемый композиционный подход. Заключается он в том, что есть класс-контейнер, он же агрегатор, который включает в себя вызовы других классов. В результате чего, что при создании объекта класса-контейнера, также создаются объекты включенных в него классов.\n",
    "\n",
    "Не следует путать композицию с наследованием, в том числе множественным. Наследование предполагает принадлежность к какой-то общности (похожесть), а композиция — формирование целого из частей. Наследуются атрибуты, т.е. возможности, другого класса, при этом объектов непосредственно родительского класса не создается. При композиции же класс-агрегатор создает объекты других классов.\n",
    "\n",
    "Рассмотрим на примере реализацию композиции в Python. Пусть, требуется написать программу, которая вычисляет площадь стен. При этом окна, двери, пол и потолок должны быть исключены.\n",
    "\n",
    "И так, комната – это прямоугольный параллелепипед, состоящий из шести прямоугольников. Его площадь представляет собой сумму площадей составляющих его прямоугольников. Площадь прямоугольника равна произведению его длины на ширину."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class WinDoor:\n",
    "     def __init__(self, x, y):\n",
    "          self.square = x * y "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Room:\n",
    "    def __init__(self, x, y, z):\n",
    "        self.square = 2 * z * (x + y)\n",
    "        self.wd = []\n",
    "    def addWD(self, w, h):\n",
    "        self.wd.append(WinDoor(w, h))\n",
    "    def workSurface(self):\n",
    "        new_square = self.square\n",
    "        for i in self.wd:\n",
    "            new_square -= i.square\n",
    "        return new_square"
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
      "48.6\n",
      "44.6\n"
     ]
    }
   ],
   "source": [
    "r1 = Room(6, 3, 2.7) \n",
    "print(r1.square)\n",
    "r1.addWD(1, 1) \n",
    "r1.addWD(1, 1)\n",
    "r1.addWD(1, 2)\n",
    "print(r1.workSurface())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение №3\n",
    "\n",
    "Дополните приведённый пример возможностью вычисления площади пола и потолка, приэтом в полу может быть квадратный проём с лестницей ведущей вниз, а на птолке круглые слуховые окна."
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
    "Создайте класс \"Геометрические фигуры\" атрибутами котрого будут: параметры периметр, площадь и координаты некотрой характерной точки или точек (например, центра или вершин). Создайте три класса потомка: треугольник, прямоугольник, круг. Для классов потомков определить функцию инициализации $__init__$ и функции для вычисления периметра и площади, функцию paint выводящую рисунок соответствующей геометрической фигуры с помощью библиотеки matplotlib."
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
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "class Figure:\n",
    "    def __init__(self, center_x, center_y):\n",
    "        self.center_x = center_x\n",
    "        self.center_y = center_y\n",
    "\n",
    "class Circle(Figure):\n",
    "    def __init__(self, center_x, center_y, radius):\n",
    "        super().__init__(center_x, center_y)\n",
    "        self.radius = radius\n",
    "        self.area = np.pi * self.radius**2\n",
    "        self.circumference = 2 * np.pi * self.radius\n",
    "\n",
    "class Triangle(Figure):\n",
    "    def __init__(self, x1, y1, x2, y2, x3, y3):\n",
    "        self.x1, self.y1 = x1, y1\n",
    "        self.x2, self.y2 = x2, y2\n",
    "        self.x3, self.y3 = x3, y3\n",
    "\n",
    "    def vertices(self):\n",
    "        return [self.x1, self.x2, self.x3, self.x1], [self.y1, self.y2, self.y3, self.y1]\n",
    "\n",
    "class Rectangle(Figure):\n",
    "    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):\n",
    "        self.x1, self.y1 = x1, y1\n",
    "        self.x2, self.y2 = x2, y2\n",
    "        self.x3, self.y3 = x3, y3\n",
    "        self.x4, self.y4 = x4, y4\n",
    "\n",
    "    def vertices(self):\n",
    "        return [self.x1, self.x2, self.x3, self.x4, self.x1], [self.y1, self.y2, self.y3, self.y4, self.y1]\n",
    "\n",
    "def draw_circle(circle):\n",
    "    fig, ax = plt.subplots()\n",
    "    circle_plot = plt.Circle((circle.center_x, circle.center_y), circle.radius, color='blue', fill=False)\n",
    "    ax.add_artist(circle_plot)\n",
    "    ax.set_xlim(circle.center_x - circle.radius - 1, circle.center_x + circle.radius + 1)\n",
    "    ax.set_ylim(circle.center_y - circle.radius - 1, circle.center_y + circle.radius + 1)\n",
    "    ax.set_aspect('equal', 'box')\n",
    "    plt.show()\n",
    "\n",
    "def draw_polygon(vertices):\n",
    "    plt.plot(vertices[0], vertices[1])\n",
    "    plt.show()\n",
    "\n",
    "print('Выберите цифру рисунка:\\n1) Треугольник\\n2) Круг\\n3) Прямоугольник')\n",
    "choice = input()\n",
    "\n",
    "if choice == '1':\n",
    "    triangle1 = Triangle(0, 0, 1, 1, 2, 0)\n",
    "    draw_polygon(triangle1.vertices())\n",
    "elif choice == '2':\n",
    "    circle1 = Circle(0, 0, 2)\n",
    "    draw_circle(circle1)\n",
    "elif choice == '3':\n",
    "    rectangle1 = Rectangle(0, 0, 0, 1, 2, 1, 2, 0)\n",
    "    draw_polygon(rectangle1.vertices())\n",
    "else:\n",
    "    print('Данная операция отсутствует')"
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
    "Реализуйте класс Matrix. Он должен содержать:\n",
    "\n",
    "- Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер. Конструктор должен копировать содержимое списка списков, т.е. при изменении списков, от которых была сконструирована матрица, содержимое матрицы изменяться не должно.\n",
    "- Метод $__str__$, переводящий матрицу в строку. При этом элементы внутри одной строки должны быть разделены знаками табуляции, а строки — переносами строк. После каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.\n",
    "- Метод size без аргументов, возвращающий кортеж вида (число строк, число столбцов). \n",
    "- $__add__$, принимающий вторую матрицу того же размера и возвращающий сумму матриц. В случае, если две матрицы сложить невозможно, должно выводиться сообщение об ошибке.\n",
    "- $__mul__$, таким образом, чтобы матрицы можно было умножать на скаляры и на другие матрицы. В случае, если две матрицы перемножить невозможно, должно выводиться сообщение об ошибке.\n",
    "- $__rmul__$, делающий то же самое, что и $__mul__$. Этот метод будет вызван в том случае, аргумент находится справа. Для реализации этого метода в коде класса достаточно написать $__rmul__$ = $__mul__$.\n",
    "- Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу."
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
    "import numpy as np\n",
    "\n",
    "class Matrix:\n",
    "    def __init__(self, data: list[list[int]]):\n",
    "        self.data = np.array(data)\n",
    "\n",
    "    def __str__(self):\n",
    "        result = ''\n",
    "        for row in self.data:\n",
    "            result += '\\t'.join(map(str, row)) + '\\n'\n",
    "        return result.strip()\n",
    "\n",
    "    def size(self) -> tuple[int, int]:\n",
    "        return self.data.shape\n",
    "\n",
    "    def __add__(self, other: 'Matrix') -> 'Matrix':\n",
    "        if self.size() != other.size():\n",
    "            raise ValueError(\"Размеры матриц не совпадают\")\n",
    "        return Matrix(self.data + other.data)\n",
    "\n",
    "    def __mul__(self, other):\n",
    "        if isinstance(other, int):\n",
    "            return Matrix(self.data * other)\n",
    "        elif isinstance(other, Matrix):\n",
    "            if self.data.shape[1] != other.data.shape[0]:\n",
    "                raise ValueError(\"Матрицы нельзя умножить\")\n",
    "            return Matrix(np.dot(self.data, other.data))\n",
    "        else:\n",
    "            raise TypeError(\"Неверный тип для умножения\")\n",
    "\n",
    "    __rmul__ = __mul__\n",
    "\n",
    "    def transpose(self) -> 'Matrix':\n",
    "        return Matrix(self.data.T)\n",
    "\n",
    "# Примеры использования\n",
    "m = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])\n",
    "n = Matrix([[1, 5, 9]])\n",
    "\n",
    "print('Сумма двух одинаковых матриц m равна:\\n' + str(m + m))\n",
    "print('Произведение матриц n и m равно:\\n' + str(n * m))\n",
    "print('Матрица m:\\n' + str(m) + '\\nТранспонированная матрица m:\\n' + str(m.transpose()))\n",
    "print('Произведение матрицы m на число 2 равно:\\n' + str(2 * m))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание №3\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "Создайте класс Vector наследующий все атрибуты класса Matrix, методы реализованные в классе из задания 3 предыдущей лабораторной и обладающим методом векторного произведения векторов."
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
    "import numpy as np\n",
    "\n",
    "class Matrix:\n",
    "    def __init__(self, data):\n",
    "        self.data = np.array(data)\n",
    "\n",
    "    def __str__(self):\n",
    "        result = ''\n",
    "        for row in self.data:\n",
    "            result += '\\t'.join(map(str, row)) + '\\n'\n",
    "        return result.strip()\n",
    "\n",
    "    def size(self):\n",
    "        return self.data.shape\n",
    "\n",
    "    def __add__(self, other):\n",
    "        if self.size() != other.size():\n",
    "            raise ValueError(\"Размеры матриц не совпадают\")\n",
    "        return Matrix(self.data + other.data)\n",
    "\n",
    "    def __mul__(self, other):\n",
    "        if isinstance(other, int):\n",
    "            return Matrix(self.data * other)\n",
    "        elif isinstance(other, Matrix):\n",
    "            if self.data.shape[1] != other.data.shape[0]:\n",
    "                raise ValueError(\"Матрицы нельзя умножить\")\n",
    "            return Matrix(np.dot(self.data, other.data))\n",
    "        else:\n",
    "            raise TypeError(\"Неверный тип для умножения\")\n",
    "\n",
    "    __rmul__ = __mul__\n",
    "\n",
    "    def transpose(self):\n",
    "        return Matrix(self.data.T)\n",
    "\n",
    "class Vector(Matrix):\n",
    "    def __init__(self, start_point, end_point):\n",
    "        self.start_point = start_point\n",
    "        self.end_point = end_point\n",
    "        super().__init__([end - start for start, end in zip(self.start_point, self.end_point)])\n",
    "\n",
    "    def __add__(self, other):\n",
    "        result_matrix = super().__add__(other)\n",
    "        if result_matrix is None:\n",
    "            return None\n",
    "        return Vector(self.start_point, result_matrix.data[0])\n",
    "\n",
    "    def __sub__(self, other):\n",
    "        return Vector(self.start_point, [end - diff for end, diff in zip(self.end_point, other.data[0])])\n",
    "\n",
    "    def __mul__(self, other):\n",
    "        if isinstance(other, Vector):\n",
    "            other = other.transpose()\n",
    "        result_matrix = super().__mul__(other)\n",
    "        if result_matrix.size() == (1, 1):\n",
    "            return result_matrix.data[0, 0]\n",
    "        return result_matrix.data\n",
    "\n",
    "    __rmul__ = __mul__\n",
    "\n",
    "    def length(self):\n",
    "        return np.linalg.norm(self.data[0])\n",
    "\n",
    "    def cosine(self, other):\n",
    "        return (self * other) / (self.length() * other.length())\n",
    "\n",
    "    def about(self):\n",
    "        print(f'Вектор №{id(self)}:')\n",
    "        print(f'\\tКоординаты вектора: {self.data}')\n",
    "        print(f'\\tКоординаты начальной точки: {self.start_point}')\n",
    "        print(f'\\tКоординаты конечной точки: {self.end_point}')\n",
    "        print(f'\\tДлина вектора: {self.length()}')\n",
    "\n",
    "    def cross_product(self, other):\n",
    "        if len(self.data[0]) not in {2, 3}:\n",
    "            raise ValueError(\"Вектор должен быть размерностью 2 или 3 для векторного произведения\")\n",
    "        return Vector([0, 0, 0], np.cross(self.data[0], other.data[0]))\n",
    "\n",
    "# Примеры использования\n",
    "b = Vector([1, 2, 3, 4, 5], [0, -1, -2, -3, -4])\n",
    "b.about()\n",
    "a = Vector([12, 18, 5, 63, 8], [1, -21, -53, -16, -8])\n",
    "print('Скалярное произведение:', a * b)\n",
    "print('Косинус угла:', a.cosine(b))"
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
    "# Геометрические фигуры.\n",
    "\n",
    "Измените классы из 1 задания следующим образом. \n",
    "\n",
    "Создайте класс \"Параметры\" состаящий из двух атрибутов: значения и описания этого параметра (т.е. строки). Сделайте каждый параметр созданных в задании 1 классов объектом класса \"Параметры\". \n",
    "\n",
    "Создайте библиотеку функций для вычисления площадей и периметров двумя способами:\n",
    "\n",
    "- соберите функции в класс и объявите их как статические (для вычисления параметров фигур вызывайте функции из этого класса);\n",
    "\n",
    "- соберите функции в класс с помощью композиции (т.е. создавая внутри этого класса объекты соответствующих геометрических фигур и проводя соответствующие вычисления)."
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
