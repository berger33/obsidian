---
id: software.seguranca.tranche18.001715
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
fontes: ["https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-overview", "https://docs.sonarsource.com/sonarqube-server/2026.2/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SonarQube Server: Definição de código novo

## Em uma frase
**SonarQube Server — Definição de código novo:** O período de referência de código novo separa regressões recentes do legado em relatórios e gates.

## Por que importa
O recorte de **definição de código novo** ajuda a padronizar análise estática e acompanhar a introdução de novos problemas em projetos e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **definição de código novo**, o scanner coleta arquivos dentro do escopo, aplica analisadores e envia um relatório que o servidor processa para issues e quality gates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Defina uma referência de baseline estável antes de avaliar a primeira pull request do projeto. Teste em staging autorizado.

## Limites e trade-offs
Uma referência inadequada pode marcar todo o repositório como novo ou esconder uma alteração. Exceções exigem responsável e prazo.

## Como verificar
Altere um arquivo conhecido e confirme que a issue aparece na área de código novo esperada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sonarqube-analise-de-taint-e-apis-internas]] — Complementa o tópico com sonarqube server: análise de taint e apis internas.

## Fontes
- [SonarQube Server — Analysis overview](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-overview) — documentação oficial sobre scanner, análise e processamento de relatórios no servidor; consultado em 2026-10-04.
- [SonarQube Server — Analysis parameters](https://docs.sonarsource.com/sonarqube-server/2026.2/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui) — referência de parâmetros de análise e delimitação de fontes, testes e quality gate; consultado em 2026-10-04.
