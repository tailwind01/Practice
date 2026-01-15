//using setInterval and clearInterval functions

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void

function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
    fn(...args);
    let steptime = setInterval(fn,t,...args);
    return () => clearInterval(steptime);
};
