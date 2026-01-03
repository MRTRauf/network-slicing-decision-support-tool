import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Network Slice Decision Support",
    layout="centered"
)

#Load model and scaler (loaded once at startup)

rf_model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Network Slice Decision Support Tool")

st.markdown(
    """
    This tool supports **QoS-aware network slicing decisions** by translating
    service requirements and SLA parameters into interpretable slice selection outcomes.
    """
)

st.divider()

#Input
st.header("Input QoS")

packet_delay = st.number_input(
    "Packet Delay (ms)",
    min_value=0,
    max_value=300,
    value=50,
    step=1,
    help="End-to-end packet delay in milliseconds. Low values indicate latency-critical services."
)


packet_loss = st.number_input(
    "Packet Loss Rate",
    min_value=0.0,
    max_value=0.01,
    value=0.001,
    step=0.00001,
    format="%.5f",
    help="Packet loss ratio (0–1%). Smaller values indicate higher reliability requirements."
)


st.caption("QoS inputs are limited to realistic SLA ranges used during model training.")

st.divider()

st.header("Service Type")

iot = st.checkbox("IoT")
smartphone = st.checkbox("Smartphone")
healthcare = st.checkbox("Healthcare")
public_safety = st.checkbox("Public Safety")
arvr = st.checkbox("AR/VR/Gaming")

st.divider()

st.header("Network Policy")

gbr = st.checkbox("Guaranteed Bit Rate (GBR)")
is_5g = st.checkbox("5G Access (LTE/5G)")

st.divider()

#Prediction Section

st.header("Slice Recommendation")

if st.button("Evaluate Slice"):

    #Build input vector
    input_data = np.array([[
        packet_delay,
        packet_loss,
        int(iot),
        int(smartphone),
        int(healthcare),
        int(public_safety),
        int(arvr),
        int(gbr),
        int(is_5g)
    ]])

    input_scaled = scaler.transform(input_data)

    predicted_slice = rf_model.predict(input_scaled)[0]

    #Output result
    st.success(f"✅ Recommended Slice: **Slice Type {predicted_slice}**")

    st.markdown("### Why this slice?")

    if packet_delay < 20:
        st.write("- Very low packet delay requirement")
    elif packet_delay > 100:
        st.write("- Delay-tolerant traffic profile")

    if packet_loss < 0.001:
        st.write("- High reliability requirement (low packet loss)")
    elif packet_loss > 0.005:
        st.write("- Packet loss tolerance is acceptable")

    if iot:
        st.write("- IoT-based service detected")

    if smartphone:
        st.write("- Smartphone broadband traffic")

    if healthcare:
        st.write("- Healthcare service with strict SLA")

    if public_safety:
        st.write("- Public safety–oriented traffic")

    if arvr:
        st.write("- AR/VR or gaming service detected")

    if gbr:
        st.write("- Guaranteed Bit Rate is required")

    if is_5g:
        st.write("- 5G access capability enabled")

    st.info(
        "Note: This tool reflects deterministic network slicing policies. "
        "High accuracy is expected because slice boundaries are explicitly defined "
        "by QoS and service intent."
    )

    #QoS Visualization
    st.markdown("### QoS Position of Current Request")

    fig, ax = plt.subplots()
    ax.scatter(packet_delay, packet_loss, color="red", s=80, label="Current Request")
    ax.set_xlabel("Packet Delay (ms)")
    ax.set_ylabel("Packet Loss Rate")
    ax.set_ylim(0, 0.01)
    ax.set_title("QoS Space")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)