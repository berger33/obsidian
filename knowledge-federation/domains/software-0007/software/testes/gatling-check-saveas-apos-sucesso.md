---
id: software.testes.tranche11.000533
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.gatling.io/concepts/checks/", "https://docs.gatling.io/concepts/session/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: validar resposta antes de guardar valor com saveAs

## Em uma frase
Checks validam request/response e podem extrair um valor para Session; saveAs só é efetivo quando check passa.

## Por que importa
Usar valor de resposta não validada pode encadear id vazio ou incorreto em requests seguintes e produzir erro secundário.

## Como funciona
Verifique status/estrutura e extraia somente campo que o próximo passo precisa, tratando check opcional explicitamente.

## Exemplo
Login valida status e existência de token antes de salvar accessToken para request autenticada.

## Limites e trade-offs
Check optional que não encontra valor não sobrescreve nem remove atributo existente; estado anterior pode permanecer.

## Como verificar
Faça teste de resposta válida e sem campo, confira falha/optional e verifique que token antigo não é reutilizado sem intenção.

## Conexões
- [[gatling-feeder-dados-variados-cache]] — Veja também: Gatling: alimentar usuários com registros distintos para workload.
- [[gatling-assertions-criterios-de-simulacao]] — Veja também: Gatling: expressar pass fail com assertions de estatísticas.

## Fontes
- [Gatling — Checks](https://docs.gatling.io/concepts/checks/) — validação de resposta e extração saveAs condicionada ao sucesso; consultado em 2026-10-02.
- [Gatling — Session API](https://docs.gatling.io/concepts/session/api/) — estado de cada virtual user e propagação de atributos; consultado em 2026-10-02.
