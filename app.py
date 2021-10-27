# Core Pkgs
import streamlit as st
import sklearn
import joblib,os
import numpy as np 

# Loading Models
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def main():
	"""Simple Linear Regression App"""

	st.title("Bicarbonate Estimation using simple Linear Regression")

	html_templ = """
	<div style="background-color:blue;padding:10px;">
	<h3 style="color:cyan">Very Simple Linear Regression Web App for Bicarbonate Estimation</h3>
	</div>
	"""

	st.markdown(html_templ,unsafe_allow_html=True)

	activity = ["Bicarbonate Estimation","About"]
	choice = st.sidebar.selectbox("Menu",activity)

# Bicarbonate Estimation CHOICE
	if choice == 'Bicarbonate Estimation':

		st.subheader("Bicarbonate Estimation")

		experience = st.slider("pH of the Water",0.0,10.0)

		#st.write(type(experience))

		if st.button("Estimate:"):

			regressor = load_prediction_model("SimpleLinearRegression-20K45A0215(ph_vs_bicar).pkl")
			experience_reshaped = np.array(experience).reshape(-1,1)

			#st.write(type(experience_reshaped))
			#st.write(experience_reshaped.shape)

			predicted_salary = regressor.predict(experience_reshaped)

			st.info("Bicarbonate with {} pH of the Water: {}".format(experience,(predicted_salary[0][0].round(2))))

# About CHOICE
	if choice == 'About':
		st.subheader("About")
		st.markdown("""
			## Simple Linear Regression App to Estimate Bicarbonates from pH of the Water
			
			##### By
			+ **[GitHub/PrabhuKiran8790](https://www.github.com/PrabhuKiran8790/)**
			+ [prabhukiran426@gmail.com](mailto:prabhukiran426@gmail.com)

			""")


if __name__ == '__main__':
	main()