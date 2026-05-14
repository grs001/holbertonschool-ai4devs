function calculateAverage(numbers) {
    if (numbers.length === 0) {
        return 0;
    }
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total / numbers.length;
}

function formatScore(numbers) {
    const avg = calculateAverage(numbers);
    return `Average score: ${avg.toFixed(2)}%`;
}

const scores = [85, 90, 78, 92, 88];
console.log(formatScore(scores));
console.log(formatScore([]));
