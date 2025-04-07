import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np
from datetime import datetime, timedelta

# Load CSV
kick_data = pd.read_csv('kick_data.csv')

# Check if the CSV already contains a device start time
try:
    device_start_time = pd.to_datetime(kick_data['device_start_time'][0])
except (KeyError, IndexError):
    # If missing, store the current time and save it
    device_start_time = datetime.now()
    kick_data['device_start_time'] = device_start_time.strftime("%Y-%m-%d %I:%M:%S %p")  # 12-hour format
    kick_data.to_csv('kick_data.csv', index=False)

# Convert 'time_ms' to actual timestamps (real-world time of kicks)
kick_data['timestamp'] = device_start_time + pd.to_timedelta(kick_data['time_ms'], unit='ms')

# Assume player mass (kg)
mass = 70  # kg

# Compute force
kick_data['acc_magnitude'] = np.sqrt(kick_data['acc_x']**2 + kick_data['acc_y']**2 + kick_data['acc_z']**2)
kick_data['force'] = mass * kick_data['acc_magnitude']

# Save the updated data with timestamps
kick_data.to_csv('kick_data_with_timestamps.csv', index=False)

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Graph(
        id='force-graph', 
        config={'scrollZoom': True},  # Allow zooming
    ),
])

# Update graph while preserving zoom/pan
@app.callback(
    Output('force-graph', 'figure'),
    Input('force-graph', 'relayoutData')
)
def update_graph(_):
    # Reload CSV
    kick_data = pd.read_csv('kick_data_with_timestamps.csv')
    kick_data['timestamp'] = pd.to_datetime(kick_data['timestamp'])

    # Create the figure
    force_fig = {
        'data': [
            go.Scatter(x=kick_data['timestamp'], y=kick_data['force'], mode='lines', name='Force'),
        ],
        'layout': go.Layout(
            title="Force of Kicks",
            xaxis={'title': 'Time of Day', 'tickformat': '%I:%M %p'},  # 12-hour format
            yaxis={'title': 'Force (N)'},
            showlegend=False,
            uirevision="constant",  # **Keeps zoom & pan settings**
        ),
    }

    return force_fig

if __name__ == '__main__':
    app.run(debug=True)
