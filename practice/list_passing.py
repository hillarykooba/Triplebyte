'''In Python, like in Java, Javascript, and many other popular languages, objects are passed to functions by reference. This means that when a list is passed as a parameter to a function, the parameter still refers to the original list (and any modification to the list will be visible outside the function). Thus, inside the function "modify", elems.append("foo") adds "foo" to the list in the outer scope. However, variable assignment (elems = ["bar", "baz"]) simply points the local reference elems to a new object, and has no impact on the outer list.'''

def modify(elems):
    elems.append("foo")
    elems = ["bar", "baz"]

array = ["qux"]
modify(array)
print array

#Output ["qux", "fox"]
