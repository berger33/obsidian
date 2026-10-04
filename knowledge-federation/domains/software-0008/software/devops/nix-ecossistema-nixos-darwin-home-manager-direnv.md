---
id: software.devops.tranche08.000790
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

# Nix: ecossistema e evolução do projeto (NixOS, nix-direnv, geração de imagens OCI e arquitetura C++/Meson)

## Em uma frase
O gerenciador de pacotes Nix (`NixOS/nix`, escrito em C++ e construído com Meson) é a base da distribuição Linux declarativa **NixOS**, integra-se ao `direnv` para ativação automática de ambientes por diretório e permite construir imagens de container OCI mínimas e reprodutíveis sem Dockerfile.

## Por que importa
Além de criar shells de desenvolvimento (`nix-shell`), os mesmos princípios puramente funcionais do Nix permitem declarar um sistema operacional Linux inteiro em um único arquivo de configuração (**NixOS**), ativar ferramentas automaticamente ao dar `cd` na pasta de um projeto (`nix-direnv`) e gerar imagens Docker/OCI enxutas contendo apenas o fechamento transitivo exato (`closure`) do binário em `/nix/store`. O README oficial do `NixOS/nix` e o portal `nix.dev` documentam esse ecossistema.

## Como funciona
(1) **NixOS**: distribuição Linux construída sobre o gerenciador Nix onde todo o sistema operacional (kernel, módulos, systemd services, usuários, firewall `/etc`) é uma única derivação em `/nix/store`, permitindo atualizações atômicas e rollback do sistema inteiro no menu de boot (GRUB/systemd-boot); (2) **Integração com `direnv` (`use nix` / `use flake`)**: carrega automaticamente as variáveis de ambiente do `shell.nix` ou `flake.nix` assim que o desenvolvedor entra no diretório do projeto no terminal; e (3) **Construção de imagens OCI (`pkgs.dockerTools`)**: gera tarballs de imagens de container camadas-por-derivação sem precisar de um daemon Docker rodando e sem incluir gerenciadores de pacotes ou shells desnecessários na imagem final.

## Exemplo
```bash
# Inspecionar o fechamento transitivo (closure) exato de dependências em /nix/store de um binário antes de empacotá-lo
nix-store -qR $(which git)
```

## Limites e trade-offs
Como todo binário compilado pelo Nix vincula suas bibliotecas dinâmicas apontando diretamente para caminhos absolutos em `/nix/store/<hash>-glibc-.../lib/ld-linux-x86-64.so.2`, você não pode simplesmente copiar um binário isolado de `/nix/store` para outra máquina sem levar junto o seu fechamento transitivo (`nix-store -qR` / `nix copy`), nem executar um binário pré-compilado genérico baixado da internet no NixOS sem usar `nix-ld` ou `steam-run`/`buildFHSEnv`.

## Como verificar
Execute `nix-store -q --tree $(which nix)` para visualizar a árvore exata de dependências de tempo de execução registradas no cabeçalho RPATH do binário no Nix Store.

## Conexões
- [[nix-perfis-atualizacoes-atomicas-rollbacks-symlinks]] — Veja também: Nix: perfis de usuário, atualizações transacionais atômicas e rollbacks instantâneos via árvores de symlinks.
- [[nix-gerenciador-pacotes-puramente-funcional-nix-store]] — Referência cruzada direta com nix-gerenciador-pacotes-puramente-funcional-nix-store.
- [[nix-arquivos-shell-nix-flakes-ambientes-declarativos]] — Referência cruzada direta com nix-arquivos-shell-nix-flakes-ambientes-declarativos.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
