from manim import *

from collections import defaultdict
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import roc_curve, auc

# Set the background color and text color
config.background_color = WHITE
Text.set_default(font="Helvetica Neue", font_size=50, color=BLACK)
MathTex.set_default(color=BLACK)
Mobject.set_default(color=BLACK)

#%%
### Create dataset
rng = np.random.default_rng(2)
true_probabilities = defaultdict(float)
many = 10000
dataset ={'x':[],'y':[]}
true_probabilities = {
    i:j for i,j in zip(range(11),sorted(rng.random(11)))
}

for i in range(11):

    for j in range(many + rng.integers(-25,25)):
        dataset['x'].append(i)
        dataset['y'].append(true_probabilities[i] >= rng.random())

dataset = pd.DataFrame(dataset)

#%% Fit logistic regression using statsmodels
X = sm.add_constant(dataset['x'])  # Add constant for intercept
Y = dataset['y']

model = sm.Logit(Y, X)
result = model.fit()

# Print summary with standard errors
print(result.summary())

# Plot the logistic regression curve
x_vals = np.linspace(0, 10,101)
y_vals = result.predict(sm.add_constant(x_vals))  # Probabilities of class 1
# Get the confidence intervals
pred = result.get_prediction(sm.add_constant(x_vals))
conf_int = pred.conf_int()  # 95% confidence intervals


class LogisticRegression(Scene):
    def construct(self):
        # Title
        title = Text("Logistic Regression", font_size=48)
        title.to_edge(UP)
        self.add(title)

        # Axes
        axes = Axes(
            x_range=[0, 10],
            y_range=[-0.1, 1.1],
            axis_config = {"include_numbers":True},
            tips = False
        )
        axes.move_to(ORIGIN)
        y_axis_label = MathTex('\\Pr(D)').rotate(PI/2).next_to(axes,LEFT)
        x_axis_label = MathTex('X').next_to(axes,DOWN)
        
        graph = VGroup(axes,y_axis_label,x_axis_label)
        
        self.play(Create(graph))

        lr = axes.plot_line_graph(x_vals,y_vals, line_color = BLACK, add_vertex_dots=False)

        self.play(Create(lr))

        # self.wait(3)
        
        v = 70
        
        l1 = axes.plot_line_graph([x_vals[v],x_vals[v]],[0,y_vals[v]],line_color=BLUE,vertex_dot_style={'color':DARK_BLUE})
        l2 = axes.plot_line_graph([x_vals[v],0],[y_vals[v],y_vals[v]],line_color=BLUE,vertex_dot_style={'color':DARK_BLUE})
        
        y_val = MathTex(f"{y_vals[v]:.2f}",color=PURE_RED).next_to(l2["vertex_dots"][1],UP/3+RIGHT/3)
        
        # self.play(Write(x_val))
        self.play(Write(l1["vertex_dots"][0]),run_time=0.5)
        self.play(Write(l1["line_graph"]),run_time=1)
        self.play(Write(l1["vertex_dots"][1]),run_time=0.5)
        self.play(Write(l2["line_graph"]),run_time=1)
        self.play(Write(l2["vertex_dots"][1]),run_time=0.5)
        self.play(Write(y_val))
        self.wait()
        

def icon_array(k,N,Y = np.linspace(-3,1.5,10),X = np.linspace(-1.5,1.5,10)):
    n = 0
    array = VGroup()
    for y in Y:
        for x in X:
            if n < int(k):
                array.add(SVGMobject("person.svg",fill_color=PURE_RED).move_to([x,y,0]).scale(0.2))
                n += 1
            else:
                array.add(SVGMobject("person.svg",fill_color=GREEN).move_to([x,y,0]).scale(0.2))
    return array

class LRIconArray(Scene):
    def construct(self):
        # Title
        title = Text("Logistic Regression", font_size=48)
        title.to_edge(UP)
        self.add(title)

        # Axes
        axes = Axes(
            x_range=[0, 10],
            y_range=[-0.1, 1.1],
            axis_config = {"include_numbers":True},
            tips = False
        )
        axes.move_to(ORIGIN)
        y_axis_label = MathTex('\\Pr(D)').rotate(PI/2).next_to(axes,LEFT)
        x_axis_label = MathTex('X').next_to(axes,DOWN)
        
        graph = VGroup(axes,y_axis_label,x_axis_label)
        
        self.add(graph)

        lr = axes.plot_line_graph(x_vals,y_vals, line_color = BLACK, add_vertex_dots=False)

        self.add(lr)

        # self.wait(3)
        
        v = 50
        
        l1 = axes.plot_line_graph([x_vals[v],x_vals[v]],[0,y_vals[v]],line_color=BLUE,vertex_dot_style={'color':DARK_BLUE})
        l2 = axes.plot_line_graph([x_vals[v],0],[y_vals[v],y_vals[v]],line_color=BLUE,vertex_dot_style={'color':DARK_BLUE})
        
        y_val = MathTex(f"{y_vals[v]:.2f}",color=PURE_RED).next_to(l2["vertex_dots"][1],UP/3+RIGHT/3)
        
        self.add(y_val,l1,l2)
        array = icon_array(y_vals[v]*100,100)
        natfreq = Text(f"{int(y_vals[v]*100)} out of 100").next_to(array,DOWN)
        
        self.play(AnimationGroup(
            AnimationGroup(Uncreate(l1),Uncreate(l2),Uncreate(graph),Uncreate(lr),run_time = 2),
            Transform(y_val,natfreq,run_time=1.5),
            LaggedStart(*[DrawBorderThenFill(i) for i in array],lag_ratio=0.01,run_time = 3),
            lag_ratio=0.5
        ))
        
        self.wait()

class LRBar(Scene):
    def construct(self):
        # Title
        title = Text("Logistic Regression", font_size=48)
        title.to_edge(UP)
        self.add(title)

        # Axes
        axes = Axes(
            x_range=[0, 10],
            y_range=[-0.1, 1.1],
            axis_config = {"include_numbers":True},
            tips = False
        )
        axes.move_to(ORIGIN)
        y_axis_label = MathTex('\\Pr(D)').rotate(PI/2).next_to(axes,LEFT)
        x_axis_label = MathTex('X').next_to(axes,DOWN)
        
        graph = VGroup(axes,y_axis_label,x_axis_label)
        
        self.add(graph)

        lr = axes.plot_line_graph(x_vals,y_vals, line_color = BLACK, add_vertex_dots=False)

        self.add(lr)

        # self.wait(3)
        
        v = 50
        
        l1 = axes.plot_line_graph([x_vals[v],x_vals[v]],[0,y_vals[v]],line_color=BLUE,vertex_dot_style={'color':DARK_BLUE})
        l2 = axes.plot_line_graph([x_vals[v],0],[y_vals[v],y_vals[v]],line_color=BLUE,vertex_dot_style={'color':DARK_BLUE})
        
        y_val = MathTex(f"{y_vals[v]:.2f}",color=PURE_RED).next_to(l2["vertex_dots"][1],UP/3+RIGHT/3)
        
        self.add(y_val,l1,l2)
        self.play(Uncreate(y_val),Uncreate(l1),Uncreate(l2))
        
        d = np.abs(axes.coords_to_point(0,0,0) - axes.coords_to_point(1,1,0))
        print(d)
        bar_chart = VGroup()
        for k,v in true_probabilities.items():
            bar_chart += Rectangle(width = 0.75*d[0],height=v*d[1],color = GREEN,fill_opacity=0.8).move_to(
                axes.coords_to_point(k,v/2,-1)
            )
            
        print(bar_chart)
        self.play(Create(bar_chart))
        
        self.wait()
