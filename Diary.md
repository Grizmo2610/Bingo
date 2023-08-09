# Nhật ký phát triển

* `May 21th 2023`:
    - Hình thành trò chơi và đưa ra ý tưởng ban đầu về phát triển trò chơi. 
    - Cách chơi: người chơi và máy sẽ có một bảng 5x5 và chứa các số từ 1 đến 25 ở các vị trí ngẫu nhiên. Mỗi khi người chơi gọi số ở cả 2 bảng sẽ đều đồng loạt được đánh và chuyển thành x. Người chơi đầu tiên có số tổng số đường thằng là 5 trước là sẽ thắng. Mỗi đường thẳng được tính là 5 ô liên tiếp.

* `Agust 3rd 2023`: 
    - Đưa ra ý tưởng về sử dụng thuật toán Minimax kết hợp với thuật toán Alpha-Beta Pruning để tìm đường đi ngắn nhất tới chiến thắng. Bước đầu ý tưởng là áp dụng thuật toán của trò chơi tic-tac-toe nhưng luật sẽ chút thay đổi là các nước đi đều được thành là x.