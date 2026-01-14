var createCounter = function(init){
    let count=init || 0;
    
    const increment = function(){
        count++;
        return count;
    };
    const decrement = function(){
        count--;
        return count;
    };
    const reset = function(){
        count = init;
        return count;
    };
    return {increment, decrement, reset};
}
