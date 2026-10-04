---
id: software.seguranca.tranche18.001717
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

# SonarQube Server: Exclusões por caminho

## Em uma frase
**SonarQube Server — Exclusões por caminho:** Exclusões globais e de projeto limitam arquivos e regras, com precedência definida na configuração.

## Por que importa
O recorte de **exclusões por caminho** ajuda a padronizar análise estática e acompanhar a introdução de novos problemas em projetos e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exclusões por caminho**, o scanner coleta arquivos dentro do escopo, aplica analisadores e envia um relatório que o servidor processa para issues e quality gates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Mantenha diretórios gerados fora do escopo por configuração explícita e documentada. Teste em staging autorizado.

## Limites e trade-offs
Exclusão global não deve ser usada para silenciar dívida técnica sem plano de remediação. Exceções exigem responsável e prazo.

## Como verificar
Revise propriedades efetivas e compare com a lista de arquivos versionados no build. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[sonarqube-cobertura-de-testes-como-dado-separado]] — Complementa o tópico com sonarqube server: cobertura de testes como dado separado.

## Fontes
- [SonarQube Server — Analysis overview](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-overview) — documentação oficial sobre scanner, análise e processamento de relatórios no servidor; consultado em 2026-10-04.
- [SonarQube Server — Analysis parameters](https://docs.sonarsource.com/sonarqube-server/2026.2/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui) — referência de parâmetros de análise e delimitação de fontes, testes e quality gate; consultado em 2026-10-04.
