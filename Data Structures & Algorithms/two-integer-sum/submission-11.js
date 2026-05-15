class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let results = [];
        for(let i = 0; i < nums.length; i++) {
            for (let k = i+1; k < nums.length; k++) {
                if (nums[i] + nums[k] === target) {
                    console.log(`i value: ${nums[i]} | k value: ${nums[k]}`);
                    results.push(i);
                    results.push(k);
                    console.log('results: ', results);
                    return results;
                }
            }
        }
    }
}
