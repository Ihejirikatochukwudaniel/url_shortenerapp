// Copy to clipboard functionality
function copyToClipboard() {
    const urlInput = document.getElementById('shortUrl') || document.querySelector('input[readonly]');
    
    if (urlInput) {
        urlInput.select();
        urlInput.setSelectionRange(0, 99999); // For mobile devices
        
        try {
            document.execCommand('copy');
            
            // Show success feedback
            const button = event.target.closest('button');
            const originalText = button.innerHTML;
            
            button.innerHTML = '<i class="fas fa-check"></i> Copied!';
            button.classList.add('btn-success');
            button.classList.remove('btn-outline-primary');
            
            setTimeout(() => {
                button.innerHTML = originalText;
                button.classList.remove('btn-success');
                button.classList.add('btn-outline-primary');
            }, 2000);
            
        } catch (err) {
            console.error('Failed to copy: ', err);
            alert('Failed to copy URL. Please copy manually.');
        }
    }
}

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const urlInput = document.getElementById('url');
    
    if (form && urlInput) {
        form.addEventListener('submit', function(e) {
            const url = urlInput.value.trim();
            
            if (!url) {
                e.preventDefault();
                alert('Please enter a URL');
                return;
            }
            
            // Add loading state
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                const originalText = submitButton.innerHTML;
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Shortening...';
                submitButton.disabled = true;
                
                // Re-enable if there's an error
                setTimeout(() => {
                    submitButton.innerHTML = originalText;
                    submitButton.disabled = false;
                }, 5000);
            }
        });
        
        // Auto-focus on URL input
        urlInput.focus();
    }
});

// Auto-dismiss alerts
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert.classList.contains('show')) {
                alert.classList.remove('show');
                setTimeout(() => alert.remove(), 150);
            }
        }, 5000);
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});