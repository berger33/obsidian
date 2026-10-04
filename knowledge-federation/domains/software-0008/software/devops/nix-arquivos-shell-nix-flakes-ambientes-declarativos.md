---
id: software.devops.tranche08.000786
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

# Nix: ambientes de desenvolvimento declarativos versionados no repositório (shell.nix e flake.nix)

## Em uma frase
Em vez de digitar longos comandos `nix-shell -p ... -I nixpkgs=...` manualmente no terminal, projetos versionam no Git um arquivo declarativo `shell.nix` (ou `flake.nix` com `flake.lock`) que define pacotes, variáveis de ambiente e hooks de inicialização do projeto.

## Por que importa
Quando um novo engenheiro clona um repositório ou um job de CI inicia, ele não deve precisar consultar uma wiki desatualizada para descobrir quais 15 pacotes e qual commit do Nixpkgs o projeto exige; basta rodar `nix-shell` (ou `nix develop`) na raiz do repositório. O guia oficial `nix.dev` conecta os ambientes ad-hoc aos ambientes declarativos reprodutíveis.

## Como funciona
No formato clássico **`shell.nix`**, o arquivo importa uma revisão fixada do `nixpkgs` (`fetchTarball`) e chama a função `mkShell`, declarando na lista `packages` (ou `buildInputs`) todas as ferramentas necessárias (ex.: `go`, `golangci-lint`, `kubectl`, `postgresql`) e em `shellHook` comandos executados automaticamente ao entrar no shell. No formato moderno **Nix Flakes** (`flake.nix` + `flake.lock`), todas as entradas externas (`inputs.nixpkgs.url`) têm seus hashes criptográficos e revisões Git gravados automaticamente no arquivo `flake.lock`, e a saída `devShells.<system>.default` é ativada com `nix develop` sob avaliação pura por padrão.

## Exemplo
```nix
# Exemplo de arquivo shell.nix declarativo com revisão do Nixpkgs fixada para ambiente de desenvolvimento DevOps
let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/2a601aafdc5605a5133a2ca506a34a3a73377247";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in
pkgs.mkShellNoCC {
  packages = with pkgs; [
    git
    jq
    kubectl
    kubernetes-helm
  ];
}
```

## Limites e trade-offs
Usar `pkgs.mkShell` padrão inclui automaticamente o compilador C (`stdenv.cc`, como GCC ou Clang) no ambiente; quando o ambiente de desenvolvimento precisa apenas de ferramentas CLI prontas (`kubectl`, `helm`, `jq`, `terraform`) e não vai compilar código C/C++, usar **`pkgs.mkShellNoCC`** evita baixar o toolchain de compilação C desnecessariamente.

## Como verificar
Salve o arquivo `shell.nix` no diretório do projeto e execute `nix-shell --pure --run "kubectl version --client && jq --version"` para confirmar o provisionamento automático do ambiente a partir do arquivo.

## Conexões
- [[nix-garbage-collection-limpeza-espaco-disco-nix-store]] — Veja também: Nix: gerenciamento de ciclo de vida de armazenamento e coleta de lixo com nix-collect-garbage.
- [[nix-busca-pacotes-search-nixos-org-multiplataforma]] — Veja também: Nix: descoberta de pacotes no Nixpkgs (search.nixos.org e nix search) e suporte multiplataforma (Linux, WSL e macOS).
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-reprodutibilidade-nix-shell-pure-pinning-nixpkgs]] — Referência cruzada direta com nix-reprodutibilidade-nix-shell-pure-pinning-nixpkgs.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
