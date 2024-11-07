import calendar
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Function to generate a styled calendar for a given month and year
def generate_calendar(year, month):
    # Get the month calendar
    month_calendar = calendar.monthcalendar(year, month)

    # Create a figure and axis to plot the calendar
    fig, ax = plt.subplots(figsize=(10, 8))

    # Set the days of the week as labels, making them bold and bigger
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    ax.set_xticks(np.arange(7))
    ax.set_xticklabels(days_of_week, fontsize=14, ha='center', fontweight='bold', color='#2C3E50')

    # Set the title for the calendar (Month and Year)
    ax.set_title(f"{calendar.month_name[month]} {year}", fontsize=18, fontweight='bold', color="#2C3E50", pad=20)

    # Plot the calendar grid (7 columns for each day of the week)
    ax.set_yticks(np.arange(5))
    ax.set_yticklabels([])  # Hide y-axis ticks as we are showing days in the grid

    # Define a color palette for the days (using a gradient of colors)
    colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5', '#FFB6B9', '#F2A7B8']

    # Row and Column positioning for each day
    row = 0
    for week in month_calendar:
        for col, day in enumerate(week):
            if day != 0:  # Skip days that are 0 (empty cells)
                ax.text(col, row, str(day), ha='center', va='center', fontsize=12, 
                        color='white', fontweight='bold',
                        bbox=dict(facecolor=colors[(col + row) % len(colors)], edgecolor='black', boxstyle="round,pad=0.4"))
        row += 1

    # Remove the x and y axis lines and labels to make it look clean
    ax.set_xticks([])
    ax.set_yticks([])

    # Set the aspect ratio to be equal for square grid
    ax.set_aspect('equal')

    # Show grid lines only for the calendar cells
    ax.grid(True, which='both', axis='both', color='black', linestyle='-', linewidth=1)

    return fig

# Streamlit App
def app():
    st.title('Interactive Calendar')

    # Allow the user to select a year and month
    year = st.slider('Select Year', min_value=1900, max_value=2100, value=2024)
    month = st.selectbox('Select Month', options=[(i, calendar.month_name[i]) for i in range(1, 13)], index=11)

    # Generate and display the calendar
    fig = generate_calendar(year, month[0])
    st.pyplot(fig)

# Run the Streamlit app
if __name__ == "__main__":
    app()
