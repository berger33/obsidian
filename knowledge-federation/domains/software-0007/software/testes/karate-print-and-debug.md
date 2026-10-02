---
id: software.testes.tranche15.000918
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
fontes: ["https://karatelabs.github.io/karate/", "https://karatelabs.github.io/karate/#parallel-execution"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: registrar evidências do passo

## Em uma frase
O comando `print` exibe valores no relatório e a resposta completa pode ser inspecionada para diagnóstico quando a asserção falha.

## Por que importa
Sem evidência dos valores comparados, investigar falha em ambiente remoto exige reproduzir o cenário localmente e adivinhar o conteúdo da resposta.

## Como funciona
Imprima apenas os valores que identificam o problema, evitando despejar dados sensíveis, e mantenha a asserção como fonte do resultado do teste.

## Exemplo
`* print 'pedido', pedidoId, 'status', responseStatus` registra a correlação sem transformar o log em fonte de verdade.

## Limites e trade-offs
Impressão em excesso polui o relatório e pode expor dados pessoais; um print não substitui a asserção e não deve ser a única verificação de um cenário.

## Como verificar
Revise a saída gerada em caso de falha e confirme que ela contém o valor comparado sem incluir tokens ou dados além do necessário.

## Conexões
- [[karate-mock-server]] — Veja também: Karate: simular serviços com o servidor mock.
- [[karate-reports-artifacts]] — Veja também: Karate: consumir o relatório da execução.

## Fontes
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
- [Karate — Parallel execution](https://karatelabs.github.io/karate/#parallel-execution) — execução paralela de features e geração de relatórios agregados; consultado em 2026-10-02.
