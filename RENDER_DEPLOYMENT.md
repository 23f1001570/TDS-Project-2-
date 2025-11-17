# Render.com Deployment Guide

## Quick Deployment Steps

### 1. Push Code to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Render deployment"

# Create repo on GitHub, then:
git remote add origin https://github.com/yourusername/tds-llm-quiz.git
git branch -M main
git push -u origin main
```

**Important:** Make repo PUBLIC!

### 2. Sign Up on Render

1. Go to: **https://render.com**
2. Click "Get Started for Free"
3. Sign up with GitHub account (easiest)

### 3. Create New Web Service

1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select your `tds-llm-quiz` repo
4. Render will auto-detect settings from `render.yaml`

### 4. Configure Environment Variables

In Render dashboard, add these environment variables:

| Key | Value |
|-----|-------|
| `STUDENT_EMAIL` | `23f1001570@ds.study.iitm.ac.in` |
| `SECRET_KEY` | `my_secret_key` |
| `GROQ_API_KEY` | `your-groq-api-key` |
| `PORT` | `10000` |

### 5. Deploy

1. Click "Create Web Service"
2. Wait 5-10 minutes for build
3. You'll get a URL like: `https://tds-llm-quiz.onrender.com`

### 6. Test Your Deployment

```bash
curl -X POST https://your-app.onrender.com/quiz \
  -H "Content-Type: application/json" \
  -d '{
    "email": "23f1001570@ds.study.iitm.ac.in",
    "secret": "my_secret_key",
    "url": "https://tds-llm-analysis.s-anand.net/demo"
  }'
```

### 7. Use in Google Form

Your API endpoint URL will be:
```
https://your-app-name.onrender.com/quiz
```

## Important Notes

### Free Tier Limitations:
- ✅ Free forever
- ✅ 750 hours/month (enough for this project)
- ⚠️ Spins down after 15 minutes of inactivity
- ⚠️ Takes 30-60 seconds to wake up on first request

### For Evaluation Day (29 Nov):
- Keep your service active by pinging it every 10 minutes before 3 PM
- Or upgrade to paid plan ($7/month) for always-on service

### Selenium Note:
Render's free tier might have issues with Chrome/Selenium. If browser fails:
1. The code will still work for non-JS pages
2. Consider upgrading to paid tier for full Chrome support
3. Or use Railway/Fly.io instead (better Selenium support)

## Alternative: Railway.app

If Render has Selenium issues, try Railway:

1. Go to: **https://railway.app**
2. Sign up with GitHub
3. "New Project" → "Deploy from GitHub"
4. Select your repo
5. Add environment variables
6. Deploy!

Railway is more developer-friendly and handles Selenium better.

## Troubleshooting

### Build Fails
- Check `requirements.txt` has all dependencies
- Ensure Python version compatibility

### App Crashes
- Check Render logs for errors
- Verify environment variables are set
- Test locally first with `gunicorn app:app`

### Selenium Issues
- Chrome might not work on free tier
- Consider Railway or Fly.io
- Or remove headless browser requirement

## Keep Service Alive

Create a simple ping script to keep it active before evaluation:

```python
# ping_service.py
import requests
import time

url = "https://your-app.onrender.com/health"

while True:
    try:
        response = requests.get(url)
        print(f"Ping: {response.status_code}")
    except:
        print("Ping failed")
    time.sleep(600)  # Every 10 minutes
```

Run this 1 hour before evaluation starts!

---

**Your Render URL will look like:**
`https://tds-llm-quiz-abc123.onrender.com/quiz`

Use this in your Google Form submission!
