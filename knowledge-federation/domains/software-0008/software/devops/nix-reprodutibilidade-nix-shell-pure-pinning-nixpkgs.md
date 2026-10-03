---
id: software.devops.tranche08.000783
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

# Nix: ambientes 100% reprodutíveis com nix-shell --pure e fixação de commit do Nixpkgs (-I nixpkgs=...)

## Em uma frase
Combinar a flag `--pure` do `nix-shell` (que descarta a maioria das variáveis de ambiente do host) com `-I nixpkgs=https://github.com/NixOS/nixpkgs/tarball/<commit>` garante que um comando execute exatamente com as mesmas versões de pacotes e bibliotecas em qualquer máquina.

## Por que importa
Apenas rodar `nix-shell -p git` em duas máquinas diferentes não garante reprodutibilidade absoluta: uma máquina pode ter utilitários extras no `$PATH` do host e pode estar apontando para um canal `nixpkgs` de 2024, enquanto a outra aponta para `nixpkgs` de 2026. A seção `Towards reproducibility` do guia oficial `nix.dev` demonstra como eliminar ambas as fontes de variação.

## Como funciona
Dois mecanismos complementares tornam o ambiente determinístico: (1) a flag **`--pure`** limpa a maioria das variáveis de ambiente herdadas do sistema hospedeiro ao iniciar o shell, de modo que apenas os binários declarados explicitamente em `-p` (e utilitários básicos do ambiente padrão `stdenv`) existem no `$PATH` (tentar rodar um comando instalado no host que não foi listado em `-p` falha com `command not found`); e (2) a flag **`-I nixpkgs=<url-tarball-commit>`** instrui o Nix a buscar a definição dos pacotes de uma revisão Git exata e imutável do repositório `NixOS/nixpkgs` (por exemplo, o commit `2a601aafdc5605a5133a2ca506a34a3a73377247`), garantindo bit a bit as mesmas versões de `git`, `neovim` e `nodejs` hoje ou daqui a cinco anos.

## Exemplo
```bash
# Executar git --version em um ambiente nix-shell puro (--pure) fixado em um commit exato do Nixpkgs
nix-shell -p git --run "git --version" --pure \
  -I nixpkgs=https://github.com/NixOS/nixpkgs/tarball/2a601aafdc5605a5133a2ca506a34a3a73377247
```

## Limites e trade-offs
Quando você executa `nix-shell --pure`, variáveis de ambiente do usuário no host — como `SSH_AUTH_SOCK`, configurações de proxy corporativo (`HTTPS_PROXY`), `KUBECONFIG` ou `AWS_PROFILE` — são limpas para garantir pureza; se um script precisar de uma variável específica do host dentro de um shell puro, é necessário preservá-la explicitamente com `--keep NOME_DA_VARIAVEL`.

## Como verificar
Execute o comando `nix-shell -p git --run "git --version" --pure -I nixpkgs=https://github.com/NixOS/nixpkgs/tarball/2a601aafdc5605a5133a2ca506a34a3a73377247` em duas máquinas diferentes e confirme que ambas imprimem exatamente `git version 2.42.0`.

## Conexões
- [[nix-ambientes-efemeros-nix-shell-pacotes-isolados]] — Veja também: Nix: criação de ambientes de shell efêmeros e aninhados com nix-shell -p e execução via --run.
- [[nix-cache-binario-cache-nixos-org-derivacoes-source]] — Veja também: Nix: modelo híbrido source/binário, derivações (.drv) e cache binário oficial (cache.nixos.org).
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-arquivos-shell-nix-flakes-ambientes-declarativos]] — Referência cruzada direta com nix-arquivos-shell-nix-flakes-ambientes-declarativos.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
