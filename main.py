def calcular_area_cômodo(largura, comprimento):
    """Calcula a área de um cômodo dado suas dimensões."""
    return largura * comprimento

def calcular_area_azulejo(largura_azulejo, comprimento_azulejo):
    """Calcula a área de um azulejo dado suas dimensões."""
    return largura_azulejo * comprimento_azulejo

def calcular_quantidade_azulejos(area_cômodo, area_azulejo):
    """Calcula a quantidade de azulejos necessária com base na área do cômodo e na área de um azulejo."""
    return area_cômodo / area_azulejo

def main():
    print("Calculadora de Quantidade de Azulejos")

    # Solicita as dimensões do cômodo
    largura_cômodo = float(input("Digite a largura do cômodo (em metros): "))
    comprimento_cômodo = float(input("Digite o comprimento do cômodo (em metros): "))

    # Calcula a área do cômodo
    area_cômodo = calcular_area_cômodo(largura_cômodo, comprimento_cômodo)
    print(f"A área do cômodo é: {area_cômodo:.2f} m²")

    # Solicita as dimensões do azulejo
    largura_azulejo = float(input("Digite a largura do azulejo (em metros): "))
    comprimento_azulejo = float(input("Digite o comprimento do azulejo (em metros): "))

    # Calcula a área do azulejo
    area_azulejo = calcular_area_azulejo(largura_azulejo, comprimento_azulejo)
    print(f"A área de um azulejo é: {area_azulejo:.2f} m²")

    # Calcula a quantidade de azulejos
    quantidade_azulejos = calcular_quantidade_azulejos(area_cômodo, area_azulejo)
    print(f"A quantidade de azulejos necessária é: {quantidade_azulejos:.0f}")

if __name__ == "__main__":
    main()
