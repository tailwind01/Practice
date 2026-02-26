func stableMountains(height []int, threshold int) []int {
    var ans []int;
    for i:=1;i<len(height);i++ {
        if height[i-1]>threshold {ans = append(ans,i)}
    }
    return ans
}
