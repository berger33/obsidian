---
id: software.testes.tranche12.000634
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md", "https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: restringir execução a pastas da collection

## Em uma frase
A opção `--folder` seleciona requests dentro de uma ou mais pastas ou requests nomeadas da collection.

## Por que importa
Uma seleção pequena dá feedback rápido sobre uma parte do fluxo, desde que a equipe reconheça que ela não representa execução integral da collection.

## Como funciona
Passe cada pasta necessária explicitamente, mantenha dependências compartilhadas visíveis e use a collection completa como verificação final do job principal.

## Exemplo
Uma pipeline pode rodar primeiro a pasta `smoke` e depois executar toda a collection antes de liberar uma versão.

## Limites e trade-offs
Uma pasta selecionada pode depender de variáveis definidas em scripts de outra pasta que não será executada, causando falha diferente da execução completa.

## Como verificar
Compare os requests selecionados com o relatório de descoberta e verifique as variáveis e fixtures que o fluxo parcial espera.

## Conexões
- [[newman-iteration-data-csv-json]] — Veja também: Newman: controlar iterações com arquivo de dados.
- [[newman-bail-exit-status]] — Veja também: Newman: decidir entre interromper cedo e preservar diagnóstico.

## Fontes
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
- [Newman — API Reference](https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference) — newman.run, eventos e callback de conclusão; consultado em 2026-10-02.
