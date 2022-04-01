candles=[4,4,1,3]
i=0
max=0
while i<len(candles):
    if candles[i]>max:
        max=candles[i]
    i=i+1
print(max)