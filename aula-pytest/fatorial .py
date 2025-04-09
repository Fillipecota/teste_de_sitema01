def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


# ------------------------------------------------------


def fatorial(factor):
  
    aux= factor
    total=factor
    while aux > 1:
        total*= aux-1
        aux -= 1

    return total

