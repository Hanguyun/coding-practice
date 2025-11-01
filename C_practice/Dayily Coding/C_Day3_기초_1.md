## 0. C 프로그램의 순서

**입력 → 처리(계산) → 출력 → 저장(메모리)**

- **입력** : scanf
- **처리** : 변수에 담아 연산 / 함수 호출
- **출력** : printf
- **저장** : 메모리(바이트들의 줄) + 주소 + “이름표(변수)”

---

## 1. 입력과 출력

### scanf/fscanf (입력)

- scanf : 키보드에서 데이터를 읽어옴.
- fscanf : 파일에서 데이터를 읽어옴. (앞에 f가 붙으면 파일 관련)

### printf (출력)

- **서식 지정자 (%)**
    - %d : 정수(int)
    - %ld : long(윈도우는 보통 4byte, 리눅스/맥은 8byte)
    - %f : 실수(double까지도 %f로 출력 가능)
    - %c : 문자(char)
    - %s : answkduf
    - %zu : 크기 출력 (sizeof 결과 타입이 size_t라서)
- **제어 문자**
    - \n 줄바꿈, \t 들여쓰기, \a 삑 소리

---

## 2. 메모리/변수/형변환(정보 손실)

- 메모리는 바이트 블록이고, 각 바이트에 주소가 있다.
- 주소를 못 외우니까 “변수 이름”을 붙여서 사용
- 형변환
    - 확대 변환(정보 비손실) : int → float/double 등
    - 축소 변환(정보 손실) : double → int (소수점 버림)

**ex)**

```c
int i = 3.14;  // i == 3 (소수점 잘림, 경고 나오는 게 정상)
float k = 3;  // k == 3.0 (정수가 실수로 안전하게 변환)
```

---

## 3.  제어문

- 조건문 : if, switch
- 반복문 : for, while

for 예시)

```c
for (int i = 1; i <= n; i++) {
// i를 1씩 증가시키며 n까지 반
}
```

---

## 4. 프로그램 시작점 & 헤더

- 시작은 무조건 main().
- #include <stdio.h> : printf, scanf를 쓰려면 필수
- #include <string.h> : strlen 처럼 문자열 함수 쓸 때 필요.

---

## 5. 자료형 크기와 플랫폼 차이

> 64비트 기준이라도 운영체제/컴파일러에 따라 long 크기가 다름.
> 

| **OS/모델**                | **short** | **int** | **long** | **long long** | **float** | **double** |
| ---                       | ---       | ---      | ---     |           --- | ---        |        --- |
| **Windows(LLP64)**        | 2         | 4        | 4       | 8             | 4          | 8          |
| **Linux/macOS(LP64)**     | 2         | 4        | 8       | 8             | 4          | 8          |

---

## 6. 문자열 : sizeof / strlen

- 문자열 리터럴 “abcd”는 끝에 \0(널 문자)가 자동으로 붙여짐.
- sizeof(”abcd”) → 5 (a b c d \0)
- strlen(”abcd”) → 4 (문자 개수)
- 한글(UTF-8)은 보통 글자당 3byte라서 sizeof(”대한민국”)은 13, strlen(”대한민국”)은 12.

필수 헤더 : #include <string.h>

---

## 7. 정수 나눗셈과 실수 나눗셈

```c
printf("%d\n", 10/3);   // 3 (정수/정수 = 정수)
printf("%f\n", (float)10/3);  // 3.333333 (실수 포함)
```

주의 (괄호 차이)

```c
(float)10/3   // 10을 먼저 float로 -> 10.0/3 -> 3.333333
(float)(10/3)   // 10/3 먼저 계산(정수) -> 3 -> 3을 float로 -> 3.000000
```

---

## 8. 문자와 ASCII(코드표)

- 문자도 숫자로 저장
- ‘A’ == 65, ‘a’ == 97
- ‘a’ + 2 == ‘c’

```c
int i = 65;
char c = 'a';
printf("%c....%c....%c\n", i, c, c+2); // A....a....c
```

결과를 숫자로 확인하고 싶다면

```c
printf("%d %d %d\n", i, c, c+2); // 65 97 99
```

---

## 9. 리터럴(진법) 표기법

- 10진수 : int i = 10;
- 16진수 : int i = 0xA;
- 8진수 : int i = 032; (앞의 0이 8진수라서 032 == 26(10진수))
- 2진수 : 표준 C는 0b1010을 공식 지원하지 않음

(GCC/Clang 확장으로 되는 경우도 있지만, 수업/온라인 저지에서 보통 비권장)

---

## 10. 부호(signed)와 무부호(unsigned)

- signed : 음수/양수 모두
- unsigned : 0 이상의 자연수만, 표현 범위가 2배
    - 8비트 기준
        - signed char : -128 ~ 127
        - unsigned char : 0 ~ 255

signed와 unsigned를 섞어 비교/연산하면 의도치 않은 결과가 도출할 수 있다.

---

## 11. 이진수와 2의 보수 개념

4bit 예시(실제는 8, 16, 32, 64bit)

```c
0111 = 7
1000 = -8
1111 = -1
```

맨 앞 bit가 1이면 보통 음수로 해석된다. (2의 보수)

---

## 12. 코드 실습

### 12-1) “한구윤” 출력

```c
#include <stdio.h>

int main(void) {
		printf("한구윤"); // 화면에 글자 그대로 출력
		return 0;   // 정상 종료
}
```

### 12-2) 1부터 n까지 합

```c
#include <stdio.h>

// 1부터 n까지의 합을 계산하는 함수
int sumToN(int n) {
		int hap = 0;
		for (int i = 1; i <= n; i++ {
		hap += i;
		}
		return hap; // 계산 결과 반환
}

int main(void) {
		int n;
		scanf("%d", &n);   // 키보드에서 정수 1개 입력
		int result = sumToN(n);   // 함수 홀출해 합 구함
		printf("1~%d 사이의 합계: %d\n", n, result);
		return 0;
}
```

## 12-3) 자료형 크기 출력

> sizeof 결과는 size_t이므로 %zu를 사용
> 

```c
#include <stdio.h>

int main(void) {
		printf("%zu...%zu\n", sizeof(short), sizeof(int));
		printf("%zu...%zu...%zu\n", sizeof(short), sizeof(int), sizeof(long));
		printf("%zu...%zu...%zu\n", sizeof(float), sizeof(double), sizeof(char));
		return 0;
}
```

## 12-4) 문자열 : sizeof / strlen

> strlen 쓰려면 #include <string.h> 필요
> 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    printf("%s...%zu...%zu\n", "abcd", sizeof("abcd"), strlen("abcd"));
    printf("%s...%zu...%zu\n", "대한민국", sizeof("대한민국"), strlen("대한민국"));
    return 0;
}
```

- 예상 출력

```c
abcd...5...4
대한민국...13...12
```

---

## 12-5) 정수/실수 나눗셈 차이

```c
#include <stdio.h>

int main(void) {
    printf("%d\n", 10/3);          // 3
    printf("%f\n", (float)10/3);   // 3.333333
    printf("%f\n", (float)(10/3)); // 3.000000 (정수 나눗셈 후 캐스팅)
    return 0;
}

```

---

## 12-6) 형변환과 서식 맞추기

```c
#include <stdio.h>

int main(void) {
    int i = 3.14;   // 3 (소수점 버림)
    float k = 3;    // 3.0 (정수 → 실수 변환)

    // ⚠️ 타입에 맞는 서식 사용
    printf("%d....%.0f\n", i, k);

    printf("%f\n", (float)(10/3)); // 3.000000
    return 0;
}

```

---

## 12-7) 문자와 아스키
#include <stdio.h>

int main(void) {
    int i = 65;     // 'A'
    char c = 'a';   // 97
    printf("%c....%c....%c\n", i, c, c+2); // A....a....c

    // 숫자(코드값)도 보고 싶다면:
    printf("%d....%d....%d\n", i, c, c+2); // 65....97....99
    return 0;
}
