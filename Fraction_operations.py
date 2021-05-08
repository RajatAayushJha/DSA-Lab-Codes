class Fraction:

    def __init__(self,num,den):
        self.numerator=num
        self.denominator=den
        

    def inverse(self):
        """Returns the inverse of this Fraction"""
        newNum=self.denominator
        newDen=self.numerator
        
        return Fraction(newNum,newDen)

    def add(self,f):
        """Adds the Fraction f to this Fraction and returns the result"""
        newNum=(self.denominator*f.numerator)+(self.numerator*f.denominator)
        newDen=self.denominator*f.denominator
        return Fraction(newNum,newDen)

    def subtract(self,f):
        """Subtracts the Fraction f from this Fraction and returns the result"""
        newNum=self.numerator*f.denominator-self.denominator*f.numerator
        newDen=self.denominator*f.denominator
        return Fraction(newNum,newDen)

    def multiply(self,f):
        """Multiplies the Fraction f to this Fraction and returns the result"""
        newNum=self.numerator*f.numerator
        newDen=self.denominator*f.denominator
        return Fraction(newNum,newDen)

    def divide(self,f):
        """Divides the Fraction f from this Fraction and returns the result"""
        newNum=self.numerator*f.denominator
        newDen=self.denominator*f.denominator
        return Fraction(newNum,newDen)

    def __str__(self):
        """Returns a string representation of this fraction"""
        
        return str(self.numerator)+'/'+str (self.denominator)

def main():
    f1 = Fraction(2,3)
    print('Fraction 1 is', f1)
    f2 = Fraction(3,4)
    print('Fraction 2 is', f2)
    print('The inverse of f1 is', f1.inverse())
    print('The inverse of f2 is', f2.inverse())
    print('f1+f2 is', f1.add(f2))
    print('f1-f2 is', f1.subtract(f2))
    print('f1 * f2 is', f1.multiply(f2))
    print('f1 / f2 is', f1.divide(f2))

if __name__ == '__main__':
    main()
