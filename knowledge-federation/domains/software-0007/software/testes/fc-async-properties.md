---
id: software.testes.tranche20.001435
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://fast-check.dev/docs/introduction/getting-started/", "https://github.com/dubzzz/fast-check"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# fast-check: verificar operações assíncronas

## Em uma frase
Existe variante de propriedade para predicados assíncronos, integrando-se a ambientes de teste com espera pela resolução.

## Por que importa
Código assíncrono exige a variante correspondente, mantendo geração, redução e sementes com o mesmo comportamento.

## Como funciona
Use a variante assíncrona, devolva a promessa no predicado e limite o tempo por caso para evitar execuções penduradas.

## Exemplo
A propriedade pode verificar que a consulta a um serviço em memória devolve o registro inserido anteriormente.

## Limites e trade-offs
Misturar predicado síncrono com operação assíncrona esconde promessas não resolvidas, e tempos altos de execução por caso inviabilizam muitas rodadas.

## Como verificar
Faça a operação devolver erro e confirme que a propriedade assíncrona falha exibindo o contraexemplo reduzido.

## Conexões
- [[fc-model-based]] — Veja também: fast-check: testar máquinas de estado com modelos.
- [[fc-number-of-runs-and-ci]] — Veja também: fast-check: ajustar execuções e usar na esteira.

## Fontes
- [fast-check — Primeiros passos](https://fast-check.dev/docs/introduction/getting-started/) — propriedades, geradores, redução de casos e sementes; consultado em 2026-10-03.
- [fast-check — repositório oficial](https://github.com/dubzzz/fast-check) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
