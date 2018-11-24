file_path = 'D:\\superresolution_dataset\\DIV2K\\DIV2K_train_HR_sub_image\\img_list.txt'

with open(file_path, 'w') as img_list:
    for i in range(1, 801):
        for j in range(1, 41):
            write_string = "%04d" % i + "_s" + "%03d" % j + ".png\n"
            img_list.write(write_string)

file_path = 'D:\\superresolution_dataset\\DIV2K\\DIV2K_train_LR_sub_image\\img_list.txt'
with open(file_path, 'w') as img_list:
    for i in range(1, 801):
        for j in range(1, 41):
            write_string = "%04d" % i + "_s" + "%03d" % j + "_bicLRx4.png\n"
            img_list.write(write_string)