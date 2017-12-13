
# coding: utf-8

# In[ ]:


"""currency.py:The currency exchange.

_author_="Lvjiawen"
_pkuid_="1600012173"
_email_="1600012173@pku.edu.cn"
"""


"""module A:severed as a tool to gain the string at a specific location.
   it contains three functions that help you finish the problems.
"""


def after_space(s):
    """gain the information in the string before space"""
    s = s.split()
    s = s[1]
    return s


def before_space(s):
    """gain the information in the string after space"""
    s = s.split()
    s = s[0]
    return s


def first_inside_quote(s):
    """the first string within quotation marks"""
    s = s.split('"')
    return(s[1])


"""module B:gain the specific string from url,it contains
   three function to
"""


def get_from(s):
    """the string after "from
    """
    s = s.split('"')
    return(s[3])


def get_to(s):
    """ the string after "from
    """
    s = s.split('"')
    return(s[7])


def has_error(s):
    """Judge whether the information contains errors
    """
    s = s.split('"')
    return s[13]


"""module C:return the string obtained after visiting the url
"""


def curenccy(currency_from, currency_to, amount_from):
    """gain the information from url
    """
    from urllib.request import urlopen

    doc = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%f" % (currency_from, currency_to, float(amount_from))
    doc = urlopen(doc)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return (jstr)


"""module D:the main function
"""


def exchange(a, b, c):
    """the main function to gain the amount of currency_to money
    """
    s = curenccy(a, b, c)
    s = get_to(s)
    num = float(before_space(s))
    return num


"""module test:the important part in the Assign2,guarantee
   the function can work normally
"""


def test_A():
    """judge whether amount of money is float
    """
    assert(amount_from.isdigit())


def test_B():
    """determine whether the str of url can be obtained correctly
    """
    s = curenccy(currency_from, currency_to, amount_from)
    assert(has_error(s)=="")
    assert(first_inside_quote(s) == "from")
    assert(get_from != "")
    assert(get_to != "")


def test_C():
    """determine whether the information is successfully gained
    """
    assert(has_error(curenccy(currency_from, currency_to, amount_from)) == "")


def test_all():
    """the funcyion that determines whether all test can work
    """
    test_A()
    test_B()
    test_C()

    print("All tests passed!")


"""input the necessary datas
"""


currency_from = input()
currency_to = input()
amount_from = input()


"""test the feasibility of all the functions and get the result
"""


if __name__ == '__main__':

    test_all()
    print(exchange(currency_from, currency_to, amount_from))
