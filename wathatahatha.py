import streamlit as st

st.title("T20 World Cup 2024 Prediction Game")

# Group stage
st.header("Group Stage")

group_a_teams = ["India", "Pakistan", "Ireland", "Canada", "USA"]  # Group A teams
group_b_teams = ["England", "Australia", "Namibia", "Scotland", "Oman"]  # Group B teams
group_c_teams = ["West Indies", "New Zealand", "Afghanistan", "Papua New Guinea", "United States"]  # Group C teams
group_d_teams = ["South Africa", "Sri Lanka", "Bangladesh", "Netherlands", "Nepal"]  # Group D teams

def select_top_2(group_name, teams):
    st.subheader(f"{group_name}")
    top_2 = st.multiselect(f"Select First & Second positions from {group_name}", teams, max_selections=2)  # Set max_selections to 2
    if len(top_2) != 2:
        st.warning(f"Please select exactly 2 teams (First & Second positions) from {group_name}")
    return top_2 if len(top_2) == 2 else None

top_a = select_top_2("Group A", group_a_teams.copy())  # Separate selections for position
top_b = select_top_2("Group B", group_b_teams.copy())
top_c = select_top_2("Group C", group_c_teams.copy())
top_d = select_top_2("Group D", group_d_teams.copy())

if None in [top_a, top_b, top_c, top_d]:
    st.warning("Please select exactly 2 teams (First & Second positions) from all groups.")
else:
    top_a_1, top_a_2 = top_a
    top_b_1, top_b_2 = top_b
    top_c_1, top_c_2 = top_c
    top_d_1, top_d_2 = top_d

    # Super 8
    st.header("Super 8")

    super_8_group_1 = [top_a_1, top_b_2, top_c_1, top_d_2]
    super_8_group_2 = [top_a_2, top_b_1, top_c_2, top_d_1]

    def select_top_2_from_group(group_name, group_teams):
        st.subheader(f"{group_name}")
        top_2 = st.multiselect(f"Select Top 2 from {group_name}", group_teams, max_selections=2)  # Set max_selections to 2
        if len(top_2) != 2:
            st.warning(f"Please select exactly 2 teams from {group_name}")
        return top_2 if len(top_2) == 2 else None

    top_2_group_1 = select_top_2_from_group("Super 8 Group 1", super_8_group_1)
    top_2_group_2 = select_top_2_from_group("Super 8 Group 2", super_8_group_2)

    if None in [top_2_group_1, top_2_group_2]:
        st.warning("Please select exactly 2 teams from Super 8 Groups.")
    else:
        # Semi-finals
        st.header("Semi-finals")

        semi_final_1 = f"{top_2_group_1[0]} vs {top_2_group_2[1]}"
        semi_final_2 = f"{top_2_group_1[1]} vs {top_2_group_2[0]}"

        semi_final_1_winner = st.radio("Winner of Semi-final 1", [top_2_group_1[0], top_2_group_2[1]])
        semi_final_2_winner = st.radio("Winner of Semi-final 2", [top_2_group_1[1], top_2_group_2[0]])

        if semi_final_1_winner and semi_final_2_winner:
            # Finals
            st.header("Finals")

            final_teams = [semi_final_1_winner, semi_final_2_winner]
            final_winner = st.radio("Winner of the Final", final_teams)

            st.subheader(f"Congratulations to {final_winner} for winning the T20 World Cup 2024!")
