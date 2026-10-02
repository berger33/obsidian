---
id: software.testes.tranche08.000167
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://testing-library.com/docs/queries/about/", "https://testing-library.com/docs/dom-testing-library/api-async/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testing Library: detectar consultas ambíguas

## Em uma frase
Use queries singulares quando o cenário espera um elemento e trate duplicidade como sinal de interface ou contexto ambíguo.

## Por que importa
Uma consulta que escolhe arbitrariamente entre elementos semelhantes pode validar o controle errado e esconder regressões de acessibilidade.

## Como funciona
Prefira getByRole ou findByRole com nome e escopo adequado; se há repetição legítima, use within no contêiner específico ou uma consulta de coleção com contagem deliberada.

## Exemplo
Em tabela com vários botões Editar, localize a linha pelo nome do registro e então procure o botão dentro daquela linha.

## Limites e trade-offs
Uma contagem fixa pode superajustar dados de fixture; use cardinalidade apenas quando ela faz parte do contrato do cenário.

## Como verificar
Adicione temporariamente um segundo elemento com mesmo nome e confirme que teste não seleciona silenciosamente o primeiro. Verifique unicidade no contêiner esperado.

## Conexões
- [[rtl-formulario-erro-associacao-label]] — Veja também: Testing Library: validar formulários pela relação label-controle.
- [[flutter-orientacao-layout-widget-test]] — Veja também: Flutter: validar orientação retrato e paisagem.

## Fontes
- [Testing Library — About Queries](https://testing-library.com/docs/queries/about/) — seleção de elementos por papel, nome e prioridade; consultado em 2026-10-02.
- [Testing Library — Async Methods](https://testing-library.com/docs/dom-testing-library/api-async/) — findBy, waitFor e remoção assíncrona; consultado em 2026-10-02.
