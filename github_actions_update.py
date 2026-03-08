# 1. 克隆你的仓库
git clone https://github.com/andy-zokelink/feishu-exhibition-updater.git
cd feishu-exhibition-updater

# 2. 复制文件到仓库
# 将以下文件复制到仓库目录：
# - .github/workflows/feishu-auto-update.yml
# - github_actions_update.py
# - 深圳会展中心2026年展会排期表_完整版.md

# 3. 提交并推送
git add .
git commit -m "添加飞书展会自动更新功能"
git push origin main
