print('Desafio011: Faça um programa que leia a largura e a altura de uma parede em metros, '
      'calcule a sua area e quantidade de tinta necessaria para pinta-lá, sabendo que cada litro de tinta, pinta uma area de 2m²:')

largura = float(input('Digite a Largura: '))
altura = float(input('Digite a Altura: '))
area = largura * altura
print('A sua parede tem dimensão de {}m²'.format(area))
tinta = area / 2
print('Essa parede você precisará de {}L de tinta.' .format(tinta))