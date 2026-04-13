#!/usr/bin/env python3
"""
飞书文档调试工具
直接保存API返回的原始内容
"""

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
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{document_token}/blocks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
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

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="飞书文档调试工具")
    parser.add_argument("document_token", help="飞书文档Token")
    parser.add_argument("--app-id", help="飞书应用App ID")
    parser.add_argument("--app-secret", help="飞书应用App Secret")
    
    args = parser.parse_args()
    
    # 获取access token
    access_token = get_app_access_token(args.app_id, args.app_secret)
    
    if access_token:
        print(f"获取到access token: {access_token}")
        content = get_document_content(args.document_token, access_token)
        
        if content:
            print(f"文档包含 {len(content.get('blocks', []))} 个块")
            
            # 保存原始内容到文件
            with open("feishu_raw.json", "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False, indent=2)
            print("原始内容已保存到 feishu_raw.json")
            
            # 打印前几个块的结构
            blocks = content.get('blocks', [])
            for i, block in enumerate(blocks[:5]):
                print(f"\n块 {i+1} 类型: {block.get('block_type')}")
                print(f"块 {i+1} 内容: {json.dumps(block, ensure_ascii=False)[:200]}...")
        else:
            print("获取文档内容失败")
    else:
        print("获取访问令牌失败")

if __name__ == "__main__":
    main()
