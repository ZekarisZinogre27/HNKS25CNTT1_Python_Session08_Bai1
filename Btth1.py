owner_video = ""
title = ""
description = ""
hash_list = ""
while True:
    print("+=============================================+")
    print("|      HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK       |")
    print("+=============================================+")
    print("| 1. Nhập và phân tích thông tin video        |")
    print("| 2. Chuẩn hóa tên tài khoản                  |")
    print("| 3. Kiểm tra tính hợp lệ của hashtag         |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong mô tả |")
    print("| 5. Thoát chương trình                       |")
    print("+=============================================+")
    choice = int(input("Mời bạn chọn chức năng (1-5): "))
    if choice == 1:
        name_owner_video = input("Tên tài khoản người đăng video: ")
        owner_video += name_owner_video
        video_title = input("Tiêu đề video: ")
        title += video_title
        description_video = input("Mô tả video: ")
        description += description_video
        hashtag_list = input("Danh sách hashtag: ")
        parts = hashtag_list.split(",")
        hash_list += hashtag_list
        print(name_owner_video.strip())
        print(video_title.strip().title())
        print(description_video.strip())
        print(len(description_video))
        print(hashtag_list.strip())
        print(hashtag_list.count)
        print(description_video.strip().lower())
        print(description_video.strip().upper())
    elif choice == 2:
        if name_owner_video != "":
            print(f"@{name_owner_video.lower()}")
        else:
            print("Lỗi đầu vào chưa nhập tên hoặc không tồn tại tên")
    elif choice == 3:
        hashtag_in = input("Nhập hashtag bạn muốn kiểm tra hợp lệ: ")
        if hashtag_in == "":
            print("Hashtag đang bị rỗng/ không có hashtag. Không hợp lệ")
            continue
        elif not hashtag_in.startswith("#"):
            print("Hashtag đang sai vì không có ký hiệu hashtag. Không hợp lệ")
            continue
        elif len(hashtag_in) < 2:
            print("Hashtag đang sai hợp lệ")
        elif not hashtag_in[1:].replace("_", "").isalnum():
            print("Hashtag không hợp lệ. Chỉ nên sử dụng chữ cái, chữ số hoặc dấu gạch dưới sau ký tự #")
            continue
        else:
            print("Hashtag hợp lệ")
            hashtag_in += hashtag_list
    elif choice == 4:
        word_find = input("Nhập ký tự/từ khóa cần tìm: ")
        word_replace = input("Nhập ký tự/từ khóa bạn muốn thay thế: ")
        if word_find in description:
            description.replace(word_replace)
    elif choice == 5:
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại")