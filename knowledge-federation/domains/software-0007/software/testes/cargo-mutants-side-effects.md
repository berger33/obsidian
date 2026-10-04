---
id: software.testes.tranche21.001532
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

# cargo-mutants: perigo de efeitos colaterais

## Em uma frase
A documentação adverte que a ferramenta compila e executa código com modificações geradas por máquina: se a suíte escreve ou apaga arquivos, a corrida pode causar estrago real.

## Por que importa
Testes de integração que limpam diretórios ou tocam serviços externos ganham um novo significado quando rodados contra uma fonte mutilada.

## Como funciona
Pense nos efeitos possíveis da sua suíte antes de rodar, ou rode em ambiente descartável; essa é a recomendação literal do projeto.

## Exemplo
Um mutante que esvazia a função de guarda de caminho pode transformar o teardown em destruição de dados de quem rodou fora da caixa.

## Limites e trade-offs
A maturidade declarada é beta, e o aviso existe porque a execução é real, não simulada; não encurte o aviso para a CI compartilhada.

## Como verificar
Rode a primeira vez em contêiner efêmero e confirme que a árvore original permanece intacta no host.

## Conexões
- [[cargo-mutants-install-run]] — Veja também: cargo-mutants: instalar e disparar.
- [[cargo-mutants-baseline-first]] — Veja também: cargo-mutants: baseline verde antes de mutar.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
