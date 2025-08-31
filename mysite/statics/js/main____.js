document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();
        let target = this.getAttribute("data-target");
        
        // همه بخش‌ها رو مخفی کن
        document.querySelectorAll("section").forEach(sec => sec.style.display = "none");

        // فقط بخش موردنظر رو نشون بده
        document.getElementById(target).style.display = "block";
    });
});



