class ArrayWrapper {
    constructor(nums: number[]) {
        (this as any).nums = nums;
    }
    valueOf(): number {
        return (this as any).nums.reduce((acc,num) => acc+num,0);
    }
    toString(): string {
        return '['+(this as any).nums.join(',')+']';
    }
};

class ArrayWrapper {
    private nums: number[];
    constructor(nums: number[]) {
        this.nums = nums;
    }
    valueOf(): number {
        return this.nums.reduce((acc,num) => acc+num,0);
    }
    toString(): string {
        return '['+this.nums.join(',')+']';
    }
};
