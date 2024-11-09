def remainder_divsion (a,b):
    if b==0:
        raise Exception('Zero cannot be used for division')
    result = a//b
    remainder = a%b
    print(a,'/', b , 'is' , result,'remainder', remainder)

#Main Program
remainder_divsion(10,5)