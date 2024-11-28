class Calculator:
    def __init__(self, num):
        if not(isinstance(num, int | float)):
            raise Exception("Wrong number")
        self.__num = num    
    
    @property
    def num(self):
        return f"Number is: {self.__num}"
 
 
    #######ADD
    def __add__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
            
        if isinstance(other , Calculator):
            return self.__num + other.__num
        return self.__num + other
    
    def __radd__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num + other.__num
        return self.__num + other
    
    def __iadd__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            self.__num += other.__num
            return self
        else:
            self.__num +=  other
            return self
  
  
    ############SUB
    def __sub__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num - other.__num
        return self.__num - other
    
    def __rsub__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return other.__num - self.__num
        return other - self.__num

    def __isub__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            self.__num -= other.__num
            return self
        else:
            self.__num -=  other
            return self



    ###############MUL
    def __mul__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num * other.__num
        return self.__num * other
    
    def __rmul__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num * other.__num
        return self.__num * other
    
    def __imul__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            self.__num *= other.__num
            return self
        else:
            self.__num *= other
            return self
   
   
    ##############TRUEDIV
    def __truediv__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num / other.__num
        return self.__num / other
    
    def __rtruediv__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return other.__num / self.__num
        return other / self.__num
    
    def __itruediv__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            self.__num /= other.__num
            return self
        else:
            self.__num /= other
            return self   
    
    
    
    
    
    
    
    ###################FLOORDIV
    def __floordiv__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num // other.__num
        return self.__num // other
    
    def __rfloordiv__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return other.__num // self.__num
        return other // self.__num   
    
    def __ifloordiv__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            self.__num //= other.__num
            return self
        else:
            self.__num //= other
            return self   
    
    #####################MOD
    def __mod__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num % other.__num
        return self.__num % other
    
    def __rmod__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return other.__num % self.__num
        return other % self.__num   
    
    def __ifloordiv__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            self.__num %= other.__num
            return self
        else:
            self.__num %= other
            return self   
    
    
    
    
    ##################POW
    def __pow__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return self.__num ** other.__num
        return self.__num ** other   
    
    def __rpow__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            return other.__num ** self.__num
        return other ** self.__num   

    def __ipow__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            raise Exception("Wrong number")
        if isinstance(other , Calculator):
            self.__num **= other.__num
            return self
        else:
            self.__num **= other
            return self   
    
    
###########
    def __eq__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            return Exception("Wrong number")
        if isinstance(other, Calculator):
            return self.__num == other.__num
        return self.__num == other
    
    def __lt__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            return Exception("Wrong number")
        if isinstance(other, Calculator):
            return self.__num < other.__num
        return self.__num < other
    
    def __le__(self, other):
        if not(isinstance(other, int | float | Calculator)):
            return Exception("Wrong number")
        if isinstance(other, Calculator):
            return self.__num <= other.__num
        return self.__num <= other
#########
    def __str__(self):
        return str(self.__num)
    
    def __repr__(self):
        return f"type: {type(self.__num)}, number: {self.__num}"
num1 = Calculator(5)
num2 = Calculator(6)
print(num1)
print(num1.num)
num1 -= 7 #n1 = -2
print(num1 - 2)
print(num2+num1)
print(num1, num2)
num2 **= num1
print(num1<=num2)



