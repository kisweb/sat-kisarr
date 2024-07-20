
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return " ".join([c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(s)])


@app.route("/")
def home():
    # auj = datetime.utcnow().strftime("%d %B, %Y")
    # ibou = "Prof de Maths"
    return render_template('index.html')

#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