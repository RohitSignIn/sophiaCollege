var numRabbits = function (answers) {
  let freqMap = {};
  for (let answer of answers) {
    if (!freqMap[answer]) freqMap[answer] = 0;
    freqMap[answer]++;
  }
  let ans = 0;
  for (let [x, n] of Object.entries(freqMap)) {
    // console.log(x, n);
    x++;
    ans += Math.ceil(n / x) * x;
  }
  return ans;
};

console.log(numRabbits([1, 1, 2]));
