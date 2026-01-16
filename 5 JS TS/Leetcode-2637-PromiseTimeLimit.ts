type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    
    return async function(...args) {
        return new Promise((delayresolve, reject)=>{
            const timeOut = setTimeout(() => {
                clearTimeout(timeOut);
                reject("Time Limit Exceeded");
            }, t);

            fn(...args)
                .then((result)=> {
                    clearTimeout(timeOut);
                    delayresolve(result);
                })
                .catch((error) => {
                    clearTimeout(timeOut);
                    reject(error);
                });
        });

    };
};
