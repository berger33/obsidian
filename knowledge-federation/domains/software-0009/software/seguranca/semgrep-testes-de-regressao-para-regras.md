---
id: software.seguranca.tranche18.001710
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

# Semgrep: Testes de regressão para regras

## Em uma frase
**Semgrep — Testes de regressão para regras:** Fixtures de entrada e resultados esperados tornam regras customizadas revisáveis antes de usá-las como gate.

## Por que importa
O recorte de **testes de regressão para regras** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **testes de regressão para regras**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Inclua arquivos marcados como positivos e negativos no diretório de teste da regra e rode-os em CI. Teste em staging autorizado.

## Limites e trade-offs
Um conjunto de fixtures pequeno não demonstra cobertura de todas as variações do parser. Exceções exigem responsável e prazo.

## Como verificar
Falhe a pipeline se a regra não produzir exatamente os casos esperados e revise diffs do resultado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sonarqube-fluxo-entre-scanner-e-servidor]] — Complementa o tópico com sonarqube server: fluxo entre scanner e servidor.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
