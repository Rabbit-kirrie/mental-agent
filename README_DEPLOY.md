# Docker 部署与云发布说明

## 一、Docker 本地构建与运行

1. 构建镜像
```powershell
docker build -t mental-agent .
```
2. 运行容器
```powershell
docker run --env-file .env -p 8000:8000 mental-agent
```

或使用 docker-compose：
```powershell
docker-compose up --build
```

访问 http://localhost:8000

---

## 二、云平台部署（以 Render/Heroku 为例）

1. 推送代码到 GitHub
2. 在 Render/Heroku 创建新 Web 服务，选择 Docker 部署
3. 配置环境变量（.env 内容填入平台环境变量设置）
4. 构建并启动，端口设为 8000
5. 绑定自定义域名、开启 HTTPS

---

## 生产建议
- API Key、数据库等敏感信息仅用平台环境变量管理
- 日志与数据合规存储，定期备份
- 可用 Sentry/Prometheus 监控
