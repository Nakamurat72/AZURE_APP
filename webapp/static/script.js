const btn = document.getElementById("new-quote-btn");
const quoteText = document.getElementById("quote-text");
const quoteAuthor = document.getElementById("quote-author");
const status = document.getElementById("status");

// Azure Function URL'niz
const API_URL = "https://nakamura-hvdnh9bqfkc4h2d2.italynorth-01.azurewebsites.net/api/GetRandomQuote";

async function fetchQuote() {
  status.textContent = "";
  btn.disabled = true;
  btn.textContent = "Yükleniyor...";

  try {
    // Yerel "/api/quote" yerine Azure Function URL'sine istek atıyoruz
    const res = await fetch(API_URL);
    
    if (!res.ok) {
      throw new Error("API yanıt vermedi.");
    }

    const data = await res.json();

    if (data.error) {
      status.textContent = data.error;
    } else {
      // NOT: Eğer Azure Function'dan gelen veri 'text' değil de 'quote' ise 
      // burayı data.quote olarak değiştirebilirsin.
      quoteText.textContent = `"${data.text || data.quote}"`;
      quoteAuthor.textContent = `— ${data.author || "Bilinmiyor"}`;
    }
  } catch (err) {
    status.textContent = "Bir hata oluştu, lütfen tekrar deneyin.";
    console.error("Hata detayı:", err);
  } finally {
    btn.disabled = false;
    btn.textContent = "Yeni Alıntı Getir";
  }
}

btn.addEventListener("click", fetchQuote);
