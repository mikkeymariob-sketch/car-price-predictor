# Car Price Predictor — CSSD 609

Random Forest ML model predicting used car prices.  
**R² = 0.75 | MAE ≈ $4,552 | 19,237 training samples | 13 features**

## Deploy to Render (3 steps)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/car-price-predictor.git
   git push -u origin main
   ```

2. **Create Render Web Service**
   - Go to https://render.com → New → Web Service
   - Connect your GitHub repo
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Click **Deploy**

3. **Done!** Your app will be live at:
   `https://car-price-predictor.onrender.com`

## Local Run
```bash
pip install -r requirements.txt
python app.py
```
Then open http://localhost:5000
