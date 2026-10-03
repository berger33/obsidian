---
id: software.devops.tranche08.000787
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
fontes: ["https://raw.githubusercontent.com/NixOS/nix/master/README.md", "https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments", "https://github.com/NixOS/nix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nix: descoberta de pacotes no Nixpkgs (search.nixos.org e nix search) e suporte multiplataforma (Linux, WSL e macOS)

## Em uma frase
O Nix suporta sistemas Unix e Unix-like — incluindo **Linux**, **Windows (WSL)** e **macOS** (`x86_64` e `aarch64`/Apple Silicon) — e permite localizar os mais de 100.000 pacotes do repositório `NixOS/nixpkgs` via `search.nixos.org` ou `nix search`.

## Por que importa
Em equipes onde parte dos engenheiros usa laptops macOS (Apple Silicon), parte usa Linux nativo e parte usa Windows com WSL2, ferramentas como `apt` (só Debian/Ubuntu) ou `brew` (focado em macOS, sem isolamento funcional) não oferecem uma definição única de ambiente que funcione nas três plataformas. O guia oficial `nix.dev` documenta o suporte multiplataforma e a busca de atributos de pacotes.

## Como funciona
Quando instalado em Linux, Windows (via WSL) ou macOS, o Nix cria o volume/diretório `/nix/store` e avalia expressões do repositório **`NixOS/nixpkgs`**. Como o nome do pacote no Nixpkgs (o atributo usado em `nix-shell -p <atributo>`) às vezes difere do nome de um binário interno (por exemplo, o comando `dig` faz parte do pacote `bind` ou `dnsutils`), o usuário pode pesquisar o identificador exato no portal oficial **`https://search.nixos.org/`** ou via linha de comando (`nix-env -qaP` / `nix search nixpkgs <termo>`), inspecionando a versão, os binários incluídos (`Programs provided`), as plataformas suportadas (`x86_64-linux`, `aarch64-linux`, `x86_64-darwin`, `aarch64-darwin`) e o código-fonte da expressão Nix.

## Exemplo
```bash
# Pesquisar pacotes relacionados a "ripgrep" diretamente pela CLI moderna do Nix no catálogo nixpkgs
nix --extra-experimental-features "nix-command flakes" search nixpkgs ripgrep
```

## Limites e trade-offs
Embora a imensa maioria das ferramentas de desenvolvimento e DevOps no `nixpkgs` suporte tanto Linux (`*-linux`) quanto macOS (`*-darwin`), pacotes que dependem diretamente de chamadas de sistema exclusivas do kernel Linux (como utilitários de `systemd`, `iptables`, `iproute2` ou ferramentas `eBPF`/`KVM`) são marcados em `meta.platforms = platforms.linux` e só podem ser construídos/executados em Linux ou dentro de uma VM Linux/WSL.

## Como verificar
Antes de adicionar um pacote a um `shell.nix` compartilhado entre desenvolvedores Linux e macOS, consulte a seção `Platforms` do pacote em `https://search.nixos.org/packages` para confirmar suporte a `x86_64-linux` e `aarch64-darwin`.

## Conexões
- [[nix-arquivos-shell-nix-flakes-ambientes-declarativos]] — Veja também: Nix: ambientes de desenvolvimento declarativos versionados no repositório (shell.nix e flake.nix).
- [[nix-builds-hermeticos-sandbox-isolamento-derivacoes]] — Veja também: Nix: builds herméticos em sandbox (isolamento de rede e sistema de arquivos durante a compilação).
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-ambientes-efemeros-nix-shell-pacotes-isolados]] — Referência cruzada direta com nix-ambientes-efemeros-nix-shell-pacotes-isolados.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
