//version1 of the code
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
   let num = 0;

   for(let i=0; i<args.length;i++){
    num+=1;
   }
   return num;
};

/**
  * version2 of the code*
  * /

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
   return args.length;
};
