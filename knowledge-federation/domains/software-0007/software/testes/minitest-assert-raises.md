---
id: software.testes.tranche15.000882
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.seattlerb.org/minitest/Minitest/Assertions.html", "https://docs.seattlerb.org/minitest/Minitest/Mock.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minitest: inspecionar a exceção capturada

## Em uma frase
`assert_raises` falha se o bloco não levantar uma das exceções esperadas e devolve a exceção capturada para verificação de mensagem e atributos.

## Por que importa
Duplicar validações frágeis de mensagem ou ignorar o retorno da asserção deixa de distinguir o erro previsto de outra falha qualquer lançada no bloco.

## Como funciona
Guarde o retorno da asserção, verifique a classe desejada e confirme a mensagem relevante com igualdade ou expressão regular, sem depender do texto completo quando ele for instável.

## Exemplo
`erro = assert_raises(ArgumentError) { validar(nil) }; assert_match(/vazio/, erro.message)` prova tipo e conteúdo do erro esperado.

## Limites e trade-offs
A asserção aceita lista de classes e um bloco sem exceção falha com mensagem própria, mas ela não cobre exceções assíncronas nem efeitos colaterais ocorridos antes do levantamento.

## Como verificar
Faça o bloco levantar uma subclasse inesperada e confirme que a asserção falha, depois ajuste o teste para a exceção correta.

## Conexões
- [[minitest-core-assertions]] — Veja também: Minitest: escolher a asserção adequada ao valor.
- [[minitest-setup-teardown]] — Veja também: Minitest: preparar e limpar cada caso.

## Fontes
- [Minitest — Assertions](https://docs.seattlerb.org/minitest/Minitest/Assertions.html) — asserções de igualdade, exceções, saída, predicados e tipos; consultado em 2026-10-02.
- [Minitest — Mock](https://docs.seattlerb.org/minitest/Minitest/Mock.html) — mocks com expectativas, verificação de chamadas e stubs temporários; consultado em 2026-10-02.
