from mypackage import mymodule

def test_idiot():

    assert mymodule.idiot([3,8,5,2], 5) == [15,40,25,10], 'incorrect'
    assert mymodule.idiot([2,1,4,2], 4) == [8,4,16,8], 'incorrect'