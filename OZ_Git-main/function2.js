// 함수를 값처럼 다루기   1) 함수를 변수에 할당할 수 있다.  2) 함수를 다른 함수의 인자로 할당할 수 있다.

function sayHello() {                      // | 함수 정의 (line4~6) 
    console.log("Hello");
};

// 함수 호출  
// sayHello();                             // | 터미널 출력 >> Hello 

// 함수 
// sayHello

// console.log(sayHello);                  // | 터미널 출력 >> [Function: sayHello] 


// 함수
// const f = sayHello;
// console.log(f);                         // | 터미널 출력 >> [Function: sayHello] 

// 함수
// const f = sayHello;
// f();                                    // | 터미널 출력 >> Hello


// 1) 함수를 변수에 할당할 수 있다.
// const f = sayHello;

// 2) 함수를 다른 함수의 인자로 할당할 수 있다.
// function run(fn) {
//     fn();
// }

// run(sayHello);                         // | 터미널 출력 >> Hello

// function run(fn) {
//     console.log("start function run...")
//     fn();
//     console.log("end function run...")
// }

// run(sayHello);                           // | 터미널 출력 >> start function run...
                                         //               Hello
                                         //               end function run...          

                                        
// (기본) 함수를 선언한 곳에서 직접 호출                        |  < 함수 사용하는 기본적인 방법
// (응용) 함수를 선언한 곳과 호출하는 곳이 달라질 수 있다.          


// ** 주의 run(sayHello())  할 경우    >> TypeError: fn is not a function 
// **       = undefined(); 와 마찬가지! 
function sayHello() {
    console.log("Hello");
};

const f = sayHello;

function run(fn) {
    console.log("start function run...")
    fn();
    console.log("end function run...")
}

run(sayHello());

// | 터미널 출력 >> ====================
// Hello
// start function run...
// /Users/admin/Desktop/oz_/0402/02_2_function2.js:60
//     fn();
//     ^
// TypeError: fn is not a function
// ====================================

// function sayHello() {
//     console.log("Hello");
// };

// const f = sayHello;

// function run(fn) {
//     console.log("start function run...")
//     fn();
//     console.log("end function run...")
//}
// undefined(); 

// | 터미널 출력 >>   위와 동일! ==========
// Hello
// start function run...
// /Users/admin/Desktop/oz_/0402/02_2_function2.js:60
//     fn();
//     ^
// TypeError: fn is not a function
// ====================================
