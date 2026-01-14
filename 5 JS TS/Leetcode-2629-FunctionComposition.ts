//version 1 of the code 
// using the reduceRight and accumulator functions
type F = (x: number) => number;

function compose(functions: F[]): F {
    
    return function(x) {
        return functions.reduceRight((acc, fn) => fn(acc), x); 
    };
};

//version 2 of the code, from basic building blocks and using for loop
//

type F = (x: number) => number;

function compose(functions: F[]): F {
    
    return function(x) {
        let ans = x;
        //because we are going to evaluate from right to left, we will reverse loop
        
        for(let i=functions.length-1; i>=0;i--){
            var functionApplied = functions[i];
            ans = functionApplied(ans);
        };

        return ans;

    };
};



