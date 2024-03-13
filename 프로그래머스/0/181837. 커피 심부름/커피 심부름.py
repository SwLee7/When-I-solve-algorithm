def solution(order):
    latte = sum([1 for latte in order if "latte" in latte])
    americano = sum([1 for americano in order if "americano" in americano])
    anything = sum([1 for anything in order if "anything" in anything])
    return (latte * 5000) + (americano * 4500) + (anything * 4500)