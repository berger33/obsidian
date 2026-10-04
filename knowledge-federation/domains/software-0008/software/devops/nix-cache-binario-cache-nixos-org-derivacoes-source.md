---
id: software.devops.tranche08.000784
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

# Nix: modelo híbrido source/binário, derivações (.drv) e cache binário oficial (cache.nixos.org)

## Em uma frase
Embora o Nix seja conceitualmente um sistema baseado em código-fonte (onde expressões Nix descrevem como compilar cada derivação `.drv` a partir do zero), na prática ele opera de forma transparente como gerenciador binário consultando `https://cache.nixos.org` pelo hash de saída.

## Por que importa
Se um gerenciador de pacotes funcional obrigasse o desenvolvedor a compilar localmente o GCC, a `glibc`, o LLVM, o Rust e o Node.js a partir do código-fonte toda vez que entrasse em um `nix-shell`, cada ambiente levaria horas para iniciar. O tutorial oficial `nix.dev` e o manual do Nix explicam como o endereçamento por hash em `/nix/store` viabiliza a substituição transparente por binários pré-compilados.

## Como funciona
Quando o Nix avalia uma expressão de pacote, ele primeiro instancia os arquivos de derivação (`/nix/store/<hash>.drv`) que descrevem todas as entradas do grafo de build e calcula antecipadamente o caminho de saída esperado em `/nix/store/<output-hash>-<nome>`. Antes de iniciar qualquer compilação local, o Nix consulta os substituters configurados (por padrão, o cache binário global oficial **`https://cache.nixos.org`**): se aquele exato `<output-hash>` já foi compilado pela infraestrutura de CI do NixOS (Hydra), o Nix simplesmente baixa e verifica a assinatura criptográfica do arquivo `.narinfo`/`.nar` (ex.: `copying path '/nix/store/...-cowsay-3.04' from 'https://cache.nixos.org'...`); caso o pacote tenha flags customizadas inéditas, o Nix compila localmente em sandbox de forma transparente.

## Exemplo
```bash
# Verificar a configuração de substituters (caches binários) e chaves públicas confiáveis do Nix no sistema
nix config show | grep -E "^(substituters|trusted-public-keys)"
```

## Limites e trade-offs
Se você fixar `-I nixpkgs=...` em um commit recém-empurrado há poucos minutos na branch `master` do `NixOS/nixpkgs` que ainda não terminou de ser compilado pelo cluster Hydra para `cache.nixos.org`, o Nix tentará compilar os pacotes localmente a partir do código-fonte; por isso, ao fixar revisões do Nixpkgs, escolha commits de branches de canal (`nixos-unstable`, `nixpkgs-unstable` ou `nixos-24.05`) que já passaram pelos testes e já estão populados no cache binário.

## Como verificar
Ao executar `nix-shell -p hello`, observe nas mensagens de log que o Nix imprime `copying path '/nix/store/...' from 'https://cache.nixos.org'...` em vez de `building '/nix/store/...drv'`.

## Conexões
- [[nix-reprodutibilidade-nix-shell-pure-pinning-nixpkgs]] — Veja também: Nix: ambientes 100% reprodutíveis com nix-shell --pure e fixação de commit do Nixpkgs (-I nixpkgs=...).
- [[nix-garbage-collection-limpeza-espaco-disco-nix-store]] — Veja também: Nix: gerenciamento de ciclo de vida de armazenamento e coleta de lixo com nix-collect-garbage.
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-ambientes-efemeros-nix-shell-pacotes-isolados]] — Referência cruzada direta com nix-ambientes-efemeros-nix-shell-pacotes-isolados.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
