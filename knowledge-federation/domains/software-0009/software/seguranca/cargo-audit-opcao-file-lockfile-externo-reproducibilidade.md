---
id: software.seguranca.tranche17.001604
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md", "https://doc.rust-lang.org/cargo/reference/config.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo audit --file`: auditar um `Cargo.lock` externo sem entrar no workspace

## Em uma frase
A opção `--file` permite apontar para um lockfile específico, útil para auditar uma cópia de revisão sem fazer o comando operar no checkout examinado.

## Por que importa
Separar o arquivo de entrada reduz a chance de confundir lockfile, manifestos e configuração do diretório atual, além de preservar o artefato que fundamenta a decisão.

## Como funciona
Aponte explicitamente para a cópia do lockfile, guarde sua origem e hash e execute em um diretório controlado; isso não desativa toda configuração externa do ambiente.

## Exemplo
Em uma pipeline isolada, materialize o `Cargo.lock` aprovado em uma pasta de artefatos e invoque `cargo audit --file artifacts/Cargo.lock` antes de publicar o binário.

```text
cargo audit --file artifacts/Cargo.lock
```

## Limites e trade-offs
O relatório descreve apenas o grafo codificado naquele lockfile; dependências opcionais, features, alvos e artefatos embarcados podem exigir análise adicional.

## Como verificar
Confirme que o argumento aponta para o arquivo esperado e compare seu SHA-256 com o artefato anexado ao commit que será construído.

## Conexões
- [[cargo-audit-lockfile-ausente-risco-cargo-update-projeto-nao-confiavel]] — `cargo-audit` e projeto sem `Cargo.lock`: por que evitar comandos Cargo em código não confiável.
- [[cargo-audit-ignorar-advisory-justificativa-expiracao]] — Ignorar um advisory em `cargo-audit`: exceção rastreável, justificativa e reavaliação.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — sintaxe de `--file` para apontar a um lockfile específico; consultado em 2026-10-04.
- [Cargo Reference — Configuration](https://doc.rust-lang.org/cargo/reference/config.html) — fontes de configuração de Cargo e separação entre arquivo de entrada e configuração de ambiente; consultado em 2026-10-04.
