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


nat_freq = lambda p, N=100: f"{round(p*N)} out of {N}"

red = "#c00"
green = "#0c0"

def icon_array(k,N,Y = np.linspace(-3,1.5,10),X = np.linspace(-1.5,1.5,10),scale = 0.2):
    n = 0
    array = VGroup()
    for x,y in it.product(X,Y):
        if n < k:
            array.add(SVGMobject("person.svg",fill_color=red).move_to([x,y,0]).scale(scale))
            n += 1
        else:
            array.add(SVGMobject("person.svg",fill_color=green).move_to([x,y,0]).scale(scale))
    return array


class BayesPrescriptedPositive(Scene):
    def construct(self):
        t1 = Tex("The patient is going to be assessed for D using test T").move_to([0,1,0])
        t2 = Tex("The patient receives a positive test result").move_to([0,-1,0])
        self.play(Write(t1))
        self.play(Write(t2))

class BayesPrescriptedNegative(Scene):
    def construct(self):
        t1 = Tex("The patient is going to be assessed for D using test T").move_to([0,1,0])
        t2 = Tex("The patient receives a negative test result").move_to([0,-1,0])
        self.play(Write(t1))
        self.play(Write(t2))
    

class BayesProbHigh(Scene):
    def construct(self):

        p = 0.66
        s = 0.95
        t = 0.85

        PPV = ppv(p,s,t)
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex("The sensitivity and specificity of the test are:").next_to(t1,DOWN)
        t3 = MathTex(f"s = {s}\\ \\ t = {t}").next_to(t2,DOWN)
        t4 = Tex("Based upon similar patients, the prevalence is").next_to(t3,DOWN)
        t5 = MathTex(f"p = {p}").next_to(t4,DOWN)
        t6 = Tex("Using Bayes rule we can calculate the\\\\ positive predictive value for the patient").next_to(t5,DOWN)

        # Bayes' Rule Formula

        ppv_formula = MathTex(
            "PPV = ","\\frac{ps}{ps + (1-p)(1-t)}"
        ).next_to(t6,DOWN*3)

        # Calculation
        ppv_calc = MathTex(
            "PPV = ",f"\\frac{{ {p:.2f}\\cdot{s:.2f} }}{{{p:.2f}\\cdot{s:.2f} + {1-p:.2f}\\cdot{1-t:.2f}}}"
        ).move_to(ppv_formula)
        
        ppv_result = MathTex(
            "PPV = ",f"{PPV:.2f}"
        ).move_to(ppv_formula)

        
        self.play(Write(t1),run_time = 1)
        self.play(Write(t2),run_time = 1)
        self.play(Write(t3),run_time = 1)
        self.play(Write(t4),run_time = 1)
        self.play(Write(t5),run_time = 1)
        self.play(Write(t6),run_time = 1)
        # self.wait(3)
        self.play(Write(ppv_formula))
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_calc),run_time=2)
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_result),run_time=2)
        self.wait(5)
     

class BayesProbMid(Scene):
    def construct(self):

        p = 0.36
        s = 0.92
        t = 0.68

        PPV = ppv(p,s,t)
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex("The sensitivity and specificity of the test are:").next_to(t1,DOWN)
        t3 = MathTex(f"s = {s}\\ \\ t = {t}").next_to(t2,DOWN)
        t4 = Tex("Based upon similar patients, the prevalence is").next_to(t3,DOWN)
        t5 = MathTex(f"p = {p}").next_to(t4,DOWN)
        t6 = Tex("Using Bayes rule we can calculate the\\\\ positive predictive value for the patient").next_to(t5,DOWN)

        # Bayes' Rule Formula

        ppv_formula = MathTex(
            "PPV = ","\\frac{ps}{ps + (1-p)(1-t)}"
        ).next_to(t6,DOWN*3)

        # Calculation
        ppv_calc = MathTex(
            "PPV = ",f"\\frac{{ {p:.2f}\\cdot{s:.2f} }}{{{p:.2f}\\cdot{s:.2f} + {1-p:.2f}\\cdot{1-t:.2f}}}"
        ).move_to(ppv_formula)
        
        ppv_result = MathTex(
            "PPV = ",f"{PPV:.2f}"
        ).move_to(ppv_formula)

        
        self.play(Write(t1),run_time = 1)
        self.play(Write(t2),run_time = 1)
        self.play(Write(t3),run_time = 1)
        self.play(Write(t4),run_time = 1)
        self.play(Write(t5),run_time = 1)
        self.play(Write(t6),run_time = 1)
        # self.wait(3)
        self.play(Write(ppv_formula))
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_calc),run_time=2)
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_result),run_time=2)
        self.wait(5)     
   

class BayesProbLow(Scene):
    def construct(self):

        p = 0.005
        s = 0.99
        t = 0.80

        PPV = ppv(p,s,t)
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex("The sensitivity and specificity of the test are:").next_to(t1,DOWN)
        t3 = MathTex(f"s = {s}\\ \\ t = {t}").next_to(t2,DOWN)
        t4 = Tex("Based upon similar patients, the prevalence is").next_to(t3,DOWN)
        t5 = MathTex(f"p = {p}").next_to(t4,DOWN)
        t6 = Tex("Using Bayes rule we can calculate the\\\\ positive predictive value for the patient").next_to(t5,DOWN)

        # Bayes' Rule Formula

        ppv_formula = MathTex(
            "PPV = ","\\frac{ps}{ps + (1-p)(1-t)}"
        ).next_to(t6,DOWN*3)

        # Calculation
        ppv_calc = MathTex(
            "PPV = ",f"\\frac{{ {p:.2f}\\cdot{s:.2f} }}{{{p:.2f}\\cdot{s:.2f} + {1-p:.2f}\\cdot{1-t:.2f}}}"
        ).move_to(ppv_formula)
        
        ppv_result = MathTex(
            "PPV = ",f"{PPV:.2f}"
        ).move_to(ppv_formula)

        
        self.play(Write(t1),run_time = 1)
        self.play(Write(t2),run_time = 1)
        self.play(Write(t3),run_time = 1)
        self.play(Write(t4),run_time = 1)
        self.play(Write(t5),run_time = 1)
        self.play(Write(t6),run_time = 1)
        # self.wait(3)
        self.play(Write(ppv_formula))
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_calc),run_time=2)
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_result),run_time=2)
        self.wait(5)     
  
       
class BayesNatFreqHigh(Scene):
    def construct(self):
        p = 0.66
        s = 0.95
        t = 0.85

        PPV = ppv(p,s,t)
        N = 100
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex(f"Based upon {N} similar patients we would expect\\\\ {round(N*p)} to have D").next_to(t1,DOWN)
        t3 = Tex(f"For those that have D, {s*100}\\% test positive").next_to(t2,DOWN)
        t4 = Tex(f"For those that do not have D, {t*100}\\% test negative").next_to(t3,DOWN)


        population = Tex(f"{N} similar patients").scale(0.5).next_to(t4,DOWN*2)
        sick = Tex(f"{N*p:.0f} have D").scale(0.5).next_to(population, 3*DOWN + 3*LEFT)
        well = Tex(f"{N*(1-p):.0f} do not have D").scale(0.5).next_to(population, 3*DOWN + 3*RIGHT)
        sickpos = Tex(f"{(N*p*s):.0f} Positive").scale(0.5).next_to(sick, 3*DOWN + 1.5*LEFT)
        sickneg = Tex(f"{(N*p*(1-s)):.0f} Negative").scale(0.5).next_to(sick, 3*DOWN + 1.5*RIGHT)
        wellpos = Tex(f"{(N*(1-p)*(1-t)):.0f} Positive").scale(0.5).next_to(well, 3*DOWN + 1.5*LEFT)
        wellneg = Tex(f"{(N*(1-p)*(t)):.0f} Negative").scale(0.5).next_to(well, 3*DOWN + 1.5*RIGHT)
        n,d = simplify_fraction(N*p*s, N*p*s + N*(1-p)*(1-t))
        t5 = Tex(f"Hence we would expect \\\\{n:.0f} out of {d:.0f}\\\\ positive tests to actually have D").move_to([0,wellneg.get_y(),0]+DOWN*1.5)
        # Create edges
        edges = [
            (population, sick),
            (population, well),
            (sick, sickpos),
            (sick, sickneg),
            (well, wellpos),
            (well, wellneg),
        ]
        graph = [Line(start=node1.get_bottom()+0.05*DOWN, end=node2.get_top()+0.05*UP) for node1, node2 in edges]

        self.play(Create(t1))
        self.play(Create(t2),Create(population))
        self.play(Create(t3))
        self.play(Create(graph[0]),Create(graph[1]))
        self.play(Create(sick),Create(well))
        self.play(Create(t3))
        self.play(Create(graph[2]),Create(graph[3]))
        self.play(Create(sickpos),Create(sickneg))
        self.play(Create(t4))
        self.play(Create(graph[5]),Create(graph[4]))
        self.play(Create(wellpos),Create(wellneg))
        self.play(Write(t5))
       
class BayesNatFreqMid(Scene):
    def construct(self):
        p = 0.36
        s = 0.92
        t = 0.68

        PPV = ppv(p,s,t)
        N = 100
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex(f"Based upon {N} similar patients we would expect\\\\ {round(N*p)} to have D").next_to(t1,DOWN)
        t3 = Tex(f"For those that have D, {s*100}\\% test positive").next_to(t2,DOWN)
        t4 = Tex(f"For those that do not have D, {t*100}\\% test negative").next_to(t3,DOWN)


        population = Tex(f"{N} similar patients").scale(0.5).next_to(t4,DOWN*2)
        sick = Tex(f"{N*p:.0f} have D").scale(0.5).next_to(population, 3*DOWN + 3*LEFT)
        well = Tex(f"{N*(1-p):.0f} do not have D").scale(0.5).next_to(population, 3*DOWN + 3*RIGHT)
        sickpos = Tex(f"{(N*p*s):.0f} Positive").scale(0.5).next_to(sick, 3*DOWN + 1.5*LEFT)
        sickneg = Tex(f"{(N*p*(1-s)):.0f} Negative").scale(0.5).next_to(sick, 3*DOWN + 1.5*RIGHT)
        wellpos = Tex(f"{(N*(1-p)*(1-t)):.0f} Positive").scale(0.5).next_to(well, 3*DOWN + 1.5*LEFT)
        wellneg = Tex(f"{(N*(1-p)*(t)):.0f} Negative").scale(0.5).next_to(well, 3*DOWN + 1.5*RIGHT)
        n,d = simplify_fraction(N*p*s, N*p*s + N*(1-p)*(1-t))
        t5 = Tex(f"Hence we would expect \\\\{n:.0f} out of {d:.0f}\\\\ positive tests to actually have D").move_to([0,wellneg.get_y(),0]+DOWN*1.5)
        # Create edges
        edges = [
            (population, sick),
            (population, well),
            (sick, sickpos),
            (sick, sickneg),
            (well, wellpos),
            (well, wellneg),
        ]
        graph = [Line(start=node1.get_bottom()+0.05*DOWN, end=node2.get_top()+0.05*UP) for node1, node2 in edges]

        self.play(Create(t1))
        self.play(Create(t2),Create(population))
        self.play(Create(t3))
        self.play(Create(graph[0]),Create(graph[1]))
        self.play(Create(sick),Create(well))
        self.play(Create(t3))
        self.play(Create(graph[2]),Create(graph[3]))
        self.play(Create(sickpos),Create(sickneg))
        self.play(Create(t4))
        self.play(Create(graph[5]),Create(graph[4]))
        self.play(Create(wellpos),Create(wellneg))
        self.play(Write(t5))

       
class BayesNatFreqLow(Scene):
    def construct(self):
        p = 0.005
        s = 0.99
        t = 0.80

        PPV = ppv(p,s,t)
        N = 200
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex(f"Based upon {N} similar patients we would expect\\\\ {round(N*p)} to have D").next_to(t1,DOWN)
        t3 = Tex(f"For those that have D, {s*100}\\% test positive").next_to(t2,DOWN)
        t4 = Tex(f"For those that do not have D, {t*100}\\% test negative").next_to(t3,DOWN)


        population = Tex(f"{N} similar patients").scale(0.5).next_to(t4,DOWN*2)
        sick = Tex(f"{N*p:.0f} have D").scale(0.5).next_to(population, 3*DOWN + 3*LEFT)
        well = Tex(f"{N*(1-p):.0f} do not have D").scale(0.5).next_to(population, 3*DOWN + 3*RIGHT)
        sickpos = Tex(f"{(N*p*s):.0f} Positive").scale(0.5).next_to(sick, 3*DOWN + 1.5*LEFT)
        sickneg = Tex(f"{(N*p*(1-s)):.0f} Negative").scale(0.5).next_to(sick, 3*DOWN + 1.5*RIGHT)
        wellpos = Tex(f"{(N*(1-p)*(1-t)):.0f} Positive").scale(0.5).next_to(well, 3*DOWN + 1.5*LEFT)
        wellneg = Tex(f"{(N*(1-p)*(t)):.0f} Negative").scale(0.5).next_to(well, 3*DOWN + 1.5*RIGHT)
        n,d = simplify_fraction(N*p*s, N*p*s + N*(1-p)*(1-t))
        t5 = Tex(f"Hence we would expect \\\\{n:.0f} out of {d:.0f}\\\\ positive tests to actually have D").move_to([0,wellneg.get_y(),0]+DOWN*1.5)
        # Create edges
        edges = [
            (population, sick),
            (population, well),
            (sick, sickpos),
            (sick, sickneg),
            (well, wellpos),
            (well, wellneg),
        ]
        graph = [Line(start=node1.get_bottom()+0.05*DOWN, end=node2.get_top()+0.05*UP) for node1, node2 in edges]

        self.play(Create(t1))
        self.play(Create(t2),Create(population))
        self.play(Create(t3))
        self.play(Create(graph[0]),Create(graph[1]))
        self.play(Create(sick),Create(well))
        self.play(Create(t3))
        self.play(Create(graph[2]),Create(graph[3]))
        self.play(Create(sickpos),Create(sickneg))
        self.play(Create(t4))
        self.play(Create(graph[5]),Create(graph[4]))
        self.play(Create(wellpos),Create(wellneg))
        self.play(Write(t5))
        
class BayesIconArrayHigh(Scene):
    def construct(self):
        p = 0.66
        s = 0.95
        t = 0.85
        PPV = ppv(p,s,t)
        N = 200
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex(f"Based upon {N} similar patients we would expect\\\\ {round(N*p)} to have D").next_to(t1,DOWN)
        t3 = Tex("The sensitivity and specificity of the test are:").next_to(t2,DOWN)
        t4 = MathTex(f"s = {s}\\ \\ t = {t}").next_to(t3,DOWN)
        t5 = Tex(f"Using Bayes Rule we can calculate $PPV = {PPV:.2f}$")
        
        X = np.linspace(-4,4,25)
        Y = np.linspace(-4,-1,8)
        
        init_array = VGroup(*[SVGMobject("person.svg").move_to([x,y,0]).scale(0.2) for x,y in it.product(X,Y)])
        
        n,d = simplify_fraction(N*p*s, N*p*s + N*(1-p)*(1-t))
        # t5 = Tex(f"Hence we would expect \\\\{n:.0f} out of {d:.0f}\\\\ positive tests to actually have D").move_to([0,wellneg.get_y(),0]+DOWN*1.5)
        
        prev_array = icon_array(p*N,N,Y,X)
        ppv_array = icon_array(PPV*N,N,Y,X)
        
        
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(LaggedStart(*[DrawBorderThenFill(i) for i in init_array],lag_ratio=0.01,run_time = 2))
        self.play(Write(t3))
        self.play(TransformMatchingShapes(init_array,prev_array))
        self.play(Write(t4))
        self.play(Write(t5),Transform(prev_array,ppv_array))
        
            
class BayesIconArrayMid(Scene):
    def construct(self):
        p = 0.36
        s = 0.92
        t = 0.68
        PPV = ppv(p,s,t)
        N = 100
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex(f"Based upon {N} similar patients we would expect\\\\ {round(N*p)} to have D").next_to(t1,DOWN)
        t3 = Tex("The sensitivity and specificity of the test are:").next_to(t2,DOWN)
        t4 = MathTex(f"s = {s}\\ \\ t = {t}").next_to(t3,DOWN)
        t5 = Tex(f"Using Bayes Rule we can calculate $PPV = {PPV:.2f}$")
        
        X = np.linspace(-4,4,25)
        Y = np.linspace(-4,-1,8)
        init_array = VGroup(*[SVGMobject("person.svg").move_to([x,y,0]).scale(0.2) for x,y in it.product(X,Y)])
        
        n,d = simplify_fraction(N*p*s, N*p*s + N*(1-p)*(1-t))
        # t5 = Tex(f"Hence we would expect \\\\{n:.0f} out of {d:.0f}\\\\ positive tests to actually have D").move_to([0,wellneg.get_y(),0]+DOWN*1.5)
        
        prev_array = icon_array(p*N,N,Y,X)
        ppv_array = icon_array(PPV*N,N,Y,X)
        
        
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(LaggedStart(*[DrawBorderThenFill(i) for i in init_array],lag_ratio=0.01,run_time = 2))
        self.play(TransformMatchingShapes(init_array,prev_array))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5),Transform(prev_array,ppv_array))
        
class BayesIconArrayLow(Scene):
    def construct(self):
        p = 0.005
        s = 0.99
        t = 0.80
        PPV = ppv(p,s,t)
        N = 200
        t1 = Tex("The patient is going to be assessed for D using test T").to_edge(UP)
        t2 = Tex(f"Based upon {N} similar patients we would expect\\\\ {round(N*p)} to have D").next_to(t1,DOWN)
        t3 = Tex("The sensitivity and specificity of the test are:").next_to(t2,DOWN)
        t4 = MathTex(f"s = {s}\\ \\ t = {t}").next_to(t3,DOWN)
        t5 = Tex(f"Using Bayes Rule we can calculate $PPV = {PPV:.2f}$")
        
        X = np.linspace(-4,4,25)
        Y = np.linspace(-4,-1,8)
        
        init_array = VGroup(*[SVGMobject("person.svg").move_to([x,y,0]).scale(0.2) for x,y in it.product(X,Y)])
        
        n,d = simplify_fraction(N*p*s, N*p*s + N*(1-p)*(1-t))
        # t5 = Tex(f"Hence we would expect \\\\{n:.0f} out of {d:.0f}\\\\ positive tests to actually have D").move_to([0,wellneg.get_y(),0]+DOWN*1.5)
        
        prev_array = icon_array(p*N,N,Y,X)
        ppv_array = icon_array(PPV*N,N,Y,X)
        
        
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(LaggedStart(*[DrawBorderThenFill(i) for i in init_array],lag_ratio=0.01,run_time = 2))
        self.play(Write(t3))
        self.play(TransformMatchingShapes(init_array,prev_array))
        self.play(Write(t4))
        self.play(Write(t5),Transform(prev_array,ppv_array))
        