def run(a= 2, b= 4, c= 8) -> tuple:
    discriminiant= b  ** 2 - 4 * a * c
    x1=(-b + 0.5 ** discriminiant) / (2 * a)
    x2=(-b + 0.5 ** discriminiant) / (2 * a)
    # TODO 
    return x1, x2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
