def modify_dictionary(bet):
    # Check if keys "a" and "b" exist in the table
    if "a" in bet and "b" in bet:
        if len(bet["a"]) != len(bet["b"]):
            bet["c"] = max(bet["a"], bet["b"], key=len)
        else:
            bet["a"] = ""
            bet["b"] = ""
    return bet


if __name__ == "__main__":
    input_table = {"a": "aaa", "b": "bb", "c": "cake"}
    modified_input = modify_dictionary(input_table)
    print(modified_input)
