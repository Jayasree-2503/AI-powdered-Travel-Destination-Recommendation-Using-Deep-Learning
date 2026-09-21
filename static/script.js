/**
 * AI Travel Destination Recommender - Client Side Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Duration Increment / Decrement Counter
    const durInput = document.getElementById('duration');
    const durDecBtn = document.getElementById('durDec');
    const durIncBtn = document.getElementById('durInc');

    if (durInput && durDecBtn && durIncBtn) {
        durDecBtn.addEventListener('click', () => {
            let currentVal = parseInt(durInput.value, 10) || 1;
            if (currentVal > 1) {
                durInput.value = currentVal - 1;
            }
        });

        durIncBtn.addEventListener('click', () => {
            let currentVal = parseInt(durInput.value, 10) || 1;
            if (currentVal < 30) {
                durInput.value = currentVal + 1;
            }
        });

        durInput.addEventListener('change', () => {
            let val = parseInt(durInput.value, 10);
            if (isNaN(val) || val < 1) durInput.value = 1;
            if (val > 30) durInput.value = 30;
        });
    }

    // 2. Form Submission & Loading Spinner State
    const recommendForm = document.getElementById('recommendForm');
    const submitBtn = document.getElementById('submitBtn');

    if (recommendForm && submitBtn) {
        recommendForm.addEventListener('submit', (e) => {
            // Check all select elements are selected
            const selects = recommendForm.querySelectorAll('select[required]');
            let allValid = true;

            selects.forEach(select => {
                if (!select.value) {
                    allValid = false;
                    select.focus();
                }
            });

            if (allValid) {
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                // Form submits naturally
                recommendForm.submit();
            }
        });
    }

    // 3. Smooth animation for confidence bar on result page
    const confBar = document.querySelector('.confidence-bar-fill');
    if (confBar) {
        const targetWidth = confBar.style.width;
        confBar.style.width = '0%';
        setTimeout(() => {
            confBar.style.width = targetWidth;
        }, 150);
    }
});
