import calendar
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def generate_calendar(year, month):
    # Get the month calendar (list of weeks with day numbers)
    month_calendar = calendar.monthcalendar(year, month)
    
    # Create a figure for plotting
    fig, ax = plt.subplots(figsize=(10, 8))

    # Set the days of the week (Mon, Tue, ..., Sun)
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    ax.set_xticks(np.arange(7))
    ax.set_xticklabels(days_of_week, fontsize=14, ha='center', fontweight='bold', color='#2C3E50')

    # Title for the calendar (Month and Year)
    ax.set_title(f"{calendar.month_name[month]} {year}", fontsize=18, fontweight='bold', color="#2C3E50", pad=20)

    # Set the y-axis to empty (as days will fill the grid)
    ax.set_yticks(np.arange(5))
    ax.set_yticklabels([])  # No labels on y-axis

    # Define a color palette for the days to give it a colorful, soft look
    day_colors = ['#FAD02E', '#F28D35', '#D83367', '#335DFF', '#44D2C2', '#FFC03B', '#FA6B6B']
    
    # Loop through the weeks and days in the month calendar
    row = 0
    for week in month_calendar:
        for col, day in enumerate(week):
            if day != 0:  # Skip days that are 0 (empty cells in the grid)
                ax.text(col, row, str(day), ha='center', va='center', fontsize=12, 
                        color='white', fontweight='bold',
                        bbox=dict(facecolor=day_colors[(col + row) % len(day_colors)], edgecolor='black', boxstyle="round,pad=0.5"))
        row += 1

    # Remove the axis ticks and set the aspect ratio to make the grid square
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    # Optional: Show gridlines inside the calendar cells
    ax.grid(True, which='both', axis='both', color='black', linestyle='-', linewidth=1)

    return fig

# Streamlit UI
def app():
    # Title of the app
    st.title('Interactive Calendar')

    # Slider to select the year
    year = st.slider('Select Year', min_value=1900, max_value=2100, value=2024)

    # Dropdown menu to select the month
    month = st.selectbox('Select Month', options=[(i, calendar.month_name[i]) for i in range(1, 13)], index=11)

    # Generate and display the calendar
    fig = generate_calendar(year, month[0])
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    app()
