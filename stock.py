import streamlit as st 
import pymysql
import pandas as pd
import seaborn as sns
import matplotlib. pyplot as plt


#title
st.title('STOCK ANALYSIS DASHBOARD')

#sidebar
s = st.sidebar.markdown('## **📊 STOCK ANALYSIS** ')

selected_option = st.sidebar.radio(label = 'Navigation',options=('HOME','STOCK ANALYSIS'))


if selected_option == 'HOME':
    st.write('Welcome to home page!🎉')
    st.image('c:/Users/ADMIN/Downloads/premium_photo-1681487769650-a0c3fbaed85a.jpg',caption='Analyze Stock Performance Effectively!', use_container_width=True)
elif selected_option == 'STOCK ANALYSIS':
    analysis_option = st.sidebar.radio(label = "📈📉 Go to", options = ('Top 10 GREEN Stocks',
                                                                    'Top 10 RED Stocks',
                                                                    'Market Summary',
                                                                    'Volatility Analysis',
                                                                    'Cumulative Return Over Time',
                                                                    'Sector-wise Performance',
                                                                    'Stock Price Correlation',
                                                                    'Top 5 Gainers and Losers (Month-wise)'))
    #green stocks
    if analysis_option == 'Top 10 GREEN Stocks': 
        #load the data 
        data = pd.read_csv('Top_10_green_stocks')
        st.subheader('TOP 10 GREEN STOCKS')
        st.dataframe(data)
        
        #plotings
        st.subheader('TOP 10 GREEN STOCKS')
        fig, ax = plt.subplots(figsize = (18,12)) 
        sns.barplot(x = 'Ticker', y = 'yearly_return', data=data, ax = ax, palette= 'viridis')
        ax.set_xlabel = ('Ticker')
        ax.set_ylabel = ('yearly_return')
        st.pyplot(fig)
    
    
    
    #red stocks    
    if analysis_option == 'Top 10 RED Stocks':
        top_10_red_stocks = pd.read_csv('Top_10_red_stocks')
        st.subheader('TOP_10_RED_STOCKS')
        st.dataframe(top_10_red_stocks)
        
        #ploting
        st.subheader('TOP 10 RED STOCKS')
        fig, ax = plt.subplots(figsize = (18,12))
        sns.barplot(x = 'Ticker', y = 'yearly_return', data = top_10_red_stocks , ax = ax, palette= 'dark')   
        ax.set_xlabel = ('Ticker') 
        ax.set_ylabel = ('yearly_return')
        st.pyplot(fig)
        
        
    #Market Summary
    if analysis_option == 'Market Summary':
        market_summary = pd.read_csv('market_summary_csv')
        st.subheader('MARKET SUMMARY')
        st.dataframe(market_summary)
        
    #volatility analysis
    if analysis_option == 'Volatility Analysis':
        volatility = pd.read_csv('volatility analysis')
        st.subheader('VOLATILITY ANALYSIS')
        st.dataframe(volatility)
        
        #ploting
        st.subheader('VOLATILITY ANALYSIS')
        fig, ax = plt.subplots(figsize = (18, 12))
        sns.barplot(x = 'Ticker', y = 'volatility', data =volatility, ax = ax, palette= 'husl')
        ax.set_xlabel = ('Ticker')
        ax.set_ylabel = ('yearly_return')
        st.pyplot(fig)
        
    # cumulative return over time
    if analysis_option == 'Cumulative Return Over Time':
       Cumulative_return = pd.read_csv('cumulative return')
       st.subheader('CUMULATIVE RETURN OVER TIME')
       st.dataframe(Cumulative_return)
       
       #ploting 
       st.subheader('CUMULATIVE RETURN OVER TIME')
       fig, ax = plt.subplots(figsize = (12,8))
       sns.lineplot(x = 'Ticker', y = 'cumulative_return', data = Cumulative_return, ax=ax, marker = 'o')
       ax.set_xlabel = ('Ticker')
       ax.set_ylabel = ('cumultive_return')
       st.pyplot(fig)
       
       
    # Sector-wise Performance
    if analysis_option == 'Sector-wise Performance':
        sector_performance = pd.read_csv('sector_performance')
        st.subheader('SECTOR-WISE PERFORMANCE')
        st.dataframe(sector_performance)
        
    # ploting
        st.subheader('SECTOR-WISE PERFORMANCE')
        fig, ax = plt.subplots(figsize = (32,20))
        sns.barplot(x = 'sector', y = 'avg_yearly_return',data = sector_performance, ax=ax, palette= 'magma') 
        ax.set_xlabel = ('sector')
        ax.set_ylabel = ('average yearly return')
        st.pyplot(fig)
        
    #Stock Price Correlation
    if analysis_option == 'Stock Price Correlation':
        stock_price_correlation = pd.read_csv('top_10_correlation')
        st.subheader('TOP 10 STOCK PRICE CORRELATION')
        st.dataframe(stock_price_correlation)
        
    # #ploting #heatmap
         
                                                                    
    # Top 5 Gainers (Month-wise)
    if analysis_option == 'Top 5 Gainers and Losers (Month-wise)':
        
        #read csv file
        top_5_gainers = pd.read_csv('top_gainers')
        
        #dict to store month wise
        monthly_top_5_gainers = {}
        
        #collect unique month
        unique_months = top_5_gainers['month'].unique()
        
        #user to select a month
        selected_month = st.selectbox('select a month', unique_months)
        
        if selected_month:
            top_5_gainers = top_5_gainers[top_5_gainers['month']== selected_month].head(5).reset_index(drop = True)
            monthly_top_5_gainers[str(selected_month)] = top_5_gainers
        
            #display the data for selected month
            st.subheader(f'TOP 5 GAINERS-{selected_month}')
            st.dataframe(top_5_gainers)
            
             #plotings 
            st.subheader(f'TOP 5 GAINERS-{selected_month}')
            fig, ax = plt.subplots(figsize = (18,12))
            sns.barplot(x = 'Ticker', y = 'monthly_return', hue = 'month', data = top_5_gainers , ax = ax, palette= 'viridis')   
            ax.set_xlabel = ('Ticker') 
            ax.set_ylabel = ('monthly_return')
            st.pyplot(fig)
            
        
    #Top 5 losers(Month_wise)  
    
        #read csv file
        top_5_losers = pd.read_csv('top_losers')
        
        #dict to store month wise
        monthly_top_5_losers = {}
        
        #collect month wise
        unique_months = top_5_losers['month'].unique()
        
        if selected_month:
            top_5_losers = top_5_losers[top_5_losers['month']== selected_month].head(5).reset_index(drop = True)
            monthly_top_5_losers[str(selected_month)] = top_5_losers
            
            #display the data for selected month
            st.subheader(f'TOP 5 LOSERS-{selected_month}')
            st.dataframe(top_5_losers)
            
            #plotings 
            st.subheader(f'TOP 5 LOSERS-{selected_month}')
            fig, ax = plt.subplots(figsize = (18,12))
            sns.barplot(x = 'Ticker', y = 'monthly_return', hue = 'month', data = top_5_losers, ax = ax, palette= 'husl')   
            ax.set_xlabel = ('Ticker') 
            ax.set_ylabel = ('monthly_return')
            st.pyplot(fig)
        
      
      