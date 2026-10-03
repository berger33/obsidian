---
id: software.testes.tranche20.001437
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

# fast-check: integrar com executores de teste

## Em uma frase
A biblioteca se integra a executores conhecidos, incluindo extensões que produzem casos de teste a partir de propriedades.

## Por que importa
A integração mantém relatórios e filtros do executor, permitindo misturar testes de exemplo e propriedades na mesma suíte.

## Como funciona
Adote a extensão do executor, descreva a propriedade no formato aceito e mantenha os testes de exemplo ao lado das propriedades.

## Exemplo
Um caso pode ser declarado como propriedade dentro da suíte existente, aparecendo no relatório junto dos demais testes.

## Limites e trade-offs
Converter toda a suíte em propriedades sem critério aumenta o tempo sem cobrir melhor as regras estáveis.

## Como verificar
Execute a suíte com a extensão e confirme que a falha de propriedade reporta a semente como nos demais casos.

## Conexões
- [[fc-number-of-runs-and-ci]] — Veja também: fast-check: ajustar execuções e usar na esteira.
- [[fc-limits-and-practices]] — Veja também: fast-check: reconhecer limites.

## Fontes
- [fast-check — Primeiros passos](https://fast-check.dev/docs/introduction/getting-started/) — propriedades, geradores, redução de casos e sementes; consultado em 2026-10-03.
- [fast-check — Pacote publicado](https://www.npmjs.com/package/fast-check) — versões, documentação de uso e recursos do pacote; consultado em 2026-10-03.
