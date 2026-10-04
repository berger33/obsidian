---
id: software.testes.tranche18.001233
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://semgrep.dev/docs/", "https://github.com/semgrep/semgrep"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: integrar a análise ao pipeline

## Em uma frase
A execução pode analisar o repositório inteiro ou apenas as mudanças, gerar saída estruturada e falhar o trabalho pela presença de achados.

## Por que importa
O recorte por mudanças dá retorno rápido na revisão, enquanto a análise completa cobre o passivo em execuções periódicas.

## Como funciona
Analise as mudanças em cada revisão, rode a análise completa periodicamente e publique a saída estruturada como artefato.

## Exemplo
Um trabalho de revisão pode falhar apenas por achados novos introduzidos pela mudança em avaliação.

## Limites e trade-offs
Bloquear por achados antigos impede qualquer avanço, e nunca bloquear permite que novos problemas se acumulem sem barreira.

## Como verificar
Introduza um trecho que viole a regra e confirme que o trabalho falha indicando o arquivo e a linha correspondentes.

## Conexões
- [[semgrep-rule-defined-fix]] — Veja também: Semgrep: sugerir correção automática.
- [[semgrep-suppressions]] — Veja também: Semgrep: registrar exceções de forma auditável.

## Fontes
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
- [Semgrep — repositório oficial](https://github.com/semgrep/semgrep) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
