---
id: software.devops.tranche07.000685
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/opencontainers/runc/main/README.md", "https://github.com/opencontainers/runtime-spec", "https://github.com/opencontainers/runc"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenContainer runc: segurança de caminhos com a biblioteca Rust libpathrs e filtragem de syscalls com libseccomp

## Em uma frase
Por padrão, a compilação do `runc` habilita as build tags `seccomp` (filtragem de chamadas de sistema via `libseccomp`) e `libpathrs` (uso da biblioteca em Rust `libpathrs` >= 0.2.5 para segurança contra ataques de resolução de caminhos e symlinks).

## Por que importa
Uma das classes mais críticas de vulnerabilidades históricas em runtimes de containers envolve ataques de corrida de caminhos e links simbólicos (TOCTOU / symlink traversal) no momento em que o runtime no host abre arquivos dentro do `rootfs` ou `/proc` controlado pelo container, além da exposição de syscalls perigosas do kernel Linux. Conforme documentado na seção `Pre-Requisites` e `Build Tags` do README oficial do `runc`, o uso padrão de `libpathrs` e `libseccomp` mitiga estruturalmente esses dois vetores.

## Como funciona
Durante o build do `runc`, duas tags vêm habilitadas por padrão no Makefile principal: (1) **`seccomp`**, que vincula a biblioteca C `libseccomp` para compilar filtros BPF de chamadas de sistema definidos na seção `linux.seccomp` do `config.json` e carregá-los no kernel antes de iniciar o processo do container; e (2) **`libpathrs`**, que integra a biblioteca escrita em Rust `libpathrs` (exigindo versão mínima `0.2.5` e Rust 1.63+ para compilação) para realizar operações de abertura e resolução de caminhos dentro do container de forma imune a escapes por symlinks e condições de corrida usando primitivas modernas do kernel (`openat2` / descritores O_PATH).

## Exemplo
```bash
# Instalar dependências de compilação em Ubuntu/Debian e verificar suporte a seccomp e libpathrs no binário runc
sudo apt update && sudo apt install -y make gcc linux-libc-dev libseccomp-dev pkg-config git
runc --version
```

## Limites e trade-offs
Conforme explica o README oficial do `runc`, como poucas distribuições Linux ainda empacotam `libpathrs >= 0.2.5` nativamente nos repositórios oficiais, compilar o `runc` a partir do código-fonte com as build tags padrão exige compilar e instalar a `libpathrs` localmente (com `cargo`, `clang` e `lld`) ou desabilitar explicitamente a tag na compilação (`make RUNC_BUILDTAGS="-libpathrs"`), o que remove a camada extra de proteção da `libpathrs`.

## Como verificar
Execute `runc features` (ou `runc --version` e `ldd $(which runc)`) para verificar se o binário em uso foi compilado com suporte a `seccomp` e às extensões de segurança do kernel.

## Conexões
- [[runc-containers-rootless-user-namespaces-configuracao]] — Veja também: OpenContainer runc: execução de containers rootless com User Namespaces (CONFIG_USER_NS).
- [[runc-compilacao-build-tags-nocriu-obsoletos]] — Veja também: OpenContainer runc: customização de compilação com RUNC_BUILDTAGS, EXTRA_VERSION e tags obsoletas.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[crun-extensoes-oci-seccomp-annotations-handlers-wasm-krun]] — Referência cruzada direta com crun-extensoes-oci-seccomp-annotations-handlers-wasm-krun.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
