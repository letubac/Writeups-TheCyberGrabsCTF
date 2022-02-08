# Writeups simple
- Load file vào idapro, nhấn f5 để vào xem chương trình chính

![image](https://user-images.githubusercontent.com/57956165/152992556-4c7069f6-2d99-4080-a418-4ed54a966c69.png)

- Mình chỉ để ý 2 hàm này
- Thứ 1: nó sẽ so sánh chuỗi v5 với "QllB^pvCloQebCfopqCi^d" để làm đầu vào
- Thứ 2: trải qua các hàm thì đến hàm
+ if ( v5[i] + 3 != *(*(a2 + 8) + i) )
- nó sẽ kiểm tra từng ký tự của chuỗi v5 với chuỗi a2 xem có giống nhau hay không
- nếu khác thì in ra màn hình: "Try Again!", còn ngược lại thì => đó là flag

![image](https://user-images.githubusercontent.com/57956165/152992625-5573ff72-f564-40ce-a828-17744b91e110.png)

![image](https://user-images.githubusercontent.com/57956165/152992649-805ebb09-0b89-4343-9fcb-15742af533d6.png)

- Vậy mình chỉ cần lấy từng phần tử của v5 + 3 => Flag

![image](https://user-images.githubusercontent.com/57956165/152993178-c7766e3f-8a0a-4843-a3ab-beeec0228e52.png)

# Flag: cybergrabs{TooEasyForTheFirstFlag}
