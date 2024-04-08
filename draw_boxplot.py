
import plotly.express as px
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go


file_name = 'eval_packnet_sfm'
#file_name = 'eval_depth_anything'
file_path = file_name+'.csv'

# Read the Excel file
df = pd.read_csv(file_path)

# Sort the DataFrame by 'weather_condition'
df = df.sort_values('weather_condition')
col="abs_rel"
# Draw boxplots with different colors for each 'weather_condition'
fig = px.box(df, y=col, x="weather_condition", color="weather_condition")

# Calculate statistics for each group
grouped = df.groupby('weather_condition')[col].describe()

# Add annotations for each group
annotations = []
for i, (place, stats) in enumerate(grouped.iterrows()):
    # Add a small offset to the x position
    x_position = i + 0.44
    annotations.append(
        go.layout.Annotation(
            x=x_position,
            y=stats['max'],
            text=f"Max: {stats['max']:.2f}",
            showarrow=False,
            font=dict(size=6, color="black", family="Arial Bold")  # Reduce the font size
        )
    )
    annotations.append(
        go.layout.Annotation(
            x=x_position,
            y=stats['75%']+0.015,
            text=f"Q3: {stats['75%']:.2f}",
            showarrow=False,
            font=dict(size=6, color="black", family="Arial Bold")  # Reduce the font size
        )
    )
    annotations.append(
        go.layout.Annotation(
            x=x_position,
            y=stats['50%']+0.015,
            text=f"Median: {stats['50%']:.2f}",
            showarrow=False,
            font=dict(size=6, color="black", family="Arial Bold")  # Reduce the font size
        )
    )
    annotations.append(
        go.layout.Annotation(
            x=x_position,
            y=stats['25%'],
            text=f"Q1: {stats['25%']:.2f}",
            showarrow=False,
            font=dict(size=6, color="black", family="Arial Bold")  # Reduce the font size
        )
    )
    annotations.append(
        go.layout.Annotation(
            x=x_position,
            y=stats['min']-0.025,
            text=f"Min: {stats['min']:.2f}",
            showarrow=False,
            font=dict(size=6, color="black", family="Arial Bold")  # Reduce the font size
        )
    )
    # Add mean to the annotations
    annotations.append(
        go.layout.Annotation(
            x=x_position,
            y=stats['mean'],
            text=f"Mean: {stats['mean']:.2f}",
            showarrow=False,
            font=dict(size=6, color="black", family="Arial Bold")  # Reduce the font size
        )
    )

fig.update_layout(
    annotations=annotations,
    # Place the color legend at the bottom
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    # Reduce the margins
    margin=dict(
        l=10,  # left margin
        r=10,  # right margin
        b=10,  # bottom margin
        t=10,  # top margin
        pad=10  # padding
    )
)

fig.show()

pio.write_image(fig, file_name+'_'+col+'.pdf')