## event-onload

```c
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>이벤트::onload</title>
</head>

<body onload="myFunction()">
  <script>
    console.log(1);

    function myFunction() {
      console.log(2);
    }

    window.onload = function () {
      console.log(3);
    }

    window.addEventListener('load', function () {
      console.log(4);
    });

    console.log(5);
  </script>
</body>
</html>
```

---

## 실행 결과

1  
5  
Live reload enabled.  
3  
4

---

### 코드 시작

```jsx
<body onload="myFunction()">
```

- HTML 파서가 <body> 태그를 읽는 순간, 문서가 다 로드되었을 때 실행할 핸들러로 myFunction을 등록한다.
- 이 onload는 Window의 onload 프로퍼티와 같은 의미다.
    
    즉, 지금 시점에 window.onload = myFunction이 걸렸다고 생각하면 됨.
    

---

### <script> 시작

```jsx
console.log(1);
```

- 스크립트는 파싱 중간에 즉시 실행된다.
- 그래서 콘솔에 1이 바로 찍힘.

```jsx
function myFunction() {
	console.log(2)
}
```

- 함수 선언. 아직 실행은 안 함.
- 호출되면 2를 찍는 함수를 준비

```jsx
window.onload = function() {
	console.log(3);
}
```

- <body onload=”myFunction()”>로 등록해 둔 핸들러를 덮어쓴다.
    
    즉, 이제 로드 완료시 실행될 핸들러는 myFunction이 아니라 console.log(3)을 찍는 이 함수가 됨.
    
- 결과적으로 myFunction은 더 이상 onload 때 호출되지 않는다.

```jsx
window.addEventListener('load', function() {
	console.log(4);
});
```

- addEventListener는 기존 핸들러를 건들이지 않고 추가로 리스너를 붙인다.
- 로드 시점에
    - window.onload에 들어있는 함수(= 3 찍는 함수)
    - 방금 추가한 ‘load’ 리스너(= 4 찍는 함수)
    
    둘 다 순서대로 실행될 수 있다.
    

```jsx
console.log(5)
```

- 이것도 즉시 실행. 콘솔에 5가 찍힘.

---

### 로드 완료 시점

- 먼저 window.onload 프로퍼티에 들어있는 함수가 실행 → 3 출력.
- 그 다음 addEventListener(’load’, …)로 붙인 리스너가 실행 → 4 출력.
- 아까 body onload=”myFunction()”는 window.onload = …에 의해 덮였기 때문에 실행되지 않는다.

따라서 2는 출력되지 않음.