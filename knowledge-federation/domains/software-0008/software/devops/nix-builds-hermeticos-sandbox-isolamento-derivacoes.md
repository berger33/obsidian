---
id: software.devops.tranche08.000788
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

# Nix: builds herméticos em sandbox (isolamento de rede e sistema de arquivos durante a compilação)

## Em uma frase
Para garantir que o hash de `/nix/store/<hash>-<nome>` reflita 100% das dependências reais do pacote, o Nix executa a compilação de derivações dentro de um **sandbox hermético** sem acesso à internet e sem visão de diretórios do host fora das entradas declaradas.

## Por que importa
Em builds tradicionais (`Makefile`, `Dockerfile` ou scripts bash), um processo de compilação pode ler silenciosamente `/usr/include/openssl` instalado na máquina do desenvolvedor ou baixar um pacote da internet sem verificar hash; meses depois, quando o servidor externo muda ou o build roda em outra máquina, a compilação quebra. O manual de arquitetura do Nix no repositório `NixOS/nix` explica como o sandboxing impede dependências não declaradas.

## Como funciona
Quando o daemon do Nix (`nix-daemon`) constrói uma derivação `.drv` no Linux, ele cria um ambiente isolado usando namespaces de usuário, mount, rede, PID e IPC: (1) **Sistema de arquivos isolado**: dentro do sandbox, diretórios globais como `/usr`, `/bin`, `/lib` e `/home` não existem; apenas os caminhos exatos de `/nix/store/...` que foram explicitamente declarados como entradas daquela derivação são montados em modo somente-leitura, mais um diretório temporário de build; e (2) **Rede bloqueada**: exceto para derivações de saída fixa (`fixed-output derivations`, como `fetchurl`/`fetchTarball` onde o hash SHA-256 exato do download já foi declarado de antemão), nenhum processo de build tem acesso à rede, forçando que todo download seja declarado e verificado por hash antes da fase de compilação.

## Exemplo
```bash
# Verificar se o modo sandbox hermético está ativo na configuração do nix-daemon do sistema
nix config show | grep -E "^sandbox ="
```

## Limites e trade-offs
Como o sandbox de compilação do Nix bloqueia qualquer conexão de rede durante a fase `buildPhase` de uma derivação normal, ferramentas de linguagens que tentam baixar dependências da internet no meio do `build` (como `go build`, `cargo build` ou `npm install` sem vendor/cache prévio) falharão dentro do sandbox até que as dependências sejam fornecidas via helpers de saída fixa do Nix (`buildGoModule` com `vendorHash`, `rustPlatform.buildRustPackage`, `buildNpmPackage`).

## Como verificar
Execute `nix config show | grep sandbox` e confirme que `sandbox = true` está habilitado para assegurar que todas as derivações locais sejam construídas de forma hermética.

## Conexões
- [[nix-busca-pacotes-search-nixos-org-multiplataforma]] — Veja também: Nix: descoberta de pacotes no Nixpkgs (search.nixos.org e nix search) e suporte multiplataforma (Linux, WSL e macOS).
- [[nix-perfis-atualizacoes-atomicas-rollbacks-symlinks]] — Veja também: Nix: perfis de usuário, atualizações transacionais atômicas e rollbacks instantâneos via árvores de symlinks.
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-cache-binario-cache-nixos-org-derivacoes-source]] — Referência cruzada direta com nix-cache-binario-cache-nixos-org-derivacoes-source.
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
