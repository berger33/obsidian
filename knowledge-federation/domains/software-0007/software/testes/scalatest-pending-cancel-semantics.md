---
id: software.testes.tranche13.000711
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://www.scalatest.org/user_guide", "https://www.scalatest.org/user_guide/running_your_tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ScalaTest: distinguir pending de cancelamento

## Em uma frase
Pending indica teste conhecido que ainda não foi implementado, enquanto cancel interrompe execução por condição que impede avaliação naquele contexto.

## Por que importa
Relatórios que separam estados mostram dívida de cobertura sem confundir indisponibilidade ambiental com comportamento deliberado ainda não especificado.

## Como funciona
Use sintaxe pending para lacuna explícita e cancel com motivo quando pressuposto do caso não se cumpre; acompanhe contagem em vez de tratar qualquer estado como aprovado.

## Exemplo
Um exemplo ainda sem decisão de negócio pode ficar pending; teste dependente de recurso opcional pode cancelar com mensagem se o ambiente não oferece requisito.

## Limites e trade-offs
Cancelamento não substitui assertion de que ambiente obrigatório está saudável; use política da pipeline para falhar quando precondição mandatória estiver ausente.

## Como verificar
Inspecione resumo de runner e confirme que pending, canceled e failed aparecem como resultados distintos para relatório.

## Conexões
- [[scalatest-style-selection]] — Veja também: ScalaTest: selecionar style trait pelo formato da equipe.
- [[scalatest-assertion-clue]] — Veja também: ScalaTest: acrescentar contexto à falha de assertion.

## Fontes
- [ScalaTest — User Guide](https://www.scalatest.org/user_guide) — suite model and guide navigation; consultado em 2026-10-02.
- [ScalaTest — Running Tests](https://www.scalatest.org/user_guide/running_your_tests) — runner integrations and execution options; consultado em 2026-10-02.
