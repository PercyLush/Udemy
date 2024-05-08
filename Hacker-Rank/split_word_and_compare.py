def count_substring(string, sub_string):
    
    counts = 0
    Data = [s for s in string]
    length = [f for f in sub_string]

    for i in range(len(Data)):
        # num[i] + num[i+1] + num[i+2] == sub_string
        try:
            Text = f"{Data[i]}"
            for l in range(1, len(length)):
                Text += f"{Data[i+l]}"
            if sub_string == Text:
                counts += 1
        except IndexError:
            break
    return counts


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

