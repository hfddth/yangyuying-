# 杨钰莹 · AIGC作品集

公开访问：https://hfddth.github.io/opc-gongsi/portfolio.html

按13个课程序号组织，每个序号单独打开。包含简历、论文答辩、低代码应用、十组文生图、产品种草视频、认证、FDE三件套、人物故事视频、数据看板、智能客服、OPC工作室、作品集及AI协作档案。

本仓库保存网页源码与32份原始文件。原文件较大，通过 `.portfolio-payload` 中25个分片归档；`ready.json` 记录逐片及整体SHA-256。发布流程会校验并恢复为普通文件，访问者可直接播放视频、阅读材料和下载原文件，无需自行拼接。

网页当前使用已经启用GitHub Pages的同账号OPC仓库发布，保留其原有主页与工具。此仓库的独立Pages尚未首次启用。

## 本地恢复

运行 `python3 restore_portfolio.py` 可将完整作品集解压至 `restored-portfolio`。运行 `python3 -m http.server --directory restored-portfolio` 后打开 `/portfolio.html`。
