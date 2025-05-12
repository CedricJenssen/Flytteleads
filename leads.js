
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("leadForm");

    form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    try {
      const response = await fetch("http://localhost:8000/send-lead", {
        method: "POST",
        body: formData
      });

      const result = await response.json();

      window.location.href = "/takk.html";

      alert(result.message);
    } catch (err) {
      console.error("Feil ved innsending:", err);
    }
  });
});

