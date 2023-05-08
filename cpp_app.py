import gzip, pickle
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


filepath = 'rfr_ht_model.pkl'
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()


def convert_var(location, owner, fuel, transmission, company):
    Location_Ahmedabad= 0 #dropped
    Location_Bangalore= 0
    Location_Chennai= 0
    Location_Coimbatore=0
    Location_Delhi= 0
    Location_Hyderabad= 0
    Location_Jaipur= 0
    Location_Kochi= 0
    Location_Kolkata= 0
    Location_Mumbai= 0
    Location_Pune= 0
    Fuel_Type_CNG= 0 #dropped
    Fuel_Type_Diesel= 0
    Fuel_Type_LPG= 0
    Fuel_Type_Petrol= 0
    Transmission_Automatic=0 #dropped
    Transmission_Manual= 0
    Company_Ambassador=0
    Company_Audi= 0
    Company_BMW= 0
    Company_Bentley= 0
    Company_Chevrolet= 0
    Company_Datsun= 0
    Company_Fiat= 0
    Company_Force= 0
    Company_Ford= 0
    Company_Honda= 0
    Company_Hyundai= 0
    Company_ISUZU= 0
    Company_Isuzu= 0
    Company_Jaguar= 0
    Company_Jeep= 0
    Company_Lamborghini= 0
    Company_Land= 0
    Company_Mahindra= 0
    Company_Maruti= 0
    Company_Mercedes_Benz= 0
    Company_Mini= 0
    Company_Mitsubishi= 0
    Company_Nissan= 0
    Company_Porsche= 0
    Company_Renault= 0
    Company_Skoda= 0
    Company_Tata= 0
    Company_Toyota= 0
    Company_Volkswagen= 0
    Company_Volvo= 0

    loc= ('Location_'+ location)
    vars()[loc]= 1
    ful= ('Fuel_Type_'+ fuel)
    vars()[ful]= 1
    trans= ('Transmission_'+ transmission)
    vars()[trans]= 1
    if company== 'Mercedes-Benz':
        vars()[company]= 1
    else:
        comp= ('Company_'+ company)
        vars()[comp]= 1

    if owner == 'First':
        owner = 1
    elif owner == 'Second':
        owner = 2
    elif owner == 'Third':
        owner = 3
    else:
        owner = 4

    return (Location_Ahmedabad, Location_Bangalore, Location_Chennai, Location_Coimbatore, Location_Delhi,
            Location_Hyderabad, Location_Jaipur, Location_Kochi, Location_Kolkata, Location_Mumbai,
            Location_Pune, Fuel_Type_CNG, Fuel_Type_Diesel, Fuel_Type_LPG, Fuel_Type_Petrol, Transmission_Automatic,
            Transmission_Manual, owner, Company_Ambassador, Company_Audi, Company_BMW, Company_Bentley, Company_Chevrolet, Company_Datsun, Company_Fiat, Company_Force, Company_Ford, Company_Honda, Company_Hyundai, Company_ISUZU, Company_Isuzu, Company_Jaguar, Company_Jeep, Company_Lamborghini, Company_Land, Company_Mahindra, Company_Maruti, Company_Mercedes_Benz, Company_Mini, Company_Mitsubishi, Company_Nissan, Company_Porsche, Company_Renault, Company_Skoda, Company_Tata, Company_Toyota, Company_Volkswagen, Company_Volvo)

def main():
    st.header('🚕Used Car Price Prediction')
    
    activities = ['Calcuate Price', 'About', 'Contact']
    
    option = st.sidebar.radio('Menu ', activities)

    if option == 'About':
        
        abt = """
        ##### Github Notebook: [Link]("https://github.com/Shaah-i/Flight_Fare_Estimator/blob/main/flightfareprediction_Nov2022.ipynb)

        ##### Used cars have a huge market base, with many people considering them as a better investment option than buying a new car because it's more feasible. The main reason for this is that when you buy a new car and sell it just a day later, the price drops by 30%. Unfortunately, there are also many frauds in the market who not only sell faulty cars but also mislead buyers about the true value of the vehicle.

        ##### So, here I used this [dataset]("https://www.kaggle.com/datasets/avikasliwal/used-cars-price-prediction") to Predict the price of any used car.

        ##### Straight away head to the Calculate Price tab and get a right estimate of price of car you are willing to buy.
        """
        st.markdown(abt)

        # st.markdown("""
        # # About Me

        # Shubham is a data enthusiast and you can know more about him [here]()
        # """)

        project_list = """
        ### See previous projects:

        * [Flight_Fare_Estimator](https://flight-fare-estimator-shaah-i.streamlit.app/)
        * [Insurance Price Prediction](https://github.com/Shaah-i/Insurance)
        * [Dashboards](https://community.powerbi.com/t5/forums/recentpostspage/post-type/message/user-id/449500)
        """
        st.markdown(project_list)


        disclaimer = "###### The theme and images have inspiration from the #RedHotDark edition of TATA MOTORS, but there is no intention of infringing on their rights or plagiarizing their work. I thank TATA MOTORS for the inspiration and their innovative ideas."
        st.caption(disclaimer)

    elif option == 'Contact':
        cntct = """
        ### Contact

        This Model is Developed by **Shubham (shaah_i)**

        LinkedIn: [Link](https://www.linkedin.com/in/shubham-shaah/)

        GitHub: [Link](https://github.com/Shaah-i)

        \t \t Made with ❤ in IN
        """
        st.markdown(cntct)
    
    else:
        image = Image.open('car.png')
        st.image(image, use_column_width=True,)
        st.subheader('Calcuate Price')
    
        dr1, dr2 = st.columns([1,1])
        cust= dr1.selectbox("Are you a Buyer or a Seller", ['Buyer', 'Seller'])
        # dr2.selectbox("", [],)

        manuf = ['Maruti', 'Hyundai', 'Honda', 'Toyota', 'Mercedes-Benz', 'Volkswagen', 'Ford', 'Mahindra', 'BMW', 'Audi', 'Tata', 'Skoda', 'Renault Chevrolet', 'Nissan', 'Land', 'Jaguar', 'Mitsubishi', 'Mini', 'Fiat', 'Volvo', 'Porsche', 'Jeep', 'Datsun,Force', 'ISUZU', 'Ambassador', 'Isuzu', 'Bentley', 'Lamborghini']
        company = dr1.selectbox("Manufacturer", manuf)
        kg_dr = dr2.number_input("Kilometers Driven", step= 100, value= 50000)
        mileage = dr1.number_input("Mileage in kmpl", value= 19.25)
        engine = dr2.number_input("Engine in CC", value= 1500)
        power = dr1.number_input("Power in bhp", value=100.00)
        city = ['Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad']
        location = dr2.selectbox('City', city)
        col1, col2, col3 = st.columns([1.6, 1.4, 0.8])
        owner = col1.radio("Choose Owner Type", ('First', 'Second', 'Third', 'Fourth & Above'))
        fuel = col2.radio("Choose Fuel Type", ('CNG', 'Diesel', 'Petrol', 'LPG'))
        transmission = col3.radio("Choose Transmission", ('Manual', 'Automatic'))
        seats = st.slider("Select Number Seats", 0.0, 12.0, step=1.0)
        year = st.slider("Select Purchase year", 1980, 2020)


        Location_Ahmedabad, Location_Bangalore, Location_Chennai, Location_Coimbatore, Location_Delhi, Location_Hyderabad, Location_Jaipur, Location_Kochi, Location_Kolkata, Location_Mumbai, Location_Pune, Fuel_Type_CNG, Fuel_Type_Diesel, Fuel_Type_LPG, Fuel_Type_Petrol, Transmission_Automatic, Transmission_Manual, owner, Company_Ambassador, Company_Audi, Company_BMW, Company_Bentley, Company_Chevrolet, Company_Datsun, Company_Fiat, Company_Force, Company_Ford, Company_Honda, Company_Hyundai, Company_ISUZU, Company_Isuzu, Company_Jaguar, Company_Jeep, Company_Lamborghini, Company_Land, Company_Mahindra, Company_Maruti, Company_Mercedes_Benz, Company_Mini, Company_Mitsubishi, Company_Nissan, Company_Porsche, Company_Renault, Company_Skoda, Company_Tata, Company_Toyota, Company_Volkswagen, Company_Volvo = convert_var(location, owner, fuel, transmission, company)

        inputs = pd.DataFrame(np.array([year, kg_dr, owner, mileage, engine, power, seats, Location_Bangalore, Location_Chennai, Location_Coimbatore, Location_Delhi, Location_Hyderabad, Location_Jaipur,Location_Kochi, Location_Kolkata, Location_Mumbai, Location_Pune, Fuel_Type_Diesel, Fuel_Type_LPG, Fuel_Type_Petrol, Transmission_Manual, Company_Audi, Company_BMW, Company_Bentley, Company_Chevrolet, Company_Datsun, Company_Fiat, Company_Force, Company_Ford, Company_Honda, Company_Hyundai, Company_ISUZU, Company_Isuzu, Company_Jaguar, Company_Jeep, Company_Lamborghini, Company_Land, Company_Mahindra, Company_Maruti, Company_Mercedes_Benz, Company_Mini, Company_Mitsubishi, Company_Nissan, Company_Porsche, Company_Renault, Company_Skoda, Company_Tata, Company_Toyota, Company_Volkswagen, Company_Volvo]).reshape(1, -1), columns=['Year', 'Kilometers_Driven', 'Owner_Type', 'Mileage', 'Engine', 'Power',
       'Seats', 'Location_Bangalore', 'Location_Chennai',
       'Location_Coimbatore', 'Location_Delhi', 'Location_Hyderabad',
       'Location_Jaipur', 'Location_Kochi', 'Location_Kolkata',
       'Location_Mumbai', 'Location_Pune', 'Fuel_Type_Diesel', 'Fuel_Type_LPG',
       'Fuel_Type_Petrol', 'Transmission_Manual', 'Company_Audi',
       'Company_BMW', 'Company_Bentley', 'Company_Chevrolet', 'Company_Datsun',
       'Company_Fiat', 'Company_Force', 'Company_Ford', 'Company_Honda',
       'Company_Hyundai', 'Company_ISUZU', 'Company_Isuzu', 'Company_Jaguar',
       'Company_Jeep', 'Company_Lamborghini', 'Company_Land',
       'Company_Mahindra', 'Company_Maruti', 'Company_Mercedes-Benz',
       'Company_Mini', 'Company_Mitsubishi', 'Company_Nissan',
       'Company_Porsche', 'Company_Renault', 'Company_Skoda', 'Company_Tata',
       'Company_Toyota', 'Company_Volkswagen', 'Company_Volvo'] )

        st.subheader("Price")

        if st.button('Calculate Price 🚗🚙🚘'):
            if cust== 'Buyer':
                st.markdown('**Hey Buyer! 💸**')
            else:
                st.markdown('**Hey Seller! 💰**')
            st.markdown('**You Car Company: **')
            st.markdown(f"### 🏭 **{company}**")
            st.markdown("**Has a Predicted Price**")
            st.header("₹ {:,}".format(round(model.predict(inputs)[0] * 100000), 0))

        st.markdown("#### Developed By: [**shaah-i**](https://github.com/Shaah-i) with 😍", )
        st.markdown(":red[⫷] Learn more about the app and the author by toggling the menu.")


if __name__== '__main__':
    main()
