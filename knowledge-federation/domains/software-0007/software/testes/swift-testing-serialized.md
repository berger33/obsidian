---
id: software.testes.tranche15.000926
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
fontes: ["https://developer.apple.com/documentation/testing", "https://developer.apple.com/documentation/testing/parameterizedtesting"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Swift Testing: serializar apenas o necessário

## Em uma frase
Testes rodam em paralelo por padrão e a trait `.serialized` restringe a execução de uma suíte à ordem sequencial.

## Por que importa
Recursos únicos, como banco compartilhado ou diretório fixo, exigem serialização; espalhá-la pela suíte inteira sacrifica tempo sem necessidade.

## Como funciona
Aplique `.serialized` na suíte que usa o recurso compartilhado e mantenha os demais casos paralelos, isolando o estado mutável por caso.

## Exemplo
`@Suite(.serialized) struct BancoTests { ... }` executa os casos em sequência, enquanto as suítes vizinhas continuam paralelas.

## Limites e trade-offs
Serializar não isola automaticamente nem torna o teste correto; apenas evita concorrência entre os casos daquela suíte e pode aumentar muito o tempo total.

## Como verificar
Meça o tempo da suíte com e sem serialização e confirme, executando repetidas vezes, que o recurso compartilhado não sofre interferência entre casos.

## Conexões
- [[swift-testing-tags]] — Veja também: Swift Testing: agrupar e filtrar por tags.
- [[swift-testing-async-tests]] — Veja também: Swift Testing: escrever testes assíncronos.

## Fontes
- [Apple — Swift Testing](https://developer.apple.com/documentation/testing) — macros @Test e @Suite, expectativas #expect e #require e modelo de suítes; consultado em 2026-10-02.
- [Apple — Parameterized testing](https://developer.apple.com/documentation/testing/parameterizedtesting) — testes parametrizados, coleções de argumentos e combinações; consultado em 2026-10-02.
