import re

with open("index.html", "r") as f:
    html = f.read()

# Add MathJax
mathjax_script = """
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""
if "MathJax" not in html:
    html = html.replace('</head>', mathjax_script + '\n</head>')

# Replace images
html = html.replace('figures/openloop-vout-il.png', 'figures/Average_Model_Vout_and_IL.png')
html = html.replace('figures/openloop-vin-iin.png', 'figures/Average_Model_Vin_Iin.png')
html = html.replace('figures/plant-bode.png', 'figures/Small_Signal_Bode.png')
html = html.replace('figures/openloop-margins.png', 'figures/Part2_OpenLoop_Margins.png')
html = html.replace('figures/closedloop-bode.png', 'figures/Part2_ClosedLoop_Bode.png')
html = html.replace('figures/thd-pf-model.png', 'figures/Simulink_Measurement_Block_.png')
html = html.replace('figures/mil-waveform.png', 'figures/MIL_WaveForms.png')
html = html.replace('figures/mil-thd-view.png', 'figures/MIL_THD.png')
html = html.replace('figures/sil-waveform.png', 'figures/SIL.png')

# PI section
html = html.replace(
    '<img src="figures/closedloop-vout.png" alt="Closed-loop Vout response" loading="lazy" />',
    '<img src="figures/After_PI_Controller.png" alt="After PI Controller" loading="lazy" />'
)
html = html.replace('Closed-loop output voltage — V<sub>out</sub> settles near 400 V', 'After PI Controller Waveforms')

html = re.sub(r'<div class="fig-wrap">\s*<img src="figures/closedloop-vin-iin.png".*?</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<div class="fig-wrap">\s*<img src="figures/inductor-current.png".*?</div>', '', html, flags=re.DOTALL)

# Topology figure
topology_html = """
      <div class="fig-block">
        <div class="fig-wrap">
          <img src="figures/Converter_Topology.png" alt="Converter Topology" loading="lazy" />
          <div class="fig-caption">Converter block diagram and control structure</div>
        </div>
      </div>
"""
html = re.sub(r'<div class="callout callout-info">\s*<strong>Note on topology figure.*?</div>', topology_html, html, flags=re.DOTALL)

# LaTeX replacements
replacements = {
    "V<sub>in</sub> (RMS)": r"\(V_{\text{in (RMS)}}\)",
    "240 V<sub>rms</sub>": r"\(240 \text{ V}_{\text{rms}}\)",
    "f<sub>line</sub>": r"\(f_{\text{line}}\)",
    "V<sub>o</sub>": r"\(V_o\)",
    "P<sub>o</sub>": r"\(P_o\)",
    "f<sub>s</sub>": r"\(f_s\)",
    "ΔV<sub>o</sub>/V<sub>o</sub>": r"\(\frac{\Delta V_o}{V_o}\)",
    "V̂<sub>p</sub> (carrier)": r"\(\hat{V}_p \text{ (carrier)}\)",
    "v<sub>rect</sub>(t) = V<sub>in,pk</sub>·|sin(ωt)|": r"\(v_{\text{rect}}(t) = V_{\text{in,pk}}|\sin(\omega t)|\)",
    "R = V<sub>o</sub>²/P<sub>o</sub>": r"\(R = \frac{V_o^2}{P_o}\)",
    "i<sub>ref</sub> = (v<sub>ea</sub> · v<sub>rect</sub>) / V<sub>rms</sub>²": r"\(i_{\text{ref}} = \frac{v_{\text{ea}} \cdot v_{\text{rect}}}{V_{\text{rms}}^2}\)",
    "V<sub>in,pk</sub>": r"\(V_{\text{in,pk}}\)",
    "I<sub>in</sub> = 500/240 = <strong>2.083 A<sub>rms</sub></strong>": r"\(I_{\text{in}} = \frac{500}{240} = \mathbf{2.083 \text{ A}_{\text{rms}}}\)",
    "I<sub>in,pk</sub>": r"\(I_{\text{in,pk}}\)",
    "I<sub>o</sub> = <strong>1.25 A</strong>": r"\(I_o = \mathbf{1.25 \text{ A}}\)",
    "R = <strong>320 Ω</strong>": r"\(R = \mathbf{320 \ \Omega}\)",
    "d = 1 − V<sub>in,pk</sub>·|sin|/V<sub>o</sub>": r"\(d = 1 - \frac{V_{\text{in,pk}}|\sin|}{V_o}\)",
    "d<sub>min</sub>": r"\(d_{\text{min}}\)",
    "ΔiL,pk": r"\(\Delta i_{L,\text{pk}}\)",
    "I<sub>in,pk</sub>": r"\(I_{\text{in,pk}}\)",
    "C<sub>o</sub>": r"\(C_o\)",
    "ΔV<sub>o,pp</sub>": r"\(\Delta V_{o,\text{pp}}\)",
    "I<sub>S,pk</sub>": r"\(I_{S,\text{pk}}\)",
    "⟨v<sub>o</sub>⟩ = ⟨v<sub>rect</sub>⟩/(1−d)": r"\(\langle v_o \rangle = \frac{\langle v_{\text{rect}} \rangle}{1-d}\)",
    "⟨iL⟩ = I<sub>in,pk</sub>·|sin(ωt)|": r"\(\langle i_L \rangle = I_{\text{in,pk}}|\sin(\omega t)|\)",
    "G<sub>id</sub>(s)": r"\(G_{id}(s)\)",
    "V<sub>o</sub>(1 + sRC<sub>o</sub>) / (s²LC<sub>o</sub>R + sL + R)": r"\(\frac{V_o(1 + sRC_o)}{s^2 L C_o R + sL + R}\)",
    "G<sub>vi</sub>(s)": r"\(G_{vi}(s)\)",
    "R/(1 + sRC<sub>o</sub>)": r"\(\frac{R}{1 + sRC_o}\)",
    "K<sub>p</sub>": r"\(K_p\)",
    "K<sub>i</sub>": r"\(K_i\)",
    "T<sub>s</sub>": r"\(T_s\)",
    "K<sub>i,i,d</sub>": r"\(K_{i,i,d}\)",
    "K<sub>i,v,d</sub>": r"\(K_{i,v,d}\)"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open("index.html", "w") as f:
    f.write(html)

print("Updated index.html")
