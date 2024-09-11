/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var n = arr.length, temp = 0;
    nums = [];
    for(var i = 0; i < n; i++){
        if(fn(arr[i], i)){
            nums[temp++] = arr[i];
        }
    }
    return nums;
};