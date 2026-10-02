---
id: software.testes.tranche15.000868
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/docs/api/setup-server/", "https://mswjs.io/docs/defaults/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: compartilhar handlers entre testes, dev e Storybook

## Em uma frase
A mesma lista de handlers pode atender testes automatizados, desenvolvimento local e catálogo de componentes, mantendo uma única descrição do comportamento simulado.

## Por que importa
Duplicar mocks por ambiente faz cada cópia divergir com o tempo e transforma ajustes de contrato em várias alterações desconectadas.

## Como funciona
Extraia handlers para um módulo comum, exporte conjuntos por cenário e registre apenas o subconjunto necessário em cada ponto de uso.

## Exemplo
Uma pasta de mocks compartilhada pode ser importada pelo servidor de testes e pelo navegador, de modo que a tela de desenvolvimento use exatamente as respostas verificadas na suíte.

## Limites e trade-offs
Compartilhar não significa cobrir todos os cenários em todos os ambientes; cenários de erro continuam sendo selecionados por teste, e o módulo comum precisa evitar dependências exclusivas de um executor.

## Como verificar
Altere um contrato simulado em um único lugar, rode os testes e abra o ambiente de desenvolvimento para confirmar que ambos refletem a mesma mudança.

## Conexões
- [[msw-async-handler-and-body]] — Veja também: MSW: ler corpo de requisição em handler assíncrono.
- [[msw-per-test-error-overrides]] — Veja também: MSW: simular erros por teste com overrides.

## Fontes
- [MSW — setupServer](https://mswjs.io/docs/api/setup-server/) — interceptação em Node.js e ciclo de vida de listen, resetHandlers e close; consultado em 2026-10-02.
- [MSW — Default behaviors](https://mswjs.io/docs/defaults/) — fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem; consultado em 2026-10-02.
