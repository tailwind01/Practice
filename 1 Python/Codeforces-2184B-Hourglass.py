import sys

def hourglass():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    t = int(input_data[0])
    results = []
    
    for i in range(t):
        s, k, m = map(int, input_data[1+i*3 : 4+i*3])
        
        # After 1 flip: top is k (if k < s) or s (if k >= s)
        # After 2 flips: top is s
        # After 3 flips: top is min(s, k)
        # After 4 flips: top is s
        
        # This pattern is: 
        # Odd flip: top = min(s, k)
        # Even flip: top = s
        
        rem = m % k
        flips = m // k
        
        if flips == 0:
            ans = max(0, s - m)
        elif flips % 2 == 1:
            # After an odd number of flips, we start with min(s, k)
            ans = max(0, min(s, k) - rem)
        else:
            # After an even number of flips, we start with s
            ans = max(0, s - rem)
            
        results.append(str(ans))
    
    sys.stdout.write('\n'.join(results) + '\n')

hourglass()
