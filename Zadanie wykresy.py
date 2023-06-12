import plotly.graph_objects as go


salaries = [
    ("Mark", 1000),
    ("John", 1500),
    ("Daniel", 2300),
    ("Greg", 5000)
]


names = list(map(lambda tup: tup[0], salaries))


salary_values = list(map(lambda tup: tup[1], salaries))


fig = go.Figure(data=go.Bar(x=names, y=salary_values))


fig.update_layout(
    title="Pensje pracowników",
    xaxis_title="Imię",
    yaxis_title="Pensja"
)


fig.show()






