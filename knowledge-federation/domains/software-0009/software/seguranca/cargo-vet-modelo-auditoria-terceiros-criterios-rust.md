---
id: software.seguranca.tranche17.001621
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://mozilla.github.io/cargo-vet/how-it-works.html", "https://mozilla.github.io/cargo-vet/first-party-code.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo-vet`: registrar auditorias de código Rust de terceiros junto ao projeto

## Em uma frase
Por padrão, `cargo-vet` exige auditorias para dependências crates.io no grafo Cargo; crates raiz, path, Git e registries customizados são tratadas como confiáveis, salvo configuração explícita.

## Por que importa
O scanner de advisories encontra vulnerabilidades conhecidas, enquanto a auditoria de supply chain busca evidência de revisão do código novo ou alterado.

## Como funciona
O projeto armazena registros sob `supply-chain/` e associa critérios ao grafo; revise também `audit-as-crates-io` quando código first-party ou uma origem não padrão precisar de enforcement.

## Exemplo
Após adicionar uma dependência nova, rode `cargo vet` na mesma branch e resolva a falta de auditoria antes de integrar o pacote.

```text
cargo vet
```

## Limites e trade-offs
Uma auditoria registrada é julgamento de revisão, não prova matemática de ausência de backdoor; o escopo padrão não audita automaticamente código first-party, path, Git ou registries customizados.

## Como verificar
Revise os arquivos de política e de auditoria no commit, confirme qual critério cobre a crate e observe se o comando reprova uma mudança não certificada.

## Conexões
- [[cargo-vet-init-supply-chain-exemptions-iniciais]] — `cargo vet init`: inicializar supply chain sem confundir exemptions com auditorias.

## Fontes
- [Cargo Vet — How it Works](https://mozilla.github.io/cargo-vet/how-it-works.html) — modelo de auditoria diferencial, confiança e fluxo de verificação; consultado em 2026-10-04.
- [Cargo Vet — First-Party Code](https://mozilla.github.io/cargo-vet/first-party-code.html) — fronteira default de crates.io e configuração de código first-party/path/Git; consultado em 2026-10-04.
