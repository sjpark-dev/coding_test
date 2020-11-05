def depth_first_search(x):
    if x > 7:
        return
    else:
        print(x, end=' ')
        depth_first_search(x*2)
        depth_first_search(x*2+1)


if __name__ == '__main__':
    depth_first_search(1)
