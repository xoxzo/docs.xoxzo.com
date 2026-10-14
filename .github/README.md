# Quick Migration Guide: Netlify to GitHub Pages (docs.xoxzo.com)

Concise guide for moving `docs.xoxzo.com` from Bitbucket & Netlify to GitHub Pages using AWS Route 53.

---

## 1. Push Bitbucket Repo to GitHub

Add your GitHub repository remote and push the `master` branch:

```bash
# Option A: Replace existing origin URL with GitHub
git remote set-url origin git@github.com:xoxzo/docs.xoxzo.com.git
# (or HTTPS: https://github.com/xoxzo/docs.xoxzo.com.git)

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main

# (Option B: Keep Bitbucket as a backup remote)
# git remote rename origin bitbucket
# git remote add origin git@github.com:xoxzo/docs.xoxzo.com.git
# git branch -M main
# git push -u origin main
```

---

## 2. Enable GitHub Pages

In the GitHub repository:
1. Go to **Settings** > **Pages**.
2. **Build and deployment > Source**: Select **`GitHub Actions`** (do not select "Deploy from a branch").
3. **Custom domain**: Enter `docs.xoxzo.com` and save.

---

## 3. Update DNS in AWS Route 53

Switch the `docs.xoxzo.com` DNS record from Netlify to GitHub Pages:

1. Open **AWS Route 53 Console** > **Hosted zones** > select `xoxzo.com`.
2. Locate the existing `CNAME` record for `docs.xoxzo.com` (currently pointing to `<site>.netlify.app`).
3. Edit the record:
   - **Record name:** `docs`
   - **Record type:** `CNAME`
   - **Value / Route traffic to:** `<your-github-org>.github.io` (e.g., `xoxzo.github.io`)
   - **TTL:** `300`
4. Save the record.
5. In GitHub **Settings** > **Pages**, wait for DNS check to pass, then check **Enforce HTTPS**.

---

## 4. Local Build & Test

Verify the build locally anytime before pushing:

```bash
# Set up environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Build both English and Japanese docs (generates CNAME, index.html, .nojekyll)
make clean site

# Preview locally
make serve
# Open http://localhost:8000
```

---

## How It Works in CI

On every push to `main` (or `master`), [`.github/workflows/deploy.yml`](workflows/deploy.yml):
1. Installs Sphinx dependencies from [`requirements.txt`](../requirements.txt).
2. Runs `make clean site` (compiles `en/` and `ja/`, outputs `.nojekyll` and `CNAME`).
3. Deploys `appengine/public/html/` to GitHub Pages.
