import streamlit as st
import plotly.express as px
import pandas as pd

def piechart():

    # Sample data for the pie chart
    labels = ['Heart', 'Diabetes', 'Parkinsons']
    values = [303, 768, 195]

    # Calculate percentage values
    total = sum(values)
    percentages = [round((value / total) * 100, 2) for value in values]

    # Create the pie chart using Plotly Express
    fig = px.pie(names=labels, values=values, title='No. of data')

    # Show the chart
    st.plotly_chart(fig)

if __name__ == '__main__':
    piechart()


def affectedvsNonAffected():
    # Sample data for the bar graph
    Diseases = ['Heart', 'Diabetes', 'Parkinsons']
    affected_data = [165, 500, 147]  # Replace this with your actual data for the "Affected" group
    not_affected_data = [138, 268, 48]  # Replace this with your actual data for the "Not Affected" group

    # Combine data for "Affected" and "Not Affected" into a single DataFrame
    import pandas as pd
    df = pd.DataFrame({
        'Diseases': Diseases * 2,
        'Status': ['Affected'] * 3 + ['Not Affected'] * 3,
        'Value': affected_data + not_affected_data
    })

    # Create the bar graph using Plotly Express
    fig = px.bar(df, x='Diseases', y='Value', color='Status', barmode='group',
                 title='Affected vs. Not Affected Bar Graph')

    # Show the graph using Streamlit
    st.plotly_chart(fig)


    categories = ['Heart', 'Diabetes', 'Parkinsons']
    test = [0.819672131147541*100, 0.7727272727272727*100, 0.8717948717948718*100]
    training = [0.8512396694214877*100, 0.7833876221498371*100, 0.8717948717948718*100]

    # Create a DataFrame for the data
    import pandas as pd
    df = pd.DataFrame({'Diseases': categories, 'Test data': test, 'Training data': training})

    # Create the grouped bar graph using Plotly Express
    fig = px.bar(df, x='Diseases', y=['Test data', 'Training data'], barmode='group', title='Accuracy test')

    # Show the graph using Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    affectedvsNonAffected()

def grouped_bar_graph():
    # Sample data for the grouped bar graph
    categories = ['Heart', 'Diabetes', 'Parkinsons']
    test = [0.819672131147541*100, 0.7727272727272727*100, 0.8717948717948718*100]
    training = [0.8512396694214877*100, 0.7833876221498371*100, 0.8717948717948718*100]

    # Create a DataFrame for the data
    import pandas as pd
    df = pd.DataFrame({'Diseases': categories, 'Test data': test, 'Training data': training})

    # Create the grouped bar graph using Plotly Express
    fig = px.bar(df, x='Diseases', y=['Test data', 'Training data'], barmode='group', title='Accuracy test')

    # Show the graph using Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    grouped_bar_graph()


