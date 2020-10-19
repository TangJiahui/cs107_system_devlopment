# Group Members
# Jiahui Tang
# Benjamin Liu
# Aleksander Aleksiev
# Xiaohan Yang

# class
class ForwardMode():
    def __init__(self, x):
        self.x = x

    def __pow__(self,r):
        return [self.x**r, r*self.x**(r-1)]

# demo
if __name__ == "__main__":
    x = 3
    r = 4
    fwd = ForwardMode(x)
    print("The value and the derivative of the function at this point is %s"%(fwd**r))
    