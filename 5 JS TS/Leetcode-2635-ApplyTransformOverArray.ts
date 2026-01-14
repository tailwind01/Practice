function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let modifiedArr: number[] = [];
    for (let x=0; x<arr.length; x++){
        modifiedArr.push(fn(arr[x],x));
    };
    return modifiedArr;
};
