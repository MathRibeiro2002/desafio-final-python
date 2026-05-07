import datetime


estoque = []      
vendas = []       



def cadastrar_produto():
    """Cadastra um novo produto no estoque ou adiciona quantidade a um existente."""
    nome = input("Nome do produto: ").strip().capitalize()
    try:
        qtd = int(input("Quantidade inicial: "))
        if qtd < 0:
            print("Quantidade não pode ser negativa. Operação cancelada.")
            return
    except ValueError:
        print("Valor inválido. Use números inteiros.")
        return

    
    for prod in estoque:
        if prod["nome"] == nome:
            prod["quantidade"] += qtd
            print(f"Estoque de '{nome}' atualizado. Nova quantidade: {prod['quantidade']}")
            return

    
    estoque.append({"nome": nome, "quantidade": qtd})
    print(f"Produto '{nome}' cadastrado com {qtd} unidades.")


def registrar_venda():
    """Registra a venda de um produto, reduz o estoque e armazena a venda."""
    nome = input("Produto vendido: ").strip().capitalize()
    try:
        valor = float(input("Valor da venda (R$): "))
        if valor <= 0:
            print("Valor deve ser positivo.")
            return
    except ValueError:
        print("Valor inválido.")
        return

    
    for prod in estoque:
        if prod["nome"] == nome:
            if prod["quantidade"] == 0:
                print(f"Erro: Estoque de '{nome}' zerado. Faça um pedido urgente antes de vender.")
                return
            
            prod["quantidade"] -= 1
            
            vendas.append({"produto": nome, "valor": valor})
            print(f"Venda de '{nome}' registrada por R$ {valor:.2f}. Estoque restante: {prod['quantidade']}")

            
            if prod["quantidade"] < 5:
                if prod["quantidade"] == 0:
                    print(f"ALERTA: Estoque de '{nome}' zerado! Fazer pedido urgente.")
                else:
                    print(f"ALERTA: Estoque de '{nome}' está baixo ({prod['quantidade']} unidades).")
            return

    
    print(f"Produto '{nome}' não encontrado no estoque. Cadastre-o primeiro.")


def exibir_alertas_estoque():
    """Percorre o estoque mostrando produtos com menos de 5 unidades e os zerados."""
    print("\n=== ALERTAS DE ESTOQUE ===")
    alertas_baixo = [p for p in estoque if 0 < p["quantidade"] < 5]
    alertas_zero = [p for p in estoque if p["quantidade"] == 0]

    if not alertas_baixo and not alertas_zero:
        print("Nenhum alerta no momento.")
    else:
        for p in alertas_baixo:
            print(f" Estoque baixo: '{p['nome']}' tem apenas {p['quantidade']} unidades.")
        for p in alertas_zero:
            print(f" ESTOQUE ZERADO: '{p['nome']}' – FAZER PEDIDO URGENTE!")


def calcular_faturamento():
    """Retorna o faturamento total do dia com base na lista de vendas."""
    total = sum(venda["valor"] for venda in vendas)
    return total


def produto_mais_caro_barato():
    """Retorna uma tupla (nome_mais_caro, valor_mais_caro, nome_mais_barato, valor_mais_barato)."""
    if not vendas:
        return None, 0, None, 0
    mais_caro = max(vendas, key=lambda v: v["valor"])
    mais_barato = min(vendas, key=lambda v: v["valor"])
    return mais_caro["produto"], mais_caro["valor"], mais_barato["produto"], mais_barato["valor"]


def quantidade_vendas_acima_100():
    """Retorna o número de vendas com valor superior a R$100."""
    return sum(1 for v in vendas if v["valor"] > 100)


def relatorio_final():
    """Exibe no console o relatório completo com data, estoque final, faturamento, etc."""
    print("\n" + "=" * 50)
    print("RELATÓRIO FINAL DA LOJA")
    print("=" * 50)
    print(f"Data de geração: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

    
    print(">>> ESTOQUE FINAL <<<")
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        for prod in estoque:
            print(f"- {prod['nome']}: {prod['quantidade']} unidades")

    
    faturamento = calcular_faturamento()
    print(f"\n>>> FATURAMENTO TOTAL DO DIA: R$ {faturamento:.2f}")

    
    caro_nome, caro_val, barato_nome, barato_val = produto_mais_caro_barato()
    if vendas:
        print(f">>> PRODUTO MAIS CARO VENDIDO: {caro_nome} (R$ {caro_val:.2f})")
        print(f">>> PRODUTO MAIS BARATO VENDIDO: {barato_nome} (R$ {barato_val:.2f})")
    else:
        print(">>> Nenhuma venda registrada para calcular produtos mais caro/barato.")

   
    qtd_acima_100 = quantidade_vendas_acima_100()
    print(f">>> VENDAS ACIMA DE R$100: {qtd_acima_100}")

    
    exibir_alertas_estoque()
    print("=" * 50)



def main():
    print("=== SISTEMA DA LOJA ===\n")
    while True:
        print("\n----- MENU -----")
        print("1 - Cadastrar produto no estoque")
        print("2 - Registrar venda")
        print("3 - Ver alertas de estoque")
        print("4 - Gerar relatório final")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando o sistema. Volte sempre!")
            break
        elif opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            registrar_venda()
        elif opcao == "3":
            exibir_alertas_estoque()
        elif opcao == "4":
            relatorio_final()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()