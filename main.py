from pyscript import document

def general_weighted_average(e=None):
    """
    Calculate the General Weighted Average based on input grades.
    This function retrieves student information and grades, calculates the GWA,
    and displays the results.
    """
    try:
        # Clear previous results
        document.getElementById("student_info").innerText = ""
        document.getElementById("summary").innerText = ""
        document.getElementById("output").innerText = ""
        document.getElementById("status").innerText = ""
        
        # Get input values
        science = document.getElementById("science").value
        math = document.getElementById("math").value
        english = document.getElementById("english").value
        filipino = document.getElementById("filipino").value
        ict = document.getElementById("ict").value
        pe = document.getElementById("pe").value
        first_name = document.getElementById("fname").value
        last_name = document.getElementById("lname").value
        
        # Validate required fields
        if not first_name or not last_name:
            document.getElementById("output").innerText = "Please enter your first and last name."
            return
        
        # Check if all grades are entered
        if not all([science, math, english, filipino, ict, pe]):
            document.getElementById("output").innerText = "Please enter all grade values."
            return
        
        try:
            # Convert to numbers
            science = float(science)
            math = float(math)
            english = float(english)
            filipino = float(filipino)
            ict = float(ict)
            pe = float(pe)
            
            # Validate grade range
            grades = [science, math, english, filipino, ict, pe]
            for grade in grades:
                if grade < 0 or grade > 100:
                    document.getElementById("output").innerText = "Grades must be between 0 and 100."
                    return
            
            # Define subject weights
            # Calculate weighted sum
            weighted_sum = (science * 5) + (math * 5) + (english * 5) + (filipino * 3) + (ict * 2) + (pe * 1)
            
            # Calculate total units
            total_units = (5 + 5 + 5 + 3 + 2 + 1)  # Sum of all weights
            
            # Calculate GWA
            gwa = weighted_sum / total_units
            
            # Create summary of grades
            subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
            grades_list = [science, math, english, filipino, ict, pe]
            
            summary = ""
            for i in range(len(subjects)):
                summary += f"{subjects[i]}: {grades_list[i]:.0f}\n"
            
            # Display results
            document.getElementById("student_info").innerText = f"Student: {first_name} {last_name}"
            document.getElementById("summary").innerText = summary
            document.getElementById("output").innerText = f"General Weighted Average: {gwa:.2f}"
            
            # Determine pass/fail status (assuming passing is 75 and above)
            if gwa >= 75:
                document.getElementById("status").innerText = "✅ Status: PASSED"
                document.getElementById("status").className = "passed"
            else:
                document.getElementById("status").innerText = "❌ Status: FAILED"
                document.getElementById("status").className = "failed"
                
        except ValueError:
            document.getElementById("output").innerText = "Invalid input. Please enter numeric values for all grades."
            
    except Exception as error:
        document.getElementById("output").innerText = f"An error occurred: {str(error)}"

# Dictionary of club information (from Skills Test)
clubs_data = {
    "glee": {
        "name": "GLEE CLUB",
        "description": "A choral group that performs at school events.",
        "meeting_time": "Monday 03:00-05:00 PM",
        "location": "High School Music Room",
        "moderator": "Mr. Denver Martin",
        "category": "Non-academic"
    },
    "dance": {
        "name": "DANCE CLUB",
        "description": "Learn various dance styles and perform at school events.",
        "meeting_time": "Tuesday 03:00-05:00 PM",
        "location": "Teatro Preciosa",
        "moderator": "Mr. Alfred Cases",
        "category": "Non-academic"
    },
    "math": {
        "name": "MATH CLUB",
        "description": "Engage in mathematical problem solving and prepare for competitions.",
        "meeting_time": "Monday 02:30-03:00 PM",
        "location": "Room 404",
        "moderator": "Mr. Nicole Gabuya",
        "category": "Academic"
    },
    "communications": {
        "name": "COMMUNICATION ARTS CLUB",
        "description": "Develop skills in public speaking, debate, and media communication.",
        "meeting_time": "Wednesday 03:00-04:00 PM, Friday 03:00-04:00 PM",
        "location": "Room 406",
        "moderator": "Ms. Yannis Fernandez",
        "category": "Academic"
    },
    "social": {
        "name": "SOCIAL SCIENCE CLUB",
        "description": "Discuss and explore topics in history, geography, and social sciences.",
        "meeting_time": "Tuesday 03:00-04:00 PM",
        "location": "Room 409",
        "moderator": "Mr. Roberto Lim",
        "category": "Academic"
    },
    "volleyball": {
        "name": "VOLLEYBALL VARSITY",
        "description": "Competitive volleyball team representing the school in tournaments.",
        "meeting_time": "Wednesday 03:00-04:00 PM",
        "location": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "category": "Non-academic"
    }
}

def display_club_info(e=None):
    """
    Display information for the selected club.
    This function retrieves the selected club from the dropdown
    and displays its information in the message area.
    """
    try:
        # Get the selected club value from the dropdown
        club_select = document.getElementById("clubs")
        selected_value = club_select.value
        
        if not selected_value:
            # If no club is selected
            message_div = document.getElementById("message")
            message_div.innerHTML = "<strong>Please select a club from the dropdown menu.</strong>"
            return
        
        # Get club data from the dictionary
        club = clubs_data.get(selected_value)
        
        if club:
            # Format the club information
            club_info = f"""
            <h4>{club['name']}</h4>
            <p><strong>Description:</strong> {club['description']}</p>
            <p><strong>Meeting Time:</strong> {club['meeting_time']}</p>
            <p><strong>Location:</strong> {club['location']}</p>
            <p><strong>Moderator/Advisor:</strong> {club['moderator']}</p>
            <p><strong>Category:</strong> {club['category']}</p>
            """
            
            # Display the information
            message_div = document.getElementById("message")
            message_div.innerHTML = club_info
        else:
            message_div = document.getElementById("message")
            message_div.innerHTML = "<strong>Club information not found.</strong>"
    
    except Exception as error:
        # Handle any errors
        message_div = document.getElementById("message")
        message_div.innerHTML = f"<strong>Error loading club information:</strong> {str(error)}"


# Initialization func
def setup():
    """
    Initialize the application.
    This function sets up event listeners and initial states.
    """
    try:
        # Set up event listeners for buttons
        compute_button = document.getElementById("compute-btn")
        if compute_button:
            compute_button.onclick = general_weighted_average
            
        info_button = document.getElementById("get-info-btn")
        if info_button:
            info_button.onclick = display_club_info
        
        # Initial message for club info
        message_div = document.getElementById("message")
        if message_div:
            message_div.innerHTML = "<strong>Select a club to see information here...</strong>"
        
        print("OB Montessori School Website initialized successfully!")
        
    except Exception as error:
        print(f"Setup error: {error}")

# Run setup when the page loads
setup()
