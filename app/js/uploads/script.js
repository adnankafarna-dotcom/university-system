/* ==========================================
   نظام الجامعة الذكي - JavaScript
   Smart University System - Interactive Features
   ========================================== */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Dark Mode
    initDarkMode();
    
    // Initialize Tooltips
    initBootstrapTooltips();
    
    // Smooth scrolling
    initSmoothScroll();
    
    // Form validation
    initFormValidation();
});

/* ==========================================
   Dark Mode Toggle
   ========================================== */

function initDarkMode() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    
    // Load saved preference
    const savedMode = localStorage.getItem('darkMode');
    if (savedMode === 'true') {
        body.classList.add('dark-mode');
        if (darkModeToggle) {
            darkModeToggle.checked = true;
            darkModeToggle.innerHTML = '<i class="bi bi-sun-fill"></i>';
        }
    }
    
    // Toggle dark mode
    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', function() {
            body.classList.toggle('dark-mode');
            localStorage.setItem('darkMode', body.classList.contains('dark-mode'));
            
            // Update icon
            const icon = this.closest('button');
            if (body.classList.contains('dark-mode')) {
                icon.innerHTML = '<i class="bi bi-sun-fill"></i>';
                icon.setAttribute('title', 'Light Mode');
            } else {
                icon.innerHTML = '<i class="bi bi-moon-fill"></i>';
                icon.setAttribute('title', 'Dark Mode');
            }
        });
    }
}

/* ==========================================
   Bootstrap Tooltips
   ========================================== */

function initBootstrapTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/* ==========================================
   Smooth Scrolling
   ========================================== */

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                document.querySelector(href).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
}

/* ==========================================
   Bootstrap Form Validation
   ========================================== */

function initFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}

/* ==========================================
   Utility Functions
   ========================================== */

// Show toast notification
function showToast(message, type = 'info', duration = 3000) {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} position-fixed bottom-0 end-0 m-3`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = message;
    toast.style.zIndex = '9999';
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, duration);
}

// Debounce function
function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}

// Format date
function formatDate(date, locale = 'en-US') {
    return new Date(date).toLocaleDateString(locale, {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Load spinner
function showSpinner() {
    const spinner = document.createElement('div');
    spinner.className = 'spinner-border text-primary position-fixed top-50 start-50 translate-middle';
    spinner.id = 'loadingSpinner';
    document.body.appendChild(spinner);
}

function hideSpinner() {
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.remove();
}

/* ==========================================
   AJAX Helpers
   ========================================== */

// Fetch helper with error handling
async function fetchAPI(url, options = {}) {
    try {
        showSpinner();
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        
        const data = await response.json();
        hideSpinner();
        return data;
    } catch (error) {
        hideSpinner();
        showToast(`Error: ${error.message}`, 'danger');
        throw error;
    }
}

/* ==========================================
   Table Features
   ========================================== */

// Sort table column
function sortTable(columnIndex) {
    const table = document.querySelector('table');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    rows.sort((a, b) => {
        const aVal = a.cells[columnIndex].textContent.trim();
        const bVal = b.cells[columnIndex].textContent.trim();
        
        return isNaN(aVal) ? 
            aVal.localeCompare(bVal) : 
            parseFloat(aVal) - parseFloat(bVal);
    });
    
    rows.forEach(row => tbody.appendChild(row));
}

// Filter table rows
function filterTable(searchTerm) {
    const table = document.querySelector('table');
    const rows = table.querySelectorAll('tbody tr');
    const term = searchTerm.toLowerCase();
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(term) ? '' : 'none';
    });
}

/* ==========================================
   Form Helpers
   ========================================== */

// Get form data as object
function getFormData(form) {
    const formData = new FormData(form);
    const data = {};
    
    formData.forEach((value, key) => {
        if (key in data) {
            if (!Array.isArray(data[key])) {
                data[key] = [data[key]];
            }
            data[key].push(value);
        } else {
            data[key] = value;
        }
    });
    
    return data;
}

// Reset form
function resetForm(formId) {
    document.getElementById(formId).reset();
}

// Clear form errors
function clearFormErrors(formId) {
    const form = document.getElementById(formId);
    form.querySelectorAll('.invalid-feedback').forEach(el => {
        el.style.display = 'none';
    });
    form.classList.remove('was-validated');
}

/* ==========================================
   File Upload Preview
   ========================================== */

function setupFilePreview(fileInputId, previewId) {
    const fileInput = document.getElementById(fileInputId);
    const preview = document.getElementById(previewId);
    
    if (!fileInput || !preview) return;
    
    fileInput.addEventListener('change', function() {
        const file = this.files[0];
        
        if (file) {
            const reader = new FileReader();
            
            reader.onload = (e) => {
                if (file.type.startsWith('image/')) {
                    preview.innerHTML = `<img src="${e.target.result}" class="img-fluid rounded" alt="Preview">`;
                } else {
                    preview.innerHTML = `<div class="alert alert-info">
                        <i class="bi bi-file-earmark"></i>
                        ${file.name}
                    </div>`;
                }
            };
            
            reader.readAsDataURL(file);
        }
    });
}

/* ==========================================
   Modal Helpers
   ========================================== */

// Open modal
function openModal(modalId) {
    const modal = new bootstrap.Modal(document.getElementById(modalId));
    modal.show();
}

// Close modal
function closeModal(modalId) {
    const modal = bootstrap.Modal.getInstance(document.getElementById(modalId));
    if (modal) modal.hide();
}

/* ==========================================
   Countdown Timer
   ========================================== */

function startCountdown(duration, elementId) {
    const countdownElement = document.getElementById(elementId);
    if (!countdownElement) return;
    
    let remaining = duration;
    
    const interval = setInterval(() => {
        const minutes = Math.floor(remaining / 60);
        const seconds = remaining % 60;
        
        countdownElement.textContent = 
            `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
        
        if (remaining <= 0) {
            clearInterval(interval);
            countdownElement.textContent = 'Time\'s up!';
        }
        
        remaining--;
    }, 1000);
}

/* ==========================================
   Export Data
   ========================================== */

// Export table to CSV
function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    const csv = [];
    
    // Get headers
    const headers = [];
    table.querySelectorAll('thead th').forEach(th => {
        headers.push(`"${th.textContent}"`);
    });
    csv.push(headers.join(','));
    
    // Get rows
    table.querySelectorAll('tbody tr').forEach(tr => {
        const row = [];
        tr.querySelectorAll('td').forEach(td => {
            row.push(`"${td.textContent}"`);
        });
        csv.push(row.join(','));
    });
    
    // Download
    const csvContent = 'data:text/csv;charset=utf-8,' + csv.join('\n');
    const link = document.createElement('a');
    link.setAttribute('href', encodeURI(csvContent));
    link.setAttribute('download', filename);
    link.click();
}

/* ==========================================
   Print Helpers
   ========================================== */

function printElement(elementId) {
    const element = document.getElementById(elementId);
    const printWindow = window.open('', '', 'width=800,height=600');
    
    printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
            <style>
                body { margin: 20px; }
                @media print {
                    .no-print { display: none; }
                }
            </style>
        </head>
        <body>
            ${element.innerHTML}
            <script>
                window.print();
                window.close();
            </script>
        </body>
        </html>
    `);
}

/* ==========================================
   Notification System
   ========================================== */

class NotificationManager {
    static notify(message, type = 'info', duration = 3000) {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
        alert.setAttribute('role', 'alert');
        alert.style.zIndex = '9999';
        alert.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(alert);
        
        setTimeout(() => {
            alert.remove();
        }, duration);
    }
    
    static success(message) {
        this.notify(message, 'success');
    }
    
    static error(message) {
        this.notify(message, 'danger');
    }
    
    static warning(message) {
        this.notify(message, 'warning');
    }
    
    static info(message) {
        this.notify(message, 'info');
    }
}
