from pyscript import document

def signup_logic(event):
    # 1. Grab values using the IDs from your HTML
    user = document.querySelector("#username").value
    pw = document.querySelector("#password").value
    confirm_pw = document.querySelector("#confirm-password").value
    
    # 2. Reference the output area (matches the div in your HTML)
    output = document.querySelector("#message")

    # 3. Logic: Check if username is too short
    if len(user) < 7:
        output.innerText = "Error: Username must be at least 7 characters!"
        output.style.color = "#EA5B6F" # Matches your Navbar color
        
    # 4. Logic: Check if passwords match
    elif pw != confirm_pw:
        output.innerText = "Error: Passwords do not match!"
        output.style.color = "#EA5B6F"
        
    # 5. Success
    elif user and pw:
        output.innerText = "Account created successfully!"
        output.style.color = "#28a745" # Success Green
    
    else:
        output.innerText = "Please fill in all fields."
