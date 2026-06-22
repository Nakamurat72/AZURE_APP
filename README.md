# Günlük Alıntı Uygulaması — Kurulum ve Deploy Rehberi

Bu proje iki parçadan oluşur:
- `function/` → Azure Function (Python, HTTP trigger, rastgele alıntı döndürür)
- `webapp/` → Flask Web App (arayüz, Function'ı çağırır)

---

## 1. Yerel Test (İsteğe bağlı, önerilir)

### Function'ı çalıştırma
```bash
cd function
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
func start
```
Azure Functions Core Tools kurulu olmalı: https://learn.microsoft.com/azure/azure-functions/functions-run-local

### Web App'i çalıştırma (başka bir terminalde)
```bash
cd webapp
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Tarayıcıda `http://localhost:8000` adresini açın.

---

## 2. Azure Kaynaklarını Oluşturma

Azure Portal (portal.azure.com) üzerinden:

### a) Resource Group
"Resource groups" → "Create" → bir isim verin (örn. `quote-app-rg`).

### b) Azure Function App
"Create a resource" → "Function App"
- Runtime stack: **Python 3.11**
- Hosting: **Consumption (Serverless)** plan (ücretsiz katman için uygun)
- Aynı resource group'u seçin
Oluşturduktan sonra **Overview** sayfasının ekran görüntüsünü alın (gereksinim b).

### c) Azure Web App
"Create a resource" → "Web App"
- Runtime stack: **Python 3.11**
- Aynı resource group'u seçin
Oluşturduktan sonra **Overview** sayfasının ekran görüntüsünü alın (gereksinim a).

**Web App → Configuration → Application settings** kısmına şu ortam değişkenini ekleyin:
- Name: `QUOTE_FUNCTION_URL`
- Value: `https://<function-app-adiniz>.azurewebsites.net/api/GetRandomQuote`

**Web App → Configuration → General settings** kısmında Startup Command:
```
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

---

## 3. GitHub Reposu Oluşturma

1. GitHub'da yeni bir repo oluşturun (örn. `quote-app`).
2. Bu klasörün içeriğini push edin:
```bash
git init
git add .
git commit -m "İlk commit: alıntı uygulaması"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git
git push -u origin main
```

---

## 4. GitHub Actions ile Otomatik Deploy

### a) Publish Profile'ları indirin
Azure Portal'da:
- **Function App → Overview → "Get publish profile"** (.PublishSettings dosyası iner)
- **Web App → Overview → "Get publish profile"**

### b) GitHub Secrets ekleyin
Repo → **Settings → Secrets and variables → Actions → New repository secret**
- `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` → Function'ın publish profile içeriğini yapıştırın
- `AZURE_WEBAPP_PUBLISH_PROFILE` → Web App'in publish profile içeriğini yapıştırın

### c) Workflow dosyalarını güncelleyin
`.github/workflows/deploy-function.yml` içinde `AZURE_FUNCTIONAPP_NAME` değerini gerçek Function App adınızla değiştirin.
`.github/workflows/deploy-webapp.yml` içinde `AZURE_WEBAPP_NAME` değerini gerçek Web App adınızla değiştirin.

### d) Push edin
Değişiklikleri push ettiğinizde workflow'lar otomatik tetiklenir. **GitHub → Actions** sekmesinde çalıştığını görebilirsiniz — bu sayfanın ekran görüntüsünü alın (gereksinim c).

---

## 5. Son Kontrol Listesi (Dokümantasyon için)

- [ ] Web App Overview sayfası ekran görüntüsü
- [ ] Function App Overview sayfası ekran görüntüsü
- [ ] GitHub Actions (Actions sekmesi, yeşil tikli/başarılı workflow) ekran görüntüsü
- [ ] GitHub repo linki
- [ ] Yayındaki web app linki (örn. `https://<webapp-adiniz>.azurewebsites.net`)

Bu bilgileri topladıktan sonra bana iletin, sizin için Word dokümanını dolduracağım.
