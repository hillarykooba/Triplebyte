'''
Regular expressions are a concise way to express pattern matching over strings. The correct answer above matches strings that have exactly three "b"s. We won't go into the details of regular expression syntax here, but you can look that up online. Interestingly, regular expressions come from theoretical computer science (they are equivalent to finite state automata). And implementing a regular expression engine involves simulating a finite state automaton! They didn't become popular with programmers until 1968, when Ken Thompson used regular expressions as a pattern matching syntax in the QED editor.
'''

Which of the following regular expressions will match blabber but not babel?

Select the correct answer:

^(b?b?)+$


^b[l].*e$


^b(a|l)+b+e.$


^([^b]*b[^b]*){3}$

# Answer: ^([^b]*b[^b]*){3}$
