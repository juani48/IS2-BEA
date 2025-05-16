tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'bob-red': '#D10000',
                        'bob-dark-red': '#A30000',
                        'bob-light-red': '#FF3333',
                    }
                },
                fontFamily: {
                    'sans': ['Montserrat', 'sans-serif'],
                }
            }
        }

// Mobile menu toggle
        document.getElementById('mobile-menu-button').addEventListener('click', function() {
            document.getElementById('mobile-nav').classList.toggle('hidden');
        });
        
        // Reservation form handling
        document.getElementById('reservation-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Generate random reservation number
            const reservationNumber = 'R' + Math.floor(Math.random() * 10000).toString().padStart(4, '0');
            document.getElementById('reservation-number').textContent = reservationNumber;
            
            // Show modal
            document.getElementById('reservation-modal').classList.remove('hidden');
        });
        
        // Reserve buttons on machine cards
        document.querySelectorAll('.reserve-btn').forEach(button => {
            button.addEventListener('click', function() {
                const machineId = this.getAttribute('data-id');
                let machineName = '';
                
                switch(machineId) {
                    case '1':
                        machineName = 'Excavadora Compacta';
                        break;
                    case '2':
                        machineName = 'Retroexcavadora Industrial';
                        break;
                    case '3':
                        machineName = 'Minicargadora Versátil';
                        break;
                }
                
                // Scroll to reservation form
                document.getElementById('reserva').scrollIntoView({ behavior: 'smooth' });
                
                // Pre-select the machine in the dropdown
                const machineSelect = document.getElementById('machine-type');
                for(let i = 0; i < machineSelect.options.length; i++) {
                    if(machineSelect.options[i].text === machineName) {
                        machineSelect.selectedIndex = i;
                        break;
                    }
                }
            });
        });
        
        // Close modal
        document.getElementById('close-modal').addEventListener('click', function() {
            document.getElementById('reservation-modal').classList.add('hidden');
        });
        
        document.getElementById('confirm-modal').addEventListener('click', function() {
            document.getElementById('reservation-modal').classList.add('hidden');
            document.getElementById('reservation-form').reset();
        });
        
        // Date validation
        document.getElementById('start-date').addEventListener('change', function() {
            const startDate = new Date(this.value);
            const endDateInput = document.getElementById('end-date');
            
            // Set minimum end date to start date
            const minEndDate = new Date(startDate);
            minEndDate.setDate(minEndDate.getDate() + 1);
            
            endDateInput.min = minEndDate.toISOString().split('T')[0];
            
            // If end date is before new start date, reset it
            if(endDateInput.value && new Date(endDateInput.value) <= startDate) {
                endDateInput.value = '';
            }
        });
        
        // Set minimum start date to today
        const today = new Date();
        const tomorrow = new Date(today);
        tomorrow.setDate(tomorrow.getDate() + 1);
        
        document.getElementById('start-date').min = today.toISOString().split('T')[0];
        document.getElementById('end-date').min = tomorrow.toISOString().split('T')[0];
        
        // Duration selection affects end date
        document.getElementById('duration').addEventListener('change', function() {
            const startDateInput = document.getElementById('start-date');
            const endDateInput = document.getElementById('end-date');
            
            if(startDateInput.value) {
                const startDate = new Date(startDateInput.value);
                const duration = parseInt(this.value);
                
                if(duration) {
                    const endDate = new Date(startDate);
                    endDate.setDate(endDate.getDate() + duration);
                    endDateInput.value = endDate.toISOString().split('T')[0];
                }
            }
        });