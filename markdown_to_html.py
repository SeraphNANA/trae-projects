#!/usr/bin/env python3
"""
Markdown转HTML工具
将Markdown文件转换为HTML，并下载图片到本地
"""

import os
import re
import requests
import markdown
from markdown.extensions import fenced_code, codehilite

def extract_images(markdown_content):
    """提取Markdown中的图片链接"""
    # 匹配Markdown图片语法：![alt](url)
    pattern = r'!\[(.*?)\]\((https://open\.feishu\.cn/open-apis/docx/v1/images/[^)]+)\)'
    return re.findall(pattern, markdown_content)

def download_image(url, save_dir):
    """下载图片到本地"""
    try:
        # 从URL中提取图片token作为文件名
        token = url.split('/')[-2]
        filename = f"{token}.png"
        save_path = os.path.join(save_dir, filename)
        
        # 下载图片
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return filename
        else:
            print(f"下载图片失败: {url}, 状态码: {response.status_code}")
            return None
    except Exception as e:
        print(f"下载图片时出错: {str(e)}")
        return None

def markdown_to_html(markdown_file, output_html):
    """将Markdown转换为HTML"""
    # 读取Markdown文件
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # 创建图片保存目录
    image_dir = os.path.join(os.path.dirname(output_html), 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    
    # 提取并下载图片
    images = extract_images(markdown_content)
    for alt, url in images:
        filename = download_image(url, image_dir)
        if filename:
            # 替换Markdown中的图片链接为本地路径
            markdown_content = markdown_content.replace(url, f'images/{filename}')
    
    # 转换Markdown为HTML
    html_content = markdown.markdown(
        markdown_content,
        extensions=[
            'fenced_code',
            'codehilite',
            'tables'
        ]
    )
    
    # 添加HTML头部和样式
    full_html = f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI智能体工具分享：【Trae】安装部署和使用教程</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 2em;
            margin-bottom: 1em;
        }}
        h1 {{
            font-size: 2.5em;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            font-size: 2em;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 8px;
        }}
        h3 {{
            font-size: 1.5em;
        }}
        h4 {{
            font-size: 1.2em;
        }}
        p {{
            margin-bottom: 1em;
        }}
        ul, ol {{
            margin-bottom: 1em;
            padding-left: 2em;
        }}
        li {{
            margin-bottom: 0.5em;
        }}
        img {{
            max-width: 100%;
            height: auto;
            margin: 1em 0;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        code {{
            background-color: #f8f8f8;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
        }}
        pre {{
            background-color: #f8f8f8;
            padding: 1em;
            border-radius: 4px;
            overflow-x: auto;
            margin-bottom: 1em;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 1em;
            margin: 1em 0;
            color: #666;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
'''
    
    # 保存HTML文件
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"转换完成，HTML文件已保存为: {output_html}")
    print(f"图片已保存到: {image_dir}")

def main():
    """主函数"""
    markdown_file = "feishu_doc.md"
    output_html = "feishu_doc.html"
    
    markdown_to_html(markdown_file, output_html)

if __name__ == "__main__":
    main()
