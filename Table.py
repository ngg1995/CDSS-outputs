from manim import *

# Set the background color and text color
config.background_color = WHITE
Text.set_default(font="Helvetica Neue", font_size=50, color=BLACK)
MathTex.set_default(color=BLACK)
Mobject.set_default(color=BLACK)
TexTemplate.default_preamble += "\n" + r"\newcommand{\interval}[1]{\left[\underline{#1},\overline{#1}\right]}"

class PreciseTable(Scene):
    def construct(self):
        
        title = Text("Precise Output")
        title.to_edge(UP)
        self.add(title)
        
        
        table = MathTable(
            [
                [
                    r"y \in \left\{ \top,\bot \right\}", 
                    r"y \in \left\{A,B,C,\cdots\right\}" 
                ],
                [
                    r"y \in [a,b]",
                    r"y = \begin{pmatrix}  y_1\in[a,b] \\  \vdots \\ y_n = [c,d]  \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        # Iterate through each cell and apply Write animation
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Write(table.get_vertical_lines()),
                    Write(table.get_horizontal_lines()),run_time=2
                ),
                AnimationGroup(
                    Write(table.get_col_labels()[0]),
                    Write(table.get_col_labels()[1]),
                    Write(table.get_row_labels()[0]),
                    Write(table.get_row_labels()[1]),
                    lag_ratio=0.75,
                    run_time=2
                ), lag_ratio=0.5
            )
        )
        for cell in table.get_entries_without_labels():
            self.play(Write(cell))

        self.wait()
        

class ProbTable(Scene):

    def construct(self):
        title = Text("Precise Output")
        title.to_edge(UP)
        self.add(title)

        table = MathTable(
            [
                [
                    r"y \in \left\{ \top,\bot \right\}", 
                    r"y \in \left\{A,B,C,\cdots\right\}" 
                ],
                [
                    r"y \in [a,b]",
                    r"y = \begin{pmatrix}  y_1\in[a,b] \\  \vdots \\ y_n = [c,d]  \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        
        updated_table = MathTable(
            [
                [
                    r"y = \Pr(y=\top)", 
                    r"y = \begin{Bmatrix}  \Pr(y=A)\\ \Pr(y=B)\\  \vdots\\ \end{Bmatrix}" 
                ],
                [
                    r"y = \Pr(y=Y\in[a,b])",
                    r"y = \begin{pmatrix}  \Pr(y_1=Y_1\in[a,b])\\  \vdots\\  \Pr(y_2=Y_2\in[a,b]) \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        
        self.add(updated_table.get_vertical_lines())
        self.add(updated_table.get_horizontal_lines())
        self.add(updated_table.get_col_labels())
        self.add(updated_table.get_row_labels())
        
        anims = []
        for old,new in zip(table.get_entries_without_labels(),updated_table.get_entries_without_labels()):
            old.move_to(new)
            self.add(old)
            anims += [Transform(old,new)]
            
        self.wait(1)
        self.play(Transform(title,Text("Probability Output").move_to(title)))
        for a in anims:
            self.play(a)
            self.wait(1)
        self.wait()


class ProbDistTable(Scene):
    def construct(self):
        title = Text("Probability Output")
        title.to_edge(UP)
        self.add(title)
        table = MathTable(
            [
                [
                    r"y = \Pr(y=\top)", 
                    r"y = \begin{Bmatrix}  \Pr(y=A)\\ \Pr(y=B)\\  \vdots\\ \end{Bmatrix}" 
                ],
                [
                    r"y = \Pr(y=Y\in[a,b])",
                    r"y = \begin{pmatrix}  \Pr(y_1=Y_1\in[a,b])\\  \vdots\\  \Pr(y_2=Y_2\in[a,b]) \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        
        updated_table = MathTable(
            [
                [
                    r"y = \Pr(y=\top) \sim f()", 
                    r"y = \begin{Bmatrix}  \Pr(y=A)\sim f_A()\\ \Pr(y=B)\sim f_B()\\  \vdots\\ \end{Bmatrix}" 
                ],
                [
                    r"y = \Pr(y=Y\in[a,b])\sim f()",
                    r"y = \begin{pmatrix}  \Pr(y_1=Y_1\in[a,b])\sim f_2()\\  \vdots\\  \Pr(y_2=Y_2\in[a,b])\sim f_2() \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        
        self.add(updated_table.get_vertical_lines())
        self.add(updated_table.get_horizontal_lines())
        self.add(updated_table.get_col_labels())
        self.add(updated_table.get_row_labels())
        
        anims = []
        for old,new in zip(table.get_entries_without_labels(),updated_table.get_entries_without_labels()):
            old.move_to(new)
            self.add(old)
            anims += [Transform(old,new)]
            
        self.wait(1)
        
        self.play(Transform(title,Text("Probability Distribution Output").move_to(title)),AnimationGroup(*[a for a in anims],lag_ratio = 0.33,length = 4))
        self.wait()

        
class IntTable(Scene):
    def construct(self):
        
        title = Text("Interval Output")
        title.to_edge(UP)
        self.add(title)
        
        table = MathTable(
            [
                [
                    r"y \in \left\{ \top,\bot \right\}", 
                    r"y \in \left\{A,B,C,\cdots\right\}" 
                ],
                [
                    r"y \in [a,b]",
                    r"y = \begin{bmatrix}  y_1\in[a,b] \\  \vdots \\ y_n = [c,d]  \end{bmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        
        updated_table = MathTable(
            [
                [
                    r"y \in \left\{\top,\bot,[\top,\bot] \right\}", 
                    r"y \subseteq \left\{A,B,C,\cdots\right\}" 

                ],
                [
                    r"y = \interval{y}  \in[a,b]",
                    r"y = \begin{pmatrix}  y_1 = \interval{y_1} \in[a,b]\\  \vdots\\  y_n = \interval{y_n} \in[c,d] \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        
        self.add(updated_table.get_vertical_lines())
        self.add(updated_table.get_horizontal_lines())
        self.add(updated_table.get_col_labels())
        self.add(updated_table.get_row_labels())
        
        anims = []
        for old,new in zip(table.get_entries_without_labels(),updated_table.get_entries_without_labels()):
            old.move_to(new)
            self.add(old)
            anims += [Transform(old,new)]
        self.wait(1)
        
        self.play(Transform(title,Text("Interval Output").move_to(title)))
    
        for a in anims:
            self.play(a)
            self.wait(1)
        self.wait()
        
        
class IPTable(Scene):
    def construct(self):
        
        title = Text("Interval Output")
        title.to_edge(UP)
        self.add(title)
        
        table = MathTable(
            [
                [
                    r"y \in \left\{\top,\bot,[\top,\bot] \right\}", 
                    r"y \subseteq \left\{A,B,C,\cdots\right\}" 

                ],
                [
                    r"y = \interval{y} \in[a,b]",
                    r"y = \begin{pmatrix}  y_1 = \interval{y_1} \in[a,b]\\  \vdots\\  y_n = \interval{y_n} \in[c,d] \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.7)
        
        updated_table = MathTable(
            [
                [
                    r"y = \Pr(y=\top) \sim \interval{f}()", 
                    r"y = \begin{Bmatrix}  \Pr(y=A)\sim \interval{f_A()}\\ \Pr(y=B)\sim \interval{f_B()}\\  \vdots\\ \end{Bmatrix}" 
                ],
                [
                    r"y = \Pr(y=Y\in[a,b])\sim f()",
                    r"y = \begin{pmatrix}  \Pr(y_1=Y_1\in[a,b])\sim \interval{f_2()}\\  \vdots\\  \Pr(y_2=Y_2\in[a,b])\sim \interval{f_2()} \end{pmatrix}"
                ]
            ],
            row_labels = [
                Tex("Discrete"),
                Tex("Continuous")
            ],
            col_labels = [
                Tex("Univariate"),
                Tex("Multivariate")
            ],
            include_outer_lines=True).scale(0.6)
        
        self.add(updated_table.get_vertical_lines())
        self.add(updated_table.get_horizontal_lines())
        self.add(updated_table.get_col_labels())
        self.add(updated_table.get_row_labels())
        
        anims = []
        for old,new in zip(table.get_entries_without_labels(),updated_table.get_entries_without_labels()):
            old.move_to(new)
            self.add(old)
            anims += [Transform(old,new)]
        self.wait(1)
        self.play(Transform(title,Text("Imprecise Probability Output").move_to(title)))
        for a in anims:
            self.play(a)
            self.wait(1)
        self.wait()
        
