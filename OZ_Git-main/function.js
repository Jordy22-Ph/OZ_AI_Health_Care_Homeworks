// function
// 입력 값을 받아서 데이터를 처리하고, 결과를 반환하는 코드 뭉치
// -> 코드를 재사용하기 위해 만들어놓은 구조

// 함수 정의 -> "~ 기능을 하는 코드 덩어리"를 X라는 이름 부르겠다
// 입력 -> 함수 동작 -> 출력
function add(n1, n2) {
    let result = n1 + n2;
    console.log(result);
}

// 함수 호출(call) -> 함수를 사용한다
let return_value = add(1, 2);
console.log(return_value); // undefined -> 함수에서 return이 없으면 undefined 반환

// return -> 함수의 결과값을 반환하는 키워드