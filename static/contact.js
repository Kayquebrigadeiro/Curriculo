document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    const message = document.getElementById('form-message');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = {
            nome: document.getElementById('nome').value,
            email: document.getElementById('email').value,
            assunto: document.getElementById('assunto').value,
            mensagem: document.getElementById('mensagem').value
        };
        
        try {
            const response = await fetch('/api/contato', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            const result = await response.json();
            
            if (response.ok) {
                message.innerHTML = '<div class="success">✅ Mensagem enviada com sucesso!</div>';
                form.reset();
            } else {
                message.innerHTML = '<div class="error">❌ Erro ao enviar mensagem.</div>';
            }
        } catch (error) {
            message.innerHTML = '<div class="error">❌ Erro de conexão.</div>';
        }
    });
});