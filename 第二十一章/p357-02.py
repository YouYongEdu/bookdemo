#coding=utf-8
class Foo(object):
     def get_bar(self):
         print("getter...")
         return 'laowang'

     def set_bar(self, value):
         #"""必须两个参数"""

         print("setter...")
         return 'set value' + value

     def del_bar(self):
         print("deleter...")

         return 'laowang'
     BAR = property(get_bar, set_bar, del_bar, "description...")


obj = Foo()
obj.BAR  # ⾃动调⽤第⼀个参数中定义的⽅法：get_bar
obj.BAR = "alex"  # ⾃动调⽤第⼆个参数中定义的⽅法：set_bar⽅法，并将“alex”当作参数传⼊
desc = Foo.BAR.__doc__  # ⾃动获取第四个参数中设置的值：description...
print(desc)
del obj.BAR  # ⾃动调⽤第三个参数中定义的⽅法：del_bar⽅法