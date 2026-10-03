---
id: software.devops.tranche08.000789
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

# Nix: perfis de usuário, atualizações transacionais atômicas e rollbacks instantâneos via árvores de symlinks

## Em uma frase
O Nix implementa atualizações atômicas e rollbacks instantâneos construindo uma nova geração de perfil (uma árvore de links simbólicos apontando para `/nix/store`) em segundo plano e trocando um único symlink atômico no final da operação.

## Por que importa
Em gerenciadores de pacotes tradicionais (`apt upgrade` ou `yum update`), se a energia cair ou o processo for interrompido no meio da atualização de 100 pacotes, o sistema fica em um estado meio-atualizado corrompido; além disso, reverter para o estado anterior exige desinstalar e reinstalar pacotes antigos que podem nem estar mais no repositório. A arquitetura do Nix documentada no repositório oficial elimina janelas de estado inconsistente.

## Como funciona
Um **perfil Nix** (`~/.nix-profile`) nunca contém binários copiados diretamente: ele é um link simbólico que aponta para a geração atual (ex.: `/nix/var/nix/profiles/per-user/alice/profile-42-link`), que por sua vez aponta para um diretório imutável em `/nix/store/<hash>-user-environment` contendo symlinks (`bin/`, `share/`) para cada pacote instalado. Quando o usuário instala, remove ou atualiza pacotes, o Nix constrói a geração `43` inteira em `/nix/store` sem tocar na geração `42` em uso; somente quando a geração `43` está 100% pronta no disco, o Nix executa uma chamada `rename(2)` POSIX atômica para atualizar o symlink do perfil de `profile-42-link` para `profile-43-link`. Fazer rollback consiste apenas em apontar o symlink de volta para a geração `42`, em milissegundos.

## Exemplo
```bash
# Inspecionar a cadeia de links simbólicos do perfil Nix do usuário apontando para a geração ativa em /nix/store
ls -la ~/.nix-profile
readlink -f ~/.nix-profile
```

## Limites e trade-offs
Como as gerações anteriores do perfil (`profile-41-link`, `profile-42-link`) são mantidas como raízes do coletor de lixo (`gcroots`) para permitir rollback instantâneo a qualquer momento, os pacotes dessas gerações antigas não serão removidos por um `nix-collect-garbage` simples até que você remova as gerações antigas que não deseja mais manter (usando `nix-collect-garbage -d` ou `--delete-older-than 30d`).

## Como verificar
Inspecione `/nix/var/nix/profiles/per-user/$USER/` para visualizar as gerações numeradas de perfil e a transição atômica de links simbólicos.

## Conexões
- [[nix-builds-hermeticos-sandbox-isolamento-derivacoes]] — Veja também: Nix: builds herméticos em sandbox (isolamento de rede e sistema de arquivos durante a compilação).
- [[nix-ecossistema-nixos-darwin-home-manager-direnv]] — Veja também: Nix: ecossistema e evolução do projeto (NixOS, nix-direnv, geração de imagens OCI e arquitetura C++/Meson).
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-garbage-collection-limpeza-espaco-disco-nix-store]] — Referência cruzada direta com nix-garbage-collection-limpeza-espaco-disco-nix-store.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
