---
id: software.testes.tranche24.001788
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/model-checking/kani/main/README.md", "https://github.com/model-checking/kani"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Licenciamento espelhado no do próprio Rust

## Em uma frase
O README encerra com a dupla licença do costume do ecossistema: o Kani é distribuído "under the terms of both the MIT license and the Apache License (Version 2.0)" — o mesmo par MIT/Apache-2.0 sob o qual o Rust é distribuído, de que o Kani contém código e que tem porções adicionais cobertas por licenças BSD-like, conforme os arquivos LICENSE-APACHE e LICENSE-MIT do repositório.

## Por que importa
Para uso corporativo a pergunta "a ferramenta é usável em produto fechado?" depende do par MIT/Apache: ambas permitem; o detalhe de atenção está no aviso explícito do README de que partes herdadas do projeto Rust trazem licenças BSD-like "various", que o consumidor deve ler no repositório do rust-lang quando a redistribuição incluir esses pedaços.

## Como funciona
Trate o Kani como ferramenta de desenvolvimento dual-licensed padrão do nicho; em redistribuições incomuns (binário do verificador embutido numa appliance), verifique as notas de licença do Rust herdadas, apontadas pela seção License do README.

## Exemplo
O LICENSE-APACHE e o LICENSE-MIT no root do repositório são os documentos canônicos da dupla licença; a seção "Rust" dentro de License explica o que veio de fora e onde ler os detalhes.

## Limites e trade-offs
O README não lista quais porções BSD-like existem nem onde; a nota afirma apenas a declaração de origem, exatamente como o texto oficial a faz.

## Como verificar
As seções "License > Kani" e "License > Rust" do README oficial definem o licenciamento e a herança.

## Conexões
- [[kani-citation]] — Veja também: Base acadêmica rastreável: o paper ASE 2026.
- [[kani-developer-docs]] — Veja também: Por dentro: developer docs e política de segurança.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial model-checking/kani](https://github.com/model-checking/kani) — Repositório oficial do Kani Rust Verifier no GitHub com código-fonte, workflows, CITATION.cff e política de segurança.; consultado em 2026-10-03.
