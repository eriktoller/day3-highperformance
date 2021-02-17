# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:41:37 2021

@author: erito849
"""

from MyModule import MyClasses as mc

me = mc.Person('Erik','Toller')

me.printname()

me = mc.Student('Erik','Toller', 'Hydrology')

me.printname()

teacher = mc.Teacher('Kim','Classon', 'Python programing')

teacher.printname()