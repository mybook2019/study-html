#!/bin/bash

# 提示输入根目录路径
read -p "请输入项目根目录路径: " root_dir

# 判断目录是否存在
if [ -d "$root_dir" ]; then
    echo "目录 $root_dir 已经存在，开始创建子目录和文件..."
else
    # 创建根目录
    mkdir -p "$root_dir"
    echo "目录 $root_dir 已创建"
fi

# 创建子目录
mkdir -p "$root_dir/assets/images"
mkdir -p "$root_dir/assets/css"
mkdir -p "$root_dir/js"

# 创建空的文件
touch "$root_dir/index.html"
touch "$root_dir/assets/css/styles.css"
touch "$root_dir/js/script.js"
touch "$root_dir/README.md"

# 提示完成
echo "项目结构已成功创建！"
