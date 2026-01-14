type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let modifiedArr = [init];
    
    for (let i=0; i<nums.length;i++){
        modifiedArr.push(fn(modifiedArr.at(-1), nums[i]))
    }
    
    return modifiedArr.at(-1);
};
