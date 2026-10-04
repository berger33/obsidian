---
id: software.devops.tranche07.000697
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
fontes: ["https://raw.githubusercontent.com/containers/crun/main/README.md", "https://raw.githubusercontent.com/containers/crun/main/crun.1.md", "https://github.com/containers/crun"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Containers crun: anotações OCI para contextos de mount SELinux, preservação de grupos, logs de hooks e pidfd receiver

## Em uma frase
O `crun` disponibiliza anotações OCI específicas para controlar o tipo de contexto de montagem SELinux (`run.oci.mount_context_type`), preservar grupos suplementares (`run.oci.keep_original_groups`), redirecionar `stdout`/`stderr` de hooks OCI e exportar `pidfd` (`run.oci.pidfd_receiver`).

## Por que importa
Em ambientes corporativos com SELinux habilitado (RHEL, CentOS Stream, Fedora CoreOS), diferentes volumes exigem flags específicas de contexto no `mount(8)` (`context`, `fscontext`, `defcontext`, `rootcontext`); similarmente, depurar falhas em hooks OCI (`prestart`, `createRuntime`, `poststop`) ou rastrear processos de containers sem condições de corrida de reciclagem de PID exige recursos dedicados no runtime. A documentação `crun.1.md` especifica as anotações que resolvem cada um desses casos.

## Como funciona
(1) **`run.oci.mount_context_type=context`** define o tipo de contexto de montagem aplicado a volumes com rótulos SELinux, aceitando `context` (padrão), `fscontext`, `defcontext` ou `rootcontext`; (2) **`run.oci.keep_original_groups=1`** instrui o `crun` a pular a chamada de sistema `setgroups`, preservando os grupos suplementares herdados do processo chamador em vez de redefini-los ou limpá-los; (3) **`run.oci.hooks.stdout=FILE`** e **`run.oci.hooks.stderr=FILE`** abrem os arquivos especificados em modo `append` (criando-os se não existirem) e os utilizam como saída padrão e erro padrão para todos os processos de hooks OCI; e (4) **`run.oci.pidfd_receiver=PATH`** envia o descritor de arquivo do processo (`pidfd`) do container para um socket UNIX, permitindo gerenciamento de processos imune à reutilização de PIDs no kernel.

## Exemplo
```json
{
  "annotations": {
    "run.oci.mount_context_type": "fscontext",
    "run.oci.hooks.stdout": "/var/log/containers/oci-hooks-out.log",
    "run.oci.hooks.stderr": "/var/log/containers/oci-hooks-err.log"
  }
}
```

## Limites e trade-offs
O uso de `run.oci.keep_original_groups=1` mantém no processo do container os grupos suplementares que o processo pai possuía no host antes de iniciar o container; por questões de isolamento de segurança (prevenção de acesso indevido por GID compartilhado), essa anotação só deve ser usada em fluxos rootless ou de computação científica/HPC onde o compartilhamento de grupos de diretórios POSIX é intencional.

## Como verificar
Configure um hook OCI simples no `config.json` junto às anotações `run.oci.hooks.stdout` e `run.oci.hooks.stderr`, inicie o container com `crun` e confirme a gravação da saída do hook nos arquivos de log indicados.

## Conexões
- [[crun-extensoes-oci-seccomp-annotations-handlers-wasm-krun]] — Veja também: Containers crun: extensões de anotações OCI para seccomp avançado, pidfd e handlers nativos para WebAssembly (wasm) e libkrun (krun).
- [[crun-compilacao-autotools-libcrun-shared-dependencies]] — Veja também: Containers crun: compilação com Autotools, geração de parser via libocispec, biblioteca compartilhada libcrun e bindings Lua.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.
- [[runc-oci-bundle-rootfs-config-json-runc-spec]] — Referência cruzada direta com runc-oci-bundle-rootfs-config-json-runc-spec.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
