{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Лабораторная работа 10. Алгоритмы сортировки и поиска."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. Алгоритмы сортировки."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "ary = [0,3,5,1,2,3,5,4,2,34,43,24]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.1. Сортировка выбором\n",
    "\n",
    "Алгоритм:\n",
    "- найти наименьший элемент в неотсортированной части массива;\n",
    "- поставить его в начало;\n",
    "- сдвинуть начало неотсортированной части. \n",
    "\n",
    "Сложность: $O(n^2)$."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Программа:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def insertion_sort(arrayToSort):\n",
    "    a = arrayToSort.copy() \n",
    "    n = len(a)\n",
    "    for i in range(n):\n",
    "        v = a[i]\n",
    "        j = i\n",
    "        while (a[j-1] > v) and (j > 0):\n",
    "            a[j] = a[j-1]\n",
    "            j = j - 1\n",
    "        a[j] = v\n",
    "    return a"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Тестовый запуск:"
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
      "[0, 1, 2, 2, 3, 3, 4, 5, 5, 24, 34, 43]\n"
     ]
    }
   ],
   "source": [
    "print (insertion_sort(ary))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.2. Сортировка вставками\n",
    "\n",
    "Алгоритм:\n",
    "- из неотсортированной части берется элемент;\n",
    "- вставляется в отсортированную часть на своё мосто (в начале массива). \n",
    "\n",
    "Сложность: $O(n^2)$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def insertion_sort(arrayToSort):\n",
    "    a = arrayToSort.copy() \n",
    "    n = len(a)\n",
    "    for i in range(n):\n",
    "        v = a[i]\n",
    "        j = i\n",
    "        while (a[j-1] > v) and (j > 0):\n",
    "            a[j] = a[j-1]\n",
    "            j = j - 1\n",
    "        a[j] = v\n",
    "    return a"
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
      "[0, 1, 2, 2, 3, 3, 4, 5, 5, 24, 34, 43]\n"
     ]
    }
   ],
   "source": [
    "print (insertion_sort(ary))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.3. Сортировка методом пузырька\n",
    "\n",
    "Алгоритм:\n",
    "- последовательно сравниваются пары элементов идущих друг за другом;\n",
    "- в случае несоответствия выбранному порядку меняются местами. \n",
    "\n",
    "Сложность: $O(n^2)$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bubble_sort(arrayToSort):\n",
    "    a = arrayToSort.copy() \n",
    "    n = len(a)\n",
    "    for i in range(n,0,-1):\n",
    "        for j in range(1, i):\n",
    "            if a[j-1] > a[j]:\n",
    "                tmp = a[j-1]\n",
    "                a[j-1] = a[j]\n",
    "                a[j] = tmp\n",
    "    return a"
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
      "[0, 1, 2, 2, 3, 3, 4, 5, 5, 24, 34, 43]\n"
     ]
    }
   ],
   "source": [
    "print (bubble_sort(ary))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.4. Сортировка слиянием\n",
    "\n",
    "Алгоритм:\n",
    "- сортируемый массив разбивается на две части примерно одинакового размера;\n",
    "- каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;\n",
    "- два упорядоченных массива половинного размера соединяются в один. \n",
    "\n",
    "Сложность: $O(n^2)$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def merge_sort(arrayToSort):\n",
    "    if len(arrayToSort)>1:\n",
    "        mid = len(arrayToSort)//2\n",
    "        lefthalf = arrayToSort[:mid]\n",
    "        righthalf = arrayToSort[mid:]\n",
    "        \n",
    "        merge_sort(lefthalf)\n",
    "        merge_sort(righthalf)\n",
    "        \n",
    "        i, j, k = 0, 0, 0       \n",
    "        while i<len(lefthalf) and j<len(righthalf):\n",
    "            if lefthalf[i]<righthalf[j]:\n",
    "                arrayToSort[k]=lefthalf[i]\n",
    "                i=i+1\n",
    "            else:\n",
    "                arrayToSort[k]=righthalf[j]\n",
    "                j=j+1\n",
    "            k=k+1\n",
    "        while i<len(lefthalf):\n",
    "            arrayToSort[k]=lefthalf[i]\n",
    "            i=i+1; k=k+1\n",
    "        while j<len(righthalf):\n",
    "            arrayToSort[k]=righthalf[j]\n",
    "            j=j+1; k=k+1"
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
      "[0, 1, 2, 2, 3, 3, 4, 5, 5, 24, 34, 43]\n"
     ]
    }
   ],
   "source": [
    "alist = ary.copy() \n",
    "merge_sort(alist); \n",
    "print(alist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.5. Быстрая сортировка\n",
    "\n",
    "Алгоритм:\n",
    "- выбрать (опорным) элемент из массива;\n",
    "- перераспределить элементы в массиве так, что элементы меньше опорного помещаются перед ним, а больше или равные после;\n",
    "- применить первые два шага к подмассивам слева и справа от опорных элементов, пока в подмассивах не останется не более одного элемента. \n",
    "\n",
    "Сложность: Средняя $O(n log_2 n)$, Худшая $O(n^2)$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def quick_sort(a, l, r):\n",
    "    if (r > l):\n",
    "        v, i, j = a[r], l - 1, r\n",
    "\n",
    "        while (True):\n",
    "            i, j = i + 1, j - 1                            \n",
    "            while(a[i] < v): i = i + 1\n",
    "            while(a[j] > v): j = j - 1\n",
    "            if (i >= j): break\n",
    "            a[i], a[j] = a[j], a[i]\n",
    "            \n",
    "        a[i], a[r] = a[r], a[i]\n",
    "\n",
    "        quick_sort(a, l, i - 1)\n",
    "        quick_sort(a, i + 1, r)"
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
      "[0, 3, 5, 1, 2, 3, 5, 4, 2, 34, 43, 24]\n"
     ]
    }
   ],
   "source": [
    "alist = ary.copy() \n",
    "quick_sort(alist, 0, len(alist)-1)\n",
    "print (ary)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение 1. Сортировка подсчётом.\n",
    "\n",
    "Есть ли алгоритмы сортировки со сложностью, меньшей $O(n log_2 n)$?\n",
    "\n",
    "Да, если известны свойства ключей. Например, если число возможных вариантов значений ограничено (и невелико) можно воспользоваться сортировкой подсчётом. \n",
    "\n",
    "Алгоритм:\n",
    "- создать массив с числом эллементов равным количеству возможным вариантов ключа, заполнить его 0;\n",
    "- перебрать (пройти) сортируемое множество подсчитывая количество ключей с конкретным значением (увеличивая на 1 значения соответствующего эллемента ранее созданного массива);\n",
    "- записать подряд все ненулевые эллементы получившегося массива соответствующее его значению число раз.\n",
    "\n",
    "Сложность: $O(n+k)$, где $k$ - число вариантов ключей.\n",
    "\n",
    "Напишите программу (функцию) реализующую данный алгоритм."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<IPython.core.display.Image object>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Так можно добавлять картинки\n",
    "\n",
    "from IPython.display import Image # вызов из библиотеки определённой функции\n",
    "Image(\"Сортировка подсчётом.png\")              # вызов функции и передача ей в качестве аргумента пути к файлу \n",
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
    "# Пример. Число $\\pi$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sympy import *\n",
    "import numpy as np\n",
    "import time\n",
    "import pylab\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Выведем 7 знаков числа пи:\n",
      " 3.141593\n"
     ]
    }
   ],
   "source": [
    "# Выведем заданное колличество знаков числа pi\n",
    "npi=7;\n",
    "print('Выведем %i знаков числа пи:\\n' %npi, pi.n(npi));"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Конвертируем дробную часть числа $\\pi$ в список:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "PI = [int(i) for i in str(pi.n(npi))[2:]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Кроме того, можем считать цифры дробной части числа $\\pi$ из файла (в котором храняться 10 000 000 его символов):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open(\"pi-10million.txt\")  #  открываем файл\n",
    "fs = f.readline(npi)          #  считываем из него npi символов\n",
    "f.close()                     #  закроем файл"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1415926'"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fs"
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
      "[1, 4, 1, 5, 9, 2, 6]\n"
     ]
    }
   ],
   "source": [
    "Pi = [int(i) for i in fs]\n",
    "print(Pi)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение. Сортировка $\\pi$\n",
    "\n",
    "Сравните временную сложность всех рассмотренных алгоритмов сортировки на примере цифр числа $\\pi$.\n",
    "\n",
    "Воспользуйтесь для этого замером времени с помощью библиотеки tame. Пример:"
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
      "Отсортированные цифры числа пи: \n",
      "\n",
      " [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]\n",
      "\n",
      " Время потраченное на сортировку составило   1.0004044e-03 секунд\n"
     ]
    }
   ],
   "source": [
    "start_time = time.time()\n",
    "PI2 = insertion_sort(PI) \n",
    "Tame=time.time()-start_time\n",
    "print ('Отсортированные цифры числа пи: \\n\\n', PI2)\n",
    "print('\\n Время потраченное на сортировку составило %15.7e секунд' %(Tame))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Запишем отсортированный список в файл:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "f1 = open(\"pi_sort.txt\", 'w')\n",
    "f1.writelines('%i' % i for i in PI2)\n",
    "f1.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Проверим что получилось:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222233333333333333333333333333333333333333333333333333333333334444444444444444444444444444444444444444444444444444444444455555555555555555555555555555555555555555555555555556666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777788888888888888888888888888888888888888888888888888888888999999999999999999999999999999999999999999999999999999999']\n"
     ]
    }
   ],
   "source": [
    "f1 = open(\"pi_sort.txt\", 'r')\n",
    "fs = f1.readlines()          #  считываем всё содержимое файла\n",
    "print(fs)\n",
    "f1.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Посмотрим как меняются затраты времени на сортировку вставками при увеличении числа сортируемых объектов:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "ik = 11\n",
    "Tame = np.zeros(ik)\n",
    "NPI = [(i+1)*50 for i in range(ik)]\n",
    "i=0\n",
    "for npi in NPI:\n",
    "    PI = [int(i) for i in str(pi.n(npi))[2:]]\n",
    "    start_time = time.time()\n",
    "    PI2 = insertion_sort(PI) \n",
    "    Tame[i]=time.time()-start_time\n",
    "    i+=1"
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
      "\t size\t Tame(sec)\n",
      "\t 50 \t 0.000e+00\n",
      "\t 100 \t 0.000e+00\n",
      "\t 150 \t 9.911e-04\n",
      "\t 200 \t 3.010e-03\n",
      "\t 250 \t 3.973e-03\n",
      "\t 300 \t 4.997e-03\n",
      "\t 350 \t 7.995e-03\n",
      "\t 400 \t 9.996e-03\n",
      "\t 450 \t 1.401e-02\n",
      "\t 500 \t 1.695e-02\n",
      "\t 550 \t 2.001e-02\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print('\\t size\\t Tame(sec)')\n",
    "for i in range(0,ik):\n",
    "    print ('\\t %i \\t %.3e' %(NPI[i], Tame[i]))\n",
    "\n",
    "# график функции\n",
    "pylab.figure ()\n",
    "plt.plot(NPI, Tame, c='b')\n",
    "plt.scatter(NPI, Tame, c='b',s=50)\n",
    "# параметры графика\n",
    "xl = plt.xlabel(\"size\");\n",
    "yl = plt.ylabel(\"tame (sec)\");\n",
    "plt.grid(True);\n",
    "plt.show();"
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
    "# Пример. Последовательный поиск"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "def dummy_search (a, key):\n",
    "    n = len(a)\n",
    "    for i in range(n):\n",
    "        if a[i] == key:\n",
    "            return i\n",
    "    return n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "ary = [7,8,1,2,3,4,13,5,1,2,44,5,1]\n",
    "print(dummy_search (ary, 13))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# вероятно чуть более рациональная реализация\n",
    "def clever_search (a, key):\n",
    "    n = len(a)\n",
    "    i=0\n",
    "    while a[i]!=key:\n",
    "        i=i+1\n",
    "    return i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "ary2 = [7,8,1,2,3,4,13,5,1,2,44,5,1,44]\n",
    "print(clever_search (ary2, 13))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.22 µs ± 16.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)\n",
      "1.12 µs ± 12.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%timeit dummy_search (ary, 44)\n",
    "    \n",
    "%timeit clever_search (ary2, 44)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Упражнение. Поиск в $\\pi$\n",
    "\n",
    "Найдите в дробной части числа $\\pi$ порядковый номер каждой цифры начиная с 1 встретившейся количество раз равное её значению (первую единицу, вторую двойку и т.д.)"
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
    "Найдите в числе $\\pi$ номер цифры в дробной части после которой идёт последовательность из:\n",
    "\n",
    "- шести 9;\n",
    "- шесть 8;\n",
    "- шесть 0;\n",
    "- первых шести цифр;\n",
    "- семь цифр вашего номера телефона."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_sequence(pi_digits, sequence):\n",
    "    \"\"\"Find the first occurrence of a sequence in the pi_digits.\"\"\"\n",
    "    seq_len = len(sequence)\n",
    "    for i in range(len(pi_digits) - seq_len + 1):\n",
    "        if pi_digits[i:i + seq_len] == sequence:\n",
    "            return (i, i + seq_len - 1)\n",
    "    return None\n",
    "\n",
    "def main():\n",
    "    with open(\"pi-10million.txt\") as f:\n",
    "        pi_digits = f.readline().strip()\n",
    "    \n",
    "    sequences_to_find = {\n",
    "        'six 9s': '999999',\n",
    "        'six 8s': '888888',\n",
    "        'six 0s': '000000',\n",
    "        '141592': '141592',\n",
    "        '8993927': '8993927'\n",
    "    }\n",
    "    \n",
    "    for name, seq in sequences_to_find.items():\n",
    "        result = find_sequence(pi_digits, seq)\n",
    "        if result:\n",
    "            print(f\"The sequence '{seq}' ({name}) was found at positions {result}\")\n",
    "        else:\n",
    "            print(f\"The sequence '{seq}' ({name}) was not found in the first 10 million digits of pi.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 2. Поиск в отсортированном массиве\n",
    "\n",
    "Реализуйте алгоритмы сужения области:\n",
    "\n",
    "- бинарный поиск (https://ru.wikipedia.org/wiki/%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA)\n",
    "- метод золотого сечения (https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%B7%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%B3%D0%BE_%D1%81%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)\n",
    "- интерполирующий поиск (https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D1%8F%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA)\n",
    "\n",
    "(см. лекцию 3 с. 17)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from timeit import default_timer\n",
    "\n",
    "def read_pi_digits(filename):\n",
    "    \"\"\"Чтение первых 100 символов из файла с числом Пи.\"\"\"\n",
    "    with open(filename) as f:\n",
    "        return f.read(100)\n",
    "\n",
    "def binary_search(numbers, target):\n",
    "    \"\"\"Бинарный поиск в отсортированном массиве.\"\"\"\n",
    "    left = 0\n",
    "    right = len(numbers) - 1\n",
    "\n",
    "    while left <= right:\n",
    "        mid = (left + right) // 2\n",
    "        if numbers[mid] == target:\n",
    "            return mid\n",
    "        elif numbers[mid] < target:\n",
    "            left = mid + 1\n",
    "        else:\n",
    "            right = mid - 1\n",
    "    return None\n",
    "\n",
    "def golden_section_search(numbers, key):\n",
    "    \"\"\"Метод золотого сечения.\"\"\"\n",
    "    phi = (1 + 5 ** 0.5) / 2\n",
    "    a = 0\n",
    "    b = len(numbers) - 1\n",
    "\n",
    "    while b - a >= 1:\n",
    "        x1 = int(b - (b - a) / phi)\n",
    "        x2 = int(a + (b - a) / phi)\n",
    "        A = numbers[a:x2 + 1]\n",
    "        B = numbers[x1:b + 1]\n",
    "\n",
    "        if key in A:\n",
    "            b = x2\n",
    "        elif key in B:\n",
    "            a = x1\n",
    "        else:\n",
    "            return None\n",
    "    return a\n",
    "\n",
    "def interpolating_search(arr, x):\n",
    "    \"\"\"\n",
    "    Интерполяционный поиск элемента в отсортированном массиве.\n",
    "\n",
    "    :param arr: Отсортированный массив.\n",
    "    :param x: Искомое число.\n",
    "    :return: Индекс искомого числа в массиве, или None, если число не найдено.\n",
    "    \"\"\"\n",
    "    l = 0\n",
    "    u = len(arr) - 1\n",
    "\n",
    "    while l <= u:\n",
    "        i = l + ((u - l) * (x - arr[l]) // (arr[u] - arr[l]))\n",
    "\n",
    "        if x == arr[i]:\n",
    "            return i\n",
    "        elif x < arr[i]:\n",
    "            u = i - 1\n",
    "        else:\n",
    "            l = i + 1\n",
    "\n",
    "# Чтение первых 100 символов числа Пи\n",
    "fs = read_pi_digits(\"pi-10million.txt\")\n",
    "\n",
    "# Создание отсортированного массива для поиска\n",
    "LS = sorted([int(i) for i in range(1, 10000000)])\n",
    "\n",
    "# Поиск с использованием бинарного поиска\n",
    "t = default_timer()\n",
    "print(binary_search(LS, 9999999))\n",
    "print(\"Время выполнения бинарного поиска: {:.10f}\".format(default_timer() - t))\n",
    "\n",
    "# Поиск с использованием метода золотого сечения\n",
    "t = default_timer()\n",
    "print(golden_section_search(LS, 9999999))\n",
    "print(\"Время выполнения метода золотого сечения: {:.10f}\".format(default_timer() - t))\n",
    "\n",
    "# Поиск с использованием интерполяционного поиска\n",
    "t = default_timer()\n",
    "print(interpolating_search(LS, 9999999))\n",
    "print(\"Время выполнения интерполяционного поиска: {:.10f}\".format(default_timer() - t))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 3.\n",
    "\n",
    "Сравните производительность алгоритмов из задания 2 на задании 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from timeit import default_timer\n",
    "\n",
    "def binary_search(numbers, num):\n",
    "    left = 0\n",
    "    right = len(numbers) - 1\n",
    "    while left <= right:\n",
    "        mid = (left + right) // 2\n",
    "        if num == numbers[mid]:\n",
    "            return mid\n",
    "        elif num < numbers[mid]:\n",
    "            right = mid - 1\n",
    "        else:\n",
    "            left = mid + 1\n",
    "    return -1  # Возвращаем -1, если число не найдено\n",
    "\n",
    "def golden_cut_search(arr, key):\n",
    "    phi = 0.5*(1 + 5 ** 0.5)\n",
    "    a = 0\n",
    "    b = len(arr) - 1\n",
    "    while b - a >= 1:\n",
    "        x1 = int(b - (b - a)/phi)\n",
    "        x2 = int(a + (b - a)/phi)\n",
    "        if arr[x1] == key:\n",
    "            return x1\n",
    "        elif arr[x2] == key:\n",
    "            return x2\n",
    "        elif key < arr[x1]:\n",
    "            b = x1\n",
    "        elif key > arr[x2]:\n",
    "            a = x2\n",
    "        else:\n",
    "            a = x1\n",
    "            b = x2\n",
    "    return -1  # Возвращаем -1, если число не найдено\n",
    "\n",
    "def interpolating_search(arr, x):\n",
    "    l = 0\n",
    "    u = len(arr) - 1\n",
    "\n",
    "    while l <= u and arr[l] <= x <= arr[u]:\n",
    "        i = l + ((u - l) * (x - arr[l]) // (arr[u] - arr[l]))\n",
    "\n",
    "        if x == arr[i]:\n",
    "            return i\n",
    "        elif x < arr[i]:\n",
    "            u = i - 1\n",
    "        else:\n",
    "            l = i + 1\n",
    "    return -1  # Возвращаем -1, если число не найдено\n",
    "\n",
    "# Загружаем данные из файла\n",
    "with open(\"pi-10million.txt\", \"r\") as f:\n",
    "    numbers = sorted(map(int, f.readline().split()))\n",
    "\n",
    "print('=====Бинарный поиск=====')\n",
    "t = default_timer()\n",
    "print(binary_search(numbers, 9999999))\n",
    "print('{:.10f}'.format(default_timer() - t))\n",
    "\n",
    "print('=====Поиск по золотому сечению=====')\n",
    "t = default_timer()\n",
    "print(golden_cut_search(numbers, 9999999))\n",
    "print('{:.10f}'.format(default_timer() - t))\n",
    "\n",
    "print('=====Интерполирующий поиск=====')\n",
    "t = default_timer()\n",
    "print(interpolating_search(numbers, 9999999))\n",
    "print('{:.10f}'.format(default_timer() - t))"
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
    "# Задание \"Пирамидальная сортировка\"\n",
    "\n",
    "Напишите программу (функцию) реализующую алгоритм пирамидальной сортировки (https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%80%D0%B0%D0%BC%D0%B8%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0,\n",
    "https://habr.com/ru/post/221095/,\n",
    "Алгоритмы. Справочник с примерами на C, C , Java и Python (Хайнеман Дж., и др - 2017) с. 87)."
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
    "# Задание \"Малые тела\"\n",
    "\n",
    "Есть база данных малых тел солнечной системы созданная под эгидой Международного астрономического союза. Файл с этой базой можно скачать здесь https://www.minorplanetcenter.net/iau/MPCORB/MPCORB.DAT, а здесь приведено его описание https://www.minorplanetcenter.net/iau/info/MPOrbitFormat.html\n",
    "\n",
    "Отсортируйте эту базу по названию малого тела. Напишите две программы реализующие поиск в отсортированном и неотсартированном массивах. В последнем случае поиск может производиться по любому параметру из таблицы."
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
