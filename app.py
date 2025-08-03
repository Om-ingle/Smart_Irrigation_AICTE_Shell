import streamlit as st
import numpy as np
import joblib

model = joblib.load("Farm_Irrigation_System.pkl")

st.title("Farm Irrigation System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

if st.button("Predict Sprinkler Status"):
    sensor_values = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(sensor_values)
    
    # Debug information
    st.write(f"Prediction type: {type(prediction)}")
    st.write(f"Prediction shape: {prediction.shape if hasattr(prediction, 'shape') else 'No shape'}")
    st.write(f"Prediction value: {prediction}")

    st.markdown("### Prediction Result")
    
    # Handle different prediction formats
    if hasattr(prediction, '__iter__') and not isinstance(prediction, str):
        # If prediction is an array/iterable
        for i, status in enumerate(prediction):
            # Handle case where status might be an array itself
            if hasattr(status, '__iter__') and not isinstance(status, str):
                # If status is an array, take the first element
                status_value = status[0] if len(status) > 0 else status
            else:
                status_value = status
            
            status_str = 'On' if int(status_value) == 1 else 'Off'
            st.write(f"Sprinkler {i}: {status_str}")
    else:
        # If prediction is a single value
        status_str = 'On' if int(prediction) == 1 else 'Off'
        st.write(f"Sprinkler Status: {status_str}")


