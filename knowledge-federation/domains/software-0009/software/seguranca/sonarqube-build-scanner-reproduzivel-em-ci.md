---
id: software.seguranca.tranche18.001720
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

# SonarQube Server: Build scanner reproduzível em CI

## Em uma frase
**SonarQube Server — Build scanner reproduzível em CI:** Parâmetros de scanner, versão do cliente e fontes do build devem permanecer consistentes entre jobs.

## Por que importa
O recorte de **build scanner reproduzível em ci** ajuda a padronizar análise estática e acompanhar a introdução de novos problemas em projetos e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **build scanner reproduzível em ci**, o scanner coleta arquivos dentro do escopo, aplica analisadores e envia um relatório que o servidor processa para issues e quality gates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Fixe a versão do scanner e passe configuração revisada em um job efêmero de integração. Teste em staging autorizado.

## Limites e trade-offs
Versões de servidor ou plugins diferentes podem alterar regras e resultados. Exceções exigem responsável e prazo.

## Como verificar
Guarde log de versão, parâmetros não secretos e resumo de análise para comparar execuções. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[snyk-preparar-autenticacao-e-ambiente]] — Complementa o tópico com snyk cli: preparar autenticação e ambiente.

## Fontes
- [SonarQube Server — Analysis overview](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-overview) — documentação oficial sobre scanner, análise e processamento de relatórios no servidor; consultado em 2026-10-04.
- [SonarQube Server — Analysis parameters](https://docs.sonarsource.com/sonarqube-server/2026.2/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui) — referência de parâmetros de análise e delimitação de fontes, testes e quality gate; consultado em 2026-10-04.
