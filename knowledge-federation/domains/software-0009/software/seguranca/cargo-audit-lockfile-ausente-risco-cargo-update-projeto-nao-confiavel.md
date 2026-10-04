---
id: software.seguranca.tranche17.001603
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md", "https://doc.rust-lang.org/cargo/reference/build-scripts.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo-audit` e projeto sem `Cargo.lock`: por que evitar comandos Cargo em código não confiável

## Em uma frase
O README do `cargo-audit` alerta que, sem lockfile, o comando pode executar `cargo update --workspace` para gerar um, e que ferramentas Cargo podem executar código do projeto.

## Por que importa
Um scanner aparentemente passivo pode acionar resolução ou etapas do ecossistema de build; executar isso dentro de um checkout hostil amplia a superfície de risco do próprio analista.

## Como funciona
Para triagem de um repositório desconhecido, use a opção de arquivo sobre um lockfile obtido como dado e execute fora do diretório do projeto, sem carregar sua configuração local.

## Exemplo
Baixe e inspecione o `Cargo.lock` como artefato, copie-o para uma área isolada e rode `cargo audit --file /tmp/review/Cargo.lock` sem invocar Cargo na árvore examinada.

```text
cargo audit --file /tmp/review/Cargo.lock
```

## Limites e trade-offs
O modo por arquivo não audita código-fonte nem torna seguro abrir qualquer artefato; preserve isolamento, confira o caminho e não execute scripts ou builds do projeto suspeito.

## Como verificar
Teste a rotina em um checkout descartável sem lockfile e observe que o pipeline bloqueia comandos no diretório original; registre hash e origem do lockfile separado.

## Conexões
- [[cargo-audit-identificadores-rustsec-faixas-versoes-triagem]] — Triagem de achados `RUSTSEC-*`: identificador, faixa afetada e versão de correção.
- [[cargo-audit-opcao-file-lockfile-externo-reproducibilidade]] — `cargo audit --file`: auditar um `Cargo.lock` externo sem entrar no workspace.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — aviso para projetos não confiáveis, ausência de lockfile e opção `--file`; consultado em 2026-10-04.
- [Cargo Reference — Build Scripts](https://doc.rust-lang.org/cargo/reference/build-scripts.html) — código de build executado pelo ecossistema Cargo e implicações ao trabalhar com fontes não confiáveis; consultado em 2026-10-04.
