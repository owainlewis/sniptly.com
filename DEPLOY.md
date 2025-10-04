# Deploying Sniptly to Netlify

## Quick Deploy (5 minutes)

### Option 1: Deploy via GitHub (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Connect to Netlify**
   - Go to [netlify.com](https://netlify.com) and sign up/login
   - Click "Add new site" → "Import an existing project"
   - Choose GitHub and authorize
   - Select your `sniptly` repository

3. **Configure Build Settings**
   - Build command: (leave empty)
   - Publish directory: `.` (current directory)
   - Click "Deploy site"

4. **Configure Custom Domain** (Optional)
   - In Netlify dashboard → Domain settings
   - Add custom domain: `sniptly.com`
   - Follow DNS instructions
   - Your app will be at `app.sniptly.com/app`

### Option 2: Drag & Drop Deploy

1. **Build locally**
   - Ensure you have `index.html`, `app/index.html`, and `netlify.toml`

2. **Deploy**
   - Go to [app.netlify.com/drop](https://app.netlify.com/drop)
   - Drag your entire project folder
   - Get instant URL like `sniptly-abc123.netlify.app`

## Structure

```
sniptly/
├── index.html          # Landing page (sniptly.com)
├── app/
│   └── index.html      # Main app (sniptly.com/app)
├── netlify.toml        # Netlify configuration
└── DEPLOY.md           # This file
```

## URLs

- **Landing page**: `https://sniptly.com`
- **App**: `https://sniptly.com/app`

## Auto-Deploy

Once connected to GitHub:
- Every push to `main` branch auto-deploys
- Get deploy previews for pull requests
- Instant rollback if needed

## Cost

- **Free tier includes:**
  - 100GB bandwidth/month
  - Unlimited sites
  - HTTPS/SSL certificate
  - Custom domain

**Perfect for 1-person SaaS!**

## Troubleshooting

**App doesn't load at /app:**
- Check `netlify.toml` exists in root
- Verify `app/index.html` exists
- Check Netlify deploy logs

**Landing page not showing:**
- Ensure `index.html` is in root directory
- Check publish directory is set to `.`

## Next Steps

After deployment:
1. Test both URLs (landing + app)
2. Set up custom domain
3. Add analytics (Netlify Analytics or Google Analytics)
4. Set up form for collecting emails (Netlify Forms)
