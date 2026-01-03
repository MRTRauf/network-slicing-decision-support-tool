# Network Slice Decision Support Tool

This project implements a simple decision support tool for 5G network slicing.
The goal is to help translate QoS requirements and service characteristics into
clear and interpretable slice selection decisions.

Rather than focusing on complex models, this project emphasizes understanding
how slicing policies are reflected in data and how those policies can be
validated and explained using machine learning.

---

## Live Demo

The application is deployed and accessible at:

https://network-slicing-rauf.streamlit.app/

---

## Overview

The tool takes a set of network and service parameters as input and produces
a recommended slice type. It is designed to mirror how slicing decisions are
commonly made in practical telecommunication systems, where policies and SLA
constraints play a central role.

The application provides both a prediction and a short explanation describing
the factors that influence the selected slice.

---

## Input Parameters

The following inputs are supported:

- Packet delay
- Packet loss rate
- Service indicators (IoT, Smartphone, Healthcare, Public Safety, AR/VR/Gaming)
- Network policy flags (Guaranteed Bit Rate and LTE/5G access)

All input ranges are limited to realistic values based on the training data
and typical SLA constraints in 5G networks.

---

## Output

For each request, the tool returns:

- The recommended slice type
- A short explanation describing why the slice was selected
- A visualization showing the position of the request in the QoS space

The visualization helps illustrate how different QoS requirements map to
different slice configurations.

---

## Model Behavior and Accuracy

The dataset used in this project represents deterministic, policy-driven
network slicing decisions. Slice types are defined explicitly by QoS thresholds,
service requirements, and network capabilities.

Because slice boundaries are clearly separated in the feature space, the model
achieves very high accuracy. This behavior is expected and indicates that the
model is correctly reconstructing existing slicing policies rather than learning
noisy or uncertain patterns.

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Random Forest
- NumPy
- Matplotlib

---

## How to Run

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
