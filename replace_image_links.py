#!/usr/bin/env python3
"""
替换HTML文件中的图片链接
将飞书的在线图片链接替换为本地图片路径
"""

import re

def replace_image_links(html_file):
    """替换HTML文件中的图片链接"""
    # 读取HTML文件
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 替换图片链接
    # 匹配飞书图片链接：https://open.feishu.cn/open-apis/docx/v1/images/{token}/download
    pattern = r'https://open\.feishu\.cn/open-apis/docx/v1/images/(.*?)/download'
    replaced_content = re.sub(pattern, r'images/\1.png', html_content)
    
    # 写回修改后的内容
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(replaced_content)
    
    print(f"图片链接替换完成，文件已更新: {html_file}")

def main():
    """主函数"""
    html_file = "feishu_doc.html"
    replace_image_links(html_file)

if __name__ == "__main__":
    main()
