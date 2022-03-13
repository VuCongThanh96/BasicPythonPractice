print('Chương trình xuất ra bảng cửu chương')
for x in range(2, 11):
    for y in range(2, 11):
        a = x*y
        line = '{0}*{1:>2} ={2:>3}'.format(y,x,a)
        print(line, end='\t')
    print(end='\n')
