    async function handleLogin() {
        if (!supabase) return document.getElementById('auth-error').innerText = "Unable to connect to Sangaia Secure Servers. Please ensure you have internet access and are not blocking scripts.";
        const email = document.getElementById('login-email').value;
        const pass = document.getElementById('login-password').value;
        const { data, error } = await supabase.auth.signInWithPassword({ email, password: pass });
        
        if (error) document.getElementById('auth-error').innerText = error.message;
    }

    async function handleSignup() {
        if (!supabase) return document.getElementById('auth-error').innerText = "Unable to connect to Sangaia Secure Servers. Please ensure you have internet access and are not blocking scripts.";
        const name = document.getElementById('signup-name').value;
        const dob = document.getElementById('signup-dob').value;
        const email = document.getElementById('signup-email').value;
        const pass = document.getElementById('signup-password').value;
        
        if(!name) return document.getElementById('auth-error').innerText = "Full Name is required.";

        const { data, error } = await supabase.auth.signUp({ email, password: pass });
        
        if (error) {
            document.getElementById('auth-error').innerText = error.message;
        } else if (data.user) {
            // Immediately insert citizen record
            const { error: insertError } = await supabase.from('sangaia_citizens').insert([{
                id: data.user.id,
                full_name: name,
                date_of_birth: dob || null
            }]);
            
            if (insertError) {
                console.error("Error creating citizen record:", insertError);
            }
            // Update UI after successful registration and insertion
            loadDashboard(data.user);
            if (typeof updateAuthWidget === 'function') updateAuthWidget();
        }
    }

    async function handleLogout() {
