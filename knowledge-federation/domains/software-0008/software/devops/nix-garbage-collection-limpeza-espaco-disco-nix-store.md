---
id: software.devops.tranche08.000785
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

# Nix: gerenciamento de ciclo de vida de armazenamento e coleta de lixo com nix-collect-garbage

## Em uma frase
Como os pacotes baixados em sessões `nix-shell` permanecem armazenados em `/nix/store` para reutilização imediata após o fechamento do shell, o comando `nix-collect-garbage` varre o grafo de referências e libera espaço em disco removendo caminhos sem raízes ativas (`GC roots`).

## Por que importa
Em máquinas de desenvolvedores e especialmente em runners de CI/CD com discos SSD de tamanho limitado, testar dezenas de versões diferentes de compiladores e ferramentas via `nix-shell` acumula gigabytes de caminhos antigos em `/nix/store`. A seção `Garbage collection` do guia oficial `nix.dev` documenta como liberar esse espaço com segurança.

## Como funciona
O Nix mantém um diretório de raízes do coletor de lixo (`/nix/var/nix/gcroots`), que aponta para os perfis de usuários atualmente instalados, gerações do sistema operacional e ambientes ativos. Quando uma sessão efêmera `nix-shell -p cowsay lolcat` é encerrada com `exit`, os caminhos `/nix/store/...-cowsay` e `/nix/store/...-lolcat` continuam no disco (fazendo com que uma segunda chamada a `nix-shell -p cowsay` seja instantânea, sem baixar nada da rede), mas deixam de ter uma raiz ativa em `gcroots`. Ao executar **`nix-collect-garbage`**, o Nix percorre o grafo a partir das raízes ativas e apaga de `/nix/store` todos os caminhos "mortos" (não referenciados), informando quantos store paths foram deletados e quantos MiB foram liberados.

## Exemplo
```bash
# Executar o coletor de lixo do Nix para remover de /nix/store todos os pacotes sem raízes ativas (ex.: de nix-shells encerrados)
nix-collect-garbage

# Remover também gerações antigas de perfis de usuário antes de coletar o lixo
nix-collect-garbage -d
```

## Limites e trade-offs
Se você executar `nix-collect-garbage` todos os dias em sua estação de trabalho sem registrar raízes persistentes (como perfis `nix-env`/`nix profile` ou diretórios `.direnv` de projetos), na próxima vez que entrar no `nix-shell` do seu projeto o Nix precisará baixar novamente os pacotes de `cache.nixos.org`.

## Como verificar
Execute `nix-store --gc --print-dead` para listar quais caminhos em `/nix/store` seriam removidos sem apagá-los de fato, e depois rode `nix-collect-garbage` verificando a mensagem `... store paths deleted, ... MiB freed`.

## Conexões
- [[nix-cache-binario-cache-nixos-org-derivacoes-source]] — Veja também: Nix: modelo híbrido source/binário, derivações (.drv) e cache binário oficial (cache.nixos.org).
- [[nix-arquivos-shell-nix-flakes-ambientes-declarativos]] — Veja também: Nix: ambientes de desenvolvimento declarativos versionados no repositório (shell.nix e flake.nix).
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-ambientes-efemeros-nix-shell-pacotes-isolados]] — Referência cruzada direta com nix-ambientes-efemeros-nix-shell-pacotes-isolados.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
