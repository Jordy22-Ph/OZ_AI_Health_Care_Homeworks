const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(prompt) {
  return new Promise(resolve => rl.question(prompt, resolve));
}

async function calculator() {
  console.log('=== 콘솔 계산기 ===');

  const num1 = parseFloat(await question('첫 번째 숫자를 입력하세요: '));
  const operator = await question('연산자를 입력하세요 (+, -, *, /): ');
  const num2 = parseFloat(await question('두 번째 숫자를 입력하세요: '));

  let result;

  // 조건문으로 연산자 처리
  if (operator === '+') {
    result = num1 + num2;
  } else if (operator === '-') {
    result = num1 - num2;
  } else if (operator === '*') {
    result = num1 * num2;
  } else if (operator === '/') {
    if (num2 === 0) {
      console.log('❌ 0으로 나눌 수 없습니다!');
      rl.close();
      return;
    }
    result = num1 / num2;
  } else {
    console.log('❌ 유효하지 않은 연산자입니다!');
    rl.close();
    return;
  }

  console.log(`\n✅ 결과: ${num1} ${operator} ${num2} = ${result}`);
  rl.close();
}

calculator();