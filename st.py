import streamlit as st
import os
import openai

openai.api_key = ""



st.sidebar.title('Apollo19 :hospital:')
st.sidebar.text("@ your service")
st.sidebar.title('Page Selection Menu')
page = st.sidebar.radio("Select Required Feature",("Headline Generator","Bio Generator"))


if page=='Headline Generator':
	st.title('LinkedIn Headline Generator')
	description = st.text_area("Enter your description",'')

	if st.button("Generate Headline!"):
		if description=="":
			st.error("Please enter your description")
		else:	
			with st.spinner("Fetching response..."):
			    response = openai.Completion.create(
	  engine="davinci-instruct-beta",
	  prompt= f"An application to create a LinkedIn headline from the given description.\n\nI am a technologist, IT leader, lecturer, and cook. I provide fractional CTO and CIO services to technology startups, helping them find the right direction for their business. I deliver talks on topics such as blockchain and cryptography to a wide variety of audiences including as a guest lecturer at the Haas School of Business.\n\nLinkedIn headline:\nBlockchain expert and lecturer. Fractional CTO/CIO services to tech startups.\n\nI am an innovative entrepreneur with more than 11 years of experience in the digital marketing, technology and service industries. I am an active member of the startup community and have founded a couple of startups and exited one of them.\n\nLinkedIn headline:\nEntrepreneur, Digital Marketing Expert, Investor, Mentor, Public Speaker, Blockchain and Cryptocurrency Expert.\n\nI am a student entrepreneur. I have created many projects in the fields of app development, python automation and machine learning. Am also a Data Science enthusiast and I wish to get a job in this field.\n\nLinkedIn headline:\nStudent Entrepreneur, Machine Learning Enthusiast, Data Science Enthusiast.\n\n{description} \n\nLinkedIn headline:\n",
	  temperature=1,
	  max_tokens=100,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0.6
	)
			    st.markdown(response['choices'][0]['text'])



elif page=='Bio Generator':
	st.title('LinkedIn Bio Generator')
	description = st.text_area("Enter your Headline",'')

	if st.button("Generate Bio!"):
		if description=="":
			st.error("Please enter your headline")
		else:	
			with st.spinner("Fetching response..."):
			    response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt= f"An application to create a description from the given LinkedIn headlines.\n###\nHeadline: \nBlockchain expert and lecturer. Fractional CTO/CIO services to tech startups.\n\nLinkedIn description:\nI am a technologist, IT leader, lecturer, and cook. I provide fractional CTO and CIO services to technology startups, helping them find the right direction for their business. I deliver talks on topics such as blockchain and cryptography to a wide variety of audiences including as a guest lecturer at the Haas School of Business.\n###\nHeadline: \nEntrepreneur, Digital Marketing Expert, Investor, Mentor, Public Speaker, Blockchain and Cryptocurrency Expert.\n\nLinkedIn description:\nI am an innovative entrepreneur with more than 11 years of experience in the digital marketing, technology and service industries. I am an active member of the startup community and have founded a couple of startups and exited one of them.\n###\nHeadline: \nStudent Entrepreneur, Machine Learning Enthusiast, Data Science Enthusiast.\n\nLinkedIn description:\nI am a student entrepreneur. I have created many projects in the fields of app development, python automation and machine learning. Am also a Data Science enthusiast and I wish to get a job in this field.\n###\nHeadline:\nE-commerce Marketing and Brand Relationship Manager at Adanola. Single point of contact skill set to drive growth.\n\nLinkedIn description:\nI am a e-commerce marketing and brand relationship manager who has a wide set of skills. I drive growth for brands, managing both online and offline marketing channels such as SEO, inbound marketing, SEM, PPC, content marketing, email campaigns, and social media. I love what I do and I hope that the career I have right now will be a great stepping stone for me.\n###\nHeadline:\n{description}\n\nLinkedIn description:",
  temperature=0.8,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["###"]
)
			    st.markdown(response['choices'][0]['text'])
