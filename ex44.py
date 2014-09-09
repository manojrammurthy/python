class parent(object):
    
    def override(self):
        print "parent override()" 
    
    def altered(self):
        print "Parent altered()"
    
    def implicit(self):
        print "parent implicit()"
        
class child(parent):
    
    def override(self):
        print "child override()"
        
    def altered(self):
        print "child before parent altered()"
        super(child, self).override()
        print "child after parent altered()"
    
dad = parent()
son = child()

dad.altered()
son.altered()

dad.override()
son.override()

dad.implicit()
son.implicit()
