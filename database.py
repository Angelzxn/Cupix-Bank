from config import get_connection
import psycopg2
import uuid

def criar_tabelas():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        print(f"Conexão bem sucedida      DATABASE: {conn}")
    


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario(
                id TEXT NOT NULL,
                tipo TEXT NOT NULL,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                email TEXT NOT NULL,
                cpf TEXT NOT NULL,
                saldo DECIMAL NOT NULL,
                data_nasc DATE NOT NULL,
                endereco TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movimentacoes(
                id TEXT NOT NULL,
                data DATE NOT NULL,
                hora TEXT NOT NULL,
                tipo TEXT NOT NULL,
                remetente_id TEXT NOT NULL,
                destinatario_id TEXT NOT NULL
                
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas(
                id TEXT NOT NULL,
                devedor_id TEXT NOT NULL,
                destinatario_id TEXT NOT NULL,
                juros_mes DECIMAL NOT NULL,
                vencimento DATE NOT NULL,
                status TEXT NOT NULL
            )
        """)
        print("Tabelas criadas")

        conn.commit()
        conn.close()
        cursor.close()

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    criar_tabelas()
