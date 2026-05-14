function findDuplicates(arr) {
    const seen = {}
    const duplicates = []
    for (let i = 0; i < arr.length i++) {
        if (seen[arr[i]]) {
            if (!duplicates.includes(arr[i])) {
                duplicates.push(arr[i])
            }
        } else {
            seen[arr[i]] = true
        }
    }
    return duplicates
}

const nums = [1, 2, 3, 2, 4, 3, 5, 1];
console.log(findDuplicates(nums));
