---
id: software.testes.component-integration.000001
tipo: tecnica
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
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Component integration testing, Unit integration testing, Teste de integração entre componentes]
lote: software-testes-2000-0001
---

# Integração de componentes e contratos entre módulos

## Em uma frase
Component integration testing verifica interfaces e interações entre componentes de um sistema, em vez de testar cada componente isoladamente.

## Por que importa
Componentes podem funcionar individualmente e ainda discordar em formato, unidades, ordem, tratamento de erro ou ciclo de vida. Testar a fronteira ajuda a localizar problemas de integração antes de depender da aplicação completa.

## Como funciona
O CTFL lista component integration testing como nível separado, com foco nas interfaces e interações entre componentes. A estratégia depende da arquitetura e da ordem de integração; os testes podem usar doubles para componentes ainda indisponíveis, mas precisam preservar contratos relevantes. O escopo pode incluir comunicação entre serviço de aplicação e armazenamento, UI e lógica ou módulos internos.

## Exemplo
Um serviço envia `amount_minor` como inteiro em centavos, enquanto o módulo contábil espera decimal em reais. Cada unidade pode passar seus testes com valores próprios; um teste de integração envia dados pela interface real e verifica que valor e moeda são interpretados de forma compatível.

## Limites e trade-offs
Uma integração com doubles não cobre comportamento real do componente substituído. Integração em lote “big bang” tende a tornar a origem de falhas mais difícil de isolar, mas a estratégia específica depende de arquitetura. Nem todo teste de componente deve ser repetido em todos os testes de integração.

## Como verificar
Escolha fronteiras críticas, documente contrato e pré-condições, teste dados válidos/inválidos e observe erros e efeitos. Registre quais dependências foram reais ou simuladas para que o alcance do resultado fique claro.

## Conexões
- [[component-testing-isolation]] — cobre lógica individual antes das interfaces.
- [[schema-based-api-testing-schemathesis-openapi]] — aplica testes de contrato/schema em APIs.
- [[test-environment-configuration-management]] — controla configuração e versões integradas.

## Fontes
- [ASTQB — ISTQB CTFL §2.2: Test Levels and Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — distinção entre níveis de teste; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 2.2.1, interfaces e interações entre componentes; acesso em 2026-10-01.
