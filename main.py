
class Stack:

    def __init__(self):
        self.len = 0
        self.top = None
        pass

    def is_empty(self):
        '''is_empty - проверка стека на пустоту.Метод возвращает True или False.'''
        return self.len == 0

    def pop(self):
        ''' '''
        if self.len > 0:
            self.len -= 1
            top, element = self.top
            self.top = top
            return element

    def push(self, element):
        self.len += 1
        self.top = (self.top, element)

    def peek(self):
        ''' '''
        return self.top[1]

    def size(self):
        ''' '''
        return self.len

    def __len__(self):
        ''' '''
        return self.len

def test_stack():
    s = Stack()
    assert s.is_empty() == True
    assert s.size() == 0
    assert len(s) == 0
    a = [1, 2, 3, 4]
    for i in a:
        s.push(i)
        assert s.peek() == i

    assert len(s) == 4
    assert s.size() == 4
    assert s.is_empty() == False
    assert s.peek() == 4

    for i in [4, 3, 2, 1]:
        assert s.peek() == i
        assert s.pop() == i

    assert s.is_empty() == True
    assert s.size() == 0
    assert len(s) == 0

def parentheses(string):
    dict_parentheses = {'{': '}', '(': ')', '[': ']'}
    s = Stack()
    for c in string:
        if c in dict_parentheses:
            s.push(c)
        elif c in '})]':
            if s.is_empty():
                return False
            elif dict_parentheses[s.pop()] != c:
                return False
    if s.is_empty():
        return True
    else:
        return False

def test_parentheses():
    balance = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[(a)]}}']
    not_balance = ['}{}', '{{[(])]}}', '[[{())}]', '([ )]', ')))', '({[', '[']
    assert all(parentheses(i) for i in balance)
    assert all(not parentheses(i) for i in not_balance)


if __name__ == '__main__':
    test_stack()
    test_parentheses()