// Animações ao fazer scroll
document.addEventListener('DOMContentLoaded', function() {
    // Animar elementos quando entram na tela
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationDelay = '0s';
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observar todas as seções
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });

    // Animar itens de contato em sequência
    const contactItems = document.querySelectorAll('.contact-item');
    contactItems.forEach((item, index) => {
        item.style.animationDelay = `${0.6 + (index * 0.1)}s`;
    });

    // Animar barras de habilidade quando visíveis
    const skillBars = document.querySelectorAll('.skill-level');
    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const skillLevel = entry.target;
                const width = skillLevel.style.width;
                skillLevel.style.setProperty('--skill-width', width);
                skillLevel.classList.add('animate-skill');
            }
        });
    }, observerOptions);

    skillBars.forEach(bar => {
        skillObserver.observe(bar);
    });

    // Animar qualidades em sequência
    const qualidades = document.querySelectorAll('.qualidades-list li');
    qualidades.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
    });
});