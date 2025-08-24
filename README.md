# 简化版旅行代理程序

一个基于OpenAI API的智能旅行建议系统，能够为不同目的地提供个性化的旅行建议。

## 🚀 功能特性

- **智能目的地推荐**：随机从预设的目的地列表中选择（巴塞罗那、巴黎、柏林、东京、悉尼）
- **AI旅行建议**：基于OpenAI GPT-4o-mini模型提供详细的旅行建议
- **异步处理**：使用异步编程提高性能
- **环境变量配置**：支持通过环境变量配置API密钥
- **跨平台兼容**：支持ARM64和x86_64架构

## 📋 系统要求

- Python 3.9+
- OpenAI API密钥或GitHub Token
- 网络连接

## 🛠️ 安装依赖

### 方法1：使用pip安装
```bash
pip install -r requirements.txt
```

### 方法2：使用conda安装（推荐）
```bash
conda install python-dotenv openai -c conda-forge
```

## ⚙️ 配置

1. 获取API密钥（OpenAI API密钥或GitHub Token）
2. 设置环境变量：
```bash
export GITHUB_TOKEN="your_api_token_here"
```

## 🎯 运行程序

### 基本运行
```bash
python simple_test.py
```

### 使用conda环境运行（推荐）
```bash
conda activate akshare
export GITHUB_TOKEN="your_api_token_here"
python simple_test.py
```

### 使用完整路径运行（解决架构兼容性问题）
```bash
export GITHUB_TOKEN="your_api_token_here"
/Users/lichaolin/miniconda3/envs/akshare/bin/python simple_test.py
```

## 📁 项目结构

```
aistart/
├── simple_test.py      # 主程序文件
├── requirements.txt    # 依赖包列表
└── README.md          # 项目说明文档
```

## 🔧 程序流程

1. **环境检查**：加载环境变量和API配置
2. **客户端初始化**：创建OpenAI API客户端
3. **目的地选择**：随机选择一个旅行目的地
4. **AI交互**：调用AI API获取旅行建议
5. **结果输出**：显示详细的旅行建议

## 🌍 支持的目的地

- 巴塞罗那, 西班牙
- 巴黎, 法国
- 柏林, 德国
- 东京, 日本
- 悉尼, 澳大利亚

## 🐛 故障排除

### 架构兼容性问题
如果遇到ARM64/x86_64架构不兼容错误，请使用conda环境：
```bash
conda activate akshare
/Users/lichaolin/miniconda3/envs/akshare/bin/python simple_test.py
```

### API密钥问题
确保正确设置环境变量：
```bash
echo $GITHUB_TOKEN
```

## 📝 示例输出

```
程序开始执行...
=== 简化版旅行代理测试 ===

步骤1: 加载环境变量...
✓ 环境变量加载成功

步骤2: 创建OpenAI客户端...
✓ OpenAI客户端创建成功

步骤3: 创建目的地插件...
✓ 推荐目的地: 东京, 日本

步骤4: 测试API调用...
用户消息: 我想去东京, 日本旅行，请给我一些建议。
✓ API调用成功
AI回复: 当然可以！东京是一个充满活力和文化的城市...
```

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

MIT License
