import os
import datetime

# 确保文章存放的目录存在
os.makedirs("content/posts", exist_ok=True)

# 批量生成 10 篇文章
for i in range(1, 11):
    filename = f"content/posts/seo-keyword-{i}.md"
    
    # 这是 Hugo 识别的 Markdown 格式
    content = f"""---
title: "关于关键词 {i} 的终极指南"
date: {datetime.date.today()}
draft: false
---

# 这是自动生成的 SEO 文章 {i}

这里先用占位符。只要这个流程跑通了，下一步我们只需要用现成的 AI 脚本把这段中文替换成 AI 生成的内容即可！
"""
    # 写入文件
    with open(filename, "w", encoding="utf-8") as f:
         f.write(content)

print("✅ 成功批量生成了 10 篇文章！")