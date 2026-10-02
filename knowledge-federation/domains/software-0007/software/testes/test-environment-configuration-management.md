---
id: software.testes.testware-configuration.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-04.md"
fontes: ["https://astqb.org/5-4-configuration-management/", "https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam4-3-Answers.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Testware configuration management, Test configuration, Gerenciamento de configuração de testes]
lote: software-testes-2000-0001
---

# Gerenciamento de configuração para testware e ambientes

## Em uma frase
Gerenciamento de configuração identifica, controla e acompanha versões e relações de itens de trabalho, incluindo test plans, casos, scripts, resultados, logs e relatórios.

## Por que importa
Uma falha que some entre builds pode ser difícil de investigar se não for possível saber qual versão do produto, do script, dos dados ou do ambiente foi usada. Controlar mudanças no testware ajuda a reproduzir resultados, identificar o que foi alterado e manter ligações entre execução e evidência.

## Como funciona
A seção 5.4 do syllabus descreve configuração como disciplina para identificar, controlar e rastrear work products. Em testes, os itens podem incluir planos, estratégias, condições, casos, scripts, resultados, logs e relatórios. Registre versões ou identificadores inequívocos e as relações relevantes: caso com requisito, execução com build e dados, resultado com defeito. Um problema reaparece em uma versão posterior? Compare as baselines do software e testware para reconstruir o contexto e repetir a execução.

## Exemplo
Ao investigar uma regressão em `build-42`, associe o relatório ao commit/build, imagem de contêiner, configuração de feature flags, versão da suíte, massa de dados e versão do ambiente. Se o defeito foi corrigido em `build-43`, mantenha o resultado de confirmação e as regressões ligadas à nova versão, sem substituir silenciosamente os logs anteriores.

## Limites e trade-offs
Rastrear cada detalhe sem critério adiciona carga e ruído; não registrar dependências relevantes impede reprodução. Uma identificação nominal não garante que o artefato esteja armazenado, íntegro ou acessível. A granularidade deve refletir risco, necessidade de auditoria e frequência de mudança.

## Como verificar
Defina quais itens são controlados e como identificar versões. Antes de executar, registre build, dados, ambiente e testware usados; após mudanças, registre o novo baseline e o vínculo com os resultados. Tente reproduzir uma falha com os itens identificados para avaliar se os registros são suficientes.

## Conexões
- [[testes-hermeticos-dependencias]] — configurações e dependências declaradas reduzem variação ambiental.
- [[test-progress-metrics-relatorios-conclusao]] — logs e resultados alimentam relatórios.
- [[regression-test-prioritization-risco-impacto]] — análise de impacto da mudança orienta seleção de regressão.

## Fontes
- [ASTQB — ISTQB CTFL §5.4: Configuration Management](https://astqb.org/5-4-configuration-management/) — identificação, controle e rastreamento de work products de teste; acesso em 2026-10-01.
- [ASTQB — CTFL v4.0 Sample Exam #4 Answers](https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam4-3-Answers.pdf) — aplicação de configuração para recuperar e inspecionar versões anteriores durante investigação; acesso em 2026-10-01.
