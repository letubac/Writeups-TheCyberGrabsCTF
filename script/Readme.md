# Writeups script
- Bài này mình sử dụng trang PyC để decompile file pyc thàng mã python
- Trang sử dụng: https://www.toolnb.com/tools-lang-en/pyc.html
- Sau khi load file thì mình nhận được mã như này

![image](https://user-images.githubusercontent.com/57956165/152991512-3aba1b82-549c-4c0e-af7b-7da35ad50e38.png)

- Xem qua mã nguồn thì mình hiểu được là nó sẽ cho mình nhập input, sau đó sẽ trải qua quá trình encode để so sánh với '*@),9.9():B@tz&k6<5i&\\mX&xmn-y&*Vu/,wD'
- Nếu đúng thì đầu vào của mình chính là flag
- Đây là hàm encode

![image](https://user-images.githubusercontent.com/57956165/152991857-014f8e35-6a39-4961-9869-334d8a0c4f31.png)

- Rất đơn giản, bây giờ mình chỉ cần Decode nó lại có thể lấy được đầu vào của mình rồi
- Ở đây, khi encode nó lấy index để cộng với 37, thì decode mình sẽ làm ngược lại là "- 37"

![image](https://user-images.githubusercontent.com/57956165/152992183-b0cc69b8-18b4-4572-bf31-39c0045613ed.png)

# Flag: cybergrabs{yOU_FounD_7H3_SHIfT_c1PheR}
