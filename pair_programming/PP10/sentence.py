#Coder: Jiahui Tang
#Listners: Eleonora Shantsila, Aleksander Aleksiev
#Discussed if we needed to implement next

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for w in self.words:
            yield w
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

# demo
text = "hello this is a test case"
s = Sentence(text)

g = s.__iter__()
for vals in g:
    print(vals)

g = s.__iter__()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
