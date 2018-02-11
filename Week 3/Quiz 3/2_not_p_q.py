""" expression not (p or not q)"""

def maybe(p,q):

        return not (p or not q)

p=True
q=False
print maybe(p,q)