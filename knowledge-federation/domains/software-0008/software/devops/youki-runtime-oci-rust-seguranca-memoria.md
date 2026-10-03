---
id: software.devops.tranche08.000731
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
fontes: ["https://raw.githubusercontent.com/youki-dev/youki/main/README.md", "https://youki-dev.github.io/youki/user/basic_setup.html", "https://github.com/youki-dev/youki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Youki: implementação da especificação OCI Runtime em Rust na CNCF

## Em uma frase
O `youki` (pronunciado `/joʊki/`, palavra japonesa para "container" e também "alegre", projeto CNCF Sandbox) é uma implementação da especificação `opencontainers/runtime-spec` escrita em Rust, combinando segurança de memória e controle direto de chamadas de sistema.

## Por que importa
Conforme explica a seção `Motivation` do README oficial do `youki`, embora muitas ferramentas excelentes de containers sejam escritas em Go (como o `runc`), um runtime de containers de baixo nível exige uso intensivo de chamadas de sistema como `namespaces(7)` e `fork(2)`, que exigem tratamento especial delicado em um runtime multithreaded com coletor de lixo como o Go. Ao mesmo tempo, diferentemente da linguagem C (usada no `crun`), o **Rust** oferece garantias de segurança de memória em tempo de compilação sem abrir mão de performance e baixo consumo de memória.

## Como funciona
Construído em Rust (edição 2024, exigindo kernel Linux >= 5.3) e apoiado no projeto irmão `youki-dev/oci-spec-rs` (implementação das especificações OCI Runtime e Image em Rust), o `youki` lê o OCI bundle (`config.json` + `rootfs`), aplica namespaces, cgroups v1/v2, capabilities (`CAP_BPF`, `CAP_PERFMON`, `CAP_CHECKPOINT_RESTORE`), seccomp e LSMs e gerencia todo o ciclo de vida do container. O projeto passou nos testes end-to-end (e2e) do `containerd` e já é adotado em ambientes de produção, funcionando como runtime drop-in para Docker (`--runtime youki`), Podman (`--runtime .../youki`) e Kubernetes/containerd.

## Exemplo
```bash
# Exibir informações detalhadas do ambiente, kernel, cgroups, namespaces e capabilities com youki info
./youki info
```

## Limites e trade-offs
Conforme demonstrado no benchmark oficial do README do `youki` (medido com `hyperfine` ao longo de 100 execuções do ciclo `create -> start -> delete`), o `youki` (`111.5 ms ± 11.6 ms`) tem a metade do tempo médio do `runc` em Go (`224.6 ms ± 12.0 ms`, `200%` vs youki), porém ainda apresenta tempo maior que o `crun` em C puro (`47.3 ms ± 2.8 ms`, `42%` vs youki), posicionando-se no ponto de equilíbrio entre a velocidade nativa e a segurança de memória do Rust.

## Como verificar
Execute `./youki info` em um host Linux (kernel >= 5.3) e confirme a detecção de `Cgroup setup: unified`, `Namespaces: enabled` e as capabilities disponíveis no sistema.

## Conexões
- [[youki-benchmarks-performance-hyperfine-runc-crun]] — Veja também: Youki: análise de desempenho e benchmark de ciclo de vida com hyperfine frente ao runc e crun.
- [[youki-compilacao-just-dependencias-linux-rust]] — Referência cruzada direta com youki-compilacao-just-dependencias-linux-rust.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
