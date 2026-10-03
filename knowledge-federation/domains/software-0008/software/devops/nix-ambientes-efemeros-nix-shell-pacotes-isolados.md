---
id: software.devops.tranche08.000782
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

# Nix: criação de ambientes de shell efêmeros e aninhados com nix-shell -p e execução via --run

## Em uma frase
O comando `nix-shell -p <pacotes>` cria ambientes de linha de comando ad-hoc e efêmeros onde ferramentas são disponibilizadas imediatamente no `$PATH` sem alterar a configuração global do sistema, suportando sessões aninhadas e execução não interativa com `--run`.

## Por que importa
Desenvolvedores frequentemente precisam usar utilitários específicos (`jq`, `kubectl`, `helm`, `git`, `neovim`, `nodejs`) para um projeto ou script de CI sem poluir o sistema operacional hospedeiro e sem deixar pacotes órfãos instalados para sempre. O tutorial oficial `Ad hoc shell environments` (`nix.dev/tutorials/first-steps/ad-hoc-shell-environments`) demonstra como o `nix-shell` resolve esse fluxo em segundos.

## Como funciona
Quando o usuário executa `nix-shell -p cowsay lolcat`, o Nix resolve as derivações dos pacotes solicitados no conjunto de pacotes Nixpkgs, baixa os binários pré-compilados do cache (ou compila se necessário) para `/nix/store` e inicia uma nova sessão de shell interativa (`[nix-shell:~]$`) onde a variável de ambiente `$PATH` foi modificada para apontar para os diretórios `/nix/store/.../bin` daqueles pacotes. Ao sair da sessão com `exit` ou `Ctrl+D`, os programas desaparecem imediatamente do `$PATH` do sistema (embora permaneçam em cache em `/nix/store` para uso instantâneo futuro). É possível abrir **sessões aninhadas** (rodar `nix-shell -p git` dentro de um `nix-shell` já ativo para adicionar pacotes temporariamente) ou rodar um único comando não interativo passando `--run "<comando>"`.

## Exemplo
```bash
# Executar um comando único dentro de um ambiente efêmero contendo cowsay e lolcat sem alterar o sistema global
nix-shell -p cowsay lolcat --run "cowsay Hello, Nix! | lolcat"
```

## Limites e trade-offs
Por padrão, o comando `nix-shell -p <pacote>` sem flags adicionais cria um ambiente **impuro**, o que significa que ele preserva as variáveis de ambiente e o `$PATH` que já existiam no sistema hospedeiro; assim, se um programa não foi solicitado no `-p`, mas já está instalado globalmente no host, ele continuará acessível dentro do `nix-shell` padrão, podendo mascarar dependências esquecidas.

## Como verificar
Execute `which cowsay` fora do `nix-shell` (confirmando que não está no `$PATH` global) e em seguida execute `nix-shell -p cowsay --run "which cowsay"` para verificar que o binário é resolvido diretamente de `/nix/store/<hash>-cowsay-.../bin/cowsay`.

## Conexões
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Veja também: Nix: gerenciador de pacotes puramente funcional e armazenamento imutável em /nix/store.
- [[nix-reprodutibilidade-nix-shell-pure-pinning-nixpkgs]] — Veja também: Nix: ambientes 100% reprodutíveis com nix-shell --pure e fixação de commit do Nixpkgs (-I nixpkgs=...).
- [[nix-garbage-collection-limpeza-espaco-disco-nix-store]] — Referência cruzada direta com nix-garbage-collection-limpeza-espaco-disco-nix-store.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
