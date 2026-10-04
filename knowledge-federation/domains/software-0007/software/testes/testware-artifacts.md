---
id: software.testes.testware.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/1-4-test-activities-testware-and-test-roles/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Testware, Test artifacts, Artefatos de teste]
lote: software-testes-2000-0001
---

# Testware: artefatos produzidos para testar

## Em uma frase
Testware é o conjunto de work products criado ou usado pelas atividades de teste, com forma e organização que podem variar entre equipes.

## Por que importa
Sem distinguir testware de código do produto, equipes podem perder casos, dados, scripts, relatórios ou a ligação com requisitos. Identificar esses artefatos ajuda a estimar esforço, controlar versões e transferir evidência entre ciclos.

## Como funciona
O syllabus ISTQB relaciona artefatos às atividades: planos, cronogramas e registros de risco para planejamento; condições priorizadas para análise; casos, charters, cobertura, dados e ambiente para desenho; procedimentos, scripts, suítes e agenda para implementação; logs e relatórios de defeito para execução; relatório de conclusão, lições e ações para encerramento. O termo é amplo e o nome/ferramenta de armazenamento varia. Gerar um arquivo de teste, porém, não demonstra que o conteúdo está correto ou foi executado.

## Exemplo
Para validar uma mudança de API, testware pode incluir o contrato OpenAPI de entrada, casos de teste, arquivo de dados, configuração de ambiente, script de execução, log associado ao build e relatório de discrepâncias. Relacione versões para que seja possível interpretar qual contrato e quais dados produziram o resultado.

## Limites e trade-offs
Documentar artefatos sem uso cria custo; manter apenas conhecimento tácito reduz reprodutibilidade. Um único artefato pode apoiar várias atividades e um projeto pode usar formatos diferentes. Não presuma que toda equipe precisa de cada documento ou que checklist substitui teste executado.

## Como verificar
Liste os work products necessários para os objetivos e riscos, atribua responsáveis e controle versões relevantes. Confirme se logs e relatórios podem ser associados ao test object, dados e configuração da execução.

## Conexões
- [[test-environment-configuration-management]] — controla versões e relações de testware.
- [[requirements-test-traceability]] — liga testware à base de teste.
- [[fundamental-test-activities]] — organiza artefatos por atividade.

## Fontes
- [ASTQB — ISTQB CTFL §1.4: Test Activities, Testware and Test Roles](https://astqb.org/1-4-test-activities-testware-and-test-roles/) — definição de testware e diversidade entre organizações; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — exemplos de work products por atividade; acesso em 2026-10-01.
