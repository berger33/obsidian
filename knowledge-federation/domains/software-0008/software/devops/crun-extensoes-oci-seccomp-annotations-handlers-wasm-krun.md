---
id: software.devops.tranche07.000696
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

# Containers crun: extensões de anotações OCI para seccomp avançado, pidfd e handlers nativos para WebAssembly (wasm) e libkrun (krun)

## Em uma frase
O `crun` estende a especificação OCI por meio de anotações `run.oci.*` que habilitam delegação de seccomp listener (`seccomp.receiver`/`plugins`), carregamento de BPF bruto (`seccomp_bpf_data`) e execução nativa de workloads WebAssembly (`handler=wasm`) ou microVMs via `libkrun` (`handler=krun`).

## Por que importa
Em arquiteturas cloud-native modernas, operadores de plataforma desejam usar a mesma infraestrutura de Kubernetes/CRI-O/Podman para rodar não apenas containers Linux tradicionais, mas também módulos WebAssembly (`.wasm`/`.wat`) ultraleves ou containers isolados em microVMs baseadas em KVM (`libkrun`), além de otimizar o carregamento de filtros seccomp. O manual `crun.1.md` documenta essas extensões nativas do `crun`.

## Como funciona
Por meio de anotações no `config.json`, o `crun` ativa comportamentos avançados: (1) **`run.oci.handler=HANDLER`** permite escolher os handlers experimentais `wasm` (executa cargas WebAssembly nativamente aceitando binários `.wasm` ou compilando automaticamente arquivos `.wat` e retransmitindo o `stdout`) ou `krun` (carrega a biblioteca compartilhada `libkrun.so` para lançar o container dentro de uma microVM isolada por hardware via `libkrun`); (2) **`run.oci.seccomp.receiver=PATH`** (ou variável `RUN_OCI_SECCOMP_RECEIVER`) envia o descritor do seccomp listener para um socket UNIX externo, enquanto **`run.oci.seccomp.plugins`** processa o listener via plugins carregados por `dlopen(3)`; (3) **`run.oci.seccomp_bpf_data=PATH`** ignora a seção seccomp do JSON e carrega diretamente um programa BPF codificado em base64 na syscall `seccomp(SECCOMP_SET_MODE_FILTER)`; e (4) **`run.oci.seccomp_fail_unknown_syscall=1`** força falha imediata caso uma syscall desconhecida seja encontrada no perfil.

## Exemplo
```json
{
  "annotations": {
    "run.oci.handler": "wasm",
    "run.oci.seccomp_fail_unknown_syscall": "1"
  }
}
```

## Limites e trade-offs
Para que `run.oci.handler=krun` ou `run.oci.handler=wasm` funcionem em tempo de execução, o binário do `crun` no host precisa ter sido compilado com suporte aos respectivos cabeçalhos e as bibliotecas compartilhadas correspondentes (como `libkrun.so` e um runtime WASM como WasmEdge/Wasmtime) devem estar instaladas no sistema hospedeiro; além disso, o handler `krun` requer acesso ao dispositivo de virtualização `/dev/kvm`.

## Como verificar
Verifique na saída de `crun --version` quais handlers e recursos opcionais (`+WASM`, `+KRUN`, `+SECCOMP`) estão compilados no binário `crun` do seu sistema.

## Conexões
- [[crun-checkpoint-restore-criu-pre-dump-gerenciamento]] — Veja também: Containers crun: Checkpoint e Restore de containers com CRIU, pre-dumps incrementais e restauração LSM.
- [[crun-anotacoes-selinux-grupos-hooks-pidfd]] — Veja também: Containers crun: anotações OCI para contextos de mount SELinux, preservação de grupos, logs de hooks e pidfd receiver.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.
- [[inspektor-webassembly-wasm-pos-processamento-operadores]] — Referência cruzada direta com inspektor-webassembly-wasm-pos-processamento-operadores.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
