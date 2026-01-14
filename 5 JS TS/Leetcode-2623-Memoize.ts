type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    
    const memory = new Map();

    return function(...args) {
        let sieve = JSON.stringify(args);

        if(memory.has(sieve)){
            return memory.get(sieve);
        }
        else{
            let result = fn(...args);
            memory.set(sieve, result);
            return result;
        }
        
    }
}
