type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void

const cancellable = (fn: Fn, args: JSONValue[], t: number): Function => {
    let called = true ; 
    setTimeout(()=>called && fn(...args),t);
    return () => called = false;
    
};
