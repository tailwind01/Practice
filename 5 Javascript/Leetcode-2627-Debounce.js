/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeID;
    return function(...args) {
        if (timeID) {
            clearTimeout(timeID);
        }

        timeID = setTimeout(() =>{
            fn(...args);

        }, t); 
    }
};
