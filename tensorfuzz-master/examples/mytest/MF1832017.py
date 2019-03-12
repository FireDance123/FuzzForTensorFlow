import sys


# 读取数据文件，获取k个最大值并输出
def my_get_top_k(file_path):
    """
    读取数据文件，获取k个最大值并输出
    :param file_path:数据文件所在路径
    :return:输出k个最大值
    """
    with open(file_path, 'r')as f:
        data = f.readlines()

    k = int(data[0])
    input_list = my_convert(data[1:])
    top_k_list = my_top_k_sort(k, input_list)

    top_k_str = "'"
    for i in range(len(top_k_list)):
        if i != len(top_k_list) - 1:
            top_k_str += str(top_k_list[i])
            top_k_str += ","
        else:
            top_k_str += str(top_k_list[i])
            top_k_str += "'"
    print(top_k_str)


# 排序方法
def my_top_k_sort(k, input_list):
    """
    找到一组数据中k个最大值
    :param k:需要找的元素个数
    :param input_list:待查找的数据
    :return:k个最大值
    """
    # 判断k值是否大于输入数据个数，若大于则直接返回
    if k > len(input_list):
        return

    top_k_list = []

    # 循环k次，每次找到剩余数据中的最大值
    for i in range(k):
        max_value = input_list[i]
        pre_index = i
        max_index = pre_index
        for j in range(len(input_list) - i - 1):
            if input_list[j + i + 1] > max_value:
                max_value = input_list[j + i + 1]
                max_index = j + i + 1
        if pre_index != max_index:
            meta_value = input_list[i]
            input_list[i] = max_value
            input_list[max_index] = meta_value
        top_k_list.append(max_value)

    return top_k_list


# 将数据由str转为float
def my_convert(input_list):
    """
    将数据由str转为float
    :param input_list: 待转换类型的数据
    :return: 转换类型后的数据
    """
    for i in range(len(input_list)):
        sub_str = input_list[i]
        sub_li = sub_str.split('\n')
        input_list[i] = float(sub_li[0])

    return input_list


def main():
    file_path = sys.argv[1]
    my_get_top_k(file_path)


if __name__ == "__main__":
    main()




