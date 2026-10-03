---
id: software.testes.tranche21.001537
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/sourcefrog/cargo-mutants", "https://crates.io/crates/cargo-mutants"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-mutants: o que há em mutants.out

## Em uma frase
A corrida cria o diretório mutants.out na raiz, com um arquivo de log por mutante e pelo baseline, contendo o diff aplicado e a saída do cargo, além de mutants.json descrevendo tudo.

## Por que importa
Sem esse arquivo de trilha, a triagem de um resultado not caught obrigaria reproduzir o mutante na mão para ver o que exatamente foi trocado.

## Como funciona
Publique mutants.out nos artefatos do job e abra o log do mutante específico antes de decidir entre escrever teste ou pular.

## Exemplo
O log individual de um not caught prova que a substituição era comportamental e que nenhum teste do crate depende dela.

## Limites e trade-offs
mutants.out cresce com a árvore; versionar o diretório inteiro no git enlameia o repositório — trate-o como artefato descartável.

## Como verificar
Abra o json gerado, encontre um mutante por função e confirme a correspondência com o log do arquivo.

## Conexões
- [[cargo-mutants-skip-annotation]] — Veja também: cargo-mutants: marcar funções para pular.
- [[cargo-mutants-speed-advice]] — Veja também: cargo-mutants: acelerar builds para acelerar mutantes.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
