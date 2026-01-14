type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
    let called = 0;
    let ans;

    return function (...args) {
        if(called==0){
            ans = fn(...args);
            called = 1;
            return ans;
        }
        else{
            return undefined;
        }
    };
}
