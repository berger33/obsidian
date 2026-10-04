---
id: software.devops.tranche07.000698
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

# Containers crun: compilação com Autotools, geração de parser via libocispec, biblioteca compartilhada libcrun e bindings Lua

## Em uma frase
A compilação do `crun` utiliza GNU Autotools (`./autogen.sh && ./configure && make`), usa Python apenas em tempo de build pelo `libocispec` para gerar o parser C, permite construir a biblioteca compartilhada `libcrun` com `--enable-shared` e oferece bindings para Lua e Python.

## Por que importa
Diferentemente de projetos puramente Go, o `crun` foi concebido desde o início para poder ser usado também como uma biblioteca C (`libcrun`) embutida diretamente dentro de outros programas e motores de containers, eliminando até mesmo o custo de criar um processo externo `fork/exec` para gerenciar containers OCI. O README oficial do `crun` detalha as dependências por distribuição (Fedora, RHEL/CentOS Stream 9/10, Ubuntu, Alpine, openSUSE Tumbleweed) e o fluxo de compilação.

## Como funciona
Para compilar o `crun` a partir do código-fonte, instalam-se os cabeçalhos de desenvolvimento do sistema (`libcap`, `libseccomp`, `systemd`, `yajl`/`json-c`, `autoconf`, `automake`, `libtool`, `go-md2man` e `python3`). A menos que os bindings Python também estejam sendo compilados, o Python é utilizado exclusivamente em tempo de compilação pelo submódulo `libocispec` para gerar automaticamente o código C que faz o parse dos esquemas JSON da OCI, não sendo necessário em tempo de execução. O fluxo padrão `./autogen.sh && ./configure && make && sudo make install` instala o binário em `/usr/local/bin/crun`; para habilitar a construção da biblioteca compartilhada `libcrun.so` (necessária para vincular outros programas à `libcrun` ou usar os bindings em `lua/`), executa-se `./configure --enable-shared`.

## Exemplo
```bash
# Compilar o crun habilitando a biblioteca compartilhada libcrun (--enable-shared)
./autogen.sh
./configure --enable-shared
make -j$(nproc)
sudo make install
```

## Limites e trade-offs
Conforme observa o README oficial do `crun`, em distribuições como o openSUSE Tumbleweed os cabeçalhos do `libseccomp` ficam em `/usr/include/libseccomp`, exigindo passar explicitamente `./configure CFLAGS='-I/usr/include/libseccomp'`; além disso, em RHEL/CentOS Stream 9 e 10, é necessário habilitar previamente o repositório `crb` (`dnf config-manager --set-enabled crb`) para encontrar todos os pacotes `-devel`.

## Como verificar
Após compilar com `./configure --enable-shared && make`, verifique a geração da biblioteca compartilhada `libcrun` e execute `./crun --version` para validar o binário resultante.

## Conexões
- [[crun-anotacoes-selinux-grupos-hooks-pidfd]] — Veja também: Containers crun: anotações OCI para contextos de mount SELinux, preservação de grupos, logs de hooks e pidfd receiver.
- [[crun-builds-estaticos-reprodutiveis-nix-verificacao-gpg]] — Veja também: Containers crun: builds estáticos reprodutíveis com Nix, automação Ansible e verificação GPG com crun.keyring.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.
- [[runc-compilacao-build-tags-nocriu-obsoletos]] — Referência cruzada direta com runc-compilacao-build-tags-nocriu-obsoletos.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
