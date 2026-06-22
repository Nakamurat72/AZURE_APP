const btn = document.getElementById("new-quote-btn");
const quoteText = document.getElementById("quote-text");
const quoteAuthor = document.getElementById("quote-author");
const status = document.getElementById("status");

async function fetchQuote() {
  status.textContent = "";
  btn.disabled = true;
  btn.textContent = "Yükleniyor...";

  try {
    const res = await fetch("/api/quote");
    const data = await res.json();

    if (data.error) {
      status.textContent = data.error;
    } else {
      quoteText.textContent = `"${data.text}"`;
      quoteAuthor.textContent = `— ${data.author}`;
    }
  } catch (err) {
    status.textContent = "Bir hata oluştu, lütfen tekrar deneyin.";
  } finally {
    btn.disabled = false;
    btn.textContent = "Yeni Alıntı Getir";
  }
}

btn.addEventListener("click", fetchQuote);
