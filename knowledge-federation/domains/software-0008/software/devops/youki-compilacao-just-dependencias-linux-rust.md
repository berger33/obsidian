---
id: software.devops.tranche08.000733
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

# Youki: requisitos de compilação (Rust edition 2024, Linux >= 5.3), dependências de sistema e automação com just

## Em uma frase
A compilação local do `youki` é suportada em Linux (kernel >= 5.3) usando Rust (edition 2024), o executor de comandos `just` (`just youki-dev` ou `just youki-release`) e bibliotecas de sistema como `libsystemd`, `libseccomp`, `libelf`, `libclang` e `openssl`.

## Por que importa
Como o `youki` interage diretamente com recursos modernos do kernel Linux (como `pidfd`, cgroup v2 unificado, filtros `seccomp` via `libseccomp` e integração com `systemd`), tentar compilá-lo em kernels muito antigos ou sem os pacotes `-dev`/`-devel` corretos falha na vinculação de crates nativas. A seção `Getting Started` do README oficial do `youki` documenta os pré-requisitos exatos para Debian/Ubuntu e Fedora/CentOS/RHEL.

## Como funciona
O projeto utiliza o utilitário **`just`** (`casey/just`) como task runner para padronizar builds e testes. Em distribuições baseadas em Debian/Ubuntu, instalam-se `pkg-config`, `libsystemd-dev`, `build-essential`, `libelf-dev`, `libseccomp-dev`, `libclang-dev` e `libssl-dev`; em distribuições Fedora/CentOS/RHEL, instalam-se `pkg-config`, `systemd-devel`, `elfutils-libelf-devel`, `libseccomp-devel`, `clang-devel` e `openssl-devel`. Com o toolchain Rust atualizado (edition 2024), executa-se `just youki-dev` (para compilação rápida de desenvolvimento) ou `just youki-release` (ou `just build`) para gerar o binário otimizado `./youki` na raiz do workspace.

## Exemplo
```bash
# Instalar dependências em Debian/Ubuntu e compilar o binário otimizado do youki usando just
sudo apt-get update && sudo apt-get install -y \
  pkg-config libsystemd-dev build-essential libelf-dev libseccomp-dev libclang-dev libssl-dev

just youki-release
./youki -h
```

## Limites e trade-offs
Ao avaliar o desempenho do `youki` ou integrá-lo ao Docker/Podman/containerd, certifique-se de usar o binário compilado com `just youki-release` (com otimizações de compilador Rust `-O` ativadas) em vez de `just youki-dev`, pois builds de debug em Rust incluem checagens extras e símbolos não otimizados que aumentam o tamanho do binário e o tempo de inicialização.

## Como verificar
Após executar `just youki-release`, rode `./youki --version` e `./youki -h` para confirmar que o executável foi gerado corretamente e responde aos subcomandos da especificação OCI.

## Conexões
- [[youki-benchmarks-performance-hyperfine-runc-crun]] — Veja também: Youki: análise de desempenho e benchmark de ciclo de vida com hyperfine frente ao runc e crun.
- [[youki-ciclo-vida-containers-spec-create-start-state-delete]] — Veja também: Youki: geração de especificação (youki spec) e operações de ciclo de vida OCI (create, state, start, list, delete).
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.
- [[youki-desenvolvimento-multiplataforma-vagrant-codespaces-testes-oci]] — Referência cruzada direta com youki-desenvolvimento-multiplataforma-vagrant-codespaces-testes-oci.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
