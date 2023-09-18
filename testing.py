from manim import *

# Set the background color and text color
config.background_color = WHITE
Text.set_default(font="Helvetica Neue", font_size=50, color=WHITE)
MathTex.set_default(color=BLACK)
Mobject.set_default(color=BLACK)

red = "#c00"
green = "#0c0"

def icon_array(k,N,Y = np.linspace(-3,1.5,10),X = np.linspace(-1.5,1.5,10)):
    n = 0
    array = VGroup()
    for y in Y:
        for x in X:
            if n < int(k):
                array.add(SVGMobject("person.svg",fill_color=red).move_to([x,y,0]).scale(0.2))
                n += 1
            else:
                array.add(SVGMobject("person.svg",fill_color=green).move_to([x,y,0]).scale(0.2))
    return array

# Calculate probabilities using Bayes' Rule
ppv = lambda p,s,t: (p * s) / ((p * s) + (1-t) * (1-p))
npv = lambda p,s,t: (t*(1-p))/(t*(1-p) + p*(1-s))

low_p = 0.95
low_s = 0.95
low_t = 0.33

mid_p = 0.3
mid_s = 0.6
mid_t = 0.6

high_p = 0.5
high_s = 0.99
high_t = 0.99


# Define custom constants
class BayesRuleMid(Scene):
    def construct(self):
        p = mid_p  # prevelence
        s = mid_s  # sensitivity
        t = mid_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        MathTex.set_default(font_size=36)
        # Title
        title = Text("Traditional Bayesian Method")
        title.to_edge(UP)
        self.add(title)

        p_text = MathTex(f"p = {p}, s = {s}, t = {t}").move_to([0,1.5,0])
        

        # Bayes' Rule Formula
        pdt = MathTex("P(D|T+) = ").move_to([1,0,0],aligned_edge=LEFT)
        ndt = MathTex("P(D|T-) = ").move_to([-6,0,0],aligned_edge=LEFT)
    
        ppv_formula = MathTex(
            "\\frac{ps}{ps + (1-p)(1-t)}"
        ).next_to(pdt,RIGHT)
        npv_formula = MathTex(
            "1-\\frac{(1-p)t}{(1-p)t + p(1-s)}"
        ).next_to(ndt,RIGHT)

        # Calculation
        ppv_calc = MathTex(
            f"\\frac{{ {p:.2f}\\times{s:.2f} }}{{{p:.2f}\\times{s:.2f} + {1-p:.2f}\\times{1-t:.2f}}}"
        ).align_to(ppv_formula,LEFT)
        npv_calc = MathTex(
            f"1-\\frac{{ {1-p:.2f}\\times{t:.2f} }}{{{1-p:.2f}\\times{t:.2f} + {p:.2f}\\times{1-s:.2f}}}"
        ).align_to(npv_formula,LEFT)
        
        ppv_result = MathTex(
            f"{PPV:.2f}"
        ).align_to(ppv_formula,LEFT)
        
        npv_result = MathTex(
            f"{1-NPV:.2f}"
        ).align_to(npv_formula,LEFT)
        
        self.add(p_text)
        self.play(Write(pdt),Write(ppv_formula),Write(ndt),Write(npv_formula))
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_calc),Transform(npv_formula,npv_calc),run_time=2)
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_result),Transform(npv_formula,npv_result),run_time=2)
        self.wait(5)
        
class IconArrayMid(Scene):
    def construct(self):
        p = mid_p  # prevelence
        s = mid_s  # sensitivity
        t = mid_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        
        title = Text("Icon Array")
        title.to_edge(UP)
        self.add(title)
        


        N = 100
        
        init_array = icon_array(p*N,N)
        p_array = icon_array(PPV*N,N,X = np.linspace(-5,-2,10))
        n_array = icon_array((1-NPV)*N,N, X = np.linspace(2,5,10))
        
        t1 = VGroup(Text("Before test", font_size=36).next_to(init_array,UP),
             Text(f"{int(p*N)} out of 100", font_size=36).next_to(init_array,DOWN))
        t2 = VGroup(Text("After positive test", font_size=36).next_to(p_array,UP),
             Text(f"{int(PPV*N)} out of 100", font_size=36).next_to(p_array,DOWN))
        t3 = VGroup(Text("After negative test", font_size=36).next_to(n_array,UP),
             Text(f"{int((1-NPV)*N)} out of 100", font_size=36).next_to(n_array,DOWN))
        
        self.play(LaggedStart(*[DrawBorderThenFill(i) for i in init_array],lag_ratio=0.01,run_time = 2),Write(t1))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Transform(init_array,p_array),
                    Transform(t1,t2),
                    run_time=4),
                LaggedStart(*[DrawBorderThenFill(i) for i in n_array],lag_ratio=0.01,run_time = 3),
                Write(t3),
                lag_ratio=0.5
                )
        )
        self.wait(5)

             
class NLineMid(Scene):
    def construct(self):
        p = mid_p  # prevelence
        s = mid_s  # sensitivity
        t = mid_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        title = Text("Number Line")
        title.to_edge(UP)
        self.add(title)
        # Create a number line
        number_line = NumberLine(
            x_range=[0, 1], 
            length=10,
            include_numbers=True,
            numbers_to_include = np.arange(0,1.1,.1),
            decimal_number_config={'num_decimal_places':2}
            ).move_to([0,0,0])
        
        # markers = VGroup(
        #     Line(UP, DOWN, color=BLUE).scale(0.2).move_to(number_line.n2p(0.1)),
        #     Line(UP, DOWN, color=BLUE).scale(0.2).move_to(number_line.n2p(0.5))
        # )
        
        # Create a ball
        ballp = Dot(color=GREEN).shift(number_line.n2p(p))
        balln = Dot(color=PURE_RED).shift(number_line.n2p(p))
        ball = Dot(color=GRAY).shift(number_line.n2p(p))

        # Animate the ball moving on the number line
        self.play(GrowFromCenter(number_line))
        self.play(FadeIn(ball))
        self.add(ballp,balln)
        
        pos_test = Text('If positive test',color=GREEN).next_to(number_line,DOWN)
        neg_test = Text('If negative test',color=PURE_RED).move_to(pos_test)
        self.wait(2)
        self.play(
            ballp.animate.move_to(number_line.n2p(PPV)),
            Write(pos_test),
            run_time=2
        ) ;  self.wait(2)
        
        self.play(
            Transform(pos_test,neg_test),
            balln.animate.move_to(number_line.n2p(1-NPV)),
            run_time=2
        )
        self.wait(5)


# Define custom constants
class BayesRuleLow(Scene):
    def construct(self):
        p = low_p  # prevelence
        s = low_s  # sensitivity
        t = low_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        MathTex.set_default(font_size=36)
        # Title
        title = Text("Traditional Bayesian Method")
        title.to_edge(UP)
        self.add(title)

        p_text = MathTex(f"p = {p}, s = {s}, t = {t}").move_to([0,1.5,0])
        

        # Bayes' Rule Formula
        pdt = MathTex("P(D|T+) = ").move_to([1,0,0],aligned_edge=LEFT)
        ndt = MathTex("P(D|T-) = ").move_to([-6,0,0],aligned_edge=LEFT)
    
        ppv_formula = MathTex(
            "\\frac{ps}{ps + (1-p)(1-t)}"
        ).next_to(pdt,RIGHT)
        npv_formula = MathTex(
            "1-\\frac{(1-p)t}{(1-p)t + p(1-s)}"
        ).next_to(ndt,RIGHT)

        # Calculation
        ppv_calc = MathTex(
            f"\\frac{{ {p:.2f}\\times{s:.2f} }}{{{p:.2f}\\times{s:.2f} + {1-p:.2f}\\times{1-t:.2f}}}"
        ).align_to(ppv_formula,LEFT)
        npv_calc = MathTex(
            f"1-\\frac{{ {1-p:.2f}\\times{t:.2f} }}{{{1-p:.2f}\\times{t:.2f} + {p:.2f}\\times{1-s:.2f}}}"
        ).align_to(npv_formula,LEFT)
        
        ppv_result = MathTex(
            f"{PPV:.2f}"
        ).align_to(ppv_formula,LEFT)
        
        npv_result = MathTex(
            f"{1-NPV:.2f}"
        ).align_to(npv_formula,LEFT)
        
        self.add(p_text)
        self.play(Write(pdt),Write(ppv_formula),Write(ndt),Write(npv_formula))
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_calc),Transform(npv_formula,npv_calc),run_time=1)
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_result),Transform(npv_formula,npv_result),run_time=1)
        self.wait(5)

        
class IconArrayLow(Scene):
    def construct(self):
        p = low_p  # prevelence
        s = low_s  # sensitivity
        t = low_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        
        title = Text("Icon Array")
        title.to_edge(UP)
        self.add(title)

        N = 100
        
        init_array = icon_array(p*N,N)
        p_array = icon_array(PPV*N,N,X = np.linspace(-5,-2,10))
        n_array = icon_array((1-NPV)*N,N, X = np.linspace(2,5,10))
        
        t1 = Text("Before test", font_size=36).next_to(init_array,DOWN)
        t1 = Text("Before test", font_size=36).next_to(init_array,DOWN)
        t2 = Text("After positive test", font_size=36).next_to(p_array,DOWN)
        t2 = Text("After positive test", font_size=36).next_to(p_array,DOWN)
        t3 = Text("After negative test", font_size=36).next_to(n_array,DOWN)
        t3 = Text("After negative test", font_size=36).next_to(n_array,DOWN)
        
        self.play(LaggedStart(*[DrawBorderThenFill(i) for i in init_array],lag_ratio=0.01,run_time = 2),Write(t1))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Transform(init_array,p_array),
                    Transform(t1,t2),
                    run_time=4),
                LaggedStart(*[DrawBorderThenFill(i) for i in n_array],lag_ratio=0.01,run_time = 3),
                Write(t3),
                lag_ratio=0.5
                )
        )
        self.wait(5)

             
class NLineLow(Scene):
    def construct(self):
        p = low_p  # prevelence
        s = low_s  # sensitivity
        t = low_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        title = Text("Number Line")
        title.to_edge(UP)
        self.add(title)
        # Create a number line
        number_line = NumberLine(
            x_range=[0, 1], 
            length=10,
            include_numbers=True,
            numbers_to_include = np.arange(0,1.1,.1),
            decimal_number_config={'num_decimal_places':2}
            ).move_to([0,0,0])
        
        # markers = VGroup(
        #     Line(UP, DOWN, color=BLUE).scale(0.2).move_to(number_line.n2p(0.1)),
        #     Line(UP, DOWN, color=BLUE).scale(0.2).move_to(number_line.n2p(0.5))
        # )
        
        # Create a ball
        ballp = Dot(color=GREEN).shift(number_line.n2p(p))
        balln = Dot(color=PURE_RED).shift(number_line.n2p(p))
        ball = Dot(color=GRAY).shift(number_line.n2p(p))

        # Animate the ball moving on the number line
        self.play(GrowFromCenter(number_line))
        self.play(FadeIn(ball))
        self.add(ballp,balln)
        
        pos_test = Text('If positive test',color=GREEN).next_to(number_line,DOWN)
        neg_test = Text('If negative test',color=PURE_RED).move_to(pos_test)
        self.wait(2)
        self.play(
            ballp.animate.move_to(number_line.n2p(PPV)),
            Write(pos_test),
            run_time=2
        ) ;  self.wait(2)
        
        self.play(
            Transform(pos_test,neg_test),
            balln.animate.move_to(number_line.n2p(1-NPV)),
            run_time=2
        )
        self.wait(5)

# Define custom constants
class BayesRuleHigh(Scene):
    def construct(self):
        p = high_p  # prevelence
        s = high_s  # sensitivity
        t = high_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        MathTex.set_default(font_size=36)
        # Title
        title = Text("Traditional Bayesian Method")
        title.to_edge(UP)
        self.add(title)

        p_text = MathTex(f"p = {p}, s = {s}, t = {t}").move_to([0,1.5,0])
        

        # Bayes' Rule Formula
        pdt = MathTex("P(D|T+) = ").move_to([1,0,0],aligned_edge=LEFT)
        ndt = MathTex("P(D|T-) = ").move_to([-6,0,0],aligned_edge=LEFT)
    
        ppv_formula = MathTex(
            "\\frac{ps}{ps + (1-p)(1-t)}"
        ).next_to(pdt,RIGHT)
        npv_formula = MathTex(
            "1-\\frac{(1-p)t}{(1-p)t + p(1-s)}"
        ).next_to(ndt,RIGHT)

        # Calculation
        ppv_calc = MathTex(
            f"\\frac{{ {p:.2f}\\times{s:.2f} }}{{{p:.2f}\\times{s:.2f} + {1-p:.2f}\\times{1-t:.2f}}}"
        ).align_to(ppv_formula,LEFT)
        npv_calc = MathTex(
            f"1-\\frac{{ {1-p:.2f}\\times{t:.2f} }}{{{1-p:.2f}\\times{t:.2f} + {p:.2f}\\times{1-s:.2f}}}"
        ).align_to(npv_formula,LEFT)
        
        ppv_result = MathTex(
            f"{PPV:.2f}"
        ).align_to(ppv_formula,LEFT)
        
        npv_result = MathTex(
            f"{1-NPV:.2f}"
        ).align_to(npv_formula,LEFT)
        
        self.add(p_text)
        self.play(Write(pdt),Write(ppv_formula),Write(ndt),Write(npv_formula))
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_calc),Transform(npv_formula,npv_calc),run_time=2)
        self.wait(2)
        self.play(Transform(ppv_formula,ppv_result),Transform(npv_formula,npv_result),run_time=2)
        self.wait(5)

        
class IconArrayHigh(Scene):
    def construct(self):
        p = high_p  # prevelence
        s = high_s  # sensitivity
        t = high_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        
        title = Text("Icon Array")
        title.to_edge(UP)
        self.add(title)

        N = 100
        
        init_array = icon_array(p*N,N)
        p_array = icon_array(PPV*N,N,X = np.linspace(-5,-2,10))
        n_array = icon_array((1-NPV)*N,N, X = np.linspace(2,5,10))
        
        t1 = Text("Before test", font_size=36).next_to(init_array,DOWN)
        t2 = Text("After positive test", font_size=36).next_to(p_array,DOWN)
        t3 = Text("After negative test", font_size=36).next_to(n_array,DOWN)
        
        self.play(LaggedStart(*[DrawBorderThenFill(i) for i in init_array],lag_ratio=0.01,run_time = 2),Write(t1))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Transform(init_array,p_array),
                    Transform(t1,t2),
                    run_time=4),
                LaggedStart(*[DrawBorderThenFill(i) for i in n_array],lag_ratio=0.01,run_time = 3),
                Write(t3),
                lag_ratio=0.5
                )
        )
        self.wait(5)

             
class NLineHigh(Scene):
    def construct(self):
        p = high_p  # prevelence
        s = high_s  # sensitivity
        t = high_t  # specificity
        PPV = ppv(p,s,t)
        NPV = npv(p,s,t)

        title = Text("Number Line")
        title.to_edge(UP)
        self.add(title)
        # Create a number line
        number_line = NumberLine(
            x_range=[0, 1], 
            length=10,
            include_numbers=True,
            numbers_to_include = np.arange(0,1.1,.1),
            decimal_number_config={'num_decimal_places':2}
            ).move_to([0,0,0])
        
        # markers = VGroup(
        #     Line(UP, DOWN, color=BLUE).scale(0.2).move_to(number_line.n2p(0.1)),
        #     Line(UP, DOWN, color=BLUE).scale(0.2).move_to(number_line.n2p(0.5))
        # )
        
        # Create a ball
        ballp = Dot(color=GREEN).shift(number_line.n2p(p))
        balln = Dot(color=PURE_RED).shift(number_line.n2p(p))
        ball = Dot(color=GRAY).shift(number_line.n2p(p))

        # Animate the ball moving on the number line
        self.play(GrowFromCenter(number_line))
        self.play(FadeIn(ball))
        self.add(ballp,balln)
        
        pos_test = Text('If positive test',color=GREEN).next_to(number_line,DOWN)
        neg_test = Text('If negative test',color=PURE_RED).move_to(pos_test)
        self.wait(2)
        self.play(
            ballp.animate.move_to(number_line.n2p(PPV)),
            Write(pos_test),
            run_time=2
        ) ;  self.wait(2)
        
        self.play(
            Transform(pos_test,neg_test),
            balln.animate.move_to(number_line.n2p(1-NPV)),
            run_time=2
        )
        self.wait(5)


