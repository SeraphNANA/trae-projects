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

def extract_text(block):
    """从块中提取文本"""
    # 检查各种可能的文本字段
    text_fields = [
        "heading1", "heading2", "heading3", "heading4", "heading5", "heading6",
        "text", "bullet", "ordered", "page"
    ]
    
    for field in text_fields:
        if field in block:
            elements = block[field].get("elements", [])
            text = ""
            for elem in elements:
                if "text_run" in elem:
                    text += elem["text_run"].get("content", "")
            return text
    return ""

def convert_to_markdown(content):
    """将飞书文档内容转换为Markdown格式"""
    if not content:
        return ""
    
    markdown = ""
    
    # 处理文档内容
    if "items" in content:
        for block in content["items"]:
            block_type = block.get("block_type")
            
            if block_type == 1:  # 标题1
                text = extract_text(block)
                markdown += f"# {text}\n\n"
                
            elif block_type == 2:  # 段落
                text = extract_text(block)
                markdown += f"{text}\n\n"
                
            elif block_type == 3:  # 标题2
                text = extract_text(block)
                markdown += f"## {text}\n\n"
                
            elif block_type == 4:  # 标题3
                text = extract_text(block)
                markdown += f"### {text}\n\n"
                
            elif block_type == 5:  # 标题4
                text = extract_text(block)
                markdown += f"#### {text}\n\n"
                
            elif block_type == 6:  # 标题5
                text = extract_text(block)
                markdown += f"##### {text}\n\n"
                
            elif block_type == 12:  # 无序列表
                text = extract_text(block)
                markdown += f"- {text}\n"
                
            elif block_type == 13:  # 有序列表
                text = extract_text(block)
                markdown += f"1. {text}\n"
                
            elif block_type == 27:  # 图片
                image = block.get("image", {})
                token = image.get("token", "")
                if token:
                    image_url = f"https://open.feishu.cn/open-apis/docx/v1/images/{token}/download"
                    markdown += f"![图片]({image_url})\n\n"
                
            elif block_type == 22:  # 分隔线
                markdown += "---\n\n"
    
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
