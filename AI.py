from manim import *
import math
import numpy as np
import itertools as it

def simplify_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    numerator = round(numerator)
    denominator = round(denominator)
    # Find the greatest common divisor (GCD) of the numerator and denominator
    gcd = math.gcd(numerator, denominator)

    # Simplify the fraction by dividing both numerator and denominator by the GCD
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    

    return simplified_numerator, simplified_denominator


config.pixel_height = 2160  # Set the vertical resolution to 2160 pixels (4K).
config.pixel_width = 2880   # Calculate the horizontal resolution for 4:3 aspect ratio.
config.frame_height = 9.0   # Set the frame height to 9 units (adjust as needed).
config.frame_width = 12.0   # Set the frame width to 12 units (adjust as needed).

# Set the background color and text color
config.background_color = WHITE
Text.set_default(font="Helvetica Neue", font_size=50, color=BLACK)
MathTex.set_default(color=BLACK)
Mobject.set_default(color=BLACK)

ppv = lambda p,s,t: (p*s)/(p*s + (1-p)*(1-t))


def nat_freq(p, N = 100):
    return f"{round(p*N)} out of {N}"
    

red = "#c00"
green = "#0c0"

def icon_array(k,N,Y = np.linspace(-3,1.5,10),X = np.linspace(-1.5,1.5,10)):
    n = 0
    array = VGroup()
    for x,y in it.product(X,Y):
        if n < k:
            array.add(SVGMobject("person.svg",fill_color=red).move_to([x,y,0]).scale(0.2))
            n += 1
        else:
            array.add(SVGMobject("person.svg",fill_color=green).move_to([x,y,0]).scale(0.2))
    return array

class AIPrescripted(Scene):
    def construct(self):
        t1 = Tex("The patient is going to be assessed for D using\\\\a machine learning based\\\\clinical decision support system").move_to([0,1,0],aligned_edge=DOWN)

        t2 = Tex("The algorithm says that the patient has D").move_to([0,-1,0])
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(5)

class AIProb(Scene):
    def construct(self):
        p = 0.38
        t1 = Tex("The patient is going to be assessed for D using\\\\a machine learning based\\\\clinical decision support system").move_to([0,1,0],aligned_edge=DOWN)
        t2 = Tex(f"The algorithm says that the probability of\\\\the patient having $D$ is {p}").move_to([0,-1,0])
        
        self.play(Write(t1),run_time = 1)
        self.play(Write(t2),run_time = 1)
        self.wait(5)

        
class AINatFreq(Scene):
    def construct(self):
        p = 0.73
        t1 = Tex("The patient is going to be assessed for D using\\\\a machine learning based\\\\clinical decision support system").to_edge(UP)
        t2 = Tex(f"The algorithm says that {nat_freq(p)}\\\\similar patients will have D")
        
        self.play(Write(t1),run_time = 1)
        self.play(Write(t2),run_time = 1)
        self.wait(5)
        
class AIIconArray(Scene):
    def construct(self):
        p = 0.38
        N = 100
        t1 = Tex("The patient is going to be assessed for D using\\\\a machine learning based\\\\clinical decision support system").to_edge(UP)
        t2 = Tex(f"The algorithm returns the following icon array:").next_to(t1,DOWN*1.5)
        
        t3 = Tex(f"{nat_freq(p,100)} similar patients have D").to_edge(DOWN)
        array = icon_array(p*N,N,Y = np.linspace(-3,0,5),X = np.linspace(-3,3,20))
        
        self.play(Write(t1),run_time = 1)
        self.play(Write(t2),run_time = 1)
        self.play(LaggedStart(*[DrawBorderThenFill(i) for i in array],lag_ratio=0.01,run_time = 2),Write(t3))
        self.wait(5)