from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/categorias")
def categorias():
    return render_template("paginas/categorias.html", \
        titulo_pagina="Categorias")

@app.route("/produto")
def produto():
    return render_template("paginas/produto.html", \
        titulo_pagina="Produtos")
    
@app.route("/carrinho")
def carrinho():
    return render_template("paginas/carrinho.html", \
        titulo_pagina="Carrinho")

@app.route("/pagamento")
def pagamento():
    return render_template("paginas/pagamento.html", \
        titulo_pagina="Pagamento")
    
if __name__ == "__main__":
    app.run(debug=True)

#https://us.shop.realmadrid.com/