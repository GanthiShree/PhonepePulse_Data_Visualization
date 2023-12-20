from tkinter import OptionMenu
import pymysql
import pandas as pd
import geopandas as gpd
import plotly
import plotly.express as px
import json
import plotly.graph_objects as go
import streamlit as st
from streamlit_option_menu import option_menu

# MySQL connection
mysql_connection  =  pymysql.connect(host = "127.0.0.1",
                                user='root',
                                passwd='Nisha@130899',
                                database ="PhonePe",
                                autocommit=True)                                
mysql_cursor  = mysql_connection.cursor()

# Fetching datas from SQL
mysql_cursor.execute('select * from Aggregated_Transaction_Data')
mysql_connection.commit()
Table_1 = mysql_cursor.fetchall()
Aggregated_Transaction = pd.DataFrame(Table_1,columns=['State', 'Year','Quater','Transaction_type', 'Transaction_count', 'Transaction_amount'])

mysql_cursor.execute('select * from Aggregated_User_Data')
mysql_connection.commit()
Table_2 = mysql_cursor.fetchall()
Aggregated_User = pd.DataFrame(Table_2,columns = ['State', 'Year','Quater','Registered_Users', 'App_open_no','Device','Count', 'Share_Percentage'])

mysql_cursor.execute('select * from Map_Transaction_Data')
mysql_connection.commit()
Table_3 = mysql_cursor.fetchall()
Map_Transaction = pd.DataFrame(Table_3,columns= ["State",'Year','Quater',"District","No_of_Transaction","Total_amount"])

mysql_cursor.execute('select * from Map_User_Data')
mysql_connection.commit()
Table_4 = mysql_cursor.fetchall()
Map_User = pd.DataFrame(Table_4,columns=["State",'Year','Quater',"District","Registered_Users","App_open_no"])

mysql_cursor.execute('select * from Top_Transaction_data')
mysql_connection.commit()
Table_5 = mysql_cursor.fetchall()
Top_Transaction = pd.DataFrame(Table_5, columns=["State", 'Year','Quater',"Pincode", "Total_No_Of_Transactions", "Total_Amount"])

mysql_cursor.execute('select * from Top_User_data')
mysql_connection.commit()
Table_6 = mysql_cursor.fetchall()
Top_Users = pd.DataFrame(Table_6, columns=["State", 'Year','Quater',"Districts","Users"])

mysql_cursor.execute('select * from Top_Ur_Pincode_data')
mysql_connection.commit()
Table_7 = mysql_cursor.fetchall()
Top_ur_pin = pd.DataFrame(Table_7,columns=["State", 'Year','Quater',"Pincode","Users"])

# Streamlit :
st.set_page_config(layout='wide')
col1, col2 , col3 = st.columns([1, 3, 5])
with col1:
    logo_image = "https://raw.githubusercontent.com/Palemravichandra/phonepe-pulse-data-visualisation/master/images/phonepe.png"
    st.image(logo_image, use_column_width=False, width=100)
with col2:
    title_text = ":violet[PhonePe Pluse |]"
    additional_text = "The Beata of progress"
# Concatenate strings
    combined_text = f"{title_text} {additional_text}"
    st.subheader(combined_text)
with col3:
        selected = option_menu(
            menu_title = None,
            options=["Home","Data API's","Explore Data","Analysis"],
            default_index= 0,
            icons =["house","reception-4","graph-up-arrow","activity"],
            orientation="horizontal",
            styles={
            "container": {"background-color": "violet","size":"cover"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": { "--hover-color": "purple","color": "white"},
            "nav-link-selected": {"background-color": "purple"}
            }           
        )
if selected== "Data API's":
        col4,col5 = st.columns(2)
        with col4:
            st.title (":violet[Introduction]")
            st.markdown("""
                            - **The Indian digital payments story has truly captured the world's imagination.**
                            - **From the largest towns to the remotest villages, 
                                there is a payments revolution being driven by the penetration of mobile phones, 
                                mobile internet and state-of-the-art payments infrastructure built as Public Goods championed 
                                by the central bank and the government.**
                            - **Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India.**
                            - **When we started, we were constantly looking for granular and definitive data sources on digital payments in India.**
                            - **PhonePe Pulse is our way of giving back to the digital payments ecosystem.**
                    """)
        with col5:
               ad = "https://pbs.twimg.com/media/D4QJf0bUYAA-UL_.png"
               st.image(ad, use_column_width=True)
        col9,col10,col11 = st.columns([5,1,1])
        with col9:
            st.title(":violet[GUIDE]")
            st.subheader("This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab.")
            col6,col7,col8 = st.columns([4,3,3])
            with col6:
                    st.header(":violet[1. Aggregated]")
                    st.subheader("   Aggregated values of various payment categories as shown under Categories section")
            with col7:
                    st.header(":violet[2. Map]")
                    st.subheader("   Total values at the State and District levels")      
            with col8:
                    st.header(":violet[3. Top]")
                    st.subheader("   Totals of top States / Districts / Postal Codes")   
if selected== "Analysis":
    st.title("Analysis of the Datas")
    st.subheader("Analysis in Table and Graph view")
    options = ["--select a query--","Determine the leading states each year, considering transaction amounts",
               "Determine the least-performing states based on both type and volume of transactions.",
               "Leading states categorized by transaction type and corresponding transaction count.",
               "Highlight the top states, districts, and postal codes along with their respective transaction values.",
               "Find the districts with the lowest transaction amounts, considering both states and transaction volumes.",
               "Determine the least-engaged registered users based on their districts and states.",
               "Top 10 transactions_type based on states and transaction_amount"
               "Rank mobile brands in the top 10 percentile in terms of transaction percentage."]
    query = st.selectbox("Select the option",options)
    if query == "Determine the leading states each year, considering transaction amounts":
        mysql_cursor.execute('''
            SELECT State, Year, SUM(Transaction_amount) AS Transaction_amount, Quater
            FROM Aggregated_Transaction_Data
            GROUP BY State, Year,Quater
            ORDER BY Transaction_amount DESC
            LIMIT 10''')
        df = pd.DataFrame(mysql_cursor.fetchall(),columns=['State','Year','Transaction_amount','Quater'])
        col1,col2 = st.columns([1,2], gap="large")
        with col1:
            # Display results in table view
            st.write(df)
        with col2:
            # Display results in bar chart view
            fig = px.bar(df, x='State', y='Transaction_amount', color='Year', title='Top States by Transaction Amount')
            st.plotly_chart(fig)

    if query == "Determine the least-performing states based on both type and volume of transactions":
        mysql_cursor.execute('''
            SELECT State,Year,Quater,Transaction_type, SUM(Transaction_count) AS Total_Count
            FROM Aggregated_Transaction_Data
            GROUP BY State,Year,Quater,Transaction_type
            ORDER BY Total_Count ASC
            LIMIT 10''')
        df = pd.DataFrame(mysql_cursor.fetchall(),columns=['State','Year','Quater','Transaction_type',"Total_Count"])
        col1,col2 = st.columns([1,2])
        with col1:
            # Display results in table view
            st.write(df)
        with col2:
            # Display results in bar chart view
            fig = px.bar(df, x='State', y='Total_Count', color='Transaction_type', title='Least Performing States by Transaction Count')
            st.plotly_chart(fig)

    # Repeat the above structure for other options
    if query == "Leading states categorized by transaction type and corresponding transaction count":
        mysql_cursor.execute('''
            SELECT State, Transaction_type, SUM(Transaction_count) AS Transaction_count
            FROM Aggregated_Transaction_Data
            GROUP BY State, Transaction_type
            ORDER BY Transaction_count DESC''')
        df = pd.DataFrame(mysql_cursor.fetchall(),columns=['State','Transaction_type',"Transaction_count"])
        col1,col2 = st.columns(2)
        with col1:
            # Display results in table view
            st.write(df)
        with col2:
            # Display results in bar chart view
            fig = px.line(df, x='State', y='Total_Count', color='Transaction_type', title='Transaction Type Distribution by State')
            st.plotly_chart(fig)

    # Repeat the above structure for other options

    if query == "Highlight the top states, districts, and postal codes along with their respective transaction values":
        merged_df = pd.merge(Top_Transaction, Top_Users, on=["State", "Year", "Quater"])
        mysql_cursor.execute('''
            SELECT State, SUM(Total_No_Of_Transactions) AS Total_Amount, Districts, Pincode
            FROM Top_Transaction_data t
            JOIN Top_User_data u ON t.State = u.State AND t.Year = u.Year AND t.Quater = u.Quater
            GROUP BY State, Districts, Pincode
            ORDER BY Total_Amount DESC
            LIMIT 10''')
        df = pd.DataFrame(mysql_cursor.fetchall(), columns=['State', "Total_Amount", "Districts", "Pincode"])
        
        col1, col2 = st.columns(2)
        with col1:
            # Display results in table view
            st.write(df)
        
        with col2:
            # Display results in pie chart view
            fig = px.pie(df, names='State', values='Total_Amount', title='Top States by Transaction Amount')
            st.plotly_chart(fig)

    # Repeat the above structure for other options

    if query == "Find the districts with the lowest transaction amounts, considering both states and transaction volumes":
        mysql_cursor.execute('''
            SELECT State, District, MIN(No_of_Transaction) AS Min_Transaction
            FROM Map_Transaction_Data
            GROUP BY State, District
            ORDER BY Min_Transaction ASC
            LIMIT 10''');
        df = pd.DataFrame(mysql_cursor.fetchall(),columns=['State',"Districts","Min_Transaction"])
        col1,col2 = st.columns(2)
        with col1:
            # Display results in table view
            st.write(df)
        with col2:        
            # Display results in bar chart view
            fig = px.bar(df, x='State', y='Min_Transaction', color='District', title='Districts with Lowest Transaction Amounts')
            st.plotly_chart(fig)

    # Repeat the above structure for other options

    if query == "Determine the least-engaged registered users based on their districts and states":
        mysql_cursor.execute('''
            SELECT State, District, MIN(Registered_Users) AS Min_Users
            FROM Map_User_Data
            GROUP BY State, District
            ORDER BY Min_Users ASC
            LIMIT 10''')
        df = pd.DataFrame(mysql_cursor.fetchall(),columns=['State',"District","Min_Users"])
        col1,col2 = st.columns(2)
        with col1:
            # Display results in table view
            st.write(df)
        with col2:        
        # Display results in line chart view
            fig = px.line(df, x='State', y='Min_Users', color='District', title='Least-Engaged Registered Users')
            st.plotly_chart(fig)

    # Repeat the above structure for other options

    if query == "Top 10 transactions_type based on states and transaction_amount":
        mysql_cursor.execute('''
            SELECT State, Transaction_type, SUM(Transaction_amount) AS Total_Amount
            FROM Aggregated_Transaction_Data
            GROUP BY State, Transaction_type
            ORDER BY Total_Amount DESC
            LIMIT 10''');
        df = pd.DataFrame(mysql_cursor.fetchall(),columns=['State',"Transaction_type","Total_Amount"])
        col1,col2 = st.columns(2)
        with col1:
            # Display results in table view
            st.write(df)
        with col2:        
        # Display results in pie chart view
            fig = px.pie(df, names='Transaction_type', values='Total_Amount', title='Top Transaction Types by Amount')
            st.plotly_chart(fig)

    # Repeat the above structure for other options

    if query == "Rank mobile brands in the top 10 percentile in terms of transaction percentage":
        mysql_cursor.execute('''
            SELECT State, Year, District, Registered_Users, App_open_no
            FROM Aggregated_User_Data
            WHERE Registered_Users / App_open_no >= PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY Registered_Users / App_open_no DESC)
            ORDER BY Registered_Users / App_open_no DESC
            LIMIT 10''')
        df = pd.DataFrame(mysql_cursor.fetchall(),columns=['State',"Year","District","Registered_Users","App_open_no"])
        col1,col2 = st.columns(2)
        with col1:
            # Display results in table view
            st.write(df)
        with col2:        
        # Display results in scatter plot view
            fig = px.scatter(df, x='State', y='Registered_Users', size='App_open_no',
                            color='District', title='Mobile Brands in Top 10 Percentile')
            st.plotly_chart(fig)

if selected == "Explore Data":
    options = ["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4" ]
    select = st.selectbox("Select Quarter", options)          
    
    numeric_part = int(''.join(filter(str.isdigit, select)))
    result_df = Aggregated_Transaction.query('Quater == @numeric_part').groupby(['State', 'Quater']).agg({
        'Transaction_amount': ['mean', 'sum'],
        'Transaction_count': 'sum'
    }).reset_index()
    result_df.columns = ['State',"Quater", 'Avg_transaction_amount', 'Total_transaction_amount', 'Total_transaction_count']
    base_map = go.Figure()
    base_map.update_layout(
        mapbox=dict(
            style="carto-positron",
            center=dict(lat=20, lon=87),
            zoom=4,
            bearing=20,
            pitch=40,
        ),
        title="Base Map" )

    # Create choropleth figure with go
    choropleth_map = go.Figure()

    choropleth_map.add_trace(go.Choroplethmapbox(
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        locations=result_df['State'],
        z=result_df['Total_transaction_amount'],
        featureidkey="properties.ST_NM",
        colorscale='sunset',
        colorbar=dict(title="Total Transactions"),
        hovertext=result_df['State'],
    ))

    # Overlay choropleth map on base map
    base_map.add_trace(choropleth_map.data[0])

# Show the combined map
    st.plotly_chart(base_map)

if selected == "Home":
    col1,col2= st.columns(2)

    with col1:
        st.header("PHONEPE")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("   **-> Credit & Debit card linking**")
        st.write("   **-> Bank Balance check**")
        st.write("   **->Money Storage**")
        st.write("   **->PIN Authorization**")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video("https://youtu.be/mMch1jF6JB8?si=qnKTXl7MDRCLGOVQ")

    col3,col4= st.columns(2)
    
    with col3:
        st.video("https://youtu.be/aXnNA4mv1dU?si=xM5DIGQHCTGyUeIS")

    with col4:
        st.write("**-> Easy Transactions**")
        st.write("**-> One App For All Your Payments**")
        st.write("**-> Your Bank Account Is All You Need**")
        st.write("**-> Multiple Payment Modes**")
        st.write("**-> PhonePe Merchants**")
        st.write("**-> Multiple Ways To Pay**")
        st.write("**-> 1.Direct Transfer & More**")
        st.write("**-> 2.QR Code**")
        st.write("**-> Earn Great Rewards**")

    col5,col6= st.columns(2)

    with col5:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("**->No Wallet Top-Up Required**")
        st.write("**->Pay Directly From Any Bank To Any Bank A/C**")
        st.write("**->Instantly & Free**")

    with col6:
        st.video("https://youtu.be/QG6iEwlnPoE?si=z7AfRmAGS4-8-xqz")