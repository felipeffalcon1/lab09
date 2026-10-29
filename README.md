Relatório - Lab9
RA: 221250731

Ex1)

a) Na suíte inicial, a cobertura de ramos cobria os caminhos principais de execução. O mutmut gerou 36 mutantes no total, resultando em 30 mortos e 6 vivos.

b) Os mutantes vivos estão relacionados às checagens das mensagens e limites de exceção. Mutantes que alteram partes internas de validação continuam vivos quando a suíte de testes valida apenas a chamada genérica do erro sem checar a mensagem exata com expressão regular completa.

c) Não existem mutantes equivalentes no código. Ao ajustar os testes de exceção para utilizar pytest.raises(ValueError, match="^...$") e cobrir todas as bordas exatas de nota e presença, os mutantes remanescentes são mortos.

d) O uso de pytest.raises(ValueError, match=msg) garante que a suíte valide a mensagem exata retornada pela exceção. Caso o mutante modifique o texto da mensagem lançada pela função, a asserção do match falha e o mutante é morto.

Ex2)

a) A cobertura de ramos de 100% combinada com a suíte inicial gerou 16 mutantes no total. Ter 100% de cobertura de ramos não garante a eliminação de todos os mutantes se as asserções forem genéricas.

b) Alterar o teste para verificar o valor exato do cálculo (== 141.0) elimina os mutantes que tentam alterar os fatores de desconto ou acumuladores de preço.

c) Pelo modelo RIPR, a verificação com asserção exata força que a infecção provocada pelo mutante no cálculo interno se propague até o retorno e seja revelada na validação final do teste.

d) Para atingir 100% de MS, foi necessário incluir cenários de teste na fronteira exata de aplicação de desconto (3 itens sem desconto e 4 itens com desconto), além de testar listas vazias e valores decimais.

Ex3)

a) Na função maior, os mutantes que alteram o operador de comparação > para >= são equivalentes, pois reatribuir o mesmo valor de temperatura máxima à variável m em caso de igualdade não altera o resultado final retornado.

b) Na função dia_do_maior, alterar > por >= não é equivalente, pois altera o índice retornado quando ocorrem empates (retornando a última ocorrência em vez da primeira).

c) Descontando os mutantes equivalentes presentes na função maior e adicionando o teste de desempate na função dia_do_maior, todos os mutantes não equivalentes são mortos e o escore chega a 100%.

d) A troca de operador é equivalente em maior porque a variável guarda o valor da temperatura, que permanece idêntico. Em dia_do_maior, a troca altera o índice do dia retornado para a última ocorrência do maior valor, violando a especificação de retornar o primeiro dia.

Ex4)

a) A técnica de valor-limite cobriu os pontos de transição das parcelas (n = 1, 3, 4, 12). A suíte alcançou 100% de cobertura de ramos e gerou 27 mutantes no total, matando 26 deles.

b) A cobertura de ramos foi de 100% e o escore de mutação inicial com valor-limite matou quase a totalidade dos mutantes de primeira ordem.

c) O mutante vivo restante ocorre em uma variação de constante que exige valores de teste com especificadores decimais exatos para causar divergência no arredondamento final (round).

d) Combinando os mutantes simples de alteração de limite (n <= 3 para n < 3) e da fórmula de juros (n - 3 para n - 4), obtém-se o seguinte mutante de segunda ordem:

if n < 3:
    juros = 0
else:
    juros = 0.02 * (n - 4)

e) Para a entrada n = 3, o programa original define juros = 0. No mutante de segunda ordem, a execução cai no bloco else e calcula juros = 0.02 * (3 - 4) = -0.02, alterando o valor final da parcela. A suíte mata esse mutante. Isso confirma a hipótese do efeito de acoplamento (Offutt, 1992), segundo a qual testes capazes de detectar mutantes simples de primeira ordem também tendem a detectar mutantes mais complexos de ordem superior.