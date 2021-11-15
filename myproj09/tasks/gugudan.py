def check_available(received_text: str) -> bool:
    return received_text == "구구단"


def make_response(received_text: str) -> str:
    num_list = []
    for num in range(2, 10):
        for i in range(1, 10):
            num_list.append(f"{num}*{i}={num*i}")
    # return str(num_list)
    return "\n".join(num_list)
