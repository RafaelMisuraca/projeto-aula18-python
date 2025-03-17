import sqlite3

def inserirProduto(nome, descricao, estoque, preco):
    cursor.execute("""
    INSERT INTO produtos(nome, descricao, estoque, preco)
    VALUES (?,?,?,?)
    """, (nome, descricao, estoque, preco))
    conexao.commit()

def removerProduto(id):
    cursor.execute("""
    DELETE FROM produtos
    WHERE id = ?
    """, (id,))
    conexao.commit()
    print("Produto deletado")

def atualizarProduto(id, nome=None, descricao=None, estoque=None, preco=None):
    campos = []
    valores = []

    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if descricao:
        campos.append("descricao = ?")
        valores.append(descricao)
    if estoque is not None:
        campos.append("estoque = ?")
        valores.append(estoque)
    if preco is not None:
        campos.append("preco = ?")
        valores.append(preco)

    if campos:
        valores.append(id)
        query = f"UPDATE produtos SET {', '.join(campos)} WHERE id = ?"
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Produto com ID {id} atualizado com sucesso!")
    else:
        print("Nenhum dado para atualizar.")

def ler_Produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Produto Não encontrado")

def inserirUsuario(nome, telefone, email):
    cursor.execute("""
    INSERT INTO clientes(nome, telefone, email)
    VALUES (?,?,?)
    """, (nome, telefone, email))
    conexao.commit()

def removerUsuario(id):
    cursor.execute("""
    DELETE FROM clientes
    WHERE id = ?
    """, (id,))
    conexao.commit()
    print("Cliente deletado")

def atualizarUsuario(id, nome=None, telefone=None, email=None):
    campos = []
    valores = []

    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if telefone:
        campos.append("telefone = ?")
        valores.append(telefone)
    if email:
        campos.append("email = ?")
        valores.append(email)

    if campos:
        valores.append(id)
        query = f"UPDATE clientes SET {', '.join(campos)} WHERE id = ?"
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Cliente com ID {id} atualizado com sucesso!")
    else:
        print("Nenhum dado para atualizar.")

def ler_Usuarios():
    cursor.execute("SELECT * FROM clientes")
    usuarios = cursor.fetchall()
    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print("Usuário Não encontrado")

def inserirVenda(id_cliente, id_produto, quantidade, data_venda):
    cursor.execute("""
    INSERT INTO vendas(id_cliente, id_produto, quantidade, data_venda)
    VALUES (?, ?, ?, ?)
    """, (id_cliente, id_produto, quantidade, data_venda))
    conexao.commit()
    print("Venda registrada com sucesso!")

def removerVendas(id):
    cursor.execute("""
    DELETE FROM vendas
    WHERE id = ?
    """, (id,))
    conexao.commit()
    print("Venda deletada")

def atualizarVenda(id, id_cliente=None, id_produto=None, quantidade=None, data_venda=None):
    campos = []
    valores = []

    if id_cliente:
        campos.append("id_cliente = ?")
        valores.append(id_cliente)
    if id_produto:
        campos.append("id_produto = ?")
        valores.append(id_produto)
    if quantidade is not None:
        campos.append("quantidade = ?")
        valores.append(quantidade)
    if data_venda:
        campos.append("data_venda = ?")
        valores.append(data_venda)

    if campos:
        valores.append(id)
        query = f"UPDATE vendas SET {', '.join(campos)} WHERE id = ?"
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Venda com ID {id} atualizada com sucesso!")
    else:
        print("Nenhum dado para atualizar.")

def ler_Vendas():
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()
    if vendas:
        for venda in vendas:
            print(venda)
    else:
        print("Venda Não encontrada")


try:
    conexao = sqlite3.connect("loja.db")
    cursor = conexao.cursor()

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   descricao TEXT NOT NULL,
                   estoque INTEGER DEFAULT 0,
                   preco REAL NOT NULL 
                   )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   telefone INTEGER NOT NULL,
                   email TEXT NOT NULL
                   )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   id_cliente INTEGER,
                   id_produto INTEGER,
                   quantidade INTEGER NOT NULL,
                   data_venda DATE DEFAULT (CURRENT_DATE),
                   FOREIGN KEY (id_produto) REFERENCES produtos(id),
                   FOREIGN KEY (id_cliente) REFERENCES clientes(id)
                   )
    """)

    conexao.commit()
    conexao.close()

except sqlite3.Error as e:
    print(e)
