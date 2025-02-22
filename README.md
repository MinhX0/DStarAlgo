# Thuật toán D*(D Star)
#Mô tả:
Thuật toán D* là một phương pháp tìm đường trong đồ thị, đặc biệt hữu ích cho các môi trường động nơi đồ thị có thể thay đổi theo thời gian. Bao gồm các bước thực hiện sau: 
1.	Khởi tạo:
- Bắt đầu bằng việc thiết lập các điều kiện ban đầu, như xác định nút bắt đầu và nút đích.
-	Khởi tạo danh sách mở (open list) là hàng đợi ưu tiên, lưu trữ các nút cần được mở rộng.
-	Thiết lập chi phí ban đầu cho nút bắt đầu là 0 và cho tất cả các nút khác là vô cực.
-	Thiết lập con trỏ quay lại cho tất cả các nút là null.
2.	Tìm đường:
-	Trong giai đoạn này, thuật toán tìm kiếm đường ngắn nhất từ nút bắt đầu đến nút đích bằng cách sử dụng hàng đợi ưu tiên.
-	Lần lượt mở rộng nút có chi phí thấp nhất trong danh sách mở.
-	Đối với mỗi nút láng giềng của nút hiện tại, tính toán chi phí tạm thời bằng cách cộng chi phí của nút hiện tại với chi phí cạnh nối tới nút láng giềng.
-	Nếu chi phí tạm thời nhỏ hơn chi phí hiện tại của nút láng giềng, cập nhật chi phí và con trỏ quay lại của nút láng giềng.
-	Thêm nút láng giềng vào danh sách mở với ưu tiên là chi phí tạm thời hoặc cập nhật ưu tiên nếu nút đã có trong danh sách mở.
3.	Lập kế hoạch lại:
-	Khi phát hiện các thay đổi trong đồ thị, như các chướng ngại vật được thêm vào hoặc loại bỏ, thuật toán cập nhật các chi phí và con trỏ quay lại của các nút bị ảnh hưởng.
-	Thuật toán sau đó lan truyền các thay đổi này qua đồ thị và lập kế hoạch lại đường đi từ nút bắt đầu đến nút đích.

#Phân tích
Hiệu suất:
1.	Độ phức tạp thời gian:
-	Thuật toán D* có độ phức tạp thời gian tương tự như thuật toán A, tức là O(E+Vlog⁡V)O(E + V \log V), trong đó EE là số cạnh và VV là số nút trong đồ thị. Tuy nhiên, vì D có thể tái sử dụng thông tin từ các lần lập kế hoạch trước đó, nó có thể hiệu quả hơn trong các môi trường động.
2.	Độ phức tạp không gian:
-	Thuật toán D* yêu cầu không gian để lưu trữ thông tin về chi phí, con trỏ quay lại và danh sách mở cho mỗi nút. Do đó, độ phức tạp không gian là O(V)O(V).
Ưu điểm:
1.	Thích ứng với môi trường động:
-	Thuật toán D* có thể cập nhật đường đi một cách hiệu quả khi đồ thị thay đổi, mà không cần phải tính toán lại từ đầu như các thuật toán khác.
2.	Hiệu quả trong việc tìm kiếm:
-	Bằng cách sử dụng hàng đợi ưu tiên, thuật toán D* mở rộng các nút có chi phí thấp nhất trước, giúp tìm kiếm đường đi ngắn nhất một cách hiệu quả.
Hạn chế:
1.	Phức tạp hơn các thuật toán đơn giản:
-	Thuật toán D* phức tạp hơn các thuật toán đơn giản như Dijkstra hay A*, và do đó có thể khó hiểu và triển khai hơn.
2.	Phụ thuộc vào cấu trúc dữ liệu:
-	Hiệu suất của thuật toán phụ thuộc vào việc sử dụng cấu trúc dữ liệu hàng đợi ưu tiên hiệu quả, chẳng hạn như heap.

