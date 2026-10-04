---
id: software.seguranca.tranche18.001712
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

# SonarQube Server: Escopo de fontes e testes

## Em uma frase
**SonarQube Server — Escopo de fontes e testes:** Parâmetros de fontes e testes definem quais diretórios entram em cada parte da análise.

## Por que importa
O recorte de **escopo de fontes e testes** ajuda a padronizar análise estática e acompanhar a introdução de novos problemas em projetos e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escopo de fontes e testes**, o scanner coleta arquivos dentro do escopo, aplica analisadores e envia um relatório que o servidor processa para issues e quality gates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Declare diretórios principais e de teste para um monorepo em vez de depender de autodetecção ambígua. Teste em staging autorizado.

## Limites e trade-offs
Padrão de escopo incorreto pode excluir código de produção ou classificar teste como fonte. Exceções exigem responsável e prazo.

## Como verificar
Compare a lista de arquivos analisados com a árvore versionada e inspecione exclusões efetivas. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sonarqube-perfis-de-qualidade-aplicados]] — Complementa o tópico com sonarqube server: perfis de qualidade aplicados.

## Fontes
- [SonarQube Server — Analysis overview](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-overview) — documentação oficial sobre scanner, análise e processamento de relatórios no servidor; consultado em 2026-10-04.
- [SonarQube Server — Analysis parameters](https://docs.sonarsource.com/sonarqube-server/2026.2/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui) — referência de parâmetros de análise e delimitação de fontes, testes e quality gate; consultado em 2026-10-04.
