---
id: software.devops.tranche07.000699
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

# Containers crun: builds estáticos reprodutíveis com Nix, automação Ansible e verificação GPG com crun.keyring

## Em uma frase
O projeto `crun` fornece derivações oficiais do gerenciador de pacotes Nix (`nix/`) para produzir binários ELF `x86_64/amd64` estaticamente vinculados e 100% reprodutíveis, além de assinar todos os artefatos de release com chaves listadas em `crun.keyring`.

## Por que importa
Em nós Kubernetes minimalistas (como imagens imutáveis de sistema operacional ou distribuições com versões diferentes de `glibc`, `libseccomp` e `libcap`), distribuir um binário dinâmico de runtime OCI pode falhar por incompatibilidade de bibliotecas compartilhadas (`GLIBC_2.XX not found`), enquanto a ausência de verificação criptográfica expõe o host a adulteração de binários. O README oficial do `crun` documenta tanto o build estático reprodutível via Nix quanto a verificação GPG das releases.

## Como funciona
Para verificar qualquer artefato oficial baixado da página de releases (como `crun-1.29.1.tar.zst` e sua assinatura `.asc`), o administrador importa o arquivo `crun.keyring` da raiz do repositório em um chaveiro GPG dedicado (`gpg --no-default-keyring --keyring ./crun.gpg --import crun.keyring`) e executa `--verify`. Para construir um binário estaticamente vinculado e totalmente reprodutível (stripped ELF para glibc), utiliza-se a derivação Nix incluída na pasta `nix/` do repositório com o comando `nix --extra-experimental-features "nix-command flakes" build "path:.#crun-static-amd64"`, que gera o executável autocontido em `./result/bin/crun` (também automatizável via role Ansible `alvistack/ansible-role-crun`).

## Exemplo
```bash
# Verificar a assinatura GPG de uma release oficial do crun usando o arquivo crun.keyring
gpg --no-default-keyring --keyring ./crun.gpg --import crun.keyring
gpg --no-default-keyring --keyring ./crun.gpg --verify crun-1.29.1.tar.zst.asc crun-1.29.1.tar.zst

# Construir um binário estático reprodutível do crun usando Nix flakes
nix --extra-experimental-features "nix-command flakes" build "path:.#crun-static-amd64"
./result/bin/crun --version
```

## Limites e trade-offs
Um binário estaticamente vinculado (`crun-static-amd64`) elimina dependências de bibliotecas dinâmicas no servidor alvo e facilita implantações portáveis, porém embute internamente o código das bibliotecas vinculadas (como `libseccomp` e `libcap`); se uma vulnerabilidade for corrigida em uma dessas bibliotecas, o binário estático do `crun` precisa ser reconstruído e redistribuído em vez de depender apenas de um `apt upgrade` da biblioteca no host.

## Como verificar
Execute `file ./result/bin/crun` e `ldd ./result/bin/crun` no binário gerado pela derivação Nix para confirmar que ele é um executável ELF estaticamente vinculado (`statically linked`).

## Conexões
- [[crun-compilacao-autotools-libcrun-shared-dependencies]] — Veja também: Containers crun: compilação com Autotools, geração de parser via libocispec, biblioteca compartilhada libcrun e bindings Lua.
- [[crun-execucao-processos-exec-capabilities-lsm-sub-cgroups]] — Veja também: Containers crun: execução de processos adicionais (crun exec) com isolamento de sub-cgroup, capabilities, AppArmor e SELinux.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.
- [[runc-assinatura-releases-gpg-keyring-auditoria-seguranca]] — Referência cruzada direta com runc-assinatura-releases-gpg-keyring-auditoria-seguranca.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
