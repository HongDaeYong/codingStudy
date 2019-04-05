def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for i, phone in enumerate(phone_book[:-1]):
        for j in range(i+1, len(phone_book)):
            if len(phone) != len(phone_book[j]) and phone_book[j].startswith(phone):
                return False
    return True


inputs = [["119", "97674223", "1195524421"],
          ["123", "456", "789"],
          ["12", "123", "1235", "567", "88"]]
for inpts in inputs:
    print(solution(inpts))

