---
id: software.devops.tranche07.000681
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

# OpenContainer runc: ferramenta CLI e runtime de referência para criar e executar containers segundo a especificação OCI

## Em uma frase
O `runc` (mantido pela Open Container Initiative sob licença Apache-2.0) é a ferramenta CLI de baixo nível de referência para criar e executar containers no Linux de acordo com a especificação OCI (`runtime-spec`).

## Por que importa
Motores de containers de alto nível como Docker, containerd, CRI-O e Podman não interagem diretamente com todas as chamadas de sistema de namespaces, cgroups e capabilities do kernel Linux ao iniciar cada processo; eles delegam essa etapa final a um runtime OCI de baixo nível. Segundo o README oficial do `runc`, embora seja projetado principalmente para ser invocado por softwares de nível superior (instalado tipicamente em `/usr/local/sbin/runc`), compreender sua operação direta é essencial para depurar falhas de inicialização de containers, segurança de kernel e conformidade OCI.

## Como funciona
O `runc` consome um **OCI bundle** — um diretório no sistema de arquivos Linux contendo um subdiretório com o sistema de arquivos raiz do container (`rootfs`) e um arquivo de especificação `config.json` que descreve namespaces (`pid`, `net`, `ipc`, `uts`, `mount`, `user`, `cgroup`), limites de recursos cgroups, capabilities Linux, perfil seccomp, rótulos SELinux/AppArmor e o processo inicial a ser executado. Quando invocado, o processo Go do `runc` utiliza um módulo auxiliar em C (`nsenter`) para configurar os namespaces antes de iniciar o processo do container e, uma vez que o processo do container está em execução, o binário do `runc` sai de cena sem permanecer residente como daemon.

## Exemplo
```bash
# Verificar a versão do runc instalado no host Linux e os recursos compilados (seccomp, libpathrs, cgroup)
runc --version
runc features
```

## Limites e trade-offs
Conforme ressalta a seção `Using runc` do README oficial, o `runc` é uma ferramenta de baixo nível que não gerencia pull de imagens de registries, camadas de overlayfs, redes virtuais CNI nem reinicialização automática de containers; tentar usá-lo diretamente no lugar de Docker, Podman ou containerd para cargas gerais exige orquestrar manualmente o rootfs, a rede e um supervisor externo como o systemd.

## Como verificar
Execute `runc --version` no host Linux para inspecionar a versão do runtime, o commit, a versão da especificação OCI suportada (`spec: 1.x.x`), a versão do Go e o status do `libseccomp`.

## Conexões
- [[runc-oci-bundle-rootfs-config-json-runc-spec]] — Veja também: OpenContainer runc: criação de OCI Bundles com rootfs e geração de config.json via runc spec.
- [[runc-ciclo-vida-create-start-list-delete-run]] — Referência cruzada direta com runc-ciclo-vida-create-start-list-delete-run.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
