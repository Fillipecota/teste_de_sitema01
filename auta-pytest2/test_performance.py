import time
from my_code import long_running_function

def test_long_performe():
    start_time = time.time()
    long_running_function()
    end_time = time.time()
    durantion = end_time - start_time
    assert durantion < 6 ,f"a função demorou{durantion}, mas que o esperado"
