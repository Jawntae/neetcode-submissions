class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = [];

        for (const s of strs) {
            const sortedWord = s.split('').sort().join('');
            if(!map[sortedWord]) {
                map[sortedWord] = [];
            }
            map[sortedWord].push(s);
            console.log(map);
        }
        return Object.values(map);
    }
}



//sort each string and use for keys in hashMap
//check to see if each sorted string matches the sorted key
// if so, append orig. string an array matching sorted key
//else, create a new empty array as the value of the key