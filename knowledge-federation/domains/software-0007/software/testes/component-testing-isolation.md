---
id: software.testes.component-testing.000001
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
aliases: [Component testing, Unit testing, Teste de componente]
lote: software-testes-2000-0001
---

# Teste de componente em isolamento

## Em uma frase
Component testing, também chamado unit testing, verifica componentes individualmente, frequentemente em ambiente controlado com harness ou framework de unidade.

## Por que importa
Testar componente perto do código oferece feedback localizado e pode revelar erros de lógica antes de integração. O resultado não demonstra que interfaces, configuração ou comportamento do sistema completo funcionam; esses aspectos exigem níveis adicionais.

## Como funciona
O CTFL descreve esse nível como teste de componentes em isolamento, normalmente executado por desenvolvedores em ambiente de desenvolvimento, com suporte como harness ou framework unitário. A base pode incluir requisitos do componente, design detalhado e código. Isolamento não significa substituir todo collaborator por mock; fakes, stubs, dependências reais locais ou outros arranjos dependem do objetivo e custo.

## Exemplo
Um módulo de imposto recebe valor, jurisdição e data; testes cobrem faixas, arredondamento e regra de validade sem depender do gateway de pagamento. Um caso que chama a API real do provedor também pode testar comportamento, mas já introduz outra fronteira, dependência e risco ambiental.

## Limites e trade-offs
Testes muito isolados podem não detectar incompatibilidade entre módulos; muitos doubles podem reproduzir a implementação em vez do contrato. Nem todo componente exige o mesmo conjunto de testes. Testar todas as linhas não garante requisitos corretos ou asserções adequadas.

## Como verificar
Verifique se cada teste tem entrada/estado e expectativa clara, executa de forma reproduzível e falha quando o comportamento relevante quebra. Mantenha outras verificações para integração e sistema onde os riscos atravessam fronteiras.

## Conexões
- [[test-doubles-fakes-stubs-spies-mocks]] — auxilia a escolher colaboradores substituídos.
- [[component-integration-testing-interfaces]] — testa interações entre componentes.
- [[cobertura-branches-statement-interpretacao]] — execução de código é apenas uma medida parcial.

## Fontes
- [ASTQB — ISTQB CTFL §2.2: Test Levels and Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — definição geral de níveis e objetos; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 2.2.1 sobre component testing, isolamento e test harness; acesso em 2026-10-01.
