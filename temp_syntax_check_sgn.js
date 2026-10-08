
    function switchTab(tabId) {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        
        event.target.classList.add('active');
        document.getElementById('tab-' + tabId).classList.add('active');
    }

    // Auth UI Toggle
    let isLogin = true;
    function toggleAuthMode() {
        isLogin = !isLogin;
        document.getElementById('login-container').classList.toggle('hidden', !isLogin);
        document.getElementById('signup-container').classList.toggle('hidden', isLogin);
        document.getElementById('auth-error').innerText = '';
    }

    // Dashboard Data Loading
    async function loadDashboard(user) {
        if (!supabase) return;
        document.getElementById('auth-section').classList.add('hidden');
        document.getElementById('dashboard-section').classList.remove('hidden');
        
        document.getElementById('sensitive-email').innerText = user.email;

        // Fetch Citizen Record
        let { data: citizen, error } = await supabase
            .from('sangaia_citizens')
            .select('*')
            .eq('id', user.id)
            .single();
            
        if (!citizen && user.user_metadata) {
            // Lazy creation if email confirmation blocked it during signup
            const { data: newCitizen } = await supabase.from('sangaia_citizens').insert([{
                id: user.id,
                full_name: user.user_metadata.full_name || 'Citizen',
                date_of_birth: user.user_metadata.date_of_birth || null
            }]).select().single();
            if (newCitizen) citizen = newCitizen;
        }

        if (citizen) {
            document.getElementById('dash-name').innerText = citizen.full_name;
            document.getElementById('id-fullname').innerText = citizen.full_name;
            document.getElementById('id-number').innerText = citizen.sangaia_id_number;
            document.getElementById('id-dob').innerText = citizen.date_of_birth || 'N/A';
            document.getElementById('id-status').innerText = citizen.account_status;
            document.getElementById('id-issued').innerText = citizen.issue_date;
            
            // Set initial
            document.getElementById('id-initial').innerText = citizen.full_name.charAt(0).toUpperCase();
            
            // Pre-fill profile setting
            document.getElementById('update-name').value = citizen.full_name;
        } else {
            document.getElementById('dash-name').innerText = user.email;
            document.getElementById('id-fullname').innerText = "Record Not Found";
            // If they signed up via another method without a citizen record, we could prompt them to create one here.
        }

        loadBenefits(user.id);
    }

    // Benefits Management
    async function loadBenefits(userId) {
        if (!supabase) return;
        const { data: benefits, error } = await supabase
            .from('government_benefits')
            .select('*')
            .eq('citizen_id', userId);
            
        const listDiv = document.getElementById('benefits-list');
        if (benefits && benefits.length > 0) {
            let html = '<ul style="padding-left: 20px;">';
            benefits.forEach(b => {
                let color = b.status === 'Pending' ? '#f39c12' : (b.status === 'Approved' ? '#27ae60' : '#333');
                html += `<li style="margin-bottom: 10px;"><strong>${b.benefit_name}</strong> - <span style="color:${color}; font-weight:bold;">${b.status}</span><br><span style="font-size:0.85em; color:#666;">${b.description || ''}</span></li>`;
            });
            html += '</ul>';
            listDiv.innerHTML = html;
        } else {
            listDiv.innerHTML = '<p style="color: #888;">No active benefits or applications.</p>';
        }
    }

    async function applyForBenefit() {
        if (!supabase) return alert("Hema i fa'afeso'ota'i i le sapalai Sangaia.");
        const { data: { user } } = await supabase.auth.getUser();
        if (!user) return;

        const name = document.getElementById('benefit-name').value;
        const desc = document.getElementById('benefit-desc').value;
        
        if(!name) return alert("Please provide a benefit name.");

        const { error } = await supabase.from('government_benefits').insert([{
            citizen_id: user.id,
            benefit_name: name,
            description: desc,
            status: 'Pending'
        }]);

        if (error) {
            alert("Error applying: " + error.message);
        } else {
            document.getElementById('benefit-name').value = '';
            document.getElementById('benefit-desc').value = '';
            loadBenefits(user.id);
            alert("Application submitted successfully.");
        }
    }

    // Handlers
    async function handleLogin() {
        const errorDiv = document.getElementById('auth-error');
        if (!supabase) return errorDiv.innerText = "Le mafai ona feso'ota'i. Fa'amolemole siaki lau initaneti po'o le poloka o skripiti.";
        errorDiv.style.color = '#c62828';
        errorDiv.innerText = "";
        
        const email = document.getElementById('login-email').value;
        const pass = document.getElementById('login-password').value;
        const { data, error } = await supabase.auth.signInWithPassword({ email, password: pass });
        
        if (error) errorDiv.innerText = error.message;
    }

    async function handleSignup() {
        const errorDiv = document.getElementById('auth-error');
        if (!supabase) return errorDiv.innerText = "Le mafai ona feso'ota'i. Fa'amolemole siaki lau initaneti po'o le poloka o skripiti.";
        errorDiv.style.color = '#c62828';
        errorDiv.innerText = "";
        
        const name = document.getElementById('signup-name').value;
        const dob = document.getElementById('signup-dob').value;
        const email = document.getElementById('signup-email').value;
        const pass = document.getElementById('signup-password').value;
        
        if(!name) return errorDiv.innerText = "E mana'omia lou igoa atoa.";

        const { data, error } = await supabase.auth.signUp({ 
            email, 
            password: pass,
            options: {
                data: {
                    full_name: name,
                    date_of_birth: dob
                }
            }
        });
        
        if (error) {
            errorDiv.innerText = error.message;
        } else if (data.user) {
            if (!data.session) {
                errorDiv.style.color = '#0077be';
                errorDiv.innerText = "Fa'amanuiaina le resitala! Fa'amolemole siaki lau imeli e fa'amaonia ai lau teugatupe.";
            } else {
                const { error: insertError } = await supabase.from('sangaia_citizens').insert([{
                    id: data.user.id,
                    full_name: name,
                    date_of_birth: dob || null
                }]);
                
                if (insertError) console.error("Error creating citizen record:", insertError);
                loadDashboard(data.user);
                if (typeof updateAuthWidget === 'function') updateAuthWidget();
            }
        }
    }

    async function handleLogout() {
        if (!supabase) return;
        await supabase.auth.signOut();
        window.location.reload();
    }
    
    async function updateProfileName() {
        if (!supabase) return alert("Le mafai ona feso'ota'i i le sapalai.");
        const newName = document.getElementById('update-name').value;
        if(!newName) return;
        const { data: { user } } = await supabase.auth.getUser();
        
        const { error } = await supabase.from('sangaia_citizens').update({ full_name: newName }).eq('id', user.id);
        if(error) alert("Error: " + error.message);
        else {
            alert("Name updated successfully!");
            loadDashboard(user);
            updateAuthWidget(); // Update navbar
        }
    }

    // Init
    if (supabase) {
        supabase.auth.onAuthStateChange((event, session) => {
            if (session) {
                loadDashboard(session.user);
            } else {
                document.getElementById('auth-section').classList.remove('hidden');
                document.getElementById('dashboard-section').classList.add('hidden');
            }
        });
    } else {
        document.getElementById('auth-section').classList.remove('hidden');
        document.getElementById('dashboard-section').classList.add('hidden');
        document.getElementById('auth-error').innerText = "Le mafai ona feso'ota'i i le sapalai Sangaia. Fa'amolemole siaki lau initaneti po'o le poloka o skripiti.";
    }


