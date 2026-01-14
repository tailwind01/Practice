function createHelloWorld() {
    let HelloWorld = "Hello World";
    return function(...args): string {
        return HelloWorld;
    };
};


