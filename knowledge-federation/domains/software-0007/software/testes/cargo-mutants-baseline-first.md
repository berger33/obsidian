---
id: software.testes.tranche21.001533
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

# cargo-mutants: baseline verde antes de mutar

## Em uma frase
Antes de qualquer mutante, a ferramenta roda os testes sem modificação; falhas ali abortam a análise e produzem código de saída quatro dedicado.

## Por que importa
Diagnósticos de mutação sobre uma suíte vermelha são ruído sobre ruído; o baseline separado protege a leitura dos resultados.

## Como funciona
Corrija os testes que já falham primeiro e reveja caminhos relativos no Cargo.toml, citados no README como causa clássica de erro por cópia.

## Exemplo
A mensagem de resultado limpa com código quatro diz exatamente: a árvore já estava quebrada, nada foi testado.

## Limites e trade-offs
Copiar a árvore para testar pode revelar dependências de caminho que só existiam no diretório original — o problema não era o mutante.

## Como verificar
Quebre um teste de propósito e confirme que a corrida para sem enumerar mutantes, com o código de saída esperado.

## Conexões
- [[cargo-mutants-side-effects]] — Veja também: cargo-mutants: perigo de efeitos colaterais.
- [[cargo-mutants-result-vocabulary]] — Veja também: cargo-mutants: caught, not caught, check e build failed.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
