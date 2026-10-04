---
id: software.seguranca.tranche18.001714
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

# SonarQube Server: Quality gate como critério de integração

## Em uma frase
**SonarQube Server — Quality gate como critério de integração:** Quality gates agregam condições sobre a análise e podem ser aguardados pelo scanner na pipeline.

## Por que importa
O recorte de **quality gate como critério de integração** ajuda a padronizar análise estática e acompanhar a introdução de novos problemas em projetos e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **quality gate como critério de integração**, o scanner coleta arquivos dentro do escopo, aplica analisadores e envia um relatório que o servidor processa para issues e quality gates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use sonar.qualitygate.wait em um job de validação para que o resultado seja consultado antes do merge. Teste em staging autorizado.

## Limites e trade-offs
O scanner pode terminar o envio antes do processamento final se a pipeline não aguardar o gate. Exceções exigem responsável e prazo.

## Como verificar
Force uma condição de teste que falhe e confirme que o job recebe o estado final não aprovado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sonarqube-definicao-de-codigo-novo]] — Complementa o tópico com sonarqube server: definição de código novo.

## Fontes
- [SonarQube Server — Analysis overview](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-overview) — documentação oficial sobre scanner, análise e processamento de relatórios no servidor; consultado em 2026-10-04.
- [SonarQube Server — Analysis parameters](https://docs.sonarsource.com/sonarqube-server/2026.2/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui) — referência de parâmetros de análise e delimitação de fontes, testes e quality gate; consultado em 2026-10-04.
