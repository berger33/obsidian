---
id: software.testes.test-levels.000001
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
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Test levels, Test level, Níveis de teste]
lote: software-testes-2000-0001
---

# Níveis de teste e seus diferentes objetivos

## Em uma frase
Níveis de teste agrupam atividades organizadas em torno de um estágio, objeto e objetivo; o CTFL v4.0.1 descreve cinco níveis distintos.

## Por que importa
Separar níveis ajuda a planejar evidências complementares sem repetir a mesma verificação em cada camada. Um teste de componente não demonstra integração correta com serviço externo; um teste de sistema não necessariamente localiza defeitos de unidade com feedback rápido.

## Como funciona
Os cinco níveis CTFL são component testing, component integration testing, system testing, system integration testing e acceptance testing. Distinguem-se por atributos como abordagem/responsabilidades, test object, objetivos, test basis e tipos de defeito/falha. Em modelos sequenciais, critérios de saída de um nível podem informar entrada do próximo; em processos iterativos as atividades podem se sobrepor ou ocorrer em ordem diferente.

## Exemplo
Em uma aplicação de transferência bancária, verificar uma função de cálculo é teste de componente; conferir chamadas entre serviço e banco é component integration; exercitar o sistema completo segundo requisitos é system testing; testar conexão com a rede bancária é system integration; confirmar se o fluxo atende usuários e critérios de negócio é acceptance testing.

## Limites e trade-offs
Os níveis não são uma pirâmide fixa de número de casos e não indicam automaticamente quem precisa executar cada teste. A nomenclatura interna pode variar; alinhe-a às definições, objetos e objetivos reais para evitar buracos ou sobreposição.

## Como verificar
Para cada suíte, registre nível, objeto, objetivo, base de teste e responsável. Procure se há evidência de interfaces internas, sistema integrado, sistemas externos e validação de necessidades, quando relevantes.

## Conexões
- [[piramide-testes-estrategia-contexto]] — modelo de estratégia por granularidade, não uma taxonomia formal de níveis.
- [[component-testing-isolation]] — descreve um dos níveis.
- [[acceptance-testing-validation]] — foca validação e readiness.

## Fontes
- [ASTQB — ISTQB CTFL §2.2: Test Levels and Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — lista e critérios de distinção dos cinco níveis; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seções 2.2.1 e objetivos por nível; acesso em 2026-10-01.
