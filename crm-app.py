import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import random

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go


# Dummy data
contacts = pd.DataFrame({
	'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown'],
	'Company': ['ABC Corp', 'XYZ Inc', '123 LLC', 'Tech Co'],
	'Email': ['john@abc.com', 'jane@xyz.com', 'bob@123.com', 'alice@tech.com'],
	'Phone': ['555-1234', '555-5678', '555-9876', '555-4321'],
	'Last Contact': ['2025-01-10', '2025-01-11', '2025-01-09', '2025-01-12'],
	'Interest Level': ['High', 'Medium', 'Low', 'High'],
	'Budget': ['$50k-$100k', '$10k-$50k', '$100k+', '$50k-$100k'],
	'Preferred Product': ['Product A', 'Product B', 'Product C', 'Product A']
})

products = pd.DataFrame({
	'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product AA', 'Product BB', 'Product CC', 'Product DD'],
	'Description': ['High-end solution', 'Mid-range option', 'Budget-friendly', 'Premium service', 'High-end solution', 'Mid-range option', 'Budget-friendly', 'Premium service'],
	'Price Range': ['$50k-$100k', '$10k-$50k', '$5k-$10k', '$100k+', '$50k-$100k', '$10k-$50k', '$5k-$10k', '$100k+']
})

deals = pd.DataFrame({
	'Deal': ['Project A', 'Service B', 'Product C', 'Consulting D'],
	'Company': ['ABC Corp', 'XYZ Inc', '123 LLC', 'Tech Co'],
	'Value': [50000, 25000, 75000, 100000],
	'Stage': ['Proposal', 'Negotiation', 'Closed Won', 'Discovery']
})

tasks = pd.DataFrame({
	'Task': ['Follow up', 'Send proposal', 'Schedule meeting', 'Prepare presentation'],
	'Assigned To': ['John', 'Jane', 'Bob', 'Alice'],
	'Due Date': ['2025-01-15', '2025-01-18', '2025-01-20', '2025-01-22']
})

# Assume we have a DataFrame 'leads' with columns 'Name' and 'Score'
leads = pd.DataFrame({
	'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown'],
	'Score': [85, 62, 93, 71]
})

def create_gauge_chart(score):
	fig = go.Figure(go.Indicator(
		mode = "gauge+number",
		value = score,
		domain = {'x': [0, 1], 'y': [0, 1]},
		title = {'text': "Lead Score"},
		gauge = {'axis': {'range': [0, 100]},
				 'bar': {'color': "darkblue"},
				 'steps': [
					 {'range': [0, 50], 'color': "lightgray"},
					 {'range': [50, 75], 'color': "gray"},
					 {'range': [75, 100], 'color': "darkgray"}],
				 'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
	return fig


def generate_dummy_interaction_history(customer_name, num_interactions=20):
	interaction_types = ['Email', 'Phone Call', 'Meeting', 'Purchase', 'Support Ticket', 'Website Visit', 'Product Demo', 'Social Media Interaction']
	
	outcomes = ['Positive', 'Neutral', 'Needs Follow-up']
	
	employees = ['John Smith', 'Emma Watson', 'Michael Brown', 'Olivia Davis', 'William Johnson']
	
	products = ['Product A', 'Product B', 'Product C', 'Service X', 'Service Y']
	
	data = []
	
	end_date = datetime.now()
	start_date = end_date - timedelta(days=365)  # Last year of interactions
	
	for _ in range(num_interactions):
		interaction_type = random.choice(interaction_types)
		date = start_date + (end_date - start_date) * random.random()
		
		interaction = {
			'Date': date.strftime('%Y-%m-%d'),
			'Type': interaction_type,
			'Employee': random.choice(employees),
			'Outcome': random.choice(outcomes)
		}
		
		if interaction_type == 'Email':
			interaction['Details'] = f"Subject: {random.choice(['Follow-up', 'Product Inquiry', 'Meeting Request', 'Thank You'])}"
		elif interaction_type == 'Phone Call':
			interaction['Details'] = f"Duration: {random.randint(1, 60)} minutes"
		elif interaction_type == 'Meeting':
			interaction['Details'] = f"Location: {random.choice(['Office', 'Video Call', 'Customer Site'])}"
		elif interaction_type == 'Purchase':
			interaction['Details'] = f"Product: {random.choice(products)}, Amount: ${random.randint(100, 10000)}"
		elif interaction_type == 'Support Ticket':
			interaction['Details'] = f"Ticket ID: #{random.randint(1000, 9999)}, Status: {random.choice(['Resolved', 'Pending', 'In Progress'])}"
		elif interaction_type == 'Website Visit':
			interaction['Details'] = f"Pages Visited: {random.randint(1, 10)}, Duration: {random.randint(1, 120)} minutes"
		elif interaction_type == 'Product Demo':
			interaction['Details'] = f"Product: {random.choice(products)}, Duration: {random.randint(15, 90)} minutes"
		elif interaction_type == 'Social Media Interaction':
			interaction['Details'] = f"Platform: {random.choice(['Twitter', 'LinkedIn', 'Facebook'])}, Type: {random.choice(['Like', 'Comment', 'Share'])}"
		
		data.append(interaction)
	
	df = pd.DataFrame(data)
	df['Date'] = pd.to_datetime(df['Date'])
	df = df.sort_values('Date', ascending=False).reset_index(drop=True)
	
	return df



# Streamlit app
st.title('CRM Dashboard for SMBs')
st.subheader('Developed by Gaurang Pendyala for DECA')

contacts_tab, pipeline_tab, tasks_tab, reports_tab, products_tab5, leadmgmt_tab, auto_tab, analytics_tab, cust360_tab, leadscore_tab = st.tabs(['Contacts', 'Pipeline', 'Tasks', 'Reports', 'Products', 'Lead Management', 'Automation', 'Analytics', 'Customer 360', 'Lead Score Viz'])

with contacts_tab:
	st.header('Contact Management')
	st.dataframe(contacts)
	
	st.subheader('Add New Contact')
	col1, col2 = st.columns(2)
	with col1:
		name = st.text_input('Name')
		company = st.text_input('Company')
		email = st.text_input('Email')
	with col2:
		phone = st.text_input('Phone')
		interest = st.selectbox('Interest Level', ['High', 'Medium', 'Low'])
		budget = st.selectbox('Budget', ['$10k-$50k', '$50k-$100k', '$100k+'])
	if st.button('Add Contact'):
		st.success('Contact added successfully!')

with pipeline_tab:
	st.header('Pipeline Management')
	fig = px.bar(deals, x='Company', y='Value', color='Stage', title='Deal Pipeline')
	st.plotly_chart(fig)
	
	st.subheader('Deal List')
	st.dataframe(deals)

with tasks_tab:
	st.header('Task and Activity Tracking')
	st.dataframe(tasks)
	
	st.subheader('Add New Task')
	task = st.text_input('Task Description')
	assigned_to = st.selectbox('Assigned To', ['John', 'Jane', 'Bob', 'Alice'])
	due_date = st.date_input('Due Date')
	if st.button('Add Task'):
		st.success('Task added successfully!')

with reports_tab:
	st.header('Reports and Analytics')
	
	# Sales Forecast
	forecast_data = deals[deals['Stage'] != 'Closed Won']
	fig1 = px.pie(forecast_data, values='Value', names='Stage', title='Sales Forecast by Stage')
	st.plotly_chart(fig1)
	
	# Activity Timeline
	today = datetime.now()
	timeline_data = pd.DataFrame({
		'Date': [today + timedelta(days=i) for i in range(7)],
		'Tasks': [3, 1, 4, 2, 5, 0, 2]
	})
	fig2 = px.line(timeline_data, x='Date', y='Tasks', title='7-Day Activity Forecast')
	st.plotly_chart(fig2)


with products_tab5:
	st.header('Product Management')
	st.dataframe(products)
	
	st.subheader('Product Matching')
	budget = st.selectbox('Select Budget', ['$10k-$50k', '$50k-$100k', '$100k+'])
	if st.button('Find Matching Products'):
		matching_products = products[products['Price Range'] == budget]
		st.write(matching_products)

with leadmgmt_tab:
	st.header('Lead Management')
	
	st.subheader('High Interest Leads')
	high_interest = contacts[contacts['Interest Level'] == 'High']
	st.dataframe(high_interest)
	
	st.subheader('Lead Scoring')
	# Placeholder for lead scoring algorithm
	st.info('Lead scoring feature to be implemented')



with auto_tab:
	st.header('Automation Tools')
	
	st.subheader('Automated Responses')
	if st.button('Send Welcome Email'):
		st.success('Welcome email sent to new leads')
	
	st.subheader('Product Demo Automation')
	if st.button('Send Product Demo Links'):
		st.success('Product demo links sent to interested leads')
	
	st.subheader('Follow-up Automation')
	days = st.number_input('Days until follow-up', min_value=1, max_value=30, value=7)
	if st.button('Schedule Follow-ups'):
		st.success(f'Follow-ups scheduled for {days} days from now')


with analytics_tab:
	st.header('Analytics & Reporting')
	
	# Dummy data for demonstration
	engagement_data = pd.DataFrame({
		'Metric': ['Open Rate', 'Click-through Rate', 'Response Rate'],
		'Percentage': [65, 25, 10]
	})
	
	fig = px.bar(engagement_data, x='Metric', y='Percentage', title='Email Engagement Metrics')
	st.plotly_chart(fig)
	
	st.subheader('Lead Conversion Insights')
	# Placeholder for more advanced analytics
	st.info('Advanced analytics features to be implemented')


with cust360_tab:
	st.header('Customer 360 View')
	selected_customer = st.selectbox('Select Customer', contacts['Name'])
	
	customer_data = contacts[contacts['Name'] == selected_customer].iloc[0]
	
	col1, col2 = st.columns(2)
	with col1:
		st.subheader('Contact Info')
		st.write(f"Name: {customer_data['Name']}")
		st.write(f"Company: {customer_data['Company']}")
		st.write(f"Email: {customer_data['Email']}")
		st.write(f"Phone: {customer_data['Phone']}")
	
	with col2:
		st.subheader('Interests & Preferences')
		st.write(f"Interest Level: {customer_data['Interest Level']}")
		st.write(f"Budget: {customer_data['Budget']}")
		st.write(f"Preferred Product: {customer_data['Preferred Product']}")
	
	st.subheader('Interaction History')
	# Placeholder for interaction history
	customer_history = generate_dummy_interaction_history(selected_customer)
	st.dataframe(customer_history)

	# You could also add some summary statistics
	st.subheader('Interaction Summary')
	col1, col2, col3 = st.columns(3)
	with col1:
		st.metric("Total Interactions", len(customer_history))
	with col2:
		st.metric("Most Common Interaction", customer_history['Type'].mode()[0])
	with col3:
		st.metric("Last Interaction Date", customer_history['Date'].max().strftime('%Y-%m-%d'))

	# You could create a chart of interactions over time
	st.subheader('Interactions Over Time')
	interaction_counts = customer_history.groupby('Date').size().reset_index(name='Count')
	fig = px.line(interaction_counts, x='Date', y='Count', title='Interactions Over Time')
	st.plotly_chart(fig)

	# You could show a pie chart of interaction types
	st.subheader('Interaction Types')
	interaction_type_counts = customer_history['Type'].value_counts()
	fig = px.pie(values=interaction_type_counts.values, names=interaction_type_counts.index, title='Distribution of Interaction Types')
	st.plotly_chart(fig)



	
	st.subheader('Documents & Paperwork')
	# Placeholder for document management
	st.info('Document management feature to be implemented')


with leadscore_tab:
	st.header(" Lead Score Visualizations")

	st.subheader("1. Heat Map or Color-Coded Table")
	st.info ("This method uses colors to represent different lead scores, making it easy to spot high-value leads at a glance.")

	fig, ax = plt.subplots(figsize=(10, 6))
	sns.heatmap(leads.set_index('Name'), annot=True, cmap="YlOrRd", cbar=False, ax=ax)
	plt.title('Lead Scores Heatmap')
	st.pyplot(fig)

	st.subheader("2. Bar Chart")
	st.info("A bar chart can effectively show the comparison of lead scores across different leads.")

	fig = px.bar(leads, x='Name', y='Score', title='Lead Scores')
	fig.update_traces(marker_color=leads['Score'], marker_colorscale='Viridis')
	st.plotly_chart(fig)

	st.subheader("3. Scatter Plot")
	st.info("If you have multiple factors contributing to the lead score, a scatter plot can be useful.")

	# Assume we have additional columns 'Engagement' and 'Budget'
	leads['Engagement'] = [75, 80, 90, 65]
	leads['Budget'] = [50000, 75000, 100000, 60000]

	fig = px.scatter(leads, x='Engagement', y='Budget', size='Score', 
					 color='Score', hover_name='Name', 
					 title='Lead Scoring: Engagement vs Budget')
	st.plotly_chart(fig)

	st.subheader("4. Gauge Chart")
	st.info("For individual lead profiles, a gauge chart can provide a quick visual representation of the lead score.")

	selected_lead = st.selectbox('Select a lead', leads['Name'])
	lead_score = leads[leads['Name'] == selected_lead]['Score'].values[0]
	st.plotly_chart(create_gauge_chart(lead_score))

	st.subheader("5. Funnel Chart")
	st.info("To visualize how leads are distributed across different score ranges.")

	score_ranges = pd.cut(leads['Score'], bins=[0, 25, 50, 75, 100], labels=['Low', 'Medium', 'High', 'Very High'])
	score_counts = score_ranges.value_counts().sort_index()

	fig = go.Figure(go.Funnel(
		y = score_counts.index,
		x = score_counts.values,
		textinfo = "value+percent total"
	))
	fig.update_layout(title='Lead Score Distribution')
	st.plotly_chart(fig)


# Sidebar for quick actions
st.sidebar.header('Quick Actions')
action = st.sidebar.selectbox('Select Action', ['Add Contact', 'Add Deal', 'Add Task', 'Send Product Demo', 'Schedule Follow-up'])
if st.sidebar.button('Perform Action'):
	st.sidebar.success(f'{action} action performed!')

# Mobile Access Note
st.sidebar.markdown('---')
st.sidebar.info('📱 Mobile app available for on-the-go access!')

# Integrations
st.sidebar.markdown('---')
st.sidebar.subheader('Integrations')
st.sidebar.markdown('✅ Email')
st.sidebar.markdown('✅ Calendar')
st.sidebar.markdown('✅ Marketing Automation')
st.sidebar.markdown('✅ Document Management')
