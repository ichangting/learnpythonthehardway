# 打印一个心形
# for 循环可以在语句内使用
print('\n'.join([''.join([('ChinaLove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
