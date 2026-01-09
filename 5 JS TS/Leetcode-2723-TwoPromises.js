/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {

   const p1 = await(promise1);
   const p2 = await(promise2);

   return p1+p2;    
};
