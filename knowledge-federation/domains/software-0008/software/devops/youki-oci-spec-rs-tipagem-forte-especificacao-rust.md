---
id: software.devops.tranche08.000736
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/youki-dev/youki/main/README.md", "https://github.com/youki-dev/oci-spec-rs", "https://github.com/youki-dev/youki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Youki: crate oci-spec-rs para serialização e validação tipada das especificações OCI Runtime e Image em Rust

## Em uma frase
O ecossistema `youki-dev` mantém o projeto relacionado `youki-dev/oci-spec-rs`, que fornece estruturas fortemente tipadas em Rust para as especificações OCI Runtime (`config.json`) e OCI Image.

## Por que importa
Em um runtime de containers, fazer o parse manual de arquivos `config.json` complexos (que contêm dezenas de estruturas aninhadas para namespaces Linux, mapeamentos de UID/GID, dispositivos cgroups, perfis seccomp, capabilities e mounts) sem tipagem estrita é uma fonte comum de bugs de deserialização e campos ignorados silenciosamente. O README oficial do `youki` destaca o `youki-dev/oci-spec-rs` como projeto base compartilhado com toda a comunidade Rust cloud-native.

## Como funciona
A biblioteca **`oci-spec-rs`** modela em structs e enums idiomáticos de Rust (com suporte a `serde` para serialização e deserialização JSON) tanto a especificação OCI Runtime (`runtime-spec`) quanto a especificação OCI Image (`image-spec`). O `youki` utiliza a `oci-spec-rs` tanto no comando `youki spec` (e `youki spec --rootless`) para construir e serializar templates `config.json` válidos quanto durante o `youki create`/`run` para validar e carregar o `config.json` do bundle em memória com segurança de tipos antes de invocar as chamadas de sistema do kernel Linux.

## Exemplo
```bash
# Gerar o arquivo config.json usando youki spec (baseado em oci-spec-rs) e validar a seção linux.namespaces
./youki spec
jq '.linux.namespaces' config.json
```

## Limites e trade-offs
Como a `oci-spec-rs` valida rigorosamente os tipos e valores esperados dos enums da especificação OCI durante a deserialização com `serde`, arquivos `config.json` gerados por ferramentas legadas fora do padrão que incluam tipos incorretos (por exemplo, strings onde a especificação OCI exige inteiros ou booleans) serão rejeitados imediatamente no parse inicial do `youki`.

## Como verificar
Execute `./youki spec --rootless` e inspecione o `config.json` gerado com `jq .` para verificar a conformidade estrutural dos blocos `process`, `root`, `mounts` e `linux`.

## Conexões
- [[youki-containers-rootless-integracao-docker-podman]] — Veja também: Youki: execução de containers em modo rootless e integração com Docker e Podman.
- [[youki-arquitetura-interna-libcontainer-crates-workspaces]] — Veja também: Youki: arquitetura modular em Rust e biblioteca libcontainer para gerenciamento de namespaces, cgroups e syscalls.
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.
- [[youki-ciclo-vida-containers-spec-create-start-state-delete]] — Referência cruzada direta com youki-ciclo-vida-containers-spec-create-start-state-delete.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://github.com/youki-dev/oci-spec-rs) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
