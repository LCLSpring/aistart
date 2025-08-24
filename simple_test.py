#!/usr/bin/env python3
"""
简化测试程序 - 逐步测试功能
"""

import os
import asyncio
import random
from dotenv import load_dotenv
from openai import AsyncOpenAI

class SimpleDestinationsPlugin:
    """简化的目的地插件"""
    
    def __init__(self):
        self.destinations = [
            "巴塞罗那, 西班牙",
            "巴黎, 法国", 
            "柏林, 德国",
            "东京, 日本",
            "悉尼, 澳大利亚"
        ]
        self.last_destination = None

    def get_random_destination(self) -> str:
        available_destinations = self.destinations.copy()
        if self.last_destination and len(available_destinations) > 1:
            available_destinations.remove(self.last_destination)
        
        destination = random.choice(available_destinations)
        self.last_destination = destination
        return destination

async def test_simple_chat():
    """测试简单的聊天功能"""
    print("=== 简化版旅行代理测试 ===\n")
    
    # 1. 加载环境变量
    print("步骤1: 加载环境变量...")
    load_dotenv()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("错误：GITHUB_TOKEN未设置")
        return
    print("✓ 环境变量加载成功")
    
    # 2. 创建OpenAI客户端
    print("\n步骤2: 创建OpenAI客户端...")
    try:
        client = AsyncOpenAI(
            api_key=token,
            base_url="https://models.inference.ai.azure.com/",
        )
        print("✓ OpenAI客户端创建成功")
    except Exception as e:
        print(f"✗ OpenAI客户端创建失败: {e}")
        return
    
    # 3. 创建目的地插件
    print("\n步骤3: 创建目的地插件...")
    destinations_plugin = SimpleDestinationsPlugin()
    destination = destinations_plugin.get_random_destination()
    print(f"✓ 推荐目的地: {destination}")
    
    # 4. 测试API调用
    print("\n步骤4: 测试API调用...")
    try:
        user_message = f"我想去{destination}旅行，请给我一些建议。"
        print(f"用户消息: {user_message}")
        
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个有用的旅行顾问，请用中文回答。"},
                {"role": "user", "content": user_message}
            ],
            max_tokens=200
        )
        
        print("✓ API调用成功")
        print(f"AI回复: {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"✗ API调用失败: {e}")
        return
    
    print("\n=== 测试完成！===")

async def main():
    try:
        await test_simple_chat()
    except Exception as e:
        print(f"程序执行错误: {e}")

if __name__ == "__main__":
    print("程序开始执行...")
    asyncio.run(main())
    print("程序执行完成")
