#!/usr/bin/env python3
"""
飞书文档转Markdown工具
直接使用飞书开放平台API获取文档内容并转换为Markdown格式
"""

import os
import json
import argparse
import requests

def get_app_access_token(app_id, app_secret):
    """获取飞书应用访问令牌"""
    url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal"
    payload = {
        "app_id": app_id,
        "app_secret": app_secret
    }
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        
        if result.get("code") == 0:
            return result.get("app_access_token")
        else:
            print(f"获取access token失败: {result.get('msg')}")
            return None
    except Exception as e:
        print(f"请求失败: {str(e)}")
        print(f"响应内容: {response.text if 'response' in locals() else '无响应'}")
        return None

def get_document_content(document_token, access_token):
    """获取飞书文档内容"""
    # 使用正确的API端点
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{document_token}/blocks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"获取文档内容响应: {response.text}")
        result = response.json()
        
        if result.get("code") == 0:
            return result.get("data", {})
        else:
            print(f"获取文档内容失败: {result.get('msg')}")
            return None
    except Exception as e:
        print(f"请求失败: {str(e)}")
        print(f"响应内容: {response.text if 'response' in locals() else '无响应'}")
        return None

def convert_to_markdown(content):
    """将飞书文档内容转换为Markdown格式"""
    if not content:
        return ""
    
    markdown = ""
    
    # 处理文档内容
    if "blocks" in content:
        for block in content["blocks"]:
            block_type = block.get("type")
            
            if block_type == "heading":  # 标题
                level = block.get("heading", {}).get("level", 1)
                # 处理标题文本
                text = ""
                if "elements" in block.get("heading", {}):
                    for elem in block["heading"]["elements"]:
                        if elem.get("type") == "text_run":
                            text += elem.get("text", "")
                markdown += f"{'#' * level} {text}\n\n"
                
            elif block_type == "paragraph":  # 段落
                # 处理段落文本
                text = ""
                if "elements" in block:
                    for elem in block["elements"]:
                        if elem.get("type") == "text_run":
                            text += elem.get("text", "")
                markdown += f"{text}\n\n"
                
            elif block_type == "bulleted_list":  # 无序列表
                if "items" in block:
                    for item in block["items"]:
                        # 处理列表项文本
                        item_text = ""
                        if "blocks" in item:
                            for item_block in item["blocks"]:
                                if item_block.get("type") == "paragraph" and "elements" in item_block:
                                    for elem in item_block["elements"]:
                                        if elem.get("type") == "text_run":
                                            item_text += elem.get("text", "")
                        markdown += f"- {item_text}\n"
                    markdown += "\n"
                
            elif block_type == "numbered_list":  # 有序列表
                if "items" in block:
                    for i, item in enumerate(block["items"], 1):
                        # 处理列表项文本
                        item_text = ""
                        if "blocks" in item:
                            for item_block in item["blocks"]:
                                if item_block.get("type") == "paragraph" and "elements" in item_block:
                                    for elem in item_block["elements"]:
                                        if elem.get("type") == "text_run":
                                            item_text += elem.get("text", "")
                        markdown += f"{i}. {item_text}\n"
                    markdown += "\n"
                
            elif block_type == "table":  # 表格
                if "table_rows" in block:
                    rows = []
                    for table_row in block["table_rows"]:
                        row_cells = []
                        if "cells" in table_row:
                            for cell in table_row["cells"]:
                                # 处理单元格文本
                                cell_text = ""
                                if "blocks" in cell:
                                    for cell_block in cell["blocks"]:
                                        if cell_block.get("type") == "paragraph" and "elements" in cell_block:
                                            for elem in cell_block["elements"]:
                                                if elem.get("type") == "text_run":
                                                    cell_text += elem.get("text", "")
                                row_cells.append(cell_text)
                        rows.append(row_cells)
                    
                    if rows:
                        # 处理表头
                        headers = rows[0]
                        markdown += "| " + " | ".join(headers) + " |\n"
                        markdown += "| " + " | ".join(["---" for _ in headers]) + " |\n"
                        
                        # 处理表格内容
                        for row in rows[1:]:
                            markdown += "| " + " | ".join(row) + " |\n"
                        markdown += "\n"
                
            elif block_type == "image":  # 图片
                if "image" in block:
                    image = block["image"]
                    url = image.get("image_token", "")
                    # 构建图片URL
                    if url:
                        image_url = f"https://open.feishu.cn/open-apis/docx/v1/images/{url}/download"
                        alt = image.get("alt", "图片")
                        markdown += f"![{alt}]({image_url})\n\n"
    
    return markdown

def save_markdown(content, output_file):
    """保存Markdown内容到文件"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"转换完成，文件已保存为: {output_file}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="飞书文档转Markdown工具")
    parser.add_argument("document_token", help="飞书文档Token")
    parser.add_argument("-o", "--output", default="output.md", help="输出Markdown文件名")
    parser.add_argument("--app-id", help="飞书应用App ID")
    parser.add_argument("--app-secret", help="飞书应用App Secret")
    
    args = parser.parse_args()
    
    # 从环境变量获取或从参数获取
    app_id = args.app_id or os.environ.get("FEISHU_APP_ID")
    app_secret = args.app_secret or os.environ.get("FEISHU_APP_SECRET")
    
    if not app_id or not app_secret:
        print("错误: 请提供飞书应用的App ID和App Secret")
        print("可以通过参数 --app-id 和 --app-secret 提供，或设置环境变量 FEISHU_APP_ID 和 FEISHU_APP_SECRET")
        return
    
    print(f"正在获取飞书文档内容...")
    access_token = get_app_access_token(app_id, app_secret)
    
    if access_token:
        print(f"获取到access token: {access_token}")
        content = get_document_content(args.document_token, access_token)
        
        if content:
            print(f"正在转换为Markdown...")
            markdown = convert_to_markdown(content)
            save_markdown(markdown, args.output)
        else:
            print("转换失败，请检查文档Token是否正确。")
    else:
        print("获取访问令牌失败，请检查App ID和App Secret是否正确。")

if __name__ == "__main__":
    main()
