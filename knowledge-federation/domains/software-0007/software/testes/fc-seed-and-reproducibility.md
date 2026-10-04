---
id: software.testes.tranche20.001433
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
fontes: ["https://fast-check.dev/docs/introduction/getting-started/", "https://www.npmjs.com/package/fast-check"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# fast-check: reproduzir execuções pela semente

## Em uma frase
Cada execução usa uma semente, exibida na falha, que permite repetir exatamente a sequência de valores gerados.

## Por que importa
A semente transforma o resultado da propriedade em algo reproduzível, requisito para investigar falhas intermitentes.

## Como funciona
Registre a semente das execuções que falham, reproduza com a mesma semente e mantenha a semente no relato do defeito.

## Exemplo
Um erro que só aparece em determinada sequência pode ser reproduzido informando a semente registrada.

## Limites e trade-offs
Rerodar sem a semente procura o erro em outro caminho e pode dar a impressão de problema intermitente não resolvido.

## Como verificar
Guarde a semente de uma falha, reproduza o caso e confirme que a falha ocorre no mesmo ponto.

## Conexões
- [[fc-shrinking]] — Veja também: fast-check: usar a redução de contraexemplos.
- [[fc-model-based]] — Veja também: fast-check: testar máquinas de estado com modelos.

## Fontes
- [fast-check — Primeiros passos](https://fast-check.dev/docs/introduction/getting-started/) — propriedades, geradores, redução de casos e sementes; consultado em 2026-10-03.
- [fast-check — Pacote publicado](https://www.npmjs.com/package/fast-check) — versões, documentação de uso e recursos do pacote; consultado em 2026-10-03.
