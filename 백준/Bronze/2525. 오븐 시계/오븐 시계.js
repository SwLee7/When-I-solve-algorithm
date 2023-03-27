const solution = (input) => {
    const [a, b, c] = input.split(/\s+/).map((s) => +s);

    const sum = b + c;
    const carry = parseInt(sum / 60);

    const m = sum % 60;
    const h = (carry > 0 ? a + carry : a) % 24;
    return `${h} ${m}`;
};
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

