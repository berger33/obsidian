---
id: software.seguranca.tranche18.001704
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://semgrep.dev/docs/running-rules", "https://semgrep.dev/docs/semgrep-ci/overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Semgrep: Análise de taint com fontes e sinks

## Em uma frase
**Semgrep — Análise de taint com fontes e sinks:** Regras de taint relacionam dados não confiáveis a operações sensíveis, em vez de buscar apenas texto idêntico.

## Por que importa
O recorte de **análise de taint com fontes e sinks** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **análise de taint com fontes e sinks**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em uma aplicação de demonstração, marque parâmetro HTTP como fonte e chamada SQL sem parametrização como sink. Teste em staging autorizado.

## Limites e trade-offs
O modelo de fonte e sink precisa corresponder à biblioteca e ao fluxo reais do projeto. Exceções exigem responsável e prazo.

## Como verificar
Teste um fluxo vulnerável e outro parametrizado e confirme que o finding aparece somente no primeiro. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-sanitizadores-em-regras-de-taint]] — Complementa o tópico com semgrep: sanitizadores em regras de taint.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
