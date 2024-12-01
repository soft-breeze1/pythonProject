import os

# def test_os():
    # print(os.listdir("D:/递归test"))         # 列出路径下的内容
    # print(os.path.isdir("D:/递归test/a"))    # 判断指定路径是不是文件夹
    # print(os.path.exists("D:/递归test/a"))   # 判断指定路径是否存在

def get_file_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方法,获取全部的文件列表
    :param path: 被判断的文件夹
    :return: 包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """
    print(f"当前判断的文件夹是:{path}")

    file_list = []

    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                #进入到这里，表明这个目录是文件夹不是文件
                file_list += get_file_recursion_from_dir(new_path)
                # 最精髓的一点:   +=    把递归后的内容都保留在file_list中
                # 进入到新的递归中，file_list重新添加文件，再将此list 加入到之前的list中
            else:
                # 说明是文件
                file_list.append(new_path)
    else:
        print(f"指定的目录{path},不存在")
        return []

    return file_list

if __name__ == '__main__':
    print(get_file_recursion_from_dir("D:/递归test"))
