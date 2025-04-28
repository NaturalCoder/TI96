try:
    # Código
except ZeroDivisionError:
    # Tratamento
except ValueError:
    # Tratamento
except Exception as e: #captura generica (pega todos os erros)
    print(f"Erro inesperado: {e}")
else:
    print("Programa concluío com sucesso!")
finally:
    # Garante o fechamento de arquivos e liberação de recursos
